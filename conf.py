# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "2i2c Team Compass"
copyright = "2021, 2i2c"
author = "2i2c"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_parser",
    "sphinx_panels",
    "sphinx_copybutton",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", ".github"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_book_theme"

html_title = "Team Compass"
html_logo = "images/logo.png"

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
    "linkify",
]
myst_url_schemes = ["https", "http", "ftp", "mailto"]
intersphinx_mapping = {
    "pi": ("https://pilot.2i2c.org", None),
    "ph": ("https://pilot-hubs.2i2c.org", None),
}

panels_add_bootstrap_css = False

# Disable linkcheck for anchors because it throws false errors for any JS anchors
linkcheck_anchors = False
linkcheck_ignore = [
    "https://github.com/2i2c-org/meta*",  # Because it's a private repo
    "https://github.com/issues*",  # Because linkcheck doesn't work with github issues + queries
    "https://github.com/orgs/2i2c-org/projects*",  # because projects don't respond properly for some reason
    "https://github.com/2i2c-org/leads*",  # Because it's a private repo
    "https://drive.google.com*",  # Because it's almost always private
    "https://icsi.berkeley.edu*",  # Because it's broken often
]
