# ---
# jupyter:
#   jupytext:
#     formats: py:hydrogen
#     text_representation:
#       extension: .py
#       format_name: hydrogen
#       format_version: '1.3'
#       jupytext_version: 1.10.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Sort cards
#
# Sort cards across all 2i2c organization-level repositories based on priority labels.

# %%
from ghapi.all import GhApi
from ghapi.actions import github_token
import os

# On GitHub Actions "ACCESS_TOKEN" should be a personal access token with r/w permissions to *other* repos
token = (
    github_token() if "ACCESS_TOKEN" not in os.environ else os.environ["ACCESS_TOKEN"]
)

# Initialize the GH API and our markdown
api = GhApi(token=token)

# These are our priority labels, in order of preferred position
priority_list = ["priority", "prio: high", "prio: med", "prio: low"]


def sort_cards(column, sort_labels, api):
    """Sort the cards in a GitHub Project column based on a list of labels.
    
    Note: cards that do not directly point to a GitHub issue will be treated
    like cards with issues that do not have one of the specified labels.
    
    Parameters
    ----------
    column: column instance
        A `ghapi` column instance
    sort_labels: list of strings
        A list of strings to use in sorting your cards. The cards will be sorted
        such that cards with first item of `sort_labels` will come first.
    """
    cards = api.projects.list_cards(column["id"])

    # Remove cards that don't directly point to an issue
    cards = [card for card in cards if "content_url" in card]

    # Grab a list of labels for each card, only keep the ones in our sort_list
    cards_with_sorting_label = []
    for card in cards:
        _, org, repo, _, num = card["content_url"].rsplit("/", 4)
        for label in api.issues.list_labels_on_issue(org, repo, num):
            if label["name"] in sort_labels:
                card["sort_label"] = label["name"]
                cards_with_sorting_label.append(card)

    # Sort the cards based on the sorting label
    cards_sorted = sorted(
        cards_with_sorting_label, key=lambda a: priority_list.index(a["sort_label"])
    )

    # Loop through the sorted cards (in reverse so we move the last label first) and move them to the top
    for card in cards_sorted[::-1]:
        api.projects.move_card(card["id"], position="top")
        print(f"\t\tMoved card {card['id']} to top")


# Loop through our projects to sort cards
for project in api.projects.list_for_org("2i2c-org"):
    print(f"Sorting columns for project {project['name']}")

    columns = api.projects.list_columns(project["id"])
    for column in columns:
        if any(ii in column["name"].lower() for ii in ["archive", "done"]):
            continue
        print(f"\tSorting column {column['name']}")
        cards = sort_cards(column, priority_list, api)
