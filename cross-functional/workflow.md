(leads:workflow)=
# Workflow

## Levels of work within 2i2c

There are roughly three levels of work at play in 2i2c's team[^flight-levels]:

[^flight-levels]: These are heavily inspired [by the Flight Levels framework](https://www.flightlevels.io/).

**Level 3: Strategy**. 2i2c's overall strategic goals and the initiatives that make progress towards them. [Defined as items in the initiatives board](#board:initiatives).

**Level 2: Coordination**. The sequence of actions that is carried out in order to complete an initiative, and the cross-team coordination needed to accomplish them. Defined as sub-issues within initiatives [on the initiatives board](#board:initiatives).

**Level 1: Operations**. The work that a team intends to deliver now and next. This is a combination of strategic work that drives an initiative forward, as well as reactive work that is driven by external processes. [Defined as items on team delivery boards](#board:delivery).

In short, our strategic goals are 2i2c's overall measure of success. Initiatives are concrete efforts in a **strategy** to make progress towards those goals. Initiatives require **coordination** across our team to plan the proper sequence of actions. These plans are then **operationalized** by being pulled into the delivery processes of each team.

```{figure} images/boards.excalidraw.svg
An overview of our boards and how they relate to one another.
Initiatives (blue) are defined to make progress towards goals (red).
Initiatives have sequences of actions to move them forward defined in Initiatives Planning sessions (yellow).
Teams pull work from these sequences and complete them in their daily workflow (green).
```

(board:initiatives)=
## Initiatives board

Initiative-led work is driven by our overall [](/operations/strategy.md) that define success for 2i2c. These are defined during our quarterly goals planning meetings. Goals should be outcome-based, measurable, and directional in nature. For example, the goals of a high value funding proposal could include checkpoint milestones written into the work plan that we need to target by certain dates.

The [**Initiatives board**](https://github.com/orgs/2i2c-org/projects/46) is where we define our team's strategic priorities, and coordinate across sub-teams to ensure that each one has a clear plan of action. An **Initiative** is an effort that makes progress towards our goals, and usually requires coordination from multiple people or many actions over time.

:::{note}
All initiatives should be driven by a goal, and all non-reactive work should be parented with an initiative via [GitHub sub-issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/adding-sub-issues) where possible.
:::

### Structure of an initiative

Initiatives should provide enough context for anyone to understand its importance and outcomes or measures for completion.
It should provide enough information that our team can prioritize the initiative in our [](#initiatives:meetings).
They should also provide a *single point of access* for visibility into any related epics, tasks, and subtasks.

`````{admonition} Example structure of an initiative
:class: dropdown
Here's the rough structure of an initiative, use this to guide the creation of new initiatives.

````markdown
title: Initiative name in GitHub issue

### Description

A short description of the initiative, with enough context so that people can understand
what kind of work it will entail, and why it is important to 2i2c's overall goals.

### Why is this important?

- This will allow us to XXX
- Link to a strategic goal or a project (2i2c-based, upstream, etc)

### Measures and definition of done

- We expect to see XXX
- This will be complete when YYY

### Sub-issues

```
- [ ] A list of sub-issues of tasks and actions used to coordinate work around this initiative.
- [ ] Each should be an actionable issue that we track independently.
- [ ] This may be empty when the initiative is created! The initiative's purpose should be used to decide what action issues to create next.
```
````
`````

`In Progress` initiatives should have a **sub-issues list of steps to complete the initiative**.
These become the issues that we plan in [Delivery Boards](#board:delivery) and iteration planning.

Ensure that every initiative has linked sub-issues so that:

1. Every task can be traced back to its parent initiative by clicking upward through parent issues.
2. You can reach each task by clicking downward through issues linked in an initiative's sub-issues list.

(initiatives:meetings)=
### Bi-weekly initiatives meetings

There is one bi-weekly meeting with the initiatives team for planning and prioritization. We first walk the board and ensure each initiative has clear next steps, assigned people, and that any coordination between teams is clear. We next zoom out and discuss our overall portfolio of initiatives to ensure we're sequencing them properly and that any upcoming high-priority work is clearly flagged. This should inform priorities for sprint planning and delivery.

Please refine issues *before* these meetings by updating and reviewing the Initiatives board.

(slack:solution-forum)=
### The `#initiatives` Slack channel

The [`#initiatives` Slack channel](https://2i2c.slack.com/archives/C06G5FAAT63) is a space for cross-organization initiatives and strategic conversation.

### Initiatives team

- @choldgraf : To represent 2i2c's overall strategy and policies
- @colliand: To represent our overall Business Development strategy
- @Gman0909 : To represent our product and services strategy
- @jmunroe: To represent our community services strategy
- @yuvipanda : To represent our technical and open source strategy
- @haroldcampbell : To represent 2i2c's overall system of work and operations
- @aprilmj : To represent 2i2c's People Operations and team support

The above list represents mandatory team members. The initiatives process is however open to all members of 2i2c.

(board:delivery)=
## Delivery boards

Our delivery boards are where we organize the tasks, deliverables and stories that drive our daily actions and our bi-weekly planning cycles.
All items on the delivery board should be linked to an `In progress` initiative, or be related to reactive work.

There are two delivery boards:

### Operations board

The [**Operations board**](https://github.com/orgs/2i2c-org/projects/50) is a board focused on delivering operational initiatives, like building and improving processes. It's owned by our Delivery Enablement team and supports all other members of the organization. This isn’t a “just catch all the other things board"; everything flows from our strategic goals and initiatives. 

- [**Board link**](https://github.com/orgs/2i2c-org/projects/50)
- [**`#initiatives`**](https://2i2c.slack.com/archives/C06G5FAAT63) is the Slack channel for this board.
- **Meetings**: Fortnightly planning, monthly retrospective, and weekly coordination.

### Product and Services board

The [**Product and Services board**](https://github.com/orgs/2i2c-org/projects/57): This is the main board used to coordinate work for the P&S team.

- [**Board link**](https://github.com/orgs/2i2c-org/projects/57)
- [**`#product-and-services`**](https://2i2c.slack.com/archives/C07SJJWVCAD) is the Slack channel for this board.
- **Meetings**: Fortnightly P&S sprint planning, showcase and retrospective meetings, synchronous standups twice weekly.

## Retrospective boards

We use [EasyRetro](https://easyretro.io) to facilitate our retrospectives.

### Board links

The paid user account is `admin@2i2c.org` and the credentails are stored in [our shared BitWarden account](#account:bitwarden).

Follow the links below to the different retro boards.

- Product and Services Retrospective [board link](https://easyretro.io/publicboard/A8bu34hcK2eyg0s5MxNX0AfQXG02/7e47da43-a12b-4d21-842d-22361b799a92)
- Operations Retrospective [board link](https://easyretro.io/publicboard/A8bu34hcK2eyg0s5MxNX0AfQXG02/8581f72e-b714-4018-9737-903272c42f36)
- Initiatives Retrospective [board link](https://easyretro.io/publicboard/A8bu34hcK2eyg0s5MxNX0AfQXG02/2f4284bb-4ea6-4c60-94cd-1c8a4f292106)

### Product and Services retrospective policy

The Product and Services team holds a retrospective every two weeks.

(slack:team-updates)=
## The `#team-updates` Slack channel

The [`#team-updates` Slack channel](https://2i2c.slack.com/archives/C01GLCC1VCN) is for organization-wide announcements and team discussion.
It is a place for the whole organization to talk to one another, share status and life updates, etc.
There's not a strict limit to topics for discussion, but if your conversation fits within the scope of another Slack channel it's better to discuss there.
