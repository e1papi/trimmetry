# Translating the documentation

The Russian `.rst` files in `docs/source` are the editable source. Sphinx uses
the English gettext catalogs in `docs/source/locale/en/LC_MESSAGES` when
`DOCS_LANGUAGE=en`.

After changing Russian text:

```powershell
.\.venv\Scripts\python.exe -m sphinx -E -b gettext docs/source docs/_build/gettext
.\.venv\Scripts\python.exe docs/i18n/build_en_catalog.py
```

Add every newly reported phrase to the appropriate dictionary in
`docs/i18n`. Then run the catalog builder again.

Build both versions locally:

```powershell
$env:DOCS_LANGUAGE = "en"
.\.venv\Scripts\python.exe -m sphinx -W --keep-going -b html -d docs/_build/doctrees/en docs/source docs/_build/html

$env:DOCS_LANGUAGE = "ru"
.\.venv\Scripts\python.exe -m sphinx -W --keep-going -b html -d docs/_build/doctrees/ru docs/source docs/_build/html/ru

Remove-Item Env:DOCS_LANGUAGE
```

GitHub Pages publishes English at `/trimmetry/` and Russian at
`/trimmetry/ru/`. The language selector preserves the current page.
