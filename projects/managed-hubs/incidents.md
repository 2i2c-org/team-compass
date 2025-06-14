(incidents)=
# Incident response

When an {term}`Incident` is declared, we trigger a special response in order to ensure that it is resolved quickly.
This section describes our incident response process, major roles and terminology, and what to expect.[^incident-refs][^google-sre][^acm-blog][^wikimedia-clinic-duty].

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
- The {term}`Support Triagers`
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
  A member on the {term}`Incident Response Team` with expertise in an area of relevance to an Incident. SMEs have a variety of backgrounds and abilities, and they should be pulled in to the Response Team as-needed by the {term}`Incident Commander`. Their goal is to take actions as-directed by the {term}`Incident Commander` to resolve an incident. The Tech Lead must always be included as a Subject Matter Expert, as they have unique expertise in solving certain problems and are ultimately accountable for successful incident resolution. 
```

(incidents:what)=
## What counts as an incident?

Eventually, we will have more nuanced and complete ways to track different kinds of incidents. However, for
now, we define an incident as one of:

1. The hub is inaccessible to a number of users (N>=2). Specifically, this manifests in three ways:
   a. They can not log in
   b. They can not start their servers
   c. They can not execute code (no kernels can be started)
2. A number of users (N>=2) cannot create or use Dask Gateway clusters.

Everything else is considered a support ticket only, not an incident. This *will* change in
the future as our process matures.

We do not have a limit on the support time we provide related to incidents (as
opposed to Change and Guidance requests, which have a {term}`Support Budget`).

```{note}
PagerDuty has a 'Severity' field for incidents. We do not use this field currently.
```

## Communication channels

### External communication

- The {term}`Incident Commander` acts as the primary point of communication with external stakeholders like the {term}`Community Representative`s.
- They may **delegate** this responsibility to another team member if they wish (e.g., to the {term}`Support Triager` team.)
- We may interact with external stakeholders via comments in Incident Response issues if it helps resolve the incident more quickly.

(incidents:communications)=
### Internal communication

- A channel *dedicated* to each incident will be created by pagerduty once an incident is created. This is where most of the
  discussion about the incident should happen.
- [`2i2c-org.pagerduty.com`](https://2i2c-org.pagerduty.com/) is a dashboard for managing incidents.
  This is the "source of truth" for any active or historical incidents.
- [The `#pagerduty-notifications` Slack channel](https://2i2c.slack.com/archives/C041E05LVHB) is *primarily* used to trigger
  new incidents and control pagerduty in other ways. Discussion of *specific* incidents should not happen here.

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

2. **Trigger an incident in PagerDuty**. Below are instructions for doing so via [the 2i2c slack](incidents:communications).
   - **Type `/pd trigger` and hit `enter` in `#pagerduty-notifications`** to trigger the incident
     After you hit `enter`, you should get a dialog box with options.
   - For "Impacted Service", **select `Managed JupyterHubs`**.
   - **Assign it to the Incident Commander**. By default this is one of the {term}`Support Triagers` or the person triggering the event, but may be delegated to others[^note-on-delegation]!
   - **Provide a descriptive but short title**, but don't sweat it too much!
   - **Add a link to the FreshDesk ticket** in the description (if there is one).
   - **Create a new Slack channel** by checking the box for `Create a dedicated Public Slack channel for this incident`.
     Use this channel for all conversations about the incident.

   This officially marks the beginning of an incident, and will help make sure we don't accidentally miss steps during or after the incident.

3. **Try resolving the issue** and communicate on the incident-specific channel while you gather information and perform actions - even if only to mark these as notes to yourself.

   ```{admonition} Do not use threaded Slack messages
   :class: warning

   Do **NOT** use threads when communicating in this Slack channel.
   When coming to write the [incident report](incidents:create-report) after the event, PagerDuty can import messages from the Slack channel in order to construct a timeline.
   However, it cannot import threaded messages, only those that are sent directly to the channel.
   Hence if the cause of an incident was established in a thread, this cannot be reflected automatically in the incident report.
   ```

4. **Delegate to Subject Matter Experts as-needed**. The Incident Commander is empowered to delegate actions to Subject Matter Experts in order to investigate and resolve the incident quickly. The {role}`Technology Lead` is available to validate and review recommended actions along with other Subject Matter Experts. When in doubt, delegate to the Tech Lead. [^note-on-delegation]
5. **Communicate our status every few hours**. The {term}`External Liason` is
   expected to communicate incident status and plan with the {term}`Community
   Representative`s. If the incident commander wants to delegate External Liason duties
   to someone else, they should:

   1. Assign the *Freshdesk* ticket to the external liason, as that is the default point of
      communication with community representatives.
   2. Make a note on the PagerDuty incident as well.

   The externl liason should provide periodic updates that describe the current
   state of the incident, what we have tried, and our intended next steps. Here is
   a canned response to get started:

   ```{button-link} https://2i2c.freshdesk.com/a/admin/canned_responses/folders/80000143608/responses/80000247492/edit
   :color: primary

   Incident update template
   ```

6. **Communicate when the incident is resolved**. When we believe the incident is resolved, communicate with the Community Representative that things should be back to normal.
   - Mark the incident as "Resolved" in pagerduty.
   - Mark the FreshDesk ticket as {guilabel}`Closed`.
7. **Create an incident report**.
   See [](incidents:create-report) for more information.

