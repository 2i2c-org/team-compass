# Incident response


When an {term}`Incident` is declared, we trigger a special response in order to ensure that it is resolved quickly.
This section describes our incident response process, major roles and terminology, and what to expect.[^incident-refs]

[^incident-refs]: The [PagerDuty Incident Response Guide](https://response.pagerduty.com/) and the [Google SRE Incident response guide](https://sre.google/workbook/incident-response/) inspired much of the content on this page.

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
- The {term}`Support Steward`s
- One or more {term}`Subject Matter Expert`s (SMEs)

```{glossary}
Incident Response Team
  The group of roles that collectively understand, plan, resolve, and communicate our actions around an {term}`Incident`. The people in these roles may change in a fluid manner, and one person may serve in multiple roles. A rough way to approximate this team is "the people that have communicated in internal and external channels to resolve an incident."

Incident Commander
  The {term}`Source of Truth` about the current state and action plan surrounding an incident. The Incident Commander has the authority to plan and delegate action to others on the {term}`Incident Response Team`. They are **not expected** to do take actions themselves. Their goal is to help the team make consistent and deliberate progress towards resolving an incident.

Subject Matter Expert
  A member on the {term}`Incident Response Team` with expertise in an area of relevance to an Incident. SMEs have a variety of backgrounds and abilities, and they should be pulled in to the Response Team as-needed by the {term}`Incident Commander`. Their goal is to take actions as-directed by the {term}`Incident Commander` to resolve an incident.
```

## Communication channels

### External communication

- The {term}`Support Steward` team acts as the primary point of communication with external stakeholders like the {term}`Community Representative`s.
- We may interact with external stakeholders via comments in Incident Response issues if it helps resolve the incident more quickly.

### Internal communication

- The Slack channel [{guilabel}`#support-freshdesk`](https://2i2c.slack.com/archives/C028WU9PFBN) contains real-time communication about support issues. Use this to signal-boost support requests related to {term}`Incident`s.
- [Issues with the {guilabel}`incident` label](https://github.com/2i2c-org/infrastructure/issues?q=is%3Aopen+label%3A%22type%3A+Hub+Incident%22+sort%3Aupdated-desc) are where we track progress when [resolving incidents](support:incident-response).


(support:incident-response)=
## Incident response process

Incidents are a special kind of support ticket, because they are related to degraded service that immediately impacts communities.
We prioritize the resolution of incidents above all other kinds of work, and have a special process for tracking conversation and progress with them.

Here is the process that we follow for incidents:

1. **Acknowledge the incident**. Communicate with the Community Representative that there is an incident. Here is a template to get started:

   ```
   Hello { NAME }, we have investigated this request and have concluded that
   it is related to an incident that is causing diminished service for your
   community.
   
   We believe that this incident is related to { CONTEXT HERE } and will
   investigate further on next actions. Information about our incident
   response process can be found [in our team support documentation](https://team-compass.2i2c.org/en/latest/projects/managed-hubs/support.html).

   We've also opened an Incident Report in this issue where you can track progress if you wish: { LINK TO INCIDENT REPORT }.
 
   We'll prioritize resolving this incident over our other work, and
   will communicate with you throughout our attempts to resolve it.
   We might be in touch with requests for clarifications if needed.
   ```
2. **Open an incident issue**.
   For each {term}`Incident` we create a dedicated issue to track its progress. [{bdg-primary}`open an incident issue`](https://github.com/2i2c-org/infrastructure/issues/new?assignees=&labels=type%3A+Hub+Incident%2Csupport&template=3_incident-report.md&title=%5BIncident%5D+%7B%7B+TITLE+%7D%7D) and notify our engineering team via Slack.
3. **If you can resolve in 30 minutes**, try doing so.
4. **If you cannot resolve in 30 minutes**, ping our engineering team and our Project Manager in the {guilabel}`#support-freshdesk` channel so that they are aware of the incident.
5. **Designate an {term}`Incident Commander`**. If the Support Steward wishes to designate another team member as Incident Commander, should do so in the Incident issue.
6. **Investigate and resolve the incident**. The Incident Commander should follow the structure of the incident issue opened in the step above.
7. **Delegate to Subject Matter Experts as-needed**. The Incident Commander is empowered to delegate actions to Subject Matter Experts in order to investigate and resolve the incident quickly.
8. **Communicate every few hours**. The {term}`Incident Commander` is expected to communicate incident status and plan with the {term}`Support Steward`s, are are expected to communicate to the {term}`Community Representative`s. Provide periodic updates to communities as we attempt to resolve the incident. Here is a template to get started:

   ```
   Hello { NAME }, this is a quick update on our progress resolving
   your incident.

   We believe the problem is { XXX } and are investigating { YYY }
   to resolve it. We will keep you updated as we continue to make progress.
   Please let us know if you have had more reports of issues,
   or reports that your issues have gone away.
   ```
9. **Communicate when the incident is resolved**. When we believe the incident is resolved, communicate with the Community Representative that things should be back to normal. Mark the FreshDesk ticket as {guilabel}`Resolved`.
10. **Fill in the {term}`Incident Report`**. The Incident Commander should do this in partnership with the Incident Response Team.
11. **Close the incident ticket**. Once we have confirmation from the community (or no response after 48 working hours), and have filled in the incident {term}`Incident Report`, then close the incident by:
    - Closing the incident issue on GitHub
    - Marking the FreshDesk ticket as {guilabel}`Closed`

## Key terms

```{glossary}
Incident Report
  A document that describes what went wrong during an incident and what we'll do to avoid it in the future. When we have an {term}`Incident`, we create an Incident Report issue.
  This helps us explain what went wrong, and directs actions to avoid the incident in the future. Its goal is to identify improvements to process, technology, and team dynamics that can avoid incidents like this in the future. It is **not** meant to point fingers at anybody and care should be taken to avoid making it seem like any one person is at fault[^post-mortems].
```

[^post-mortems]: See the [Google SRE post-mortem culture](https://sre.google/sre-book/postmortem-culture/) and the [Blameless guide to post-mortems](https://www.blameless.com/sre/what-are-blameless-postmortems-do-they-work-how) for some guidelines.
