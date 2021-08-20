# Structure and governance of 2i2c

2i2c is an organization dedicated to supporting open infrastructure in interactive computing for research and education, as well as the open source communities that underlie this infrastructure. Its fiscal sponsor is {term}`Code for Science and Society`.

This page describes the major organizational structures of 2i2c, and how they relate to governance and operations.

:::{admonition} A few notes on governance
- All 2i2c members act as individuals, and not on behalf of their affiliated institutions.
- All decisions made by the 2i2c Steering Council or Teams must abide by the policies of its fiscal sponsor, {term}`Code for Science and Society`.
:::

(structure:steerco)=
## Steering Council

The Steering Council defines the mission, vision, and values of 2i2c. It also sets the strategic direction and priorities for 2i2c. The Steering Council provides oversight to the Executive Director of 2i2c and the Operations Team. The Steering Council group (`[steering-council@2i2c.org](mailto:steering-council@2i2c.org)`) is the only “official” way to communicate with others on the Steering Council.

The Steering Council makes decisions via consensus (specifically, it strives for [rough consensus](https://tools.ietf.org/html/rfc7282)). It is restricted by the legal obligations and policies of CS&S, 2i2c's fiscal sponsor.

See the [Proposal process section](proposal-process) for information about how the Steering Council makes decisions and conducts discussion.

:::{seealso}
The current Steering Council is [listed on the 2i2c website](https://2i2c.org/about/#steering-council).
:::

(proposal-process)=
### Proposal discussion and voting process

The following sections describe our process for officially communicating and proposing changes to 2i2c policy with the Steering Council.

#### How are proposals encoded?

There are two major places where each proposal is encoded/tracked:

- A Google Doc for the proposal language (and discussion). Each proposal should [follow this proposal template](https://docs.google.com/document/d/103B-WfaDte8PB1rfO86MHvYGCGrRJPm9Cbb0cPjq67k/edit?usp=sharing).
- An Issue in a GitHub repository to track the “to-do” item of discussing the proposal. Cross-link the issue with the Google Doc.

#### How do we discover and discuss proposals?

We use the [Steering Council group](mailto:steering-council@2i2c.org) to describe and discuss all proposals.

In addition:

- The Executive Director of 2i2c should provide regular (e.g., weekly) updates to the Steering Council email about active proposals or proposals that are currently being discussed and/or voted on.
- We maintain [a shared Google Calendar](https://calendar.google.com/calendar/u/2?cid=Y184ZmhrOXBtZmxocWM3OWI2bWY0dnEwYjlwc0Bncm91cC5jYWxlbmRhci5nb29nbGUuY29t) that contains voting dates as well as Steerco meeting dates.

#### When does voting happen, and how long do we discuss?

Proposals should be open for feedback and discussion for a minimum of 2 weeks. After 2 weeks, the proposal author may decide to call a vote (if necessary) or to accept and implement the proposal (if a vote is not required). Any Steering Council member may request that the discussion period be extended.

Votes happen on either the first or the third week of the month. When a proposal is made, add 2 weeks to the date, then find the next voting day. This is the assumed day of the vote (or implementation, if a vote is not needed) unless requested otherwise by a steering council member.

#### How does voting work?

Votes are encoded in a table at the top of the document.

For proposals that require a vote, we track the “stage” of the discussion at the top of the Google Doc. Once a proposal is in the “voting” stage (where people are recording their votes), the proposal should not substantively change. Steering Council members then put their votes in this table.

#### How are proposals implemented?

If a vote passes, or if a proposal does not require a vote and enough time has passed to move forward, we implement it via changes to the Team Compass. The actions that implement a policy should be linked to from the Google Doc.

#### How are proposals archived?

After a decision has been made about the proposal (regardless of whether a vote was needed), then take these steps:

- If relevant, add links to any pull requests that implement the proposal (e.g., in the Team Compass).
- Move the proposal [to the proposal archive](https://drive.google.com/drive/folders/1y0nxUPj_d2TJt388rD-ewt_08-UM2kGB?usp=sharing).
 
:::{note}
We do not yet have a policy about whether / how proposals should be made public.
For now, the proposal archive is only available to 2i2c team members.
:::

#### What kind of changes must follow this process?

Policy changes that require a steering council vote or notification must follow this process. See the [Proposal Guidelines](proposal-guidelines) below.

(proposal-guidelines)=
### Policies and guidelines for consulting the Steering Council

The Steering Council provides valuable perspective and insight for strategic decisions of major importance. As such, the Executive Director should leverage the Steering Council by asking for its counsel on a regular basis, particularly for strategic and organizational matters.

In addition to generally consulting the Steering Council when it is helpful, there are also some situations where the Executive Director _should_ or _must_ consult the Steering Council and/or get approval before moving forward. This section describes those scenarios.

#### Decisions that require a full steering council vote

The [Steering Council](https://2i2c-team-compass--61.org.readthedocs.build/en/61/about/structure.html#structure-steerco) defines the strategy and major direction of 2i2c. It must vote on major decisions that have strong implications for 2i2c’s strategy or financial well-being. See [the proposal process section](proposal-process) for information about how it votes.

Here are some major decision areas that require a full steering council vote.

- Unplanned financial decisions over $20,000 (e.g., deciding to hire a contractor that has not been written into a grant)
- Decisions that have significant implication for 2i2c’s financial health.
- Major changes in strategic direction and roadmaps for business or technical development.
- Changes to governance.
- Hiring Director-level positions within the 2i2c org.
- Defining salaries for Director-level positions within 2i2c.
- Changes to the Code of Conduct.

For other kinds of decisions, the [Executive Director](structure:ed) is given authority to decide.

#### Decisions that require notification, but not a vote

These decisions are significant or public-facing, and would benefit from SC input, but do not require a vote to move forward. The Steering Council should be notified via the `@steering-council` handle, and discussion left open for a reasonable amount of time so that the SC has time to give input. Any SC member can request a vote on any of these topics if they believe it requires consensus.

Here are some decisions that would require notification, but not a vote.

- Significant public-facing changes to the 2i2c website.
- Significant Human Resources (hiring, firing ,etc) decisions that were already planned.
- Operational policy for 2i2c staff (unless they have major financial implications).
- Decisions about grants to pursue and submit.
- Operational decisions around the “Managed Hub Service” business, within the strategic plan defined by the Steering Council.

#### Decisions that do not require notification/consultation

These are decisions that should be visible to the steering council, but not strictly required that they are consulted.

- In general, decisions that are more about execution of pre-defined strategy/goals/plans, rather than _changing_ strategy, goals, and plans.
- Any decision that doesn’t fit in the above categories.

:::{admonition} To Do
These are items that we should clarify in future conversations:

- Create a job description of the Executive Director position
- Create an annual review process + subcommittee for the Executive Director
:::

(structure:ed)=
## Executive Director

The Executive Director oversees the execution of the mission and strategy provided by the Steering Council.
They are the primary interface to {term}`CS&S` administration, and coordinate activity in the 2i2c Teams.
The Executive Director oversees each team, and makes tie-breaking decisions if they are at an impasse in decision-making.
The Executive Director reports to the Steering Council.

:::{seealso}
The current Executive Director of 2i2c is listed on the [Our Team page of the website](https://2i2c.org/about/#our-team).
:::


## 2i2c Teams

2i2c Teams carry out the mission of 2i2c with a specific focus or project.
They are made up of staff funded through {term}`CS&S`, employees at other organizations providing in-kind support, or volunteers contributing their time to 2i2c.
Each team has a decision-making process as well as a scope.

You can find a list of teams below.

```{contents}
:local: true
:backlinks: none
```

### 2i2c Open Engineering Team

**Team focus:** Build infrastructure for the 2i2c Hub service, contributions to open source contributions for projects that underlie this infrastructure, and development of a bootstrap business model around that service.

**Governance:** [Lazy consensus-seeking](http://smallcultfollowing.com/babysteps/blog/2019/04/19/aic-adventures-in-consensus/), or via delegation to individuals or groups within that team. This does not currently follow a formal process, but is made in good-faith conversation across the 2i2c repositories and issues.

(structure:fiscal-sponsor)=
## Fiscal sponsorship

2i2c does not have its own standalone non-profit status.
Instead, it inherits this status by being a [**fiscally sponsored project**](https://en.wikipedia.org/wiki/Fiscal_sponsorship#:~:text=Fiscal%20sponsorship%20refers%20to%20the,and%20an%20established%20non%2Dprofit.).
This means that it relies on its fiscal sponsor for major administrative and legal services, including 501(c)(3) status and financial management.
2i2c's fiscal sponsor is {term}`Code for Science and Society`.