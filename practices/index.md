# Team Practices

As a totally distributed team, it is important to have team practices that give one another insight into what we're working on, identify opportunities to collaborate, and un-block one another.
This chapter describes some of the practices that we adopt towards these goals.

## What are our goals?

Here are the goals we optimize for in organizing our team coordination practices.

- Give team members insight into what one another is working on (not to "report up")
- Look for opportunities to work together and/or support one another's work efficiently
- Provide some social accountability to get stuff done

We want to do this with high efficiency so that people can quickly get on the same page and focus efforts around decision-making and collaboration. We also wish to do it in a 💯 remote-friendly way since we are split across many different time-zones.


(coordination:team-syncs)=
## Weekly team syncs

Every Monday, the 2i2c Hub Operations team conducts a team sync to get on the same page and coordinate their tasks for the week.

A GitHub Action will automatically create a new Team Sync issue at the beginning of each Monday.
This action uses [this issue template](https://github.com/2i2c-org/team-compass/blob/main/.github/ISSUE_TEMPLATE/team-update.md) and inserts currently open/actionable issues before creating the sync issue.
It uses [this Python/ipynb script to generate the issue](https://github.com/2i2c-org/team-compass/blob/main/scripts/post-team-sync.py).

Here is the process for our team syncs.

1. **On Mondays a new issue is created automatically**. This issue is our space to discuss, update, and sync.
2. **Team members give their responses**. You can copy/paste the template, and then give your responses in comments to the issue. You shouldn't feel forced to add content if you can't think of anything, use it as much as is useful.
3. **Discuss and agree on next steps throughout the day**. The goal is to ensure that important issues have somebody paying attention to them, and that team members are supported in the tasks they work towards. At the end of the day the issue is automatically closed.

```{note}
While these syncs happen once a week, the process of communicating with team members and working on tasks / deliverables can be dynamic and constantly updating.
The syncs are just to get everyone on the same page.
```

```{toctree}
communication
development
secrets
cloud-access
meetings
github-conventions
team-compass
```
