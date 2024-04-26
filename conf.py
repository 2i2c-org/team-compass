from pathlib import Path
from subprocess import run

# -- Project information -----------------------------------------------------
# ref: https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
#
project = "Team Compass"
copyright = "2023, 2i2c"
author = "2i2c"


# -- General Sphinx configuration ---------------------------------------------------
# ref: https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
#
extensions = [
    "myst_nb",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinx.ext.intersphinx",
    "sphinx_togglebutton",
    "sphinxext.rediraffe",
]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", ".github", ".nox", "README.md"]



# -- General MyST configuration -----------------------------------------------------
# ref: https://myst-parser.readthedocs.io/en/latest/configuration.html
#
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "dollarmath",
    "linkify",
    "tasklist",
]



# -- Options for HTML output -------------------------------------------------
# ref: https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
#
html_static_path = ["_static"]
html_css_files = ["custom.css"]

# sphinx-2i2c-theme inherits from sphinx-book-theme, that in turn inherits from
# pydata-sphinx-theme. Due to this, all their configuration can be relevant.
#
# sphinx-2i2c-theme ref:   https://github.com/2i2c-org/sphinx-2i2c-theme
# sphinx-book-theme ref:   https://sphinx-book-theme.readthedocs.io/en/stable/reference.html
# pydata-sphinx-theme ref: https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/index.html
#
html_theme = "sphinx_2i2c_theme"
html_theme_options = {
    "repository_url": "https://github.com/2i2c-org/team-compass",
    "repository_branch": "main",
    "use_repository_button": True,
    "use_edit_page_button": True,
}
html_js_files = [
    "https://cdn.plot.ly/plotly-2.31.1.min.js", #  NOTE: load plotly before require
    "https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js"
]


# -- Options for intersphinx extension ---------------------------------------
# ref: https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html#configuration
#
# The extension makes us able to link like to other projects like below.
#
#     {external+infra:doc}`folder/subfolder/file`
#     {external+infra:ref}`reference-label-name-here`
#     {external+infra:ref}`explicit link title <reference-label-name-here>`
#
# To see what we can link to, do the following where "objects.inv" is appended
# to the sphinx based website:
#
#     python -m sphinx.ext.intersphinx https://docs.2i2c.org/objects.inv
#     python -m sphinx.ext.intersphinx https://infrastructure.2i2c.org/objects.inv
#
intersphinx_mapping = {
    "docs": ("https://docs.2i2c.org/", None),
    "infra": ("https://infrastructure.2i2c.org/", None),
}

# intersphinx_disabled_reftypes set based on recommendation in
# https://docs.readthedocs.io/en/stable/guides/intersphinx.html#using-intersphinx
intersphinx_disabled_reftypes = ["*"]



# -- Options for linkcheck builder -------------------------------------------
# ref: https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-the-linkcheck-builder
#
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



# -- Sphinx setup script ---------------------------------------------------
def setup(app):
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

# -- myst_nb configuration --

nb_execution_timeout = 300
nb_execution_mode = 'auto'
suppress_warnings = ["mystnb.unknown_mime_type"]
