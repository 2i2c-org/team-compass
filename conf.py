from pathlib import Path

# -- Project information -----------------------------------------------------

project = "Team Compass"
copyright = "2021, 2i2c"
author = "2i2c"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_nb",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinx.ext.intersphinx",
    "sphinx_togglebutton",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", ".github", ".nox", "README.md"]


# -- Options for HTML output---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_2i2c_theme"
html_static_path = ["_static"]
html_title = "Team Compass"

show_navbar_depth = 3
html_theme_options = {
    "repository_url": "https://github.com/2i2c-org/team-compass",
    "repository_branch": "main",
    "use_repository_button": True,
    "use_edit_page_button": True,
    "extra_navbar": "",
}
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "dollarmath",
    "linkify",
]

intersphinx_mapping = {
    "docs": ("https://docs.2i2c.org/en/latest/", None),
    "infra": ("https://infrastructure.2i2c.org/en/latest/", None),
}

# Disable linkcheck for anchors because it throws false errors for any JS anchors
linkcheck_anchors = False
linkcheck_ignore = [
    "https://github.com/2i2c-org/meta*",  # Because it's a private repo
    "https://github.com/issues*",  # Because linkcheck doesn't work with github issues + queries
    "https://github.com/orgs/2i2c-org/projects*",  # because projects don't respond properly for some reason
    "https://github.com/2i2c-org/leads*",  # Because it's a private repo
    "https://drive.google.com*",  # Because it's almost always private
    "https://icsi.berkeley.edu*",  # Because it's broken often
    "https://sociocracyforall.org*",  # Because it raises a 403 but still works
    "https://airtable.com*",  # Because it has some kind of security that returns a 403
]

# -- Sphinx setup script ---------------------------------------------------

def setup(app):
    app.add_css_file("custom.css")
