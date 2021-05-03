# GitHub repository conventions

This page describes team 

## Issue labels

There are a few issue labels that we use to provide key metadata in our issues.
These are added to all `2i2c-org/` repositories, and share the same meaning across each.

### Issue Type

**REQUIRED**

Issue type determines the kind of issue and implies what sorts of actions must be taken to close it.
Issue types are mutually-exclusive - there may only be one issue type per issue.

There are a few issue types that are defined for all repositories:

- {badge}`type: enhancement, badge-info`: an improvement to be made to the repository.
- {badge}`type: bug, badge-info`: something that is not working or incorrect in the repository.
- {badge}`type: task, badge-info`: an action to take that is not well-categorized by enhancement/bug.
- {badge}`type: goal, badge-info`: a high-level goal or outcome that we should work towards, with a specific completion criteria.

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

### Issue State

**OPTIONAL**

Issue state describes the current state of an issue, and implies the next action that must be taken in order to close it.
Issue states are mutually-exclusive - there should not be more than one state label for an issue.
Issues without a state label are assumed to be ready for implementation.

There are a few issue states that are defined for all repositories:

- {badge}`state: needs-info, badge-secondary`: the issue requires more information from the author in order to move forward. It may be closed after a few days of non-response.
- {badge}`state: needs-discussion, badge-secondary`: the issue requires discussion and scoping from the team to create an actionable path.
- {badge}`state: duplicate, badge-secondary`: the issue has already been reported. It may be closed with a link the the original issue.
- {badge}`state: invalid, badge-secondary`: the reported problem cannot be reproduced, or the requested feature or task is not appropriate. It may be closed.
- {badge}`state: upstream, badge-secondary`: resolution depends on actions of other 3rd party projects. It may be closed if necessary, or left open if needed for tracking.
- {badge}`state: wontfix, badge-secondary`: determined to be a real issue, but for strong reasons the behavior will not be changed. It may be closed.
