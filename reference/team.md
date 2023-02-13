---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.13.8
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# List of team members

The 2i2c team is defined on [the `team/` page of our website](https://2i2c.org/organization/).
Below is a summary of the people on that page.

% The code below uses urllib and beautifulsoup to grab the HTML of the team section
% defined at https://2i2c.org/organization/ . It then directly places the HTML here
% and applies some light styles to make it look nice. This way the team structure
% here and on our website is always in-sync.
%
% TODO: We should define our organization's membership in a more structured and
%   central place (like a CSV or YAML file) and re-use that information here
%   and in our website.

<style>
.people-widget .avatar {
    width: 100%;
    max-width: 150px;
    height: auto;
    text-align: center;
}

.avatar-circle {
    border-radius: 50%;
}

.avatar {
  margin: 0px auto;
  object-fit: cover;
}

.people-person {
    width: 25%;
}

.people-person img {
    border-radius: 10em;
}

.people-person h1 {
    font-size: 1.5rem;
}

.portrait-title h2 {
    font-size: 1rem;
    margin-top: 1rem;
    text-rendering: optimizelegibility;
    text-align: center;
}

.portrait-title h3 {
    font-size: .7rem;
    font-weight: 300;
    color: rgba(0,0,0,.54);
    margin: 0 0 10px;
    display: block;
    font-family: montserrat,sans-serif;
    line-height: 1.25;
    text-rendering: optimizelegibility;
    text-align: center;
}


.people-person ul {
    list-style: none;
    display: flex;
    gap: 0.5rem;
    justify-content: center;
    padding: 0;
}
</style>

```{code-cell} ipython3
---
mystnb:
  markdown_format: myst
tags: [remove-input]
---
from urllib import request
from bs4 import BeautifulSoup
from IPython.display import HTML

# Grab the latest HTML for our teams
html = request.urlopen("https://2i2c.org/organization/").read().decode()
people = BeautifulSoup(html, features="html.parser").select("div.people-widget")[0]

# Replace links and image sources with 2i2c versions so they work
for a in people.findAll('a'):
  a['href'] = a['href'].replace("/author/", "https://2i2c.org/author/")
for img in people.findAll('img'):
  img['src'] = img['src'].replace("/author/", "https://2i2c.org/author/")

# Output as HTML so MyST-NB will display it
HTML(str(people))
```

## Team member locations and times

For a quick glance at which timezone each team member is in, see the [this `whena.re` website](https://whena.re/2i2c-engineering-team), or the iframe below.

<div class="full-width">
    <iframe style="width: 100%; height: 600px" src="https://whena.re/2i2c-engineering-team" />
</div>
