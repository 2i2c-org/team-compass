# How we coordinate and plan

As a totally distributed team, it is important to have team practices that give one another insight into what we're working on, identify opportunities to collaborate, and un-block one another. This page describes some of the practices that we adopt towards these goals.

## What are our goals?

Here are the goals we optimize for in organizing our team coordination practices.

- Give team members insight into what one another is working on (not to "report up")
- Look for opportunities to work together and/or support one another's work efficiently
- Provide some social accountability to get stuff done

We want to do this with high efficiency so that people can quickly get on the same page and focus efforts around decision-making and collaboration. We also wish to do it in a 💯 remote-friendly way since we are split across many different time-zones.

## Team development workflow

This section describes how our development team carries out its planning and day-to-day work.
Here's a quick summary:

* [Deliverables](coordination:deliverables) are discrete units of value that we bring to others. To be ready for work, they should be scoped properly, with enough information to complete them (e.g., a set of [tasks](coordination:tasks)).
* The [Project Backlog](coordination:project-backlog) contains lists of **deliverables** that we are currently working towards across all of the 2i2c projects. Deliverables on the Project Backlog define our team priorities at any moment.
* [Tasks](coordination:tasks) are concrete actions to take, and should be accomplishable in a single work session by one person.
* The [Activity Backlog](coordination:active-backlog) contains lists of **tasks** that we are currently working on. This defines 2i2c's current activity.

(coordination:project-backlog)=
### Project Backlogs

The Project Backlog contains all of the deliverables across our projects that we wish to work on quickly.
These are organized into a few columns, representing the _state_ of each deliverable.
Here is a common column structure:

