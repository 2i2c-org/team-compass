# Incident response


When an {term}`Incident` is declared, we trigger a special response in order to ensure that it is resolved quickly.
This section describes our incident response process, major roles and terminology, and what to expect.[^google-sre][^acm-blog][^wikimedia-clinic-duty].

[^incident-refs]: The [PagerDuty Incident Response Guide](https://response.pagerduty.com/) is a good description of the Incident Command role and how it relates to similar roles.

[^google-sre]: The [Google SRE Incident response guide](https://sre.google/workbook/incident-response/) has a wealth of information about incident response and distributed SRE teams.

[^acm-blog]: This [ACM blog post](https://queue.acm.org/detail.cfm?id=3380779) describes the complexity of coordinating across a team of distributed responders during an incident, and notes a places where Incident Commander roles may actually hinder responsiveness. It is a good lesson in the complexity of incidents with distributed teams!

[^wikimedia-clinic-duty]: The [WikiMedia Clinic Duty](https://wikitech.wikimedia.org/wiki/SRE/Clinic_Duty#Responsibilities) process also inspired our process here, and is a great overall workflow around distributed SRE.

:::{admonition} In Beta!
:class: warning
We are currently working out our Incident Response process.
The content on this page might change over time, and we welcome suggested changes and pull requests!
:::

## Roles and team structure

An {term}`Incident Response Team` is formed when an {term}`Incident` has been declared.
The goal of the Incident Response Team is to collectively resolve incidents.

An Incident Response Team is generally made up of:

- An {term}`Incident Commander`
- The {term}`Support Stewards`
- One or more {term}`Subject Matter Experts` (SMEs)

```{glossary}
Incident Response Team
  The group of roles that collectively understand, plan, resolve, and communicate our actions around an {term}`Incident`. The people in these roles may change in a fluid manner, and one person may serve in multiple roles. A rough way to approximate this team is "the people that have communicated in internal and external channels to resolve an incident."

Incident Commander
  The Incident Commander has the authority to plan and delegate action to others on the {term}`Incident Response Team`. They are **not expected** to take actions themselves. Their goal is to help the team make consistent and deliberate progress towards resolving an incident. They are the {term}`Source of Truth` about the current state and action plan surrounding an incident.

External Liason
External Liasons
  The person that is responsible for communicating with external stakeholders during an incident. This is either the {term}`Incident Commander`, or somebody to which they delegate this role. Every few working hours, they should communicate the status of the incident, updates about our current thinking and what we have tried, and any expected changes coming.

Subject Matter Expert
Subject Matter Experts
  A member on the {term}`Incident Response Team` with expertise in an area of relevance to an Incident. SMEs have a variety of backgrounds and abilities, and they should be pulled in to the Response Team as-needed by the {term}`Incident Commander`. Their goal is to take actions as-directed by the {term}`Incident Commander` to resolve an incident.
```

## Communication channels

### External communication

- The {term}`Incident Commander` acts as the primary point of communication with external stakeholders like the {term}`Community Representative`s.
- They may **delegate** this responsibilitiy to another team member if they wish (e.g., to the {term}`Support Steward` team.)
- We may interact with external stakeholders via comments in Incident Response issues if it helps resolve the incident more quickly.

### Internal communication

- The Slack channel [{guilabel}`#support-freshdesk`](https://2i2c.slack.com/archives/C028WU9PFBN) contains real-time communication about support issues. Use this to signal-boost support requests related to {term}`Incidents`.
- [Issues with the {guilabel}`incident` label](https://github.com/2i2c-org/infrastructure/issues?q=is%3Aopen+label%3A%22type%3A+Hub+Incident%22+sort%3Aupdated-desc) are where we track progress when [resolving incidents](support:incident-response).


(support:incident-response)=
## Incident response process

Incidents are a special kind of support ticket, because they are related to degraded service that immediately impacts communities.
We prioritize the resolution of incidents above all other kinds of work, and have a special process for tracking conversation and progress with them.

Here is the process that we follow for incidents:

1. **Acknowledge the incident**. Communicate with the Community Representative that there is an incident. Use this canned response as a start for responding:

   ```{button-link} https://2i2c.freshdesk.com/a/admin/canned_responses/folders/80000143608/responses/80000247490/edit
   :color: primary

   Incident first response template
   ```

2. **Trigger an incident in PagerDuty**, using the 2i2c slack so we have a central location to discuss the incident.
   Use `/pd trigger` in the {guilabel}`#pagerduty-notifications` channel on the 2i2c slack to trigger the incident -
   after you type the command and hit `enter`, you should get a dialog box with options.

   For "Impacted Service", select "Managed JupyterHubs". We can have more fine-grained services here later if we wish.

   Assign it to whoever is the **Incident Commander**. This is by default one of the support stewards or whoever is
   triggering the event, but not necessarily[^note-on-delegation]!

   Provide a descriptive but short Title, but don't sweat it too much!

   If there is a freshdesk ticket for this, provide a link to that in the description.

   Check the box for "Create a dedicated Public Slack channel for this incident" to create a *new slack channel*
   for discussing the incident. This helps keep chatter off other channels *and* provides an easy location to gather
   information for the incident report afte the fact.

   This officially marks the beginning of an incident, and will help make sure we don't accidentally miss steps during
   or after the incident.

3. **Try resolving the issue** and communicate on the incident specific channel while you gather information and perform
   actions - even if only to mark these as notes to yourself.
4. **Designate an {term}`External Liason`**. Do this in the Incident issue. By default, this is the Incident Commander, though they may delegate this to others.[^note-on-delegation]
5. **Delegate to Subject Matter Experts as-needed**. The Incident Commander is empowered to delegate actions to Subject Matter Experts in order to investigate and resolve the incident quickly.[^note-on-delegation]
6. **Communicate our status every few hours**. The {term}`External Liason` is expected to communicate incident status and plan with the {term}`Community Representative`s. They should provide periodic updates that describe the current state of the incident, what we have tried, and our intended next steps. Here is a canned response to get started:

   ```{button-link} https://2i2c.freshdesk.com/a/admin/canned_responses/folders/80000143608/responses/80000247492/edit
   :color: primary

   Incident update template
   ```

7. **Communicate when the incident is resolved**. When we believe the incident
   is resolved, communicate with the Community Representative that things should be
   back to normal. Mark the FreshDesk ticket as {guilabel}`Resolved`.
8. **Fill in the {term}`Incident Report`**. The Incident Commander should do this in partnership with the Incident Response Team. We
   use PagerDuty's [postmortem](https://support.pagerduty.com/docs/postmortems) functionality to create the incident report. This
   allows us to easily incorporate notes and slack messages sent to pagerduty during the course of the incident, drastically reducing
   the amount of effort required to create the incident report.
9. **Mark the incident as resolved**. Once we have confirmation from the community (or no response after 48 working hours), and have filled in the incident {term}`Incident Report`, then close the incident by:
    - Marking the incident as "Resolved" in pagerduty.
    - Marking the FreshDesk ticket as {guilabel}`Closed`

[^note-on-delegation]: If you cannot find somebody to take on this work, or feel uncomfortable delegating, the {term}`Project Manager` should help you, and is empowered to delegate on your behalf.

## Handing off Incident Commander status

During an incident, it may be necessary to designate another person to be the Incident Commander.
For example, if it is getting late in the current IC's time zone, they feel burnt out from leading the incident response, or there is someone with better visibility or experience to be the Incident Commander.
This is encouraged and expected, especially for more complex or longer incidents!

To designate another team member as the Incident Commander, follow these steps:

1. **Confirm with them** that they are able and willing to serve as the Incident Commander.
2. **Reassign the incident on PagerDuty** to the new commander. This should produce a message in the slack channel for this event,
   thus communicating this change to the rest of the team.

## Key terms

```{glossary}
Incident Report
Incident Reports
  A document that describes what went wrong during an incident and what we'll do to avoid it in the future. When we have an {term}`Incident`, we create an Incident Report issue.
  This helps us explain what went wrong, and directs actions to avoid the incident in the future. Its goal is to identify improvements to process, technology, and team dynamics that can avoid incidents like this in the future. It is **not** meant to point fingers at anybody and care should be taken to avoid making it seem like any one person is at fault[^post-mortems].
```

[^post-mortems]: See the [Google SRE post-mortem culture](https://sre.google/sre-book/postmortem-culture/) and the [Blameless guide to post-mortems](https://www.blameless.com/sre/what-are-blameless-postmortems-do-they-work-how) for some guidelines.
