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

### What is an initiative?

Initiatives represent significant progress towards a strategic goal. They are usually *accountable* to one area of 2i2c, but require action from many people across the organization to complete. Initiatives are not single actions, and often span multiple weeks of time. However, they should still be time-boxed and have a definition of “done”. A rule of thumb is that quarterly goals should take 2-5 initiatives to complete.

An initiative IS:

- Significant progress towards a quarterly goal  
- Described as an outcome or created artifact  
- A child of a quarterly objective

An initiative is NOT:

- An action, quarterly objective, or routine task.  
- (usually) not completable with a single day’s work.

### How we track initiatives on our initiatives board

We define and prioritize initiatives on [our Initiatives Board](https://github.com/orgs/2i2c-org/projects/46). It has **three** types of cards:

1. **Quarterly objectives.** Objectives that guide the creation of initiatives. At the end of quarterly planning, we should have one issue for each quarterly objective.  
2. **Initiatives.** Outcomes-based cards that describe significant progress toward a quarterly objective.
3. **Exceptionally complex and critical upcoming efforts.** Non-initiative cards may exist on the board if they are exceptionally important for us to track cross-functionally.

### Structure of an initiative

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

- [ ] A list of sub-issues of tasks and actions used to coordinate work around this initiative.
- [ ] Each should be an actionable issue that we track independently.
- [ ] This may be empty when the initiative is created! The initiative's purpose should be used to decide what action issues to create next.

````

`In Progress` initiatives should have a **sub-issues list of steps to complete the initiative**.
These become the issues that we plan in [Delivery Boards](#board:delivery) and iteration planning.

### Initiatives cycle 

We operate on a monthly sprint cycle for initiatives.

**On an ongoing basis,** area leads are responsible for:

- Providing guidance, refinement, and accountability to ensure initiatives are completed by their responsible individuals.
- The Executive Director is responsible for ensuring that area leads follow this process, and have the support they need to do it effectively.

**At the start of each month**, we have an initiatives planning meeting with the following goals:

- Align on progress towards our quarterly objectives  
- Share the strategic priorities that are area-specific, and that might impact our capacity to complete org-wide initiatives (e.g., major product or sales initiatives and effort).
- Identify risks that mean we may not complete an initiative.
- Decide if we have new information that should shift our quarterly objectives.

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

(delivery:asana)=
## Asana project with CS&S

2i2c uses [this Asana project](https://app.asana.com/1/1159648458748488/project/1208704062483139/list/1208704065114251) to coordinate asks to and from CS&S. This is the primary way to request action from any CS&S team member.

**To request action from CS&S** follow these guidelines:

- All Asana tasks need to be on the [2i2c project](https://app.asana.com/1/1159648458748488/project/1208704062483139/list/1208704065114251)
- **Always assign a CS&S team member**. Use your best judgment for who you think is best.
- **Always assign a due date**. Use your best judgment for a due date.
- CS&S is encouraged to change the responsible person, or the due date, as long as you communicate it back in the comments.

## Retrospective boards

We use [EasyRetro](https://easyretro.io) to facilitate our retrospectives.
The paid user account is `admin@2i2c.org` and the credentails are stored in [our shared BitWarden account](#account:bitwarden).

Follow the links below to the different retro boards.

- Product and Services Retrospective [board link](https://easyretro.io/publicboard/A8bu34hcK2eyg0s5MxNX0AfQXG02/7e47da43-a12b-4d21-842d-22361b799a92)
- Operations Retrospective [board link](https://easyretro.io/publicboard/A8bu34hcK2eyg0s5MxNX0AfQXG02/8581f72e-b714-4018-9737-903272c42f36)
- Initiatives Retrospective [board link](https://easyretro.io/publicboard/A8bu34hcK2eyg0s5MxNX0AfQXG02/2f4284bb-4ea6-4c60-94cd-1c8a4f292106)

### Product and Services retrospective policy

The Product and Services team holds a retrospective every two weeks.
