(coordination:development)=
# Team development workflow

This section describes how our development team carries out its planning and day-to-day work.

:::{admonition} Helpful links
👉 [Here is a link to all 2i2c GitHub Issues that have been assigned to you](https://github.com/issues?q=is%3Aissue+is%3Aopen+archived%3Afalse+sort%3Aupdated-desc+assignee%3A%40me+user%3A2i2c-org+)
👉 [Here's a link to see all Pull Requests for which your review is requested](https://github.com/issues?q=is%3Aopen+archived%3Afalse+sort%3Aupdated-desc+user%3A2i2c-org+type%3Apr+review-requested%3A%40me+)
:::

## Cadence of work

Our team works in one week cycles.
Each cycle begins on Monday with our [team deliverables review meeting](meetings:deliverables-review).
In this meeting we prioritize and assign the items that each team member will work on for the next week, and review items that require discussion and planning.
At the end of each week, we should have completed all of the major deliverables set out for that week.
  
(coordination:deliverables)=
## Deliverables

Deliverables represent incremental amounts of value we can deliver to a particular stakeholder, and should be completable in a week.
They are **encoded as GitHub Issues**.

Most issues in our repositories are deliverables, in varying states of readiness.
Deliverables that are added to the [Activity Board](coordination:activity-board) should have enough context and tasks that a team member can realistically close them on their own. [^invest]

[^invest]: A good resource for considering what kinds of information makes a deliverable "ready" is [the INVEST methodology](https://agileforall.com/new-to-agile-invest-in-good-user-stories).

:::{admonition} Deliverables should...
:class: tip
- **Have a short title and description:** Deliverables should be glanceable and have enough context that the reader can quickly understand the scope.
- **Have one or more [user stories](https://www.atlassian.com/agile/project-management/user-stories):** User stories should define who benefits from the deliverable, and why they want it.
- **Have tasks to complete it**: Deliverables should have a set of tasks, which are actions needed to complete the deliverable.
:::

(coordination:activity-board)=
## The Activity Board

The [Activity Board](https://github.com/orgs/2i2c-org/projects/5?fullscreen=true) contains the collection of [Deliverables](coordination:deliverables) that the team is currently working on.
All deliverables on the Activity Board should be accomplished by the end of the week.
This board is filled during our [Deliverables review meeting](meetings:deliverables-review).

:::{admonition} The Activity Board should...
:class: tip
- Have enough deliverables to keep the team occupied for the week
- Not have so many deliverables that a team member gets overwhelmed
- Under-estimate our team's total capacity, to provide room for unexpected work (e.g., support work)
- Have a team member assigned to each item on the board
:::

The Activity Board is broken down into these columns:

- {guilabel}`Up Next` Deliverables that are ready to be worked on.
- {guilabel}`In progress` A deliverable that a team member is currently working towards.
- {guilabel}`Done` Tasks that are complete! When you move a task here, make sure to update any relevant deliverables.

## Requesting reviews

When you have an implementation that requires feedback, use GitHub's **Request Review** feature to ask other team members to take a look.
You can either add all team members as a request, or add specific team members if you believe they'll be particularly helpful in a review.

% TODO: We should define a more structured process for requesting reviews and how it fits in with our merge policies.

## Encoding longer-term efforts

Longer-term projects are generally more complex and may be made up of many actions and deliverables to accomplish.
There is no official way to track long-term projects within 2i2c, but there are a few patterns that may be useful to do so.

% TODO: We should define a more reliable process for tracking long-term projects

### Tracking issues

The simplest way to track longer-term efforts is with a **Tracking Issue**.
This is a GitHub Issue whose job is to keep track of many actions and deliverables over time that are needed to close the issue.
They are generally encoded as **Task Lists** in the issue's top comment.
Each item in the list tends to be a deliverable, and can be converted into its own GitHub Issue (e.g., to put on the [Activity Board](coordination:activity-board)) as-needed.

(coordination:project-backlog)=
### Project Backlogs

For more complex efforts, it can be useful to create a Project Backlog.
These are GitHub Projects boards that contain all of the deliverables that will complete a given project.
These are often organized into a few columns, representing the _state_ of each deliverable.
Here is a common column structure:

- {guilabel}`Needs Discussion/Refinement`: Deliverables that are high-priority but un-refined. Our goal should be having discussion and doing research in order to get these deliverables ready for work.
- {guilabel}`Ready to Work`: Deliverables that are well-scoped and have a clear path forward, and are thus ready to implement. As deliverables in {guilabel}`In progress` are completed, we should replace them with deliverables from this column. Generally speaking, deliverables near the top have higher priority than those at the bottom.
- {guilabel}`In progress`: Deliverables that we are currently working towards. This means that they should be added to the [Activity Board](coordination:activity-board) to track its completion.
- {guilabel}`Blocked`: Deliverables that require another action or delivearable from the 2i2c team to complete before they can move forward.
- {guilabel}`Waiting`: Deliverables that require another action from a **non-2i2c team member** before they can move forward.
- {guilabel}`Done`: Deliverables that have been completed. We should close these issues and celebrate the improvements that we have made!
