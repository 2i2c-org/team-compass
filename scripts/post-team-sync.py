# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.10.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
from ghapi.all import GhApi
from IPython.display import Markdown
from datetime import date
from ghapi.actions import github_token
import os
from pathlib import Path

# %% [markdown]
# # Priority issues

# %%
# On GitHub Actions "ACCESS_TOKEN" should be a personal access token with r/w permissions to *other* repos
token = github_token() if "ACCESS_TOKEN" not in os.environ else os.environ["ACCESS_TOKEN"]

# Initialize the GH API and our markdown
api = GhApi(token=token)

# %%
# Grab Ready to Work cards that point to issues of high priority
boards = api.projects.list_for_org("2i2c-org")
priority_labels = ['prio: high', 'priority']

priority_issues = []
for board in boards:
    if "Activity" in board.name:
        continue
    columns = api.projects.list_columns(board['id'])
    for column in columns:
        if any(ii in column['name'].lower() for ii in ("in progress", "ready to work")):
            for card in api.projects.list_cards(column['id']):
                if "content_url" in card:
                    _, org, repo, _, num = card.content_url.rsplit('/', 4)
                    issue = api.issues.get(org, repo, num)
                    for prio_label in priority_labels:
                        if any(prio_label in issue_label['name'] for issue_label in issue['labels']):
                            priority_issues.append(issue)

# %% [markdown]
# # Update the template
#
# Update our team sync issue template with some priority issues.

# %%
# Read in our issue template (using `__file__` check to see if we are not running interactively)
if '__file__' not in globals():
    curdir = Path(os.getcwd())
else:
    curdir = Path(__file__).parent
template = curdir.joinpath("..", ".github", "ISSUE_TEMPLATE", "team-update.md").read_text()

# This removes the header bracketed by ---
template = "---".join(template.split("---")[2:]).strip()

# Replace our priority issues
md = [f"* [**{issue.title}**]({issue.html_url})" for issue in priority_issues]
if md:
    priority = "\n".join(md)
else:
    priority = "\nNo priority issues should be prioritized over others! 🎉\n\n"


template = template.replace(
    "{{INSERT PRIORITY ISSUES HERE}}",
    priority
)

# %% [markdown]
# # Display for demo

# %%
Markdown(template)

# %% [markdown]
# # Create an issue

# %%
# Now create an issue with this content
resp = api.issues.create("2i2c-org", "team-compass", title=f"Team Sync - {date.today():%b %d, %Y}", body=template, labels=["team-sync"])
url = f"https://github.com/{resp.url.split('repos/')[-1]}"
print(f"Finished posting team sync to {url} !")
