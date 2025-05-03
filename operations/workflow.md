(leads:workflow)=
# Workflow for planning and delivery

This describes the process we follow to accomplish our [organizational goals and high-level strategy](../organization/strategy.md).[^flight-levels]

In short:

- [Our goals and high-level strategy](../organization/strategy.md) drive all of our work.
- Quarterly objecties allow us to define high-level outcomes in service of this strategy.
- Initiatives help us coordinate work to make significant progress towards these outcomes.
- Sub-issues in initiatives have planning and coordination to make initiatives actionable.
- Tasks and epics are chunks of work that drive our actions and complete initiatives.

```{figure} images/boards.excalidraw.svg
An overview of our boards and how they relate to one another.
Initiatives (blue) are defined to make progress towards goals (red).
Initiatives have sequences of actions to move them forward defined in Initiatives Planning sessions (yellow).
Teams pull work from these sequences and complete them in their daily workflow (green).
```

[^flight-levels]: These are heavily inspired [by the Flight Levels framework](https://www.flightlevels.io/).

(quarterly-objectives)=
## Quarterly objectives

Each quarter, we consider the progress that we made last quarter, and set objectives for the next quarter.

[You can find the quarterly planning process we follow here](https://docs.google.com/document/d/1aI-NhVOqx6G1n8pBMS6oDSBaZlSoR2Z-jhudJMBbhg8/edit?usp=sharing). Duplicate the Google doc and update it for our next quarter.

In order to make progress towards our quarterly objectives, we define [_initiatives_](#board:initiatives).

(board:initiatives)=
## Initiatives

**Initiatives** are major efforts that represent significant progress towards our quarterly objectives. We define and prioritize them on [our Initiatives Board](https://github.com/orgs/2i2c-org/projects/46). An initiative usually requires coordination from multiple people or many actions over time.

### Structure of an initiative

Initiatives should provide enough context for anyone to understand its importance and outcomes or measures for completion.
It should provide enough information that our team can prioritize the initiative in our [](#initiatives:meetings).
They should also provide a *single point of access* for visibility into any related epics, tasks, and subtasks.

Here's the minimal information that must be in an initiative in order to be Ready to Work.

````{code-block} markdown
:caption: Information needed to make an initiative Ready to Work
title: Initiative name in GitHub issue
body:

### Description

A short description of the initiative, with enough context so that people can understand
what kind of work it will entail, and why it is important to 2i2c's overall goals.

### Why is this important?

- This will allow us to XXX
- Link to a strategic goal or a project (2i2c-based, upstream, etc)

### Measures and definition of done

- We expect to see XXX
- This will be complete when YYY

### Next actions

```
- [ ] A list of sub-issues of tasks and actions used to coordinate work around this initiative.
- [ ] Each should be an actionable issue that we track independently.
- [ ] This may be empty when the initiative is created! The initiative's purpose should be used to decide what action issues to create next.
```
````

`In Progress` initiatives should have a **sub-issues list of steps to complete the initiative**.
These become the issues that we plan in [Delivery Boards](#board:delivery) and iteration planning.

(board:delivery)=
## Delivery boards

Our delivery boards are where we organize the tasks, deliverables and stories that drive our daily actions and our bi-weekly planning cycles.
All items on the delivery board should be linked to an `In progress` initiative, or be related to reactive work.

There are two delivery boards:

### Operations board

The [**Operations board**](https://github.com/orgs/2i2c-org/projects/50) is a board focused on delivering operational initiatives, like building and improving processes. It's owned by our Delivery Enablement team and supports all other members of the organization. This isn’t a “just catch all the other things board"; everything flows from our strategic goals and initiatives. 

- [**Board link**](https://github.com/orgs/2i2c-org/projects/50)
- [**`#initiatives`**](https://2i2c.slack.com/archives/C06G5FAAT63) is the Slack channel for this board.

### Product and Services board

The [**Product and Services board**](https://github.com/orgs/2i2c-org/projects/57): This is the main board used to coordinate work for the P&S team.

- [**Board link**](https://github.com/orgs/2i2c-org/projects/57)
- [**`#product-and-services`**](https://2i2c.slack.com/archives/C07SJJWVCAD) is the Slack channel for this board.

## Retrospective boards

We use [EasyRetro](https://easyretro.io) to facilitate our retrospectives.
The paid user account is `admin@2i2c.org` and the credentails are stored in [our shared BitWarden account](#account:bitwarden).

Follow the links below to the different retro boards.

- Product and Services Retrospective [board link](https://easyretro.io/publicboard/A8bu34hcK2eyg0s5MxNX0AfQXG02/7e47da43-a12b-4d21-842d-22361b799a92)
- Operations Retrospective [board link](https://easyretro.io/publicboard/A8bu34hcK2eyg0s5MxNX0AfQXG02/8581f72e-b714-4018-9737-903272c42f36)
- Initiatives Retrospective [board link](https://easyretro.io/publicboard/A8bu34hcK2eyg0s5MxNX0AfQXG02/2f4284bb-4ea6-4c60-94cd-1c8a4f292106)

### Product and Services retrospective policy

The Product and Services team holds a retrospective every two weeks.
