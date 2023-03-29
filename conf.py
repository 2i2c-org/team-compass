import os
from pathlib import Path
from subprocess import run

# -- Project information -----------------------------------------------------

project = "Team Compass"
copyright = "2023, 2i2c"
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
    "sphinxext.rediraffe",
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
    "https://app.asana.com*",  # Because it has some kind of security that returns a 403
]

# -- Sphinx setup script ---------------------------------------------------

def setup(app):
    app.add_css_file("custom.css")
    
    # Add a `role` domain that we can reference in our text.
    # To add a new role, use the `role` directive just above the section where you describe it.
    #
    # ```{role} Some new role name
    # ```
    #
    # And then document it like: {role}`Some new role name` to generate a link.
    # ref: https://www.sphinx-doc.org/en/master/extdev/appapi.html#sphinx.application.Sphinx.add_crossref_type
    app.add_crossref_type("role", "role")
    app.add_crossref_type("team", "team")

# -- Generate table of Support Stewards --------------------------------------
# This requires a token to be set, but will fail semi-gracefully if it is not.
# The token exists in our RTD environmet so it should work there.
path_script = Path(__file__).parent / "_data/support_stewards/gen_support_stewards.py"
run(f"python {path_script}", shell=True)

# -- Options for the rediraffe extension -------------------------------------
# ref: https://github.com/wpilibsuite/sphinxext-rediraffe#readme
#
# This extensions help us relocated content without breaking links. If a
# document is moved internally, put its path as a dictionary key in the
# redirects dictionary below and its new location in the value.
#
rediraffe_branch = "main"
rediraffe_redirects = {
    "get-started": "operations/index",
}
