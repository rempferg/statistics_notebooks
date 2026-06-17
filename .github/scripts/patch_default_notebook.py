"""
Patch dist/config-utils.js so the root redirect lands on the default notebook.
config-utils.js redirects the root page to `appUrl/index.html`; we append
`?path=<notebook>` so JupyterLite opens the file directly.
"""
NOTEBOOK = "README.ipynb"

MARKER = "config.appUrl.replace(/\\/?$/, '/index.html')"
REPLACEMENT = f"config.appUrl.replace(/\\/?$/, '/index.html') + '?path={NOTEBOOK}'"

path = "dist/config-utils.js"
content = open(path).read()

if MARKER not in content:
    raise SystemExit(
        f"ERROR: redirect marker not found in {path}. "
        "config-utils.js may have changed — update MARKER in this script."
    )

patched = content.replace(MARKER, REPLACEMENT, 1)
open(path, "w").write(patched)
print(f"Patched {path}: root redirect now opens {NOTEBOOK}")
