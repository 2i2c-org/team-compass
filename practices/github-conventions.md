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

- {badge}`type: enhancement, badge-info`: an improvement to be made to the repository.
- {badge}`type: bug, badge-info`: something that is not working or incorrect in the repository.
- {badge}`type: task, badge-info`: an action to take that is not well-categorized by enhancement/bug.

In addition, other repositories may use repository-specific types, with the caveat that **all issues must still only have one `type` label**.

### Issue priority

**OPTIONAL**

Issue priority is used to classify some issues as requiring action before others.
Any issue without a priority tag should be assumed as lower priority than {badge}`prio: low,badge-danger`.
 
Here are the priority labels for our issues:

- {badge}`prio: high, badge-danger`
- {badge}`prio: medium, badge-danger`
- {badge}`prio: low, badge-danger`

### Issue tag

**OPTIONAL**

Tag labels provide hints about what topics that issue is relevant to.
They are highly repository-specific, optional, and non-exclusive (so issues may have many tags associated with them).

Here are some example tags:

- {badge}`🏷: documentation,badge-warning`: related to documentation in a repository
- {badge}`🏷: CI/CD,badge-warning`: related to continuous integration/deployment
- {badge}`🏷: documentation,badge-warning`: related to data access functionality
- {badge}`🏷: hub admin,badge-warning`: related to hub administrator functionality
