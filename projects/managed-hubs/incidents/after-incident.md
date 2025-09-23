(incidents:after)=
# After the incident
After an incident is resolved, there are a few important steps to take to ensure that we learn from the incident and make sure it doesn't happen again.

(incidents:create-report)=
## Create an Incident Report

Once the incident is resolved, we must create an {term}`Incident Report`.
The {term}`Incident Responder` is responsible for **starting the incident report process**, and **making sure the Incident Report is completed**.
They are not required to fill out all of the information in the report, though they may do so if they wish.
If another person will fill out the report, check with them first. See more detailed steps below.

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

## Post-incident action items

After the incident is over, we *must* prioritize any action items that prevent this kind of incident at the same level as a contract deliverable, and attempt to bring it into the next sprint. While we can't guarantee there shall be no outages, we must do everything we can to prevent known causes of outages from recurring.

It's the tech lead's responsibility to shape an absolute minimum sized task to mitigate the issue that caused this incident, and the responsibility of the tech lead & engineering manager to advocate for bringing it in during the next sprint.

## Key terms

```{glossary}
Incident Report
Incident Reports
  A document that describes what went wrong during an incident and what we'll do to avoid it in the future. When we have an {term}`Incident`, we create an Incident Report issue.

  This helps us understand what went wrong, and how we can improve our systems to prevent a recurrance. Its goal is to identify improvements to process, technology, and team dynamics that can avoid incidents like this in the future. It is **not** meant to point fingers at anybody and care should be taken to avoid making it seem like any one person is at fault.

  This is a *very important* part of making our infrastructure and human processes more stable and stress-free over time, so we should do this after each incident.[^post-mortems].
```

[^post-mortems]: See the [Google SRE post-mortem culture](https://sre.google/sre-book/postmortem-culture/) and the [Blameless guide to post-mortems](https://www.blameless.com/sre/what-are-blameless-postmortems-do-they-work-how) for some guidelines.