- {guilabel}`Needs Discussion/Refinement`: Deliverables that are high-priority but un-refined. Our goal should be having discussion and doing research in order to get these deliverables ready for work.
- {guilabel}`Ready to Work`: Deliverables that are well-scoped and have a clear path forward, and are thus ready to implement. As deliverables in {guilabel}`In progress` are completed, we should replace them with deliverables from this column. Generally speaking, deliverables near the top have higher priority than those at the bottom.
- {guilabel}`In progress`: Deliverables that we are currently working towards. This means that we should be generating [Tasks](coordination:tasks) in our [Activity Backlog](https://github.com/orgs/2i2c-org/projects/5?fullscreen=true) to complete this deliverable (more on this below).
- {guilabel}`Blocked/Waiting`: Deliverables for which we are waiting for some action that is out of our team's immediate control.
- {guilabel}`Done`: Deliverables that have been completed. We should close these issues and celebrate the improvements that we have made!

:::{note}
In general, there should be only two or three deliverables per team member, per column on this board.
It should not become so heavily-populated that it is hard to keep track of deliverables!
:::

There are two Project Backlogs at 2i2c:

- The [2i2c Development Projects Backlog](https://github.com/orgs/2i2c-org/projects/7?fullscreen=true) contains deliverables for our development-focused projects.
- The [Organizational Project Backlog](https://github.com/orgs/2i2c-org/projects/8?fullscreen=true) contains deliverables that are organization-wide and not related to development.

(coordination:deliverables)=
### Deliverables

Deliverables represent incremental amounts of value we can deliver to a particular stakeholder, and should be completable in a week or two. 

Most issues in our repositories are deliverables, in varying states of readiness. When a deliverable is first created, it may lack information, be improperly scoped, or have an unclear path to implementation. We improve this through _deliverable refinement_ (see below).

A deliverable is ready to work (and can thus be added to the Project Backlog) when it has the following properties (adapted from the [INVEST methodology](https://agileforall.com/new-to-agile-invest-in-good-user-stories/)).

- **Have a short title and description:** Deliverables should be glanceable and have enough context that the reader can quickly understand the scope.
- **Have one or more [user stories](https://www.atlassian.com/agile/project-management/user-stories):** User stories should define who benefits from the deliverable, and why they want it.
- **Have completion criteria:** We have clear completion criteria for this deliverable to denote it as “done”.
- **Have tasks to complete it**: Deliverables should have a set of tasks, which are actions needed to complete the deliverable.

#### How refinement happens

_Deliverable Refinement_ is the process of improving the scoping, context, and structure of our Deliverables issues so that they are ready for us to work on them. When a deliverable is created, it may not have all of the information needed to take the next step. Adding that information is the goal of Deliverable Refinement.

All team members are expected to participate in deliverable refinement, though the more experienced and higher-level you are, the more you should be contributing to this process.
The important thing is that we always have a list of high-quality deliverables ready to work towards.

Here's a small table that explains how to decide whether deliverables issues should be put in a project backlog:

:::{list-table}
:header-rows: 1
- -
  - Needs more information
  - Ready for working
- - Low priority
  - Stays in issues
  - Put in {guilabel}`Ready to work`
- - High Priority
  - Manually put in \
    {guilabel}`Needs Discussion/Refinement`
  - Put in {guilabel}`Ready to work`
:::

(coordination:active-backlog)=
### Activity Backlog

The [Activity Backlog](https://github.com/orgs/2i2c-org/projects/5?fullscreen=true) contains the collection of **Tasks** that the team is currently working on.
Tasks are actions that are needed to accomplish some deliverable.
These tasks are generated from the deliverables on the Projects Backlog.
They define a “to do” list of tasks to complete on a day-to-day basis.

The Activity Backlog is broken down into these columns:

- {guilabel}`Needs Discussion/Refinement` Tasks that require some team discussion around _implementation_. If there are higher-level discussions about the deliverable itself, perhaps the deliverable is not yet ready to be worked on.
- {guilabel}`Ready to Work` Tasks that are ready to be worked on. Roughly speaking, tasks higher on the list are of higher priority.
- {guilabel}`In progress` A task that a team member is currently working towards. When you move a task to In progress, indicate that you are working on it (either by adding your username to the card, or “assigning yourself” in the issue/PR associated with it.
- {guilabel}`Needs review` Tasks that have an implementation that require feedback from others. For example, reviews for pull requests.
- {guilabel}`Done` Tasks that are complete! When you move a task here, make sure to update any relevant deliverables.

There is one Activity Backlog defined [at this GitHub Projects Board](https://github.com/orgs/2i2c-org/projects/5?fullscreen=true).

(coordination:tasks)=
### Tasks

Deliverables of sufficient complexity are broken down into _tasks_. Tasks should be completable by a single person in less than one day (generally, completable with a few hours of focused work at most). Make sure to attach a link between your deliverable and its tasks (e.g., by adding links to issues in the deliverable’s "tasks" checklist)

Tasks are generally encoded as checklist items in a deliverable, then added to the Activity Backlog when the deliverable is being worked on.

Here’s an example of a deliverable with a few tasks:

- **Deliverable:** Side notes in Jupyter Books. \
  **User story**: _As a book author, I want to be able to create “aside” content that does not break up the narrative flow of my text._ \
  **Tasks:**
    - Create design doc for directive name and general API
    - PR to prototype functionality and documentation
    - Add tests and QA
    - Final approval + merge

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

## Taking time off

First and foremost, 2i2c fosters a culture of healthy balance between work and life. All 2i2c team members should take the time they need to thrive - this will both make you happier and help us accomplish our mission most effectively.

The 2i2c team uses [a shared Google Calendar](https://calendar.google.com/calendar/u/2?cid=Y19pNTJqZGNhbTZ0M3FsaDF1NTNqdG42MjNwY0Bncm91cC5jYWxlbmRhci5nb29nbGUuY29t) to keep track of when team members will be away.
Everyone at 2i2c has access to it, and has the ability to add events to this calendar.

**Use the Calendar to let the team know you're taking time off**.
Here are the reasons that you might do so:

**Personal Time Off**: If you're taking personal time off (e.g., vacation, holidays, personal leave, etc), add an event to this calendar with a title to let others know you'll be away.

For example:

```
AWAY: <your name> - <optional reason>
```

**Reduced time**: If you expect to be on **reduced time** for an extended period, please use the calendar for this as well.

For example:

```
REDUCED: <your name> - <optional reason>
```

**Holidays**: Please add any national holidays for your location of residence if you expect that you (or others in your location) may take time off for this as well.

For example:

```
HOLIDAY: <holiday name>
```
