(incidents:after)=

# After the incident

After an incident is resolved, there are a few important steps to take to ensure that we learn from the incident and make sure it doesn't happen again.

These steps are encoded in three GitHub issues that are automatically opened in https://github.com/2i2c-org/infrastructure, whenever a PagerDuty incident is assigned a P1 priority.

1. One representing the ongoing outage
   - this issue must be sized, added to the current iteration and closed after the incident is over
   - the responsibility goes to the people assigned to the issues, but especially the incident responder
   - e.g. https://github.com/2i2c-org/infrastructure/issues/7638

2. One representing the incident report and action items drafting
   - the responsibility goes to the people assigned to the issues, but especially the incident responder
   - e.g. https://github.com/2i2c-org/infrastructure/issues/7639

3. One representing the review of the incident resolution, report and action items and making the report public
   - the responsability goes to the Team Lead and Engineer Manager
   - e.g. https://github.com/2i2c-org/infrastructure/issues/7640

## 1. Create an Incident Report in PagerDuty

We use [PagerDuty's postmortem feature](https://support.pagerduty.com/docs/postmortems) to create the Incident Report. This lets us use notes, status updates from PagerDuty as well as messages from Slack easily in the incident report!

1. **Open the incident** in the PagerDuty web interface, and click the {guilabel}`New Postmortem Report` button on top. We do not need to populate the report at this stage.
1. Copy the report URL for the next step.

## 2. Create post-incident action items

After the incident is over, we _must_ prioritize any action items that prevent this kind of incident at the same level as a contract deliverable, and attempt to bring it into the next sprint. While we can't guarantee there shall be no outages, we must do everything we can to prevent known causes of outages from recurring.

Use the {guilabel}`Incident Action Item` template to create an issue in the [infrastructure repository](https://github.com/2i2c-org/infrastructure/issues)

### Responsibility

It's the {role}`Technical Lead`'s responsibility to make sure that an absolute minimum sized task to mitigate the issue that caused this incident, exists and the responsibility of the {role}`Technical Lead` & {role}`Engineering Manager` to advocate for bringing it in during the next sprint.

(incidents:create-report)=

## 3. Fill out the Incident Report

Once the incident is resolved, we must create an {term}`Incident Report`. Our incidents are all [_public_](https://github.com/2i2c-org/incident-reports/tree/main/reports), so others can learn from them as well.

We practice a [blameless culture](https://www.blameless.com/sre/what-are-blameless-postmortems-do-they-work-how) around incident reports.
Incidents are **always** caused by systemic issues, and hence solutions must be systemic too. Go out of your way to make sure there is no finger-pointing.

### Report lifecycle

The incident report goes through a few stages before it gets public:

1. The incident report has a `Draft` status in PagerDuty, after it was redacted by the first person
2. The incident report has a `Reviewed` status in PagerDuty, after the second person has reviewed it
3. The incident report has a `Closed` status in PagerDuty, after the `Tech Lead` has reviewed it, its resolution and its action items

### Responsibility

The Incident Responder and the incident team are responsible for **drafting the incident report process**, and **doing an initial review of the report and action items**

Ultimately, {role}`Technical Lead` & {role}`Engineering Manager` are responsible for **making sure the Incident Resolution, Report and action items are completed, correct and public**.

### Steps

```{note}
The [Oct 2025 UToronto Incident Report](https://github.com/2i2c-org/incident-reports/blob/main/reports/2025-10-03-utoronto-new-server-startup.pdf) is a good example of a short, simple and clear incident report.
```

1. **Visit the Postmortem Report** URL that we saved earlier, and start to fill out the sections.
   - `Owner of the Review Process` should be set to the person writing the incident report.
   - `Impact Start Time` is our best guess for when the incident started (_not_ when the report came in).
   - `Impact End Time` is when service was restored.
     Best guesses will do!
2. **Add Data Sources**
   - Link to the Slack channel we created for this incident, with an appropriate time to cover all the messages
3. **Fill out the timeline**
   - The goal is to be concise but make it possible for someone reading it to answer "what happened, and when?".
   - See [](incidents:postmortem-timeline) for more information.
4. **Fill out the "Analysis" section** to the extent possible.
   - Perfection is the enemy of the good here. Save as you go.
   - In particular, the `Action Items` should be a list with items linked out to GitHub issues created for follow-up.
5. **Click "Save & View Report"** when you are done
   - Ask other members of the incident response team to review the incident report
   - In particular, the {role}`Technical Lead` should review and approve the report before it is marked as "Reviewed".
6. After sufficient review, and if the {role}`Technical Lead` is happy with its completeness, edit the report again, **mark the Status dropdown as "Reviewed"**, and then click "Save & View Report" again.
7. **Download the PDF**, and add it to the [`2i2c/incident-reports`](https://github.com/2i2c-org/incident-reports) repository
   - Given review is already completed in the pagerduty interface, you don't need to wait for review to add the report here.
8. **Email** a link to the incident report to the community representative, ideally via the Freshdesk ticket used to communicate with them during the incident itself.

(incidents:postmortem-timeline)=

### Tips for writing an incident timeline

Below are some tips and crucial information that is needed for a useful and thorough incident timeline. You can see
examples of previous incident reports at the [2i2c-org/incident-reports](https://github.com/2i2c-org/incident-reports/tree/main/reports)
repository.

The timeline should include:

1. The beginning of the impact.
2. When the incident was brought to our attention, with a link to the source (Freshdesk ticket, slack message, etc).
3. When we responded to the incident. This would coincide with the creation of the PagerDuty incident.
4. Various debugging actions performed to ascertain the cause of the issue.
   Talking to yourself as you do this on the Slack channel helps a lot here, as it helps communicate your methods to others on the team as well as help improve
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
7. When the incident was fixed, and how that was verified.
8. Whatever else you think would be helpful to someone who finds this incident report a few months from now, trying to fix a similar incident.

## Key terms

```{glossary}
Incident Report
Incident Reports
  A document that describes what went wrong during an incident and what we'll do to avoid it in the future. When we have an {term}`Incident`, we create an Incident Report issue.

  This helps us understand what went wrong, and how we can improve our systems to prevent a recurrance. Its goal is to identify improvements to process, technology, and team dynamics that can avoid incidents like this in the future. It is **not** meant to point fingers at anybody and care should be taken to avoid making it seem like any one person is at fault.

  This is a *very important* part of making our infrastructure and human processes more stable and stress-free over time, so we should do this after each incident.[^post-mortems].
```

[^post-mortems]: See the [Google SRE post-mortem culture](https://sre.google/sre-book/postmortem-culture/) and the [Blameless guide to post-mortems](https://www.blameless.com/sre/what-are-blameless-postmortems-do-they-work-how) for some guidelines.
