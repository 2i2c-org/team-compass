# Tech team coordination process

As a totally distributed team, it is important to have team practices that give one another insight into what we're working on, identify opportunities to collaborate, and un-block one another. This page describes some of the practices that we adopt towards these goals.


(coordination:team-syncs)=
## Weekly team syncs

Every Monday, the 2i2c Hub Operations team conducts a team sync to get on the same page and coordinate their work for the week.

A GitHub Action will automatically create a new Team Sync issue at the beginning of each Monday.
This action uses [this issue template](https://github.com/2i2c-org/team-compass/blob/main/.github/ISSUE_TEMPLATE/team-update.md) and inserts currently open/actionable issues before creating the sync issue.
It uses [this Python/ipynb script to generate the issue](https://github.com/2i2c-org/team-compass/blob/main/scripts/post-team-sync.py).

Here is the process for our team syncs.

1. **On Mondays new issue is created automatically**. This issue is our space to discuss, update, and sync.
2. **Team members give their responses**. You can copy/paste the template, and then give your responses in comments to the issue. You shouldn't feel forced to add content if you can't think of anything, use it as much as is useful.
3. **Discuss and agree on next steps throughout the day**. The goal is to ensure that important issues have somebody paying attention to them, and that team members are supported in the goals they work towards. At the end of the day the issue is automatically closed.


```{note}
While these syncs happen once a week, the process of communicating with team members and working on goals / issues / etc can be dynamic and constantly updating.
The syncs are just to get everyone on the same page.
```

## Our goals

Here are the goals we optimize for in organizing our team coordination practices.

- Give team members insight into what one another is working on (not to "report up")
- Look for opportunities to work together and/or support one another's work efficiently
- Provide some social accountability to get stuff done

We want to do this with high efficiency so that people can quickly get on the same page and focus efforts around decision-making and collaboration. We also wish to do it in a 💯 remote-friendly way since we are split across many different time-zones.

## Overview of what happens where

**Active projects list**: The 2i2c team compass has [a projects page](https://2i2c.org/team-compass/projects/) that has details about major projects that we run at 2i2c. We use this as {term}`Source of Truth` for the major projects that we are working on, and this can be a combination of development-focused things and higher-level project-focused things. These projects should contain links to the location that daily "project management" and goal-setting are happening.

**Per-project to-dos and conversation**: Generally speaking specific projects will have their own place for team conversation, to-do items, and strategy. This is generally *not* in the 2i2c team compass, but there should always be links and references in the team compass that points somebody in the right direction.

**Discussion around team practices**: For discussion around strategy that doesn't have a natural place elsewhere, we use `team-compass` issues and PRs. If an issue, it should be actionable (and "closeable"), generally in a way that results in a change to the team compass. If a PR, it should be a proposal to change the team compass and thus update some strategic information in there.

(coordination:team-activity)=
## How we organize team goals and activity

Most of the conversations and issues for the 2i2c Hub engineers happens in [the `pilot-hubs/` repository](https://github.com/2i2c-org/pilot-hubs).

### Issues to track hubs

When a new hub is created, [create a new GitHub issue for the hub](https://github.com/2i2c-org/pilot-hubs/issues/new) using the "New Hub" template.
This issue is a "meta" issue that tracks the state of this hub over time.
These issues serve both as a "Source of Truth" of information about the hub, as well as a place for conversation around operating that hub.

### Team goals

Team goals are high-level goals (AKA, there's no single action that will "complete" them) and span a longer period of time.
Goals generally contain pointers to other issues / PRs / discussions where the work of more specific tasks is getting done.
You should regularly communicate with other team members about which goals you're focusing on (e.g., via Slack, GitHub Issues, or via the [](coordination:team-syncs))

:::{tip}
When opening a new issue in the 2i2c `pilot-hubs/` repository, first check if it would be better to add it to the to-do list of a pre-existing goal.
:::

We keep track of team goals via the [{guilabel}`goal` label in GitHub](https://github.com/2i2c-org/pilot-hubs/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc+label%3Agoal).


## What about stuff that shouldn't be public?

For technical and infrastructure development, we should default to public. However, if something should *not* be public, mark it as-such in the HackMD and it won't be included in the public notes.

## Inspiration

This is a similar process as the one followed in the **jupyterhub `team-compass`**. It also follows a similar model to how [`gitlab` uses their handbook](https://about.gitlab.com/handbook/engineering/).
