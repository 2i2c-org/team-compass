(meetings:intro)=
# Meeting guidelines and policy

This section describes our broad team practices for meetings.
Its goal is to be relatively high-level and to provide guidelines that can be interpreted in different ways by team leads and meeting facilitators.

The source of truth for team meetings is [the 2i2c Team calendar](calendars:team).
These may link to other sources of information such as meeting notes.

## Guidelines

In general, our meetings should be **asynchronous friendly** and **focused on issues that need high-bandwidth conversation**.
As a distributed team, we pay a high coordination penalty for getting multiple people on a Zoom at once, so use this time carefully.

- **Take notes and make them accessible**.
  Meetings must have written notes that are accessible to others on the team.
  These must be made available to the team reasonably soon after the meeting.

- **Meeting agendas must be available at least 36 hours (not counting weekends) ahead**.
  Agendas should list:
  1. Any **questions** that people wish to discuss and answer during the meeting.
  2. Any **decisions** people want to make progress on during the meeting, and where the final decision will be made.
  3. Any **topics** to discuss in the meeting, with enough detail to help others decide if they wish to participate.

  Agendas should be concrete enough that people who can not be synchronously
  present can make comments on it, as well as make choices on whether they
  would like to attend or not.
  Provide links to the **source of truth for discussion**, as well as any context needed to meaningfully participate.

- **If there's not an agenda 36 hours before, the facilitator should cancel the meeting**.
  Meeting facilitators should collect _potential_ agenda items from others ahead of time, and _set_ the agenda at least 36 hours prior to the meeting start.
  If there is no set agenda at this time, facilitator should inform the team in Slack and delete the calendar event.

- **Focus time on resolving uncertainty and making decisions**.
  Avoid the tendency to use meetings for updates - we should use asynchronous team processes (discussion in issues, Geekbot standups, etc) for sharing what we are up to day-to-day.

(meetings:roles)=
## Roles

These are major roles that should be filled in any team meeting[^1].

[^1]: See [this blog post on team meeting roles](https://cfe.unc.edu/facilitator-recorder-and-timekeeper-roles/) for more inspiration here.

```{role} Meeting Facilitator
```

### Meeting Facilitator

The meeting facilitator structures the agenda so that it is well-scoped, and guides conversation to be productive and inclusive.

**Who serves in this role?**

They are generally the person that leads the meeting on an ongoing basis.
They may delegate this role to others.

**Before the meeting**

- Collect rough agenda items from team members
- Set the agenda

**During the meeting**

- Run the meeting, ensuring that conversations are inclusive and productive

```{role} meeting Recorder
```

### Meeting Recorder

The Meeting Recorder is responsible for encoding the discussion points and actionable items that came out of a meeting.
Their primary goal is to make sure that the content of the meeting is saved for reference from others.

**Who serves in this role?**

Anyone may serve in this role.
Define a meeting recorder at the beginning of each meeting.

**During the meeting**

- Write down major discussion points and ideas during the meeting
- Write down action items / to-dos explicitly so that we know what to follow up on

## Types of meetings

(meetings:content-meetings)=
### Content meetings

Meetings for discussion to help us resolve uncertainty and make decisions more quickly.

**What these meetings are for**:

- Discuss questions that arise when we review one another's work
- Refine work items in backlogs
- Prioritize work items in backlogs
- Discuss complex or sensitive topics that require high-bandwidth conversation

**What these meetings are not for**:

- Status updates about what we've been up to
- Short-term coordination and planning

### Coordination meetings

Short, focused meetings to align team members on a short-term plan of action.

**What these meetings are for**:

- Short-term planning given our priorities and any new work items
- Assign backlog items to team members to finish within a specific time window

**What these meetings are not for**:

- Discussing new ideas and proposals

(coordination:team-syncs)=
### Asynchronous team syncs

A lightweight way to share what we've been up to and signal-boost items for other team members to pay attention to.
These are managed by [an automated Geekbot questionnaire](https://geekbot.com/) in [our team slack](communication:slack).

To manage the Geekbot in Slack, send the word `dashboard` as DM to the bot and it'll bring up the page with all of the standups.

**What these meetings for**:

- To share what we've been up to lately
- To signal-boost requests for review and help
- To share context between a team member who is logging off and others who are logging on

### Team retrospectives

Reflect on our team practices over the recent past and surface opportunities and plans for improvement.

**What these meetings are for**:

- Discussing recent incidents and our process for resolving them
- Discuss our roles and distribution of work to be equitable and efficient
- Discuss any challenges in communication and coordination

**What these meetings are not for**:

- Critiquing a single team member's actions - these meetings are about our team system, not an individual.

### Professional development

A place to provide feedback to one another in order to improve our individual practices and let team members know how they are doing.
These are generally done between managers and direct reports, but can be between any two team members that wish to do this.

Below is a meeting template that many have found useful, and that you may adapt for your own meetings if you wish.

:::{admonition} One on one meeting template
:class: dropdown

```md
## <YYYY-MM-DD>

### ToDo

_Use these to keep track of follow-ups after the meeting_

- [ ] Fill in `To Do` throughout meeting
- [ ] ...

### Pre-meeting reflection

_Fill this out before the meeting to help guide our discussion_

- Who did you help this week/fortnight/...?
- Who helped you this week/fortnight/...?
- What did you achieve this week/fortnight/...?
- What did you struggle with this week/fortnight/...?
- What do you plan to work on next week/fortnight/...?
- Where do you need extra help?

### Quick Updates

_Any short updates on work items you'd like to add?_

- Update 1
- ...

### Discussion Points

_Topics that we should discuss together._

- Discussion 1
- ...

```

:::


**What these meetings are for**:

- Providing feedback about a team member's performance over the recent past
- Discussing how things are going in general and ensuring a team member feels supported
- Agreeing on a learning and personal development plan for team members

### All-hands

Align the entire organization on our progress, near-term strategy, and major upcoming plan.

**What these meetings are for**:

- Functional areas share their most important accomplishments with one another
- Share significant strategic decisions and policy changes
- Highlighting our organizational plan and financial situation

**What these meetings are not for**:

- Having tactical or planning conversations about work items
