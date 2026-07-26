# Trimmetry

Official documentation for the Trimmetry generator plug-in for Cinema 4D.

The documentation is built with [Sphinx](https://www.sphinx-doc.org/) and
[Sphinx Book Theme](https://sphinx-book-theme.readthedocs.io/) and published
automatically with GitHub Pages.

## Local preview

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r docs\requirements.txt
sphinx-build -b html docs\source docs\_build\html
py -m http.server 8000 --directory docs\_build\html
```

Open <http://localhost:8000>.