[^note-on-delegation]: If you cannot find somebody to take on this work, or feel uncomfortable delegating, the {role}`Technology Lead` should help you, and is empowered to delegate on your behalf.

(incidents:create-report)=
## Create an Incident Report

Once the incident is resolved, we must create an {term}`Incident Report`.
The **Incident Commander** is responsible for **starting the incident report process**, and **making sure the Incident Report is completed**.
They are not required to fill out all of the information in the report, though they may do so if they wish.
If another person will fill out the report, check with them first and then assign them as `Owner of the Review Process`.
See more detailed steps below.

We practice a [blameless culture](https://www.blameless.com/sre/what-are-blameless-postmortems-do-they-work-how) around incident reports.
Incidents are **always** caused by systemic issues, and hence solutions must be systemic too.
Go out of your way to make sure there is no finger-pointing.

We use [PagerDuty's postmortem feature](https://support.pagerduty.com/docs/postmortems) to create the Incident Report.
This lets us use notes, status updates from pagerduty as well as messages from Slack easily in the incident report!

1. **Ensure that the incident is resolved**.
   If not, refer to the proper step in [](support:incident-response).
   The incident needs to be resolved before a report can be generated.
2. **Open the incident** in the PagerDuty web interface, and click the `New Postmortem Report` button on top.
3. `Owner of the Review Process` should be set to the Incident Commander, or someone else they delegate to explicitly.
4. `Impact Start Time` is our best guess for when the incident started (*not* when the report came in).
   `Impact End Time` is when service was restored.
   Best guesses will do!
5. **Add Data Sources** that we will use to keep track of the actions that happened around the incident.
   - Link to the slack channel we created for this incident as a "Data Source", filled in with an appropriate time to cover all the messages there.
   % TODO: Add info on how to add GitHub issues/PRs to the timeline when we figure out how to do it.
   % - Add any other channels where there was conversation there about the incident (e.g., GitHub Issues or Pull Requests).

   Click `Save Data Sources` to populate the timeline below with messages from the slack channels.
6. **Fill out the timeline**. The goal is to be concise but make it possible for someone reading it to answer "what happened, and when?".
   See [](incidents:postmortem-timeline) for more information.
7. **Fill out the "Analysis" section** to the extent possible.
   In particular, the "Action Items" should be a list with items linked out to GitHub issues created for follow-up.
   Perfection is the enemy of the good here. Save as you go.
8. **Click "Save & View Report"** when you are done, and ask other members of the incident response team to review the incident report.
   They might add missing context, additional action items / summary details, or redact information. The person listed as
   the "Owner of the Review Process" is still responsible for making sure the rest of the process is completed.
9. After sufficient review, and if the Incident Commander is happy with its completeness, edit the report again, **mark the Status dropdown as "Reviewed"**, and then click "Save & View Report" again.
10. Download the PDF, and add it to the [`2i2c/incident-reports`](https://github.com/2i2c-org/incident-reports) repository under
    the `reports/` directory. This make sure our incidents are all *public*, so
    others can learn from them as well. Given review is already completed in the pagerduty interface, you don't need to wait
    for review to add the report here.
11. Email a link to the incident report to the community representative, ideally via the Freshdesk ticket used to communicate with
    them during the incident itself.



(incidents:postmortem-timeline)=
### Writing an incident timeline

Below are some tips and crucial information that is needed for a useful and thorough incident timeline. You can see
examples of previous incident reports at the [2i2c-org/incident-reports](https://github.com/2i2c-org/incident-reports/tree/main/reports)
repository.

The timeline should include:

1. The beginning of the impact.
2. When the incident was brought to our attention, with a link to the source (Freshdesk ticket, slack message, etc).
3. When we responded to the incident. This would coincide with the creation of the PagerDuty incident.
4. Various debugging actions performed to ascertain the cause of the issue.
   Talking to yourself as you do this on the slack channel helps a lot here, as it helps communicate your methods to others on the team as well as help improve
   processes in the future more easily.

   For example:

   - `Looked at hub logs with "kubectl logs -n temple -l component=hub" and found <this>`
   - `Opened the cloud console and discovered notifications about quota`.

   Pasting in commands is very helpful!
   This is an important way for team members to learn from each other - what you take for granted is perhaps news to someone else, or you might learn alternate ways of doing things!
5. Actions taken to attempt to fix the issue, and their outcome.
   Paste commands executed if possible, as well as any GitHub PRs made.
   If you've already done this in the incident Slack channel you may simply copy/paste text here.
6. Any extra communication from the community affected that helped.
7. Whenever the incident was fixed, and how that was verified.
8. Whatever else you think would be helpful to someone who finds this incident report a few months from now, trying to fix a similar incident.

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

  This helps us understand what went wrong, and how we can improve our systems to prevent a recurrance. Its goal is to identify improvements to process, technology, and team dynamics that can avoid incidents like this in the future. It is **not** meant to point fingers at anybody and care should be taken to avoid making it seem like any one person is at fault.

  This is a *very important* part of making our infrastructure and human processes more stable and stress-free over time, so we should do this after each incident.[^post-mortems].
```

[^post-mortems]: See the [Google SRE post-mortem culture](https://sre.google/sre-book/postmortem-culture/) and the [Blameless guide to post-mortems](https://www.blameless.com/sre/what-are-blameless-postmortems-do-they-work-how) for some guidelines.
