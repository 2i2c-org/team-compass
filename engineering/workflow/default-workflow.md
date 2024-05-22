(coordination:workflow)=
# 2-week iterations - Our default process

```{admonition} Out of date!

Many of the sections below are out of date, particularly those related to the Engineering team's delivery workflow.
```

This section describes how our development team carries out its planning and day-to-day work.

:::{admonition} Helpful links
👉 [Here's a link to all 2i2c GitHub Issues that have been assigned to you](https://github.com/issues?q=is%3Aissue+is%3Aopen+archived%3Afalse+sort%3Aupdated-desc+assignee%3A%40me+user%3A2i2c-org)

👉 [Here's a link to see all Pull Requests for which your review is requested](https://github.com/issues?q=is%3Aopen+archived%3Afalse+sort%3Aupdated-desc+user%3A2i2c-org+type%3Apr+review-requested%3A%40me)

👉 [Here's a link to all GitHub Issues that are open but are not (yet) being tracked on a Project Board](https://github.com/search?q=is%3Aissue+org%3A2i2c-org+archived%3Afalse+is%3Aopen+no%3Aproject)
:::

(coordination:decisions)=
## Pull request workflow

See [](development:merge-policy).

(coordination:sprints)=
## Team Sprints

The 2i2c team uses Sprints to coordinate with one another in focused cycles of work.
To begin each sprint, we collectively choose items to work on in the next sprint.
Each item should have a person assigned to it, who will be responsible for ensuring that the work gets done.
However, our work within a sprint is a **team commitment**, and we are all responsible for helping one another accomplish our tasks.
Each sprint ends with a [](meetings:retrospective) in which the team reflects on what went well, what could be improved, and how to go about implementing those improvements.

### Sprint cadence

Our team works in **two-week sprints**.
Here is a brief overview of each sprint.

Beginning of sprint
: Sprint begins with our [sprint planning meeting](meetings:sprint-planning).

  In this meeting we discuss major accomplishments in the previous sprint. We then prioritize and assign the items that each team member will work on for the next sprint, and review items that require discussion and planning.

During the sprint
: Team members work on the items assigned to them at the sprint planning meeting.
  We use [the Sprint Board](coordination:sprint-board) to coordinate our activities during the sprint.
  We provide updates about what we've been up to, what we're doing next, and where we need help via regular **asynchronous Slack stand-ups**.

Last day of sprint
: By the end of the day, team members should have completed all of their items for that sprint.

(meetings:sprint-planning)=
### Sprint planning meeting

The team conducts a Sprint Planning meeting for 60 minutes at the beginning of each sprint.
The goal of this meeting is to review our major work items, synchronize with one another, and prioritize work across team members.

See [the Sprint Planning issue template](https://github.com/2i2c-org/team-compass/blob/main/.github/ISSUE_TEMPLATE/meeting-sprint-planning.md) for the agenda / structure of these meetings.
 
(coordination:sprint-board)=
### The Sprint Board

The Sprint Board is a place to keep track of the [Deliverables and tasks](coordination:deliverables) our team intends to work on for the week.
It is a GitHub Projects board that is created for each week, and closed at the end of each week.
The team's goal is to complete all items on the Sprint Board by the end of the Sprint.
This is a team commitment - while one person may be assigned to a deliverable, we all commit to working together to get the work done.

:::{admonition} The Sprint Board should...
:class: tip
- Have enough items to keep the team occupied for the week
- Not have so many items that a team member gets overwhelmed
- Under-estimate our team's total capacity, to provide room for unexpected work (e.g., support work)
- Have a team member assigned to each item on the board
:::

The Sprint Board is broken down into these columns:

- {guilabel}`Up Next` Items that are ready to be worked on.
- {guilabel}`In progress` An item that a team member is currently working towards.
- {guilabel}`Done` Items that are complete! These should be celebrated archived in the next Sprint Planning meeting.

In addition, we have a few other pieces of metadata to signal different kind of actions that would be needed 

(meetings:retrospective)=
### The Retrospective Meeting

At the end of each sprint, the team holds a retrospective meeting to reflect and generate some improvements.

#### The Duration of the Retrospective

The retrospective is one hour long on the last day of each sprint.
It is held at a time to maximise attendance from the engineering team.

% TODO: Move the meeting into the team calendar for visibility: https://calendar.google.com/calendar/embed?src=c_4hjjouojd8psql9i1a8nd1uff4%40group.calendar.google.com

#### The Roster for Facilitating Retrospectives

There is a [Google Sheet](https://docs.google.com/spreadsheets/d/1s0ZSAxwFzJ-_WgDkZeicfuUadSFEjkjS6ZcNk4N7Mmg/edit?usp=sharing) in the shared team drive that determines who will be facilitating each retrospective meeting (as well as [sprint planning](meetings:sprint-planning) and backlog refinement meetings).
Members of the engineering team are encouraged to self-nominate for this role.

#### Retrospective Tool

The team uses an [EasyRetro board](https://easyretro.io/) to collect cards representing feedback concerning the last sprint.
There are columns for: Thanks and Celebrations, things that Went Well, things To Improve, and Action Items to take forward into the next sprint.

% TODO: Add information about how to access the easyretro account

#### When should the Retro Board be Populated

The team are expected to populate the retro board before the meeting - either as thoughts occur to them throughout the sprint, or by taking some time to fill it in the day of the meeting.
This is to ensure that team members have enough time to properly articulate their thoughts and recall as much of what they want to feedback on as possible.
Some time will be reserved in the meeting to add cards to the board in case extenuating circumstances prevented team members from adding their thoughts, but this will only be a few minutes since we want to utilise the synchronous time for discussion.

#### The Retrospective Process

The retrospective meeting follows the below outline.

1. _Review the previous retrospective actions._

   % TODO: Clarify: what are we reviewing *for*?
   % TODO: Document where and how to previous retro actions can be found.

1. _Set the context for the retrospective._

   This could involve reviewing the 'Done' column in [](coordination:sprint-board).

1. _Set aside a short amount of time for the team to add any last minute cards._
   
   This should only be a few minutes.

1. _Everyone reads through (quietly to themselves) the Thanks and Celebrations, Went Well, and To Improve columns._

   During this time, the Facilitator can also add themes to the cards (in the form of hashtags) in the To Improve column to form categories, and potentially merge cards that are discussing similar issues.

1. _Discussion amongst the team on the To Improve items._

   Team members can ask clarifying questions of each other.

1. _Voting on the To Improve items._

   The team can then vote on which To Improve items they think are the most important.
   Each member gets 3 votes that they can distribute as they see fit, e.g., give all 3 votes to one item, 2 to one item and 1 to another, or 1 vote for 3 items.

1. _Identify actions._

   For the top-voted actions (limited to only 2 or 3), the team generates some concrete actions to try and resolve the issues.
   These are captured in the Action Items column.

1. _Close the meeting._

  After the meeting, the facilitator is responsible for converting the Action Items into GitHub issues to be refined for the next sprint, and then clearing the retro board.

#### How do Generated Actions move into and get committed to the Team's Next Sprint?

_TBA_

% TODO: We need to decide on this, but likely this will be in the sprint planning meeting.

(coordination:deliverables)=
## Deliverables and work issues

Deliverables represent incremental amounts of value we can deliver to a particular stakeholder.
They are **encoded as GitHub Issues** and updated over time as we learn more about the particular deliverable.
Most issues in our repositories are deliverables, in varying states of readiness.

:::{note}

We use the word "deliverable" loosely here - some issues may be more like tasks rather than an end-product.
The important thing is that they have high-quality information and structure, clearly denote value, and are actionable.

:::

### How are deliverables structured?

There are a few special sections of a deliverable issue.
Not all of them are strictly required, but are particularly useful for more complex or long-lasting deliverables.

See [this Github Issue template](https://github.com/2i2c-org/team-compass/blob/main/.github/ISSUE_TEMPLATE/01_new-issue.yml) for an example of a deliverable's structure.
Below are some major sections that are common:

Top Comment
: The top comment of a deliverable has meta information associated with that deliverable.
  This includes background information, user stories, task lists, etc.
  **The top comment should be frequently updated** by anybody on the team with relevant information to add.
  Do not hesitate to update somebody's top comment with new information, even if you didn't open the issue (though you're encouraged to leave a comment noting what has changed!).

Benefit
: What is the benefit for completing this deliverable?
  This should be in the form of [user stories](https://www.atlassian.com/agile/project-management/user-stories) that explicitly define the stakeholders that care about a deliverable, and why.

Tasks to complete
: Use task lists encode discrete steps to take in order to complete a deliverable.
  All deliverables should have either a set of concrete steps to take to meet the deliverable, or at least one task with the **acceptance criteria** for when the deliverable will be complete.
  Task lists should be in the top comment of the deliverable, and are encoded as markdown tasks lists (e.g. with `- [ ]`).
  Task lists should be updated over time as we learn the steps needed to close the deliverable.
  For more complex deliverables, these tasks may be what goes onto the Sprint Board, rather than the deliverable itself.

(coordination:deliverables-backlog)=
## The Team Backlog

[Click here to go to the Team Backlog](https://github.com/orgs/2i2c-org/projects/22).

The Team Backlog is a GitHub Projects Board with a list of [Deliverables and tasks](coordination:deliverables) across all of our active projects.
This represents the work that the team is planning to do in the near future.
These items adhere to the following principles:

- The order of items should be roughly according to priority, with higher priority items at the top of lists.
- Items on the board should have a **status** that signals whether they are ready to work or need more refinement before working.
- If an item has multiple components or would otherwise take longer than a sprint to complete, create new issues as sub-tasks, and add *them* to the Sprint Board.

### Assigning to an issue

Only assign a backlog issue to somebody if it is **actively being worked on**.
We assume that once somebody is assigned to an issue, it is part of an active sprint.
Note that **all** issues on our Sprint Backlog should have somebody assigned to them.

:::{admonition} Our definition of "Work in Progress"
Because issues that are actively being worked on must have somebody assigned to them, we use "the issues that have somebody assigned to them" as our definition of Work in Progress.
:::

### Backlog item limits

Our goal is to have backlog items that roughly cover the next 3 [sprint cycles](coordination:sprints).
We **should not have more backlog items than this amount**.

You can estimate the number of items on the board at any one time by assuming that **each team member (at 100% FTE) can accomplish about 2 items per sprint**.
You can then calculate the rough number of items on this board with the equation:

```
n_team_members * 2 (items per sprint) * 3 (sprints on the board)
```

So if we have 5.5 team members available (if one of them is at 50% FTE), then the team backlog should have around `5.5 * 2 * 3 = 33 deliverables` on it.

### Adding backlog items

We should add items to our team backlog when we have capacity to do the work in the next 3 sprints, and when those items are ready to be prioritized over all the other work that we *could* do (e.g., all issues in our repositories and encoded in project backlogs).

:::{tip}

It can be difficult to keep track of issues across all of our repositories, so using a [Project Backlog](coordination:project-backlog) can be helpful to track longer-term planning for a specific project.

:::

To add an item to the backlog, take the following steps:

- Look at the team backlog to make sure that it has capacity to absorb a new item.
- If it does not have capacity
  - Consider adding it to a [Project Backlog](coordination:project-backlog) or leave it in the issues of a repository.
    We can always get to it later.
  - Choose whether you wish to **remove** an item from the backlog in order to make space.
    Use your best judgment about whether this is the right thing to do, depending on the priority of the backlog items that are already on there.
- Place the new backlog item in the appropriate location, according to its perceived importance and urgency.

### How to prioritize backlog items

It can be difficult to prioritize backlog items, and is ultimately a subjective decision.
These criteria can be used to help guide your actions:

- **Impact**: How impactful will it be to resolve this item?
  Will it affect many users or be particularly useful?
- **Urgency**: How important is it that we resolve this item quickly?
  If it is lower impact, but urgent to accomplish, we may nonetheless wish to prioritize it.
- **Effort**: How many moving pieces does this item have and how much deep thinking will it take to resolve?
  All else being equal, we should prioritize backlog items that are easier or faster to accomplish since this will be more bang for our buck.
  This is obviously very subjective, so is probably best-estimated when there's a candidate person to work on an item.

### Working on backlog items

Backlog items are ready to work when they have enough context and tasks so that a team member can begin making progress towards closing them.
This doesn't mean that we know **all** of the tasks needed to complete the item, but that there's enough information to begin work. [^invest]

[^invest]: A good resource for considering what kinds of information makes a deliverable "ready" is [the INVEST methodology](https://agileforall.com/new-to-agile-invest-in-good-user-stories).

The team picks up work associated with a backlog item via our Sprint Planning meeting.
In this case, there are two options:

1. **Add the item to the Sprint Board**. If an item is scoped tightly enough that it can be completed within one sprint, then add it to the [Sprint Board](coordination:sprint-board) and complete it in a sprint.
2. **Generate issues from tasks and add them to the Sprint Board**. For items that are more complex and require tasks that would take more than one sprint, use the **Task List** in the issue to generate new issues for use on the Sprint Board.

   :::{tip}
   You can [use GitHub's task issue tracking features](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-task-lists) to keep track of tasks associated with an issue.
   :::

As work is done towards a backlog item, **update the top comment of the issue** with new information and tasks.
Each parent issue is the {term}`Source of Truth` for all work associated with it (instead of, for example, an issue created as a sub-task for that item).

(coordination:deliverables:upstream)=
### Tracking upstream issues

In some cases we want to do work in an upstream repository or project.
To do this, add upstream issues to our Team Backlog as we would add any other issue.

## How to keep track of projects

Longer-term projects are generally more complex and may be made up of many actions and deliverables to accomplish.
There is no official way to track long-term projects within 2i2c, but there are a few patterns that may be useful to do so, described in this section.

% TODO: We should define a more reliable process for tracking long-term projects

### Tracking issues

The simplest way to track longer-term efforts is with a **Tracking Issue**.
This is a GitHub Issue whose job is to keep track of many actions and deliverables over time that are needed to close the issue.
They are generally encoded as **Task Lists** in the issue's top comment.
Each item in the list tends to be a deliverable, and can be converted into its own GitHub Issue (e.g., to put on the [Sprint Board](coordination:sprint-board)) as-needed.

(coordination:project-backlog)=
### Project Backlogs

For more complex efforts, it can be useful to create a Project Backlog.
These are GitHub Projects boards that contain all of the deliverables that will complete a given project.
These are often organized into a few columns, representing the _state_ of each deliverable.
Here is a common column structure:

- {guilabel}`Needs Discussion/Refinement`: Deliverables that are high-priority but un-refined. Our goal should be having discussion and doing research in order to get these deliverables ready for work.
- {guilabel}`Ready to Work`: Deliverables that are well-scoped and have a clear path forward, and are thus ready to implement. As deliverables in {guilabel}`In progress` are completed, we should replace them with deliverables from this column. Generally speaking, deliverables near the top have higher priority than those at the bottom.
- {guilabel}`In progress`: Deliverables that we are currently working towards. This means that they should be added to the [Sprint Board](coordination:sprint-board) to track its completion.
- {guilabel}`Blocked`: Deliverables that require another action or delivearable from the 2i2c team to complete before they can move forward.
- {guilabel}`Waiting`: Deliverables that require another action from a **non-2i2c team member** before they can move forward.
- {guilabel}`Done`: Deliverables that have been completed. We should close these issues and celebrate the improvements that we have made!

(slack:engineering)=
## The `#engineering` Slack channel

The [`#engineering` Slack channel](https://2i2c.slack.com/archives/C055A1J1DRP) is a place for the engineering team to coordinate, plan, and discuss their work.
