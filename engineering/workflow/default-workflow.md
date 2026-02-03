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

Tasks in the backlog are continually added and refined asynchronously by the whole team, ready for Iteration planning meetings, which rely on having sequenced and prioritized tasks to be available in the board's Up next column.
The backlog is regularly culled of tasks that are stale, in a monthly Backlog refinement meeting 

Backlog refinement meetings should aim to prepare our backlog for planning by
- Gaining a shared understanding of work to be done
- Estimating work
- Identifying and removing tasks that are stale or obsolete
- Adjusting tasks that are in the wrong status or priority on the board
- Identifying tasks that need further asynchronous refinement

Tasks should tie back to initiatives or contract deliverables, and the refined column should also function as a buffer of uncommitted work to pull from if needed. This also allows initiative owners to queue up more than one sprint worth of work when they have a solid understanding of an initiative.

Attendees of the Refinement meeting should include representatives from the following teams:
- Engineering: for technical decision-making
- Product: for product decision-making

Product Managers at the meeting should come prepared to represent and advocate for Business Development interests.

(meetings:sprint-planning)=

### 2. Iteration Planning Guide

#### 🗓️ Between Refinement and Planning

A Product Manager will:

- **Add deadlines to issues that need them**  
  A Product Manager will ensure that any issue with a contractual obligation or expected delivery has a clear due date.

- **Mark contract deliverables with dates**  
  Use labels to easily identify Contract Deliverables.

- **Assign preferred sprint-end dates**  
  If a card is intended for the upcoming sprint, team members let a Product Manager know and they will mark it with this sprint’s end date.

- **Organize in 'Up Next'**  
  A Product Manager manages and sorts cards in the ‘Up Next’ column for visibility.

The Team will:

- **Review open-source contributions**  
  Include relevant contributions and initiatives in planning discussions.

- **Advocate for priority cards**  
Team members are expected to speak up for issues they’re most invested in or want to lead. For quarterly objective and initiative owners, that does not mean they need to do all the work of refinement, but they should make sure refinement is complete. Reach out to a Product Manager in the days leading up to a sprint to discuss the priority of the issues you wish to champion:
  - First check that the issues you want to suggest are not already in the Up Next column and dated for the upcoming sprint. 
  - Send a message to the PM at least one day prior to the planning session with a list of issues you feel need to be included in the upcoming sprint.
  - Please include as much context as needed for the PM to understand why these issues need to be in the upcoming sprint
  - The PM will take your suggestions under advisement and make a best effort to include them, but cannot guarantee that to be the case as other priorities and capacity will need to be considered. 

#### 🗺️ Roadmap & Initiative Review

The Product Manager will:

- **Review roadmap tab for issues with dates**  
  - Pull in overdue items.
  - Reassign unrealistic dates to achievable ones.
  - Ensure no items lag behind without follow-up.
 
#### ✅ Preparing for Planning

The Team will:

- **Ensure issues are current**  
  - All team members should update and clean up any issues to which they are assigned prior to the planning session
  - Ensure the use of the Standard Definition of Done available in the General Issue template where possible (See "How are Deliverabled Structured", below).

The Engineering Manager will:

- **Report on last sprint’s progress**  
  Add totals for:
  - ✅ Done  
  - 📂 Open  
  - ❌ Unplanned  
  to the previous sprint’s **Status Update**.

#### 📆 At the Planning Session 


#### 🔁 Sprint Review & Retrospective

The Engineering Manager will:

- **Review last sprint’s outcomes**
  - Compare *actual velocity* vs. target
  - Document the *status update*
  - Identify questions or blockers on leftover cards
  - Incorporate *retro feedback* to adjust workflows

The Tech Lead will:

- **Review last sprint's outages** (maximum 3 minutes)
  - List all the P1 outages during the last sprint
  - Flag any pending incident reports that have not been completed

#### 🎯 Define Sprint Goals

The Engineering Manager will:

- **Establish sprint themes**
  - Ask the Head of Product and the Technical Lead to share focus areas or big goals
  - Ask initiative owners to highlight the next demo reel or learning we're aiming for 
  - Invite input from the whole team for broader context

The Team will:

- **Identify a “1” (low-effort card)**  
  Start with the easiest, quickest win for the sprint.

#### 🃏 Committing Cards

The Team will:

- **Sort Board by date**  
  - Focus first on items due or overdue before exploring the rest.
  - Make sure to check dated items in the Up Next, Refined, Upcoming and In Flight columns are not being left behind

