# How we coordinate and plan

As a totally distributed team, it is important to have team practices that give one another insight into what we're working on, identify opportunities to collaborate, and un-block one another. This page describes some of the practices that we adopt towards these goals.

## What are our goals?

Here are the goals we optimize for in organizing our team coordination practices.

- Give team members insight into what one another is working on (not to "report up")
- Look for opportunities to work together and/or support one another's work efficiently
- Provide some social accountability to get stuff done

We want to do this with high efficiency so that people can quickly get on the same page and focus efforts around decision-making and collaboration. We also wish to do it in a 💯 remote-friendly way since we are split across many different time-zones.


## Projects and deliverables are our main units of work

A new project should be created for anything with a specific scope and set of deliverables that spans a reasonably long amount of time. 2i2c projects should all feed into the [2i2c organizational strategy and goals](../about/strategy.md).

Each project should have the following things:

1. **Summarize the project**. What is the overarching scope and deverables for the project? Who is it in collaboration with? How does it fit in with the overarching [strategic goals of 2i2c](../about/strategy.md)?
2. **Define the project's key goal**. What is the one key goal to accomplish with this project?
3. **A {term}`Source of Truth`**.  Where does project management and tracking take place? Where do we track progress? What about to-do items? Where does communication happen around this project? (e.g., in a GitHub repository, in Slack, in a Google doc).
4. **A collection of deliverables**. What are the deliverables that must exist in order to complete the project? These can start off more abstract, but over time they should become more concrete, and ultimately, lead to actionable tasks.

:::{note}
Deliverables are generally written as **user stories** - that is, with a particular user in mind, and a particular outcome they want to see.
For example, "As a 2i2c Hub User, I want to install a package on my own."
Deliverables should be accomplishable in one or two sprints, and may have many tasks associated with them.
:::

## Tasks are steps to complete a deliverable

In order to meet a deliverable, we need to take a set of actions, called **Tasks**.
Tasks are verbs, not outcomes, and they should be extremely concrete and obvious what needs to be done.
In addition, they should be accomplishable in one setting.

Tasks are the things that 2i2c team members *plan to do* in a sprint.
This helps keep our actions concrete, while still working towards a deliverable.

### Keeping track of our goals

:::{warning}
We are considering phasing out team goals, and simply using **Projects** and **Deliverables** as described above.
:::

Team goals are high-level goals (AKA, there's no single action that will "complete" them) and span a longer period of time.
Goals generally contain pointers to other issues / PRs / discussions where the work of more specific tasks is getting done.
You should regularly communicate with other team members about which goals you're focusing on (e.g., via Slack, GitHub Issues, or via the [](coordination:team-syncs))

:::{tip}
When opening a new issue in the 2i2c `pilot-hubs/` repository, first check if it would be better to add it to the to-do list of a pre-existing goal.
:::

We keep track of team goals via the [{guilabel}`goal` label in GitHub](https://github.com/2i2c-org/pilot-hubs/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc+label%3Agoal).

(coordination:team-syncs)=
## Weekly team syncs

Every Monday, the 2i2c Hub Operations team conducts a team sync to get on the same page and coordinate their tasks for the week.

A GitHub Action will automatically create a new Team Sync issue at the beginning of each Monday.
This action uses [this issue template](https://github.com/2i2c-org/team-compass/blob/main/.github/ISSUE_TEMPLATE/team-update.md) and inserts currently open/actionable issues before creating the sync issue.
It uses [this Python/ipynb script to generate the issue](https://github.com/2i2c-org/team-compass/blob/main/scripts/post-team-sync.py).

Here is the process for our team syncs.

1. **On Mondays new issue is created automatically**. This issue is our space to discuss, update, and sync.
2. **Team members give their responses**. You can copy/paste the template, and then give your responses in comments to the issue. You shouldn't feel forced to add content if you can't think of anything, use it as much as is useful.
3. **Discuss and agree on next steps throughout the day**. The goal is to ensure that important issues have somebody paying attention to them, and that team members are supported in the tasks they work towards. At the end of the day the issue is automatically closed.


```{note}
While these syncs happen once a week, the process of communicating with team members and working on tasks / deliverables can be dynamic and constantly updating.
The syncs are just to get everyone on the same page.
```



## What about stuff that shouldn't be public?

For technical and infrastructure development, we should default to public. However, if something should *not* be public, mark it as-such in the HackMD and it won't be included in the public notes.
