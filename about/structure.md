# Structure and governance of 2i2c

2i2c is an organization dedicated to supporting open infrastructure in interactive computing for research and education, as well as the open source communities that underlie this infrastructure. Its host organization is {ref}`structure:icsi`.

This page describes the major organizational structures of 2i2c, and how they relate to governance and operations.

:::{admonition} A few notes on governance
- All 2i2c members act as individuals, and not on behalf of their affiliated institutions.
- All decisions made by the 2i2c Steering Council or Teams must abide by the policies of its host organization, {ref}`structure:icsi`.
:::

(structure:steerco)=
## Steering Council

The Steering Council defines the mission, vision, and values of 2i2c. It also sets the strategic direction and priorities for 2i2c. The Steering Council provides oversight to the Executive Director of 2i2c and the Operations Team.

The Steering Council makes decisions via consensus (all members voting in the affirmative), and is restricted by the legal obligations and policies of ICSI. It uses the following process for these decisions:

* Open an issue in the `meta/` GitHub repository using [the {guilabel}`decision` template](https://github.com/2i2c-org/meta/issues/new?assignees=&labels=decision&template=decision.md&title=%7B%7B+Decision+Summary+%7D%7D).
* Have conversation around the decision in that issue. This may happen in the issue directly, or in ancillary issues, meetings, etc that are relevant. The decision issue should link to these relevant spaces.
* Once everybody has voted, if all vote in favor, then the vote passes. If anyone votes against, the vote does not pass. Either way, note the decision in the issue, close it, and take necessary action.

:::{seealso}
The current Steering Council is [listed on the 2i2c website](https://2i2c.org/about/#steering-council).
:::

(structure:ed)=
## Executive Director

The Executive Director oversees the execution of the mission and strategy provided by the Steering Council.
They are the primary interface to {ref}`ICSI's <structure:icsi>` administration, and coordinate activity in the 2i2c Teams.
The Executive Director oversees each team, and makes tie-breaking decisions if they are at an impasse in decision-making.
The Executive Director reports to the Steering Council.

:::{seealso}
The current Executive Director of 2i2c is listed on the [Our Team page of the website](https://2i2c.org/about/#our-team).
:::


## 2i2c Teams

2i2c Teams carry out the mission of 2i2c with a specific focus or project.
They are made up of staff funded through ICSI, employees at other organizations providing in-kind support, or volunteers contributing their time to 2i2c.
Each team has a decision-making process as well as a scope.

You can find a list of teams below.

```{contents}
:local: true
:backlinks: none
```

### 2i2c Open Engineering Team

**Team focus:** Build infrastructure for the 2i2c Hub service, contributions to open source contributions for projects that underlie this infrastructure, and development of a bootstrap business model around that service.

**Governance:** [Lazy consensus-seeking](http://smallcultfollowing.com/babysteps/blog/2019/04/19/aic-adventures-in-consensus/), or via delegation to individuals or groups within that team. This does not currently follow a formal process, but is made in good-faith conversation across the 2i2c repositories and issues.

(structure:icsi)=
## International Computer Science Institute (ICSI)

[ICSI](https://icsi.berkeley.edu) is the host organization of 2i2c. It provides administrative and strategic resources for 2i2c and leadership to support them in their mission. ICSI supports 2i2c by assisting in managing partnerships with 2i2c collaborators and contracts with 2i2c customers, connecting with the larger open research and education community, fundraising, grant and financial management, assuming legal and financial risk for 2i2c, and hiring and management of staff.

## Scope of governance

There are several kinds of governance scopes within 2i2c, described below.

### Decisions that require a full steering council vote

The [Steering Council](structure:steerco) defines the strategy and major direction of 2i2c. It must vote on major decisions that have strong implications for 2i2c's strategy or financial well-being. See [the Steering Council structure page](structure:steerco) for information about how it votes.

Here are some major decision areas that require a full steering council vote.

- Unplanned financial decisions over $20,000 (e.g., deciding to hire a contractor that has not been written into a grant)
- Decisions that have significant implication for 2i2c's financial health.
- Major changes in strategic direction and roadmaps for business or technical development.
- Changes to governance.
- Hiring Director-level positions within the 2i2c org.
- Defining salaries for Director-level positions within 2i2c.
- Changes to the Code of Conduct.

For other kinds of decisions, the [Executive Director](structure:ed) is given authority to decide.

### Decisions that require notification, but not a vote

These decisions are significant or public-facing, and would benefit from SC input, but do not require a vote to move forward.
The Steering Council should be notified via the `@steering-council` handle, and discussion left open for a reasonable amount of time so that the SC has time to give input.
Any SC member can request a vote on any of these topics if they believe it requires consensus.

Here are some decisions that would require notification, but not a vote.

- Significant public-facing changes to the 2i2c website.
- Significant hiring decisions that were already planned.
- Operational policy for 2i2c staff (unless they have major financial implications).
- Decisions about grants to pursue and submit.
- Operational decisions around the "Hubs as a Service" business, within the strategic plan defined by the Steering Council.

### Decisions that do not require notification/consultation

These are decisions that should be visible to the steering council, but not strictly required that they are consulted.

- In general, decisions that are more about execution of pre-defined strategy/goals/plans, rather than _changing_ strategy, goals, and plans.
- Any decision that doesn't fit in the above categories.
