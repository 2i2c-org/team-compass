# GitHub repository conventions

This page describes some common conventions and patterns that we follow in our GitHub repositories.

## Issue labels

There are a few issue labels that we use to provide key metadata in our issues.
These are added to all `2i2c-org/` repositories, and share the same meaning across each.

:::{note}
- Only **Issue Type** is required for all issues.
- Repositories may define their own labels in addition to the ones described here for a given category, unless otherwise noted.
:::

### Issue Type

**REQUIRED**

Issue type determines the kind of issue and implies what sorts of actions must be taken to close it.
Issue types are mutually-exclusive - there may only be one issue type per issue.

There are a few issue types that are defined for all repositories:

- {bdg-info}`type: enhancement`: an incremental improvement to something. See [](coordination:deliverables) for more information.
- {bdg-info}`type: bug`: something that is not working or incorrect in the repository.
- {bdg-info}`type: task`: an action to take.

In addition, other repositories may use repository-specific types, with the caveat that **all issues must still only have one `type` label**.

### Issue impact

**OPTIONAL**

Issue impact is used to signal how much of an impact resolving an issue will have.
The meaning of this depends on the issue type (e.g., enhancement, bug, etc), but our general guidelines are the following:

:::{epigraph}
The impact should be proportional to a combination of:

- The number of users that will be impacted by an issue's resolution,
- The extent of the impact our users will feel (e.g., major change in experience vs. minor improvement)
- The importance of communities or stakeholders that are impacted by the issue.
:::

Here are the impact labels for our issues:

- {bdg-danger}`impact: high`
- {bdg-danger}`impact: medium`
- {bdg-danger}`impact: low`

#### Categorizing impact

Here are a few guidelines for how to categorize impact across a few major types of issues.

Features / Enhancements
: - `impact: high`: Will be seen and commonly used by nearly all users. Has been requested by an abnormally large number of users. Is of particular importance to a key community.
  - `impact: med`: Useful to many users but not an overwhelming amount. Will be a less-obvious improvement. Most issues should be in this category.
  - `impact: low`: Useful but not a critical part of workflows. Is a niche use-case that only a few users may need.

Bugs
: - `impact: high`: Disruptive to nearly all users, or critically disruptive to many users or key communities (e.g., sessions won't work at all).
  - `impact: med`: Disruptive to some users, but not in a critical way. Only noticeable under circumstances that aren't very common. Most issues should be in this category.
  - `impact: low`: Minimally disruptive or cosmetic, or only affects a small number of users or niche use-cases.

### Issue tag

**OPTIONAL**

Tag labels provide hints about what topics that issue is relevant to.
They are highly repository-specific, optional, and non-exclusive (so issues may have many tags associated with them).

Here are some example tags:

- {bdg-warning}`🏷: documentation`: related to documentation in a repository
- {bdg-warning}`🏷: CI/CD`: related to continuous integration/deployment
- {bdg-warning}`🏷: data access`: related to data access functionality
- {bdg-warning}`🏷: hub admin`: related to hub administrator functionality

## Documentation

All of our team documentation is built with the [Sphinx documentation engine](https://www.sphinx-doc.org/en/master/).
We use a [shared Sphinx theme](https://github.com/2i2c-org/sphinx-2i2c-theme/blob/main/docs/index.md) across all of our repositories, in order to standardize the look and feel of our docs, and to ensure we have cross-references and navigation links across various documentation sites.
See [the Sphinx 2i2c theme documentation](https://github.com/2i2c-org/sphinx-2i2c-theme/blob/main/docs/index.md) for instructions about how to use and contribute to this theme.
