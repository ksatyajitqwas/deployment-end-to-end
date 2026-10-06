#!/usr/bin/env bash
# Daily Velero backup of critical namespaces
set -euo pipefail

velero backup create "daily-$(date +%Y%m%d)" \
  --include-namespaces production,staging \
  --wait
