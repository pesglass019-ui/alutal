#!/usr/bin/env bash
# Usage: add_images.sh <prefix> <photo1> [photo2 ...]
# Converts photos to img/<prefix>-N.webp (auto-rotated, max 1400px, quality 80),
# continuing the numbering if <prefix>-1.webp etc. already exist.
set -euo pipefail
cd "$(dirname "$0")/../../../.."
prefix="$1"; shift
n=$(ls img/"$prefix"-*.webp 2>/dev/null | wc -l)
for f in "$@"; do
  n=$((n+1))
  convert "$f" -auto-orient -resize '1400x1400>' -strip -quality 80 "img/$prefix-$n.webp"
  echo "img/$prefix-$n.webp  ($(identify -format '%wx%h' "img/$prefix-$n.webp"))"
done
