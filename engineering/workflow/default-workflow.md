(coordination:workflow)=
# 2-week iterations - Our default process

```{admonition} Out of date!

Many of the sections below are out of date, particularly those related to the Engineering team's delivery workflow.
```

This section describes how our development team carries out its planning and day-to-day work.

:::{admonition} Helpful links
👉 [Here's a link to all 2i2c GitHub Issues that have been assigned to you](https://github.com/issues?q=is%3Aissue+is%3Aopen+archived%3Afalse+sort%3Aupdated-desc+assignee%3A%40me+user%3A2i2c-org)

👉 [Here's a link to see all Pull Requests for which your review is requested](https://github.com/issues?q=is%3Aopen+archived%3Afalse+sort%3Aupdated-desc+user%3A2i2c-org+type%3Apr+review-requested%3A%40me)
:::

(coordination:decisions)=
## Pull request workflow

See [](development:merge-policy).

(coordination:sprints)=
## Team Iterations

The 2i2c team uses Iterations to coordinate with one another in focused cycles of work (referred to as our [Iteration Cadence](coordination:iteration-cadence)). Our team works in **two-week iterations**.

We rely on 5 sub-processes to move work through the delivery workflow. Namely: 
- _Refinement_
- _Planning_
- _Progress Update_
- _Showcase_
- _Retrospective_.

These sub-processes are defined in more detail below.

(coordination:iteration-cadence)=
### Iteration cadence

Our team works in **two-week iterations**. Here is a brief overview of each Iteration.

Before Iteration
: Ensure the Refined column has ranked (prioritized and sequenced) work items 

Beginning of Iteration
: Iteration begins with our [Iteration planning meeting](meetings:sprint-planning).

  In this meeting we discuss major accomplishments in the previous iteration, review past capacity committments. We then size and assign the items that each team member will work on for the next iteration, and review items that require discussion and planning.

During the Iteration
: Team members work on the items assigned to them at the iteration planning meeting.
  We use [the Iteration Board](coordination:sprint-board) to coordinate our activities during the iteration.
  We provide updates about what we've been up to, what we're doing next, and where we need help via regular **asynchronous Slack stand-ups**.

Last day of Iteration
: By the end of the day, team members should have completed all of their items for that iteration. The iteration is closed off with a Retrospective to identify improvement opportunities.

:::{admonition} Iteration Cadence
- Default: Two weeks.
- Funding-crunch: One Weekly.
:::

(meetings:backlog-refinement)=
### 1. Pre-planning and refinement

The Refinement meetings prepares the Iteration board for the Iteration planning
meetings, which relies on having sequenced and prioritized tasks to be available in the board's Refined column.

Backlog refinement meetings should drive:
- creation of tasks into the sprint board's backlog column
- promotion of tasks into the sprint board's refined column
- prioritization of task in the sprint board's refined column

Tasks should tie back to initiatives, and the refined column should also function as a buffer of uncommitted work to pull from if needed.

Attendees of the Refinement meeting should include representatives from the following teams:
- Engineering: for technical decision-making
- Product: for product decision-making
- Partnerships and Community Success: for community/grant decision-making.

(meetings:sprint-planning)=
### 2. Iteration Planning

The team conducts a synchronous iteration planning meeting for 60 minutes at the beginning of each iteration.

The goal of this meeting is to synchronize with one another and commit to work to do during the iteration that gets us closer to achieving the initiatives objectives.

#### Planning Outcomes:
At the end of this meeting, we will have:
1. A [_sized_](eng:processes:task-sizing) list of team deliverables that the team commits to completing within the iteration time box. These deliverables will represent work from:
    - Grant/Funding
    - Partnerships
    - Product Roadmap
    - Support request
    - Internal Engineering
    - Upstream community

1. Identified and shared the core risks impacting the deliverables. NB: The meeting will not be used to brainstorm solutions to resolve the risks.

1. Owners assigned to resolve the different risks. These individuals will create working sessions and coordinate the necessary domain experts who will be responsible for resolving the risks. NB: The owner is accountable to ensure the working sessions happen. They are not responsible for the actual solutions as this may belong to separate domain experts. A deliverable cannot be committed as part of the iteration if there are dependencies with other teams AND those other teams have not committed to completing the work within the current iteration or if the work was not previously completed in an earlier iteration.

```{tip}
This meeting provides us a golden opportunity to:
- Not overwhelm any team member
- Under-estimate our team's total capacity and to provide room for unexpected work (e.g., support work)
- Limit the amount of work in process across Engineering (system optimisation)
- Ensure that we are focused on delivering the highest value work (value optimisation).
```

See [the Sprint Planning issue template](https://github.com/2i2c-org/team-compass/blob/main/.github/ISSUE_TEMPLATE/meeting-sprint-planning.md) for the agenda / structure of these meetings.

### 3. Progress Update (and blockers)

This is a short, synchronous, alignment meeting (sometimes referred to as a "_Standup_"). It occurs on Tuesdays and Thursdays, and is designed to help us coordinate and realign ourselves around the work. 

Each sync ensures team members focus on the most important tasks and allows the team to pivot and self-organize when unforeseen changes occur. It helps catch and address unplanned challenges, work, and risks, providing a way to transparently discuss any issues that may hinder achieving our iteration goals.

#### Guidelines for the standup
These are guidelines for the standup. Ideally, these meetings should not extend beyond 15 minutes and each person will answer these questions:
- _What am I working on?_ This helps the team to understand their progress towards completing work towards their iteration goal.
- _What will I work on next?_ This ensures that we working on the "right things" and limiting unplanned work.
- _What am I blocked on, or what do I foresee could be a blocker?_ This provides an opportunity for team members to ask for help and surface issues that may prevent the team from achiving it's iteration goal. 
- _Have I learned anything that needs to be addressed by/shared with the group?_ This maximizes shared-learning across the team (e.g. Here's a faster way to configure and deploy docker scripts from Kubernetes).

This is done in conjunction to using the board to identify:
- Work that has become stuck (or will become blocked)
- Work that is unplanned or should not be started
- Work that is urgent
- People that need assistance (or ask for help)
- Opportunities to pair/collaborate with team members to complete work.

### 4. Demo/Showcase (NOT CURRENTLY IMPLEMENTED)
To be implemented.

(meetings:retrospective)=
### 5.Retrospective/Continuous improvement

At the end of each iteration, the team holds a retrospective meeting to reflect and identify actions to improve the team's ways of working and delivery process. The retrospective is the process through which the team achieves continuous improvement for **all** their other processes. When done effectively, this event will enable us to make data-informed decisions regarding what key changes to adopt, amplify or discard from our processes.

#### The Duration of the Retrospective

The retrospective is 45 minutes long and is usually held on the last day of each iteration. It is held at a time to maximise attendance from the engineering team.

On rare occasions, when the team experiences duress or unpredictable and disruptive events, they may choose to have a specific retrospective to learn from those events.

#### The Roster for Facilitating Retrospectives

There is a [Google Sheet](https://docs.google.com/spreadsheets/d/1s0ZSAxwFzJ-_WgDkZeicfuUadSFEjkjS6ZcNk4N7Mmg/edit?usp=sharing) in the shared team drive that determines who will be facilitating each retrospective meeting (as well as [sprint planning](meetings:sprint-planning) and backlog refinement meetings).
Members of the engineering team are expected to self-nominate for this role because it is _their_ improvement process.

#### Retrospective Tool

The team uses an [EasyRetro board](https://easyretro.io/publicboard/A8bu34hcK2eyg0s5MxNX0AfQXG02/7e47da43-a12b-4d21-842d-22361b799a92) to collect cards representing feedback concerning the last sprint.
There are columns for:

- Thanks and Celebrations
- Things That Went Well
- Things To Improve
- Actions (Items to take forward into the next sprint).

This template can be changed by the facilitator. There are [many](https://retromat.org/) different template formats and the facilitator should choose one that is most appropriate for the team's need.

#### EasyRetro user account

We have a paid Team subscription for EasyRetro, to make it easier to facilitate retrospectives. The user account is **admin@2i2c.org**. The credentials are stored in our [shared BitWarden account](https://vault.bitwarden.com/#/vault?organizationId=11313781-4b83-41a3-9d35-afe200c8e9f1).


#### The General Format of an Iteration Retrospective

The retrospective meeting follows the below outline.

1. _Identify a facilitator._

    The facilitator has the responsibility to:

    * Ensure that their is psychological safety in the meeting.
    * Ensure that the meeting isn't used as a blaming/ranting/finger pointing session.
    * Share the [Retrospective Prime directive](https://retrospectivewiki.org/index.php?title=The_Prime_Directive) with the participants.

1. _Set the context for the Iteration retrospective._

   This involves explaining the period under observation, which process(es) we are trying to improve and what has been achieved by the current process. This could involve reviewing the 'Done' column in [](coordination:sprint-board).

1. _Review the previous retrospective actions._

    Reviewing previous retrospective actions involves:

    * checking if the team completed all of the previous actions that they committed to
    * noting how many actions were completed
    * briefly discussing if the action has had the intended impact.

   Retrospective actions are stored in the team's Sprint board and are tagged with the `Retro action` label.

1. _Set aside time for the team reflect and capture input on cards._

   Team members need ample time to reflect on their work, interactions and the effectiveness of process from the past iteration. This time will vary based on the size of the team, the duration of the retrospective and temperament of the team.

   This duration of this step is usually between 5 - 15 minutes.

   In some cases, the team is invited to pre-populate the board with input before the actual retrospective.

1. _Thanks and Celebrations_

    Ultimately, the team needs to find a way to celebrate each other. In some cases, this may be simply the team reading the cards themselves or the facilitator doing this.

1. _Create shared understanding on Went Well, and To Improve columns._

   During this time, the facilitator groups the cards into themes (in the form of hashtags), potentially merging similar cards.

1. _Discussion amongst the team on the To Improve items._

   For cards that are unclear, the facilitator should encourage the person that wrote the card to provide context. Team members can ask clarifying questions of each other.

   :::{note}
   It is important to discourage "solutioning" at this stage.
   :::

1. _Voting on the To Improve items._

   The team can then vote on which To Improve items they think are the most important.

   _For example: Each member gets 3 votes that they can distribute as they see fit, e.g., give all 3 votes to one item, 2 to one item and 1 to another, or 1 vote for 3 items._

1. _Identify actions._

   For the top-voted actions (limited to only 2 or 3), the team generates some concrete actions to try and resolve the issues.
   These are captured in the Action Items column.

1. _Close the meeting._

  After the meeting, the facilitator is responsible for converting the Action Items into GitHub issues to be put in the sprint board's backlog column, and then clearing the retro board.

#### When should the Retro Board be Populated

Team members are expected to try populate the board ahead of time to the extent that what remains could be populated in five minutes just-in-time during the meeting.

#### How do Generated Actions move into and get committed to the Team's Next Sprint?

The _general rule_ is that actions are also work and should be refined and prioritized like any other work.

(coordination:sprint-board)=
### The Iteration Board

The [Iteration Board](https://github.com/orgs/2i2c-org/projects/49/views/1) is a place to keep track of the [Deliverables and tasks](coordination:deliverables) our team intends to work on for a two week iteration.

The board is a GitHub Projects board that is populated with tasks during the teams Iteration Planning activity.

The team's goal is to complete all items on the Sprint Board by the end of the Sprint.
This is a team commitment - while one person may be assigned to a deliverable, we all commit to working together to get the work done.

The Sprint Board is broken down into different columns that represent the team's delivery workflow. The team owns the design of this workflow and should change the workflow process to best suit their way of working and to optimize for sustainable delivery.

The current queues of work represented by the board are:

- {guilabel}`Backlog` represents tasks pending refinement as driven by backlog refinement meetings.
- {guilabel}`Refined` represents prioritized tasks ready to be worked, with the highest priority towards the top.
- {guilabel}`Committed` represents tasks we've committed to complete during the current sprint in the most recent sprint planning meeting. Each item should have at least one owner.
- {guilabel}`In Progress` represents actively worked tasks.
- {guilabel}`In Review/Blocked` represents tasks that need to be review before being marked as done or that cannot be completed without additional actions/support.
- {guilabel}`Done` represents completed tasks to be celebrated and archived in the next sprint planning meeting.

(coordination:deliverables)=
## Deliverables and work issues

Deliverables represent incremental amounts of value we can deliver to a particular stakeholder.
They are **encoded as GitHub Issues** and updated over time as we learn more about the particular deliverable.
Most issues in our repositories are deliverables, in varying states of readiness.

:::{note}
We use the word "deliverable" loosely here - some issues may be more like tasks rather than an end-product.
The important thing is that they have high-quality information and structure, clearly denote value, and are actionable.
:::

### How are deliverables structured? (OUTDATED)

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
## The Team Backlog (OUTDATED)

[Click here to go to the Team Backlog](https://github.com/orgs/2i2c-org/projects/22).

The Team Backlog is a GitHub Projects Board with a list of [Deliverables and tasks](coordination:deliverables) across all of our active projects.
This represents the work that the team is planning to do in the near future.
These items adhere to the following principles:

- The order of items should be roughly according to priority, with higher priority items at the top of lists.
- Items on the board should have a **status** that signals whether they are ready to work or need more refinement before working.
- If an item has multiple components or would otherwise take longer than a sprint to complete, create new issues as sub-tasks, and add *them* to the Sprint Board.

### Assigning to an issue (OUTDATED)

Only assign a backlog issue to somebody if it is **actively being worked on**.
We assume that once somebody is assigned to an issue, it is part of an active iteration.
Note that **all** issues on our Iteration Backlog should have somebody assigned to them.

:::{admonition} Our definition of "Work in Progress"
Because issues that are actively being worked on must have somebody assigned to them, we use "the issues that have somebody assigned to them" as our definition of Work in Progress.
:::

### Backlog item limits (OUTDATED)

Our goal is to have backlog items that roughly cover the next 3 [iteration cycles](coordination:sprints).
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
