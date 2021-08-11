(coordination:development)=
# Team development workflow

This section describes how our development team carries out its planning and day-to-day work.

:::{admonition} Helpful links
👉 [Here is a link to all 2i2c GitHub Issues that have been assigned to you](https://github.com/issues?q=is%3Aissue+is%3Aopen+archived%3Afalse+sort%3Aupdated-desc+assignee%3A%40me+user%3A2i2c-org+)
👉 [Here's a link to see all Pull Requests for which your review is requested](https://github.com/issues?q=is%3Aopen+archived%3Afalse+sort%3Aupdated-desc+user%3A2i2c-org+type%3Apr+review-requested%3A%40me+)
:::

## Cadence of work

Our team works in one week sprints.
Here is a brief overview of each sprint.

Monday
: Sprint begins with our [sprint planning meeting](meetings:sprint-planning).

  In this meeting we prioritize and assign the items that each team member will work on for this week, and review items that require discussion and planning.

Tues-Thurs
: Team members work on the deliverables assigned to them at the sprint planning meeting.

Friday
: By the end of the day, team members should have completed all of their deliverables for that week.
  Each team member fills out a **team sync update** to share the major things they worked on, and note any unexpected challenges or blockers.

(coordination:deliverables)=
## Deliverables

Deliverables represent incremental amounts of value we can deliver to a particular stakeholder.
They are **encoded as GitHub Issues** and updated over time as we learn more about the particular deliverable.
Most issues in our repositories are deliverables, in varying states of readiness.

### How are deliverables structured?

There are a few special sections of a deliverable issue.
Not all of them are strictly required, but are particularly useful for more complex or long-lasting deliverables.

See [this Github Issue template](https://github.com/2i2c-org/team-compass/blob/main/.github/ISSUE_TEMPLATE/new-deliverable.md) for an example of a deliverable's structure.
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
  All deliverables should have either a set of concrete steps to take to meet the delivearble, or at least one task with the **acceptance criteria** for when the deliverable will be complete.
  Task lists should be in the top comment of the deliverable, and are encoded as markdown tasks lists (e.g. with `- [ ]`).
  Task lists should be updated over time as we learn the steps needed to close the deliverable.
  For more complex deliverables, these tasks may be what goes onto the Sprint Board, rather than the deliverable itself.

### Working on deliverables

Deliverables are ready to work when they have enough context and tasks so that a team member can begin making progress towards closing them.
This doesn't mean that we know **all** of the tasks needed to complete the deliverable, but that there's enough information to begin work. [^invest]

[^invest]: A good resource for considering what kinds of information makes a deliverable "ready" is [the INVEST methodology](https://agileforall.com/new-to-agile-invest-in-good-user-stories).

The team picks up work associated with a deliverable via our Sprint Planning meeting.
In this case, there are two options:

1. **Add the deliverable to the Sprint Board**. If a deliverable is scoped tightly enough that it can be completed within one sprint, then add it to the [Sprint Board](coordination:sprint-board) and complete it in a sprint.
2. **Generate issues from tasks and add them to the Sprint Board**. For deliverables that are more complex and require tasks that would take more than one sprint, use the **Task List** in the deliverable to generate issues for use on the Sprint Board.

   :::{tip}
   You can [use GitHub's task issue tracking features](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-task-lists) to keep track of tasks associated with a deliverable issue.
   :::

As work is done towards a deliverable, update the top comment of the **deliverable** with new information and tasks.
The deliverable issue is the {term}`Source of Truth` for all work associated with it (instead of, for example, an issue created for a task for that deliverable).

(coordination:deliverables-backlog)=
## The Deliverables Backlog

[Click here to go to the Deliverables Backlog](https://github.com/orgs/2i2c-org/projects/7?fullscreen=true).

The Deliverables Backlog is a GitHub Projects Board with a list of [Deliverables](coordination:deliverables) across all of our active projects.
These deliverables adhere to the following principles:

- Each item on this board should be **ready to work**, meaning that it has enough background information and context for a team member to steward it to completion.
- The order of these deliverables should be roughly according to priority, with higher priority deliverables at the top of lists.
- High-priority deliverables should be added to a [weekly sprint board](coordination:sprint-board) in order to be worked on.
- If a deliverable has multiple components or would otherwise take longer than a week to complete, create task lists inside it to track steps. Add those steps to the Sprint board, not the whole deliverable.

(coordination:sprint-board)=
## The Sprint Board

The Sprint Board is a place to keep track of the [Deliverables](coordination:deliverables) our team intends to work on for the week.
It is a GitHub Projects board that is created for each week, and closed at the end of each week.
All deliverables on the Sprint Board should be accomplished by the end of the week.
This board is filled during our [Sprint Planning meeting](meetings:sprint-planning).

:::{admonition} The Sprint Board should...
:class: tip
- Have enough deliverables/tasks to keep the team occupied for the week
- Not have so many deliverables that a team member gets overwhelmed
- Under-estimate our team's total capacity, to provide room for unexpected work (e.g., support work)
- Have a team member assigned to each item on the board
:::

The Sprint Board is broken down into these columns:

- {guilabel}`Up Next` Deliverables that are ready to be worked on.
- {guilabel}`In progress` A deliverable that a team member is currently working towards.
- {guilabel}`Done` Tasks that are complete! When you move a task here, make sure to update any relevant deliverables.

## Requesting reviews

When you have an implementation that requires feedback, use GitHub's **Request Review** feature to ask other team members to take a look.
In general, add specific team members so that it is clear who is needed to review the PR.

% TODO: We should define a more structured process for requesting reviews and how it fits in with our merge policies.

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
