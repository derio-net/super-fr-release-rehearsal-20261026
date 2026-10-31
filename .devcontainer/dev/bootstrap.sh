#!/usr/bin/env bash
# Fixture-only startup. No floating Git install, external sdist, or host install.
set -euo pipefail
umask 077

if [[ "$(uname -s)" != Linux || "$(uname -m)" != x86_64 ]]; then
  echo "fixture bootstrap requires the validated Linux x86_64 prebuilt runtime" >&2
  exit 1
fi
if [[ "${HOME:-}" != /home/vscode ]]; then
  echo "fixture bootstrap requires the profile's /home/vscode user" >&2
  exit 1
fi

ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/../.." && pwd -P)"
ENV_DIR=/home/vscode/.local/share/fr/closeout-1206-runtime-py314
SAFE_PATH=/home/vscode/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
UV="$(PATH="$SAFE_PATH" command -v uv)"
cd "$ROOT"
test -f uv.lock
test -f packages/fr/pyproject.toml
if [[ -e "$ENV_DIR" || -L "$ENV_DIR" ]]; then
  echo "refusing to replace an existing environment: $ENV_DIR; retain and inspect it" >&2
  exit 1
fi

# Trust only this actual container workspace, never '*' or an unrelated checkout.
git config --global --add safe.directory "$ROOT"
test "$(git rev-parse --show-toplevel)" = "$ROOT"

# Whitelist the resolver environment: no inherited index/build/credential overrides.
# --no-build still permits first-party pure-Python workspace assembly (uv help sync).
run_uv() {
  env -i HOME="$HOME" PATH="$SAFE_PATH" \
    UV_PROJECT_ENVIRONMENT="$ENV_DIR" \
    UV_NO_BUILD=1 UV_CONCURRENT_BUILDS=1 UV_CONCURRENT_INSTALLS=1 \
    UV_CONCURRENT_DOWNLOADS=1 UV_HTTP_RETRIES=0 \
    "$UV" "$@"
}

run_uv python install --no-bin 3.14.10
PYTHON="$(run_uv python find --no-python-downloads 3.14.10)"
test "$("$PYTHON" -c 'import sys; print(".".join(map(str, sys.version_info[:3])))')" = 3.14.10
run_uv venv --python "$PYTHON" --no-python-downloads "$ENV_DIR"
run_uv sync --frozen --no-build --python "$PYTHON" --no-python-downloads

# This is the real installed workspace entrypoint, not a shim or a tool download.
test -x "$ENV_DIR/bin/fr"
test "$(command -v fr)" = "$ENV_DIR/bin/fr"
"$ENV_DIR/bin/fr" --identity
