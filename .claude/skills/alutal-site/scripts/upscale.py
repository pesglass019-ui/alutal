# 4x photo upscaler (Real-ESRGAN x4plus, ONNX, CPU). For small/blurry project photos.
# Setup once:
#   python3 -m venv /tmp/sr && /tmp/sr/bin/pip install onnxruntime pillow numpy huggingface_hub
#   HF_HUB_DISABLE_XET=1 /tmp/sr/bin/python -c "from huggingface_hub import hf_hub_download as d; print(d(\"bukuroo/RealESRGAN-ONNX\",\"real-esrgan-x4plus-128.onnx\"))"
# Usage: /tmp/sr/bin/python upscale.py MODEL.onnx in.jpg=out.png [in2.jpg=out2.png ...]
# Then convert the PNG with add_images.sh (it downsizes to 1400px max).
import sys, numpy as np, onnxruntime as ort
from PIL import Image

MODEL, T, PAD, S = sys.argv[1], 128, 12, 4
sess = ort.InferenceSession(MODEL, providers=["CPUExecutionProvider"])
iname = sess.get_inputs()[0].name

def up(path, out):
    im = np.asarray(Image.open(path).convert("RGB"), dtype=np.float32) / 255.0
    h, w, _ = im.shape
    core = T - 2 * PAD
    # reflect-pad so every tile is full size
    ph = (core - h % core) % core
    pw = (core - w % core) % core
    src = np.pad(im, ((PAD, PAD + ph), (PAD, PAD + pw), (0, 0)), mode="reflect")
    H, W = h + ph, w + pw
    res = np.zeros((H * S, W * S, 3), np.float32)
    for y in range(0, H, core):
        for x in range(0, W, core):
            tile = src[y:y + T, x:x + T].transpose(2, 0, 1)[None]
            o = sess.run(None, {iname: tile})[0][0].transpose(1, 2, 0)
            res[y * S:(y + core) * S, x * S:(x + core) * S] = o[PAD * S:(PAD + core) * S, PAD * S:(PAD + core) * S]
    res = np.clip(res[:h * S, :w * S], 0, 1)
    Image.fromarray((res * 255 + .5).astype(np.uint8)).save(out, quality=95)
    print(out, w, h, "->", w * S, h * S, flush=True)

for a in sys.argv[2:]:
    i, o = a.split("=")
    up(i, o)
