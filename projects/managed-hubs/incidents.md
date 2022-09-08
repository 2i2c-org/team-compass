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
   back to normal.
   - Marking the incident as "Resolved" in pagerduty.
   - Marking the FreshDesk ticket as {guilabel}`Closed`

[^note-on-delegation]: If you cannot find somebody to take on this work, or feel uncomfortable delegating, the {term}`Project Manager` should help you, and is empowered to delegate on your behalf.

## Creating the Incident Report

Once the incident is resolved, we must create an {term}`Incident Report`. This helps us understand what went wrong,
and how we can improve our systems to prevent a recurrance. This is a *very important* part of making our infrastructure
and human processes more stable and stress free over time, so we should try to do this after each incident. The
**Incident Commander** is responsible for making sure the Incident Report is done, even though they may not be the
person doing it.

Note that we *must* practice a [blameless culture](https://www.blameless.com/sre/what-are-blameless-postmortems-do-they-work-how)
around incident reports - Incidents are *always* caused by systemic issues, and hence solutions must be systemic
too. Go out of your way to make sure there is no finger-pointing.

We use PagerDuty's [postmortem](https://support.pagerduty.com/docs/postmortems) feature to create the Incident Report.
This lets us use notes, status updates from pagerduty as well as messages from Slack easily in the incident report!

1. Open the incident in the PagerDuty web interface, and Click the "New Postmortem Report" button on top. The incident
   needs to be already resolved before this feature is available.

2. The "Owner of the Review Process" should be set to the Incident Commander, or someone else they delegate to explicitly.

3. Fill out the "Impact Start Time" to be our best guess for when the incident started (*not* when the report came in), and
   the "Impact End Time" to be when service was restored. Best guesses will do!

4. Add the slack channel we created for this incident as a "Data Source", filled in with an appropriate time to cover all
   the messages there. You can add other channels too if there was conversation there about the incident. Click "Save Data Sources"
   to populate the timeline below with messages from the slack channels.

5. Fill out the timeline! The goal is to be concise but make it possible for someone reading it to answer "what happened, and when?".
   The timeline should include:

   1. The beginning of the impact.
   2. When the incident was brought to our attention, with a link to the source (Freshdesk ticket, slack message, etc).
   3. When we responded to the incident. This would coincide with the creation of the PagerDuty incident.
   4. Various debugging actions performed to ascertain the cause of the issue. Talking to yourself as you do this on the
      slack channel helps a lot here, as it helps communicate your methods to others on the team as well as help improve
      processes in the future more easily.

      Examples here would be things like `Looked at hub logs with "kubectl logs -n temple -l component=hub" and found <this>` or
      `Opened the cloud console and discovered notifications about quota". Pasting in commands is very helpful! This is an
      important way for team members to learn from each other - what you take for granted is perhaps news to someone else, or
      you might learn alternate ways of doing things!
   5. Actions taken to attempt to fix the issue, and their outcome. Paste commands executed if possible, as well as any
      GitHub PRs made. Putting this in Slack again helps.
   6. Any extra communication from the community affected that helped.
   7. Whenever the impact was fixed, and how that was verified.
   8. Whatever else you think would be helpful to someone who finds this incident report a few months from now, trying to fix a
      similar incident.

6. Fill out the "Analysis" section to the extent possible. In particular, the "Action Items" should be a list with items
   linked out to GitHub issues created for follow-up. Perfection is the enemy of the good here.

7. Review the report, and if the Incident Commander is happy with its completeness, mark the Status dropdown up top as "Reviewed".

8. Click "Save & View Report" button.

9. Download the PDF, and add it to the `2i2c/infrastrtucture` repository under the `incidents/` directory. This make sure our
   incidents are all *public*, so others can learn from them as well.

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
