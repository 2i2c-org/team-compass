(coordination:development)=
# Development and backlog workflow

This section describes how our development team carries out its planning and day-to-day work.

:::{admonition} Helpful links
👉 [Here is a link to all 2i2c GitHub Issues that have been assigned to you](https://github.com/issues?q=is%3Aissue+is%3Aopen+archived%3Afalse+sort%3Aupdated-desc+assignee%3A%40me+user%3A2i2c-org)

👉 [Here's a link to see all Pull Requests for which your review is requested](https://github.com/issues?q=is%3Aopen+archived%3Afalse+sort%3Aupdated-desc+user%3A2i2c-org+type%3Apr+review-requested%3A%40me)
:::

(coordination:cycles)=
## Team Cycles

To begin each cycle, we collectively choose items to work on (or continue working) in the next cycle.
Each item should have a person assigned to it, who will be responsible for ensuring that the work gets done and a another person as a helper.
However, our work within a cycle is a **team commitment**, and we are all responsible for helping one another accomplish our tasks.

### Cycle cadence

Our team works in **two-week cycles**.
Here is a brief overview of each cycle.

Wednesday (beginning of cycle)
: Cycle begins with our [coordination planning meeting](meetings:coordination-planning).

  In this meeting we discuss major accomplishments in the previous cycle. We then prioritize and assign the items that each team member will work on for the next cycle, and review items that require discussion and planning.

During the cycle
: Team members work on the items assigned to them at the coordination planning meeting.
  We use [the Team Backlog Board](coordination:deliverables-backlog) to coordinate our activities during the cycle.
  We provide updates about what we've been up to, what we're doing next, and where we need help via regular **asynchronous Slack stand-ups**.
  We add issues (or standalone PRs) belonging to the activities developed during the cycle into the [the Cycle Board](coordination:cycle-board).

(coordination:planning)=  
### Coordination planning meeting

The team conducts a Coordination Planning meeting for 60 minutes at the beginning of each cycle.
The goal of this meeting is to review our major work items, synchronize with one another, and prioritize work across team members.
Our **Project Manager** role leads these meetings.
It is also a chance to hand off the Support Steward role to the next person.

See [the Coordination Planning issue template](https://github.com/2i2c-org/team-compass/blob/main/.github/ISSUE_TEMPLATE/meeting-coordination-planning.md) for the agenda / structure of these meetings.

(coordination:cycle-board)=
### The Cycle Board

The Cycle Board is a place to keep track of the [Deliverables and tasks](coordination:deliverables) our team is working on for the cycle.
It is a GitHub Projects board that is created for each cycle, and closed at the end of each cycle.

The Cycle Board is broken down into these columns:

- {guilabel}`Todo` Items that are ready to be worked on.
- {guilabel}`In Progress` An item that a team member is currently working towards.
- {guilabel}`Review / QA` Items that are ready to be reviewed/tested.
- {guilabel}`Done` Items that are complete! These should be celebrated and archived in the next Coordination Planning meeting.

(coordination:team-syncs)=
## Daily team syncs

Throughout the week we have a lightweight asynchronous team sync process so that we can get on the same page.
These currently happen on Monday, Wednesday, and Friday in the morning time of each team member.
The primary goals of this process are:

- To ensure that nobody is stuck on something
- To signal-boost requests for review and help
- To provide accountability of what we've been up to
- To help us coordinate what to do next

We use [the Geekbot](https://geekbot.com/) to manage this process.
During a sync, each team member gets a message in their morning time with a few questions.
Answer each question, and at the end the answers will be posted to our `#team-updates` channel.

:::{seealso}
You can customize the way that Geekbot standups work for you.
See [the Geekbot workflow guides](https://help.geekbot.com/en/articles/4283332-commands-how-to-streamline-your-workflow) for some helpful information.
:::

:::{admonition} TODO: Share this publicly
We are exploring ways to aggregate and share our team sync activity publicly, to be more transparent with others about what we are up to.
We will update this section once we better-understand this process.
:::

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
  For more complex deliverables, these tasks may be what goes onto the Cycle Board, rather than the deliverable itself.

(coordination:deliverables-backlog)=
## The Team Backlog

[Click here to go to the Team Backlog](https://github.com/orgs/2i2c-org/projects/22).

The Team Backlog is a GitHub Projects Board with a list of [Deliverables and tasks](coordination:deliverables) across all of our active projects.
This represents the work that the team is doing AND planning to do in the near future.
These items adhere to the following principles:

- The order of items should be roughly according to priority, with higher priority items at the top of lists.
- Items on the board should have a **status** that signals whether they are ready to work or need more refinement before working.
- If an item has multiple components or would otherwise take longer than a cycle to complete, create new issues as sub-tasks, and add *them* to a dedicated [Project Backlog](coordination:project-backlog).

### Assigning to an issue

Only assign a backlog issue to somebody if it is **actively being worked on**.
We assume that once somebody is assigned to an issue, it is part of an active cycle.
Note that **all** issues on our Cycle Backlog should have somebody assigned to them.

:::{admonition} Our definition of "Work in Progress"
Because issues that are actively being worked on must have somebody assigned to them, we use "the issues that have somebody assigned to them" as our definition of Work in Progress.
:::

### Backlog item limits

Our goal is to have backlog items that roughly cover the next 3 [cycle cycles](coordination:cycles).
We **should not have more backlog items than this amount**.

You can estimate the number of items on the board at any one time by assuming that **each team member (at 100% FTE) can accomplish about 2 items per cycle**.
You can then calculate the rough number of items on this board with the equation:

```
n_team_members * 2 (items per cycle) * 3 (cycles on the board)
```

So if we have 5.5 team members available (if one of them is at 50% FTE), then the team backlog should have around `5.5 * 2 * 3 = 33 deliverables` on it.

### Adding backlog items

We should add items to our team backlog when we have capacity to do the work in the next 3 cycles, and when those items are ready to be prioritized over all the other work that we *could* do (e.g., all issues in our repositories and encoded in project backlogs).

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

The team picks up work associated with a backlog item via our Coordination Planning meeting.
In this case, there are three options:

1. **Add the item to the Team Backlog Board**. If an item is scoped tightly enough that it can be completed within one cycle, then add it to the [Team Backlog Board](coordination:deliverables-backlog) and complete it in a cycle.
2. **Generate issues from tasks and add the parent item to the Team Backlog Board**. For items that are more complex and require tasks that would take more than one cycle, use the **Task List** in the issue to generate new issues.

   :::{tip}
   You can [use GitHub's task issue tracking features](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-task-lists) to keep track of tasks associated with an issue.
   :::

As work is done towards a backlog item, **update the top comment of the issue** with new information and tasks.
Each parent issue is the {term}`Source of Truth` for all work associated with it (instead of, for example, an issue created as a sub-task for that item).

   :::{tip}
   Using a dedicated [Project Backlog](coordination:project-backlog) can be helpful to track longer-term planning (encompassing multiple cycles) for a specific project.
   :::

(coordination:deliverables:upstream)=
### Tracking upstream issues

In some cases we want to do work in an upstream repository or project.
To do this, add upstream issues to our Team Backlog as we would add any other issue.

(development:merge-policy)=
## Merging and Reviewing policy

The sections below describe major policies around merging and reviewing depending on the kind of change being made.
There are some extra policies for changes that **affect actively-running infrastructure**.
See the section below for details.

Not all of them are followed strictly, though some are more important than others, and are marked with **REQUIRED**.

- **Always make a Pull Request**. (REQUIRED).
  All changes to 2i2c repositories should be made via a Pull Request.
  This should be enforced by setting the `main`/`master` branch of each repository to be "protected".
- **PRs should reference (and close) issues**.
  A pull request should almost always be related to an issue.
  Ideally, the issue should be tightly-scoped enough that the PR will close it when merged.
  If you have an idea that *doesn't* yet have an issue, open an issue first and then make the PR to close it.
  This ensures that the team has context around Pull Requests, and a chance to discuss before we implement.
- **Use GitHub's `Request Review` feature**.
  Add specific team members so that it is clear who is needed to review the PR.
- **Be explicit about what feedback you want**.
  When you open a PR, include some language about specific things you'd like feedback with, if applicable.
  This helps others focus their attention.
- **Use the Slack Geekbot to ask for help**.
  When a PR needs review and there is no feedback, use the help section from the bot update to ask others for feedback!
- **Merge after one approval**.
  If there is at least one approval on a PR, then anybody, including the PR author, may merge the PR.
  PR authors should not hesitate to merge their own PR after an approval if they think it is ready to go!
- **Merging without review is discouraged, but not forbidden**.
  For changes that are minor, very straightforward, and do not affect actively-running infrastructure, it is acceptable to self-merge a PR without getting an approval.  
  If you don't believe that your PR requires an approval before merging, make it clear in your PR or in a comment that you plan to merge it in 24 hours.
- **Leave PRs open for at least 24 working hours**.
  This helps ensure that others on the team have a chance to look at the PR and give their thoughts (by working hours we mean hours during a weekday).


### Policy for changes to running infrastructure

Changing active infrastructure is a bit different from developing technology that is not immediately in production.
As such, we follow some more specific guidelines for these kinds of changes.
See {ref}`infra:infrastructure:review`.

### Policy for team compass changes

If a change affects the 2i2c team policies, or makes significant changes to our documentation or public-facing material, then you should also follow these extra policies:

- **Ensure that the team has consented**.
  For any major change, you should make sure that you have followed best-practices in consent-based decision making. See [](development:decisions) for more information.

## How to keep track of projects

Longer-term projects are generally more complex and may be made up of many actions and deliverables to accomplish.
There is no official way to track long-term projects within 2i2c, but there are a few patterns that may be useful to do so, described in this section.

% TODO: We should define a more reliable process for tracking long-term projects

### Tracking issues

The simplest way to track longer-term efforts is with a **Tracking Issue**.
This is a GitHub Issue whose job is to keep track of many actions and deliverables over time that are needed to close the issue.
They are generally encoded as **Task Lists** in the issue's top comment.
Each item in the list tends to be a deliverable, and can be converted into its own GitHub Issue as-needed.

(coordination:project-backlog)=
### Project Backlogs

For more complex efforts, it can be useful to create a Project Backlog.
These are GitHub Projects boards that contain all of the deliverables that will complete a given project.
These are often organized into a few columns, representing the _state_ of each deliverable.
Here is a common column structure:

- {guilabel}`Needs Discussion/Refinement`: Deliverables that are high-priority but un-refined. Our goal should be having discussion and doing research in order to get these deliverables ready for work.
- {guilabel}`Ready to Work`: Deliverables that are well-scoped and have a clear path forward, and are thus ready to implement. As deliverables in {guilabel}`In progress` are completed, we should replace them with deliverables from this column. Generally speaking, deliverables near the top have higher priority than those at the bottom.
- {guilabel}`In progress`: Deliverables that we are currently working towards. This means that they should be added to the [Cycle Board](coordination:cycle-board) to track its completion.
- {guilabel}`Blocked`: Deliverables that require another action or delivearable from the 2i2c team to complete before they can move forward.
- {guilabel}`Waiting`: Deliverables that require another action from a **non-2i2c team member** before they can move forward.
- {guilabel}`Done`: Deliverables that have been completed. We should close these issues and celebrate the improvements that we have made!

(development:decisions)=
## How we make decisions

The 2i2c Team follows [consent based decision-making](https://thedecider.app/consent-decision-making) in making all of its team decisions.
This roughly means the following for **any decision that impacts all team members**:

- The proposed decision and relevant context must be available to all team members.
  This is generally done via opening GitHub issues.
- Ensure that team members have time to understand the proposal, and ask questions about it to understand its ramifications.
- Ensure that team members have time to object and make suggested changes.
- Ensure that the result of the decision is recorded somewhere that is available to all team members.

Generally speaking, this process is carried out via GitHub Issues and Pull Requests.
See [](development:merge-policy) for how this works in practice.

### Resources to learn about consent-based decision making

Here are some helpful resources for more information about consent-based decision-making.

- A short primer: https://thedecider.app/consent-decision-making
- A more in-depth discussion: https://sociocracyforall.org/consent-decision-making/
- A well-known technical proposal on "Consent via humming": https://tools.ietf.org/html/rfc7282
