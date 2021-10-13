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
    "myst_parser",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinx.ext.intersphinx",
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
    "linkify",
]
myst_url_schemes = ["https", "http", "ftp", "mailto"]
intersphinx_mapping = {
    "pi": ("https://pilot.2i2c.org/en/latest/", None),
    "ph": ("https://pilot-hubs.2i2c.org/en/latest/", None),
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
]


# -- Custom scripts ---------------------------------------------------

# Hacky solution to list the latest engineering team members as reference
# This grabs the latest list of team members from https://2i2c.org/about/
# It then parses the HTML to grab the names and GitHub handles, then sorts by name
# We can use this to define the order of team roles.
from urllib import request
from bs4 import BeautifulSoup
import pandas as pd
from pathlib import Path

resp = request.urlopen("https://2i2c.org/about/")
text = resp.read().decode()

teams = []
for row in BeautifulSoup(text, features="html.parser").select("div.people-widget > div"):  
    # If not a `.people-person` item, it will be a group title
    if "people-person" not in row.attrs.get("class"):
        category = row.text.strip()
        continue
    entry = {"name": row.select("h2 a")[0].text, "team": category}

    # Grab the listed contact links for this person
    for link in row.select("ul.network-icon a"):
        if "fa-github" in str(link):
            handle = link.attrs["href"].split("/")[-1]
            entry["github"] = f"[@{handle}]({link.attrs['href']})"
        elif "mailto" in str(link):
            entry["email"] = link.attrs["href"].split(":")[-1]
        elif "twitter" in str(link):
            handle = link.attrs["href"].split("/")[-1]
            entry["twitter"] = f"[@{handle}]({link.attrs['href']})"
    teams.append(entry)

# Sort and create CSV files to be imported in the Team page
teams = pd.DataFrame(teams)
Path(__file__).parent.joinpath("tmp").mkdir(exist_ok=True)
for team, people in teams.groupby("team"):
    people.sort_values("name").drop(columns=["team"]).to_csv(f"tmp/{team}.csv" , index=None)


# -- Sphinx setup script ---------------------------------------------------

def setup(app):
    app.add_css_file("custom.css")