- **Start from the top of ‘Up Next’**
  - ✍️ Summarize each card for shared understanding  
  - 🧠 Estimate effort using Planning Poker or expert judgment  
  - 🙋 Assign responsible team member(s)  
  - 🔖 Move card to **Committed** and tag with sprint iteration

- **Prioritize initiative-linked and Contract Deliverable tasks**  
  - Reinforce the importance of completing tasks tied to Initiatives in Flight and Contract Deliverables.

- **Ensure coverage of key categories**  
Explicitly address these before moving to anything else:
  1. Contract Deliverables
  2. BD requests
  3. Incident Mitigation issues
  4. Support Tickets (including workshop requests and support issues that can't be resolved in 30 minutes)  
  5. Platform Initiatives
  6. Service Initiatives

- **Continue until reaching target velocity**  
  Adjust as needed to fill capacity without overloading.

- **Balance workloads**  
  - Review assignments for each member  
  - Shuffle cards to prevent burnout or neglect  
  - Add or remove cards to ensure smooth sprint flow

#### 📊 Final Sprint Setup

- Ping anyone who was not able to attend the meeting and ensure they are aware of the tasks they have been assigned. 

- **Update new sprint’s status dashboard**
  - Include total points in **Committed**
  - Ensure visibility across stakeholders

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

The [Iteration Board](https://github.com/orgs/2i2c-org/projects/57/views/1) is a place to keep track of the [Deliverables and tasks](coordination:deliverables) our team intends to work on for a two week iteration.

The board is a GitHub Projects board that is populated with tasks during the teams Iteration Planning activity.

The team's goal is to complete all items on the Sprint Board by the end of the Sprint.
This is a team commitment - while one person may be assigned to a deliverable, we all commit to working together to get the work done.

The Sprint Board is broken down into different columns that represent the team's delivery workflow. The team owns the design of this workflow and should change the workflow process to best suit their way of working and to optimize for sustainable delivery.

The current queues of work represented by the board are:

- {guilabel}`Upcoming P&S Initiatives` represents high level initiatives waiting to be picked up, with highest priority towards the top.
- {guilabel}`P&S Initiatives in flight` represents high level initiatives that are actively being worked on, with highest priority towards the top.
- {guilabel}`Refined` represents prioritized tasks ready to be worked, with the highest priority towards the top.
- {guilabel}`Up Next` represents prioritized tasks that will be included into the upcoming sprint(s) with the highest priority towards the top.
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

### How are deliverables structured?

There are a few special sections of a deliverable issue.
Not all of them are strictly required, but are particularly useful for more complex or long-lasting deliverables.

See [this Github Issue template](https://github.com/2i2c-org/infrastructure/blob/main/.github/ISSUE_TEMPLATE/01_new-issue.yaml) for an example of a deliverable's structure.
Below are some major sections that are common:

Context
: The top comment of a deliverable has meta information associated with that deliverable.
  This includes background information, user stories, task lists, etc.
  **The top comment should be frequently updated** by anybody on the team with relevant information to add.
  Do not hesitate to update somebody's top comment with new information, even if you didn't open the issue (though you're encouraged to leave a comment noting what has changed!).

What we need to do
: What is the intended aim of the deliverable?
  This should be in the form of [user stories](https://www.atlassian.com/agile/project-management/user-stories) or a thorough description that explicitly define the stakeholders that care about a deliverable, and why.

Definition of Done
: Use task lists encode discrete steps to take in order to complete a deliverable.
  All deliverables should have either a set of concrete steps to take to meet the deliverable, or at least one task with the **acceptance criteria** for when the deliverable will be complete.
  Task lists should be in the top comment of the deliverable, and are encoded as markdown tasks lists (e.g. with `- [ ]`).
  Task lists should be updated over time as we learn the steps needed to close the deliverable.
  For more complex deliverables, these tasks may be what goes onto the Sprint Board, rather than the deliverable itself.

  We use a Standard Definition of Done to guide the creation of any issue's DoD, suggesting a selection of the following steps to delivery:

      - [ ] The feature/service is technically complete
      - [ ] The feature/service been tested with one or more users (if applicable)
      - [ ] The feature/service been deployed to a production cluster
      - [ ] The feature/service has been shown to be replicably deployable
      - [ ] The feature/service is well documented, and the documentation is accessible for the target user base
      - [ ] The feature/service has been added to our product menu (if applicable).
      - [ ] Lessons learned have been documented
      - [ ] The feature's availability has been communicated to Sales
      - [ ] The feature has been communicated to our communities


## The `#product-and-services` Slack channel

The [`#product-and-services` Slack channel](https://2i2c.slack.com/archives/C07SJJWVCAD) is a place for the P&S team to coordinate, plan, and discuss their work.
