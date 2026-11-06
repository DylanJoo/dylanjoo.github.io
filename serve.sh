#!/usr/bin/env bash
# Local preview at http://localhost:4000 (reloads the browser when you save a file).
# One-time setup: brew install ruby@3.3, then run this script (it installs gems on first run).
set -euo pipefail
cd "$(dirname "$0")"
export PATH="/opt/homebrew/opt/ruby@3.3/bin:$PATH"
bundle _2.4.1_ check >/dev/null 2>&1 || bundle _2.4.1_ install
exec bundle _2.4.1_ exec jekyll serve --livereload "$@"
