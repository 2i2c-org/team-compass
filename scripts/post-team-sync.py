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
from textwrap import dedent
from datetime import date
from ghapi.actions import github_token
import os

# On GitHub Actions "ACCESS_TOKEN" should be a personal access token with r/w permissions to *other* repos
token = github_token() if "ACCESS_TOKEN" not in os.environ else os.environ["ACCESS_TOKEN"]

# %%
# Initialize the GH API and our markdown
api = GhApi(token=token)

# %% [markdown]
# # Base template
# The base template is defined here: https://github.com/2i2c-org/team-compass/blob/main/.github/ISSUE_TEMPLATE/team-update.md
# It has placeholders for lists of issues, and these will be automatically filled in below, then a new issue will be created.

# %%
# Grab our issue template
from base64 import b64decode
template = api.repos.get_content("2i2c-org", "team-compass", ".github/ISSUE_TEMPLATE/team-update.md")
template = b64decode(template.content).decode("utf-8")

# This removes the header bracketed by ---
template = "---".join(template.split("---")[2:]).strip()

# %% [markdown]
# # New Hubs

# %%
issues = api.issues.list_for_repo("2i2c-org", "pilot-hubs", labels="Needs Hub")
if issues:
    new_hubs = "\n".join([f"* [{issue.title}]({issue.html_url})" for issue in issues])+ "\n\n"
else:
    new_hubs = "No new hubs to deploy! 🎉\n\n"
template = template.replace(
    "{{INSERT NEW HUBS ISSUES HERE}}",
    new_hubs
)

# %% [markdown]
# # Needs Triage

# %%
issues = api.issues.list_for_repo("2i2c-org", "pilot", labels="needs:triage")
if issues:
    needs_triage = "\n".join([f"* [{issue.title}]({issue.html_url})" for issue in issues])+ "\n\n"
else:
    needs_triage = "No issues need triage! 🎉\n\n"
    
template = template.replace(
    "{{INSERT NEEDS TRIAGE ISSUES HERE}}",
    needs_triage
)

# %% [markdown]
# # Priority issues

# %%
issues = api.issues.list_for_repo("2i2c-org", "pilot-hubs", labels="priority")
if issues:
    priority = "\n".join([f"* [{issue.title}]({issue.html_url})" for issue in issues])+ "\n\n"
else:
    priority = "\nNo priority issues to tackle! 🎉\n\n"
    
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
