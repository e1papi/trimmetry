import os


project = "Trimmetry"
author = "e1papi"
copyright = "2026, e1papi"
release = "1.0"
language = os.getenv("DOCS_LANGUAGE", "en")
locale_dirs = ["locale/"]
gettext_compact = True
gettext_additional_targets = ["literal-block"]

extensions = [
    "sphinx.ext.githubpages",
]

templates_path = ["_templates"]
exclude_patterns = []

html_theme = "sphinx_book_theme"
html_title = "Trimmetry"
html_logo = "_static/LOGO.png"
html_favicon = "_static/icon.png"
html_static_path = ["_static"]
html_css_files = ["trimmetry.css"]
html_js_files = ["language-switcher.js"]

html_theme_options = {
    "repository_url": "https://github.com/e1papi/trimmetry",
    "repository_branch": "main",
    "path_to_docs": "docs/source",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_download_button": True,
    "use_fullscreen_button": True,
    "show_navbar_depth": 2,
    "max_navbar_depth": 4,
    "collapse_navbar": False,
    "home_page_in_toc": True,
    "toc_title": "На этой странице" if language == "ru" else "On this page",
}

html_last_updated_fmt = "%d.%m.%Y" if language == "ru" else "%Y-%m-%d"

