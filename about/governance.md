# Governance and decision making


(development:decisions)=
## How teams make decisions

Most decisions in 2i2c are made on-the-fly by subsets of 2i2c team members.
We try to follow [consent based decision-making](https://thedecider.app/consent-decision-making) in making decisions[^consent-decision-making].
This roughly means that:

- The proposed decision and relevant context must be available to all relevant team members.
  This is generally done via opening GitHub issues.
- Team members should have time to understand the proposal, and ask questions about it to understand its ramifications.
- Team members should have time to object and make suggested changes.
- The result of the decision should be recorded somewhere that is available to all team members.

Generally speaking, this process is carried out via GitHub Issues and Pull Requests.
See [](development:merge-policy) for how this works in practice.

[^consent-decision-making]:

    Here are some helpful resources for more information about consent-based decision-making.

    - A short primer: https://thedecider.app/consent-decision-making
    - A more in-depth discussion: https://sociocracyforall.org/consent-decision-making/
    - A well-known technical proposal on "Consent via humming": https://tools.ietf.org/html/rfc7282

(proposal-process)=
## How the Steering Council makes decisions

The Steering Council makes decisions via consensus (specifically, it strives for [rough consensus](https://tools.ietf.org/html/rfc7282)). It is restricted by the legal obligations and policies of {term}`CS&S`.

The following sections describe our process for officially communicating and proposing changes to 2i2c policy with the Steering Council.

### How are proposals encoded?

There are two major places where each proposal is encoded/tracked:

- A Google Doc for the proposal language (and discussion). Each proposal should [follow this proposal template](https://docs.google.com/document/d/103B-WfaDte8PB1rfO86MHvYGCGrRJPm9Cbb0cPjq67k/edit?usp=sharing).
- An Issue in a GitHub repository to track the “to-do” item of discussing the proposal. Cross-link the issue with the Google Doc.

### How do we discover and discuss proposals?

We use the [Steering Council group](mailto:steering-council@2i2c.org) to describe and discuss all proposals.

In addition:

- The Executive Director of 2i2c should provide regular (e.g., weekly) updates to the Steering Council email about active proposals or proposals that are currently being discussed and/or voted on.
- We maintain [a shared Google Calendar](https://calendar.google.com/calendar/u/2?cid=Y184ZmhrOXBtZmxocWM3OWI2bWY0dnEwYjlwc0Bncm91cC5jYWxlbmRhci5nb29nbGUuY29t) that contains voting dates as well as Steerco meeting dates.

### When does voting happen, and how long do we discuss?

Proposals should be open for feedback and discussion for a minimum of 2 weeks. After 2 weeks, the proposal author may decide to call a vote (if necessary) or to accept and implement the proposal (if a vote is not required). Any Steering Council member may request that the discussion period be extended.

Votes happen on either the first or the third week of the month. When a proposal is made, add 2 weeks to the date, then find the next voting day. This is the assumed day of the vote (or implementation, if a vote is not needed) unless requested otherwise by a steering council member.

### How does voting work?

Votes are encoded in a table at the top of the document.

For proposals that require a vote, we track the “stage” of the discussion at the top of the Google Doc. Once a proposal is in the “voting” stage (where people are recording their votes), the proposal should not substantively change. Steering Council members then put their votes in this table.

### How are proposals implemented?

If a vote passes, or if a proposal does not require a vote and enough time has passed to move forward, we implement it via changes to the Team Compass. The actions that implement a policy should be linked to from the Google Doc.

### How are proposals archived?

After a decision has been made about the proposal (regardless of whether a vote was needed), then take these steps:

- If relevant, add links to any pull requests that implement the proposal (e.g., in the Team Compass).
- Move the proposal [to the proposal archive](https://drive.google.com/drive/folders/1y0nxUPj_d2TJt388rD-ewt_08-UM2kGB?usp=sharing).
 
:::{note}
We do not yet have a policy about whether / how proposals should be made public.
For now, the proposal archive is only available to 2i2c team members.
:::

### What kind of changes must follow this process?

Policy changes that require a steering council vote or notification must follow this process. See the [Proposal Guidelines](proposal-guidelines) below.

(proposal-guidelines)=
## Policies and guidelines for consulting the Steering Council

The Steering Council provides valuable perspective and insight for strategic decisions of major importance. As such, the Executive Director should leverage the Steering Council by asking for its counsel on a regular basis, particularly for strategic and organizational matters.

In addition to generally consulting the Steering Council when it is helpful, there are also some situations where the Executive Director _should_ or _must_ consult the Steering Council and/or get approval before moving forward. This section describes those scenarios.

### Decisions that require a full steering council vote

The [Steering Council](structure:steerco) defines the strategy and major direction of 2i2c. It must vote on major decisions that have strong implications for 2i2c’s strategy or financial well-being. See [the proposal process section](proposal-process) for information about how it votes.

Here are some major decision areas that require a full steering council vote.

- Unplanned financial decisions over $20,000 (e.g., deciding to hire a contractor that has not been written into a grant)
- Decisions that have significant implication for 2i2c’s financial health.
- Major changes in strategic direction and roadmaps for business or technical development.
- Changes to governance.
- Hiring Director-level positions within the 2i2c org.
- Defining salaries for Director-level positions within 2i2c.
- Changes to the Code of Conduct.

For other kinds of decisions, the [Executive Director](structure:ed) is given authority to decide.

### Decisions that require notification, but not a vote

These decisions are significant or public-facing, and would benefit from SC input, but do not require a vote to move forward. The Steering Council should be notified via the `@steering-council` handle, and discussion left open for a reasonable amount of time so that the SC has time to give input. Any SC member can request a vote on any of these topics if they believe it requires consensus.

Here are some decisions that would require notification, but not a vote.

- Significant public-facing changes to the 2i2c website.
- Significant Human Resources (hiring, firing ,etc) decisions that were already planned.
- Operational policy for 2i2c staff (unless they have major financial implications).
- Decisions about grants to pursue and submit.
- Operational decisions around the “Managed Hub Service” business, within the strategic plan defined by the Steering Council.

### Decisions that do not require notification/consultation

These are decisions that should be visible to the steering council, but not strictly required that they are consulted.

- In general, decisions that are more about execution of pre-defined strategy/goals/plans, rather than _changing_ strategy, goals, and plans.
- Any decision that doesn’t fit in the above categories.

:::{admonition} To Do
These are items that we should clarify in future conversations:

- Create a job description of the Executive Director position
- Create an annual review process + subcommittee for the Executive Director
:::