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

The 2i2c team is defined on [the `team/` page of our website](https://2i2c.org/team/).
Below is a summary of the people on that page.

% Uses the CSV auto-generated from the HTML at https://2i2c.org/team/

```{code-cell}
---
mystnb:
  markdown_format: myst
tags: [remove-input]
---
import pandas as pd
from IPython.display import display, Markdown

# This should be generated automatically by `conf.py`
team = pd.read_csv("../tmp/team_membership.csv").fillna("")

for team, people in team.groupby("team", sort=False):
    display(Markdown(f"**{team}**"))
    display(Markdown(people.drop(columns=["team"]).to_markdown(index=False)))
```

## Engineering team locations and times

For a quick glance at which timezone each team member is in, see the [this `whena.re` website](https://whena.re/2i2c-engineering-team), or the iframe below.

<div class="full-width">
    <iframe style="width: 100%; height: 600px" src="https://whena.re/2i2c-engineering-team" />
</div>
