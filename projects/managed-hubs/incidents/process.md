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

3. **Set priority on PagerDuty**: If this incident affects end users, please set Priority field in PagerDuty to "P1".

4. **Try resolving the issue** and communicate on the incident-specific channel while you gather information and perform actions - even if only to mark these as notes to yourself.

   ```{admonition} Do not use threaded Slack messages
   :class: warning

   Do **NOT** use threads when communicating in this Slack channel.
   When coming to write the [incident report](incidents:create-report) after the event, PagerDuty can import messages from the Slack channel in order to construct a timeline.
   However, it cannot import threaded messages, only those that are sent directly to the channel.
   Hence if the cause of an incident was established in a thread, this cannot be reflected automatically in the incident report.
   ```

5. **Delegate to Subject Matter Experts as-needed**. The Incident Commander is empowered to delegate actions to Subject Matter Experts in order to investigate and resolve the incident quickly. The {role}`Technology Lead` is available to validate and review recommended actions along with other Subject Matter Experts. When in doubt, delegate to the Tech Lead. [^note-on-delegation]

6. **Communicate our status every few hours**. The {term}`External Liason` is
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

7 **Communicate when the incident is resolved**. When we believe the incident is resolved, communicate with the Community Representative that things should be back to normal.
   - Mark the incident as "Resolved" in pagerduty.
   - Mark the FreshDesk ticket as {guilabel}`Closed`.
8. **Create an incident report**.
   See [](incidents:create-report) for more information.

[^note-on-delegation]: If you cannot find somebody to take on this work, or feel uncomfortable delegating, the {role}`Technology Lead` should help you, and is empowered to delegate on your behalf.
