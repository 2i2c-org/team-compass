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

token = github_token() if "GHAPI_TOKEN" not in os.environ else os.environ["API_TOKEN"]

# %%
# Initialize the GH API and our markdown
api = GhApi(token=github_token())
md = ""

# %% [markdown]
# # New Hubs

# %%
issues = api.issues.list_for_repo("2i2c-org", "pilot-hubs", labels="Needs Hub")
md += "**New Hubs**: _The [Needs Hub issues](https://github.com/2i2c-org/pilot-hubs/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc+label%3A%22Needs+Hub%22) are new hubs that need deployments._\n"
if issues:
    md += "\n".join([f"* [{issue.title}]({issue.url})" for issue in issues])+ "\n\n"
else:
    md += "No new hubs to deploy! 🎉\n\n"

# %% [markdown]
# # Needs Triage

# %%
issues = api.issues.list_for_repo("2i2c-org", "pilot", labels="needs:triage")
md += "**Needs Triage**: _The [Needs Triage issues](https://github.com/2i2c-org/pilot/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc+label%3Aneeds%3Atriage) require an initial assessment and labeling._\n"
if issues:
    md += "\n".join([f"* [{issue.title}]({issue.url})" for issue in issues])+ "\n\n"
else:
    md += "No issues need triage! 🎉\n\n"

# %% [markdown]
# # Priority issues

# %%
issues = api.issues.list_for_repo("2i2c-org", "pilot-hubs", labels="priority")
md += "**Priority Issues**: _The [Priority Label issues](https://github.com/2i2c-org/pilot-hubs/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc+label%3Apriority) are important and should be given attention over other issues._\n"
if issues:
    md += "\n".join([f"* [{issue.title}]({issue.url})" for issue in issues])+ "\n\n"
else:
    md += "\nNo priority issues to tackle! 🎉\n\n"

# %% [markdown]
# # Display for demo

# %%
Markdown(md)

# %% [markdown]
# # Create an issue

# %%
# Grab our issue template
from base64 import b64decode
template = api.repos.get_content("2i2c-org", "team-compass", ".github/ISSUE_TEMPLATE/team-update.md")
template = b64decode(template.content).decode("utf-8")
template = template.replace("{GENERATE PROGRAMMATICALLY OR ADD HERE BY HAND}", md)

# This removes the header bracketed by ---
template = "---".join(template.split("---")[2:]).strip()

# %%
# Now create an issue with this content
resp = api.issues.create("2i2c-org", "team-compass", title=f"Team Sync - {date.today():%b %d, %Y}", body=template, labels=["team-sync"])
url = f"https://github.com/{resp.url.split('repos/')[-1]}"
print(f"Finished posting team sync to {url} !")
