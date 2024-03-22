(leads:workflow)=
# Workflow

## Levels of work within 2i2c

There are roughly three levels of work at play in 2i2c's team[^flight-levels]:

[^flight-levels]: These are heavily inspired [by the Flight Levels framework](https://www.flightlevels.io/).

**Level 3: Strategy**. 2i2c's overall strategic goals and the initiatives that make progress towards them. [Defined as items in the initiatives board](#board:initiatives).

**Level 2: Coordination**. The sequence of actions that is carried out in order to complete an initiative, and the cross-team coordination needed to accomplish them. Defined as tasklists within initiatives [on the initiatives board](#board:initiatives).

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

The [**Initiatives board**](https://github.com/orgs/2i2c-org/projects/46) is where we define our team's strategic priorities, and coordinate across the team to ensure that each one has a clear plan of action.

There are three types of items on the initiatives board:

- **Strategic goals**: A high-level goal that defines success for 2i2c. This should be outcome-based, measurable, and directional in nature. All strategic initiatives should be linked to a goal.
- **Initiatives**: An effort that makes progress towards our goals, and usually requires coordination from multiple people or many actions over time. All non-reactive work should be tied to an initiative.

  - Strategic initiatives represent progress made towards a strategic goal or a major project. These should all result in value delivered to communities.
  - Investment initiatives are an investment in our team, technology, etc that does not immediately deliver value to communities, but helps us build a better foundation to do so.
- **Lists of Tasks and Epics**: Are the sequence of steps or deliverables that are taken to complete an initiative. These are defined as `[tasklist]` objects in each initiative, and are the main units of work that drive our actions.

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

```[tasklist]
- [ ] A growing list of tasks and actions used to coordinate work around this initiative.
- [ ] Each should be an actionable issue that we track independently.
- [ ] This may be empty when the initiative is created! The initiative's goals should be used to decide what action issues to create next.
```
````
`````

### Bi-weekly initiatives meetings

There are two bi-weekly meetings with the initiatives team.

- **Initiative planning and refinement**: A combination of **coordination** and **prioritization**. We first walk the board and ensure each initiative has clear next steps, assigned people, and that any coordination between teams is clear. We next zoom out and discuss our overall portfolio of initiatives to ensure we're sequencing them properly. This should inform priorities for sprint planning and delivery.
- **Initiative retrospectives**: The Initiatives team follows the same retrospective structure we follow for any team. This should consider the results generated from sprint delivery and team retrospectives.

(slack:solution-forum)=
### The `#initiatives` slack channel

The [`#initiatives` Slack channel](https://2i2c.slack.com/archives/C06G5FAAT63) is a space for cross-organization initiatives and strategic conversation.

### Initiatives team

- @choldgraf : To represent 2i2c's overall strategy and policies
- @colliand: To represent our overall partnerships strategy and team
- @jmunroe: To represent our community success efforts
- @Gman0909 : To represent our product operations and strategy
- @damianavila : To represent our engineering team's needs
- @yuvipanda : To represent our technical and open source strategy
- @haroldcampbell : To represent 2i2c's overall system of work and operations
- @aprilmj : To represent 2i2c's People Operations and team support

(board:delivery)=
## Delivery boards

Our delivery boards are where we organize the tasks, deliverables and stories that drive our daily actions and our bi-weekly planning cycles.
All items on the delivery board should be linked to an `In progress` initiative, or be related to reactive work.

There are two delivery boards:

### Operations board

The [**Operations board**](https://github.com/orgs/2i2c-org/projects/47) is a team-wide board focused around delivery. Includes all organizational tasks/actions except for Engineering.

- [**Board link**](https://github.com/orgs/2i2c-org/projects/47)
- [**`#initiatives`**](https://2i2c.slack.com/archives/C06G5FAAT63) is the Slack channel for this board.
- **Meetings**: Bi-weekly organization-wide sprint planning meetings (except for engineering).

### Engineering board

The [**Engineering board**](https://github.com/orgs/2i2c-org/projects/49): A "special case" of the Operations board. It is functionally the same but focused on tech development cycles and largely attended to by the engineering team.

- [**Board link**](https://github.com/orgs/2i2c-org/projects/47)
- [**`#engineering`**](https://2i2c.slack.com/archives/C055A1J1DRP) is the Slack channel for this board.
- **Meetings**: Bi-weekly Engineering sprint planning meetings.

(slack:team-updates)=
## The `#team-updates` Slack channel

The [`#team-updates` Slack channel](https://2i2c.slack.com/archives/C01GLCC1VCN) is for organization-wide announcements and team discussion.
It is a place for the whole organization to talk to one another, share status and life updates, etc.
There's not a strict limit to topics for discussion, but if your conversation fits within the scope of another Slack channel it's better to discuss there.
