(support:incident-response)=
# Incident response process

We prioritize the resolution of incidents above all other kinds of work, and have a special process we follow.

## Incident sources

1. [Automated Pagerduty alerts](https://infrastructure.2i2c.org/topic/monitoring-alerting/alerting)
2. [Support Freshdesk tickets](support:index)

## Steps to take
When an incident is identified via any of the above sources, the following steps must be taken:

### Validate that we are dealing with an outage
   ````{tab-set}
   ```{tab-item} Pagerduty alert
   :sync: pagerduty
   - If the incident came via an automated Pagerduty alert and has a `take immediate action` tag, then **it is definitely an outage**.
   - If if doesn't have this tag, then based on the alert's type follow the [Manage Alerts guide](https://infrastructure.2i2c.org/howto/manage-alerts/#what-to-do-when-an-alert-fires-based-on-its-type-and-severity) and manually test the infrastructure to determine if it's matching the [definition of an outage](https://2i2c-pilot-documentation--272.org.readthedocs.build/admin/topics/outages/#outages) or not.
   ```

   ```{tab-item} Freshdesk ticket
   :sync: freshdesk
   - If the incident report was triggered via a Freshdesk ticket, then try to reproduce the issue.
   - If you cannot reproduce it, ask for more information from the community representative via Freshdesk. If the issue is reproducible and matching the [definition of an outage](https://2i2c-pilot-documentation--272.org.readthedocs.build/admin/topics/outages/#outages), then proceed with the next steps.
   ```
   ````

### Acknowledge the incident
   To acknowledge an incident, we need to make sure that:
   - a **PagerDuty P1 incident** exists
   - someone has **acknowledged the incident** in PagerDuty
   - a separate **Slack channel** for this incident exists
   - the **community has been informed** via Freshdesk of the ongoing incident

   Once these conditions are met, this **officially marks the beginning of an incident**, and will help make sure we don't accidentally miss steps during or after the incident.

   `````{tab-set}
   ````{tab-item} Pagerduty alert
   :sync: pagerduty
   The incident already exists in PagerDuty, so make sure the conditions above are met.
   ````

   ````{tab-item} Freshdesk ticket
   :sync: freshdesk
   1. You need to first create a `P1` incident in PagerDuty

      The fields are self-explanatory, but the most important ones are:
      - Setting the priority to `P1`
      - Choosing one of the Impacted Services that matches best the affected hub service. If not sure, choose `Misc alerts from Prometheus Alert Manager`.
      - Create a new Slack channel by checking the box for `Create a dedicated Public Slack channel for this incident`. Use this channel for all conversations about the incident.

      You can create a PagerDuty incident in two ways:
      - [Using the UI](https://2i2c-org.pagerduty.com/incidents/create?service_id=PC33P4Y)
      - Using Slack by typing `/pd trigger` and hitting `enter` in `#pagerduty-notifications`

   2. Validate to the Community Representative, via the Freshdesk ticket, that there is indeed an incident happening. If you wish, use this canned response as a start for responding:
      ```{button-link} https://2i2c.freshdesk.com/a/admin/canned_responses/folders/80000143608/responses/80000247490/edit
      :color: primary

      Incident first response template
      ```
   ````
   `````

### Try resolving the issue
   At all times, try to communicate on the incident-specific channel while you gather information and perform actions - even if only to mark these as notes to yourself.

   ```{admonition} Do not use threaded Slack messages
   :class: warning

   Do **NOT** use threads when communicating in this Slack channel.
   When coming to write the [incident report](incidents:create-report) after the event, PagerDuty can import messages from the Slack channel in order to construct a timeline.
   However, it cannot import threaded messages, only those that are sent directly to the channel.
   Hence if the cause of an incident was established in a thread, this cannot be reflected automatically in the incident report.
   ```

### Get all hands on deck
   If there are other Infrastructure Engineering team members available, pull them in as Subject Matter Experts in order to investigate and resolve the incident quickly.

   When the {role}`Technology Lead` will be available, they will validate and review recommended actions. When in doubt, delegate to the Tech Lead.[^note-on-delegation]

### Communicate our status every few hours
   The {term}`Communication Liaison` is expected to communicate incident status and plan with the {term}`Community Representative`s.

   They should provide periodic updates that describe the current state of the incident, what we have tried, and our intended next steps. Here is a canned response to get started:

   ```{button-link} https://2i2c.freshdesk.com/a/admin/canned_responses/folders/80000143608/responses/80000247492/edit
   :color: primary

   Incident update template
   ```

### Communicate when the incident is resolved
   When we believe the incident is resolved, communicate with the Community Representative that things should be back to normal.
   - Mark the incident as "Resolved" in pagerduty.
   - Mark the FreshDesk ticket as {guilabel}`Resolved`.

### Take follow-up actions
   See [](incidents:create-report) for more information.

[^note-on-delegation]: If you cannot find somebody to take on this work, or feel uncomfortable delegating, the {role}`Technology Lead` should help you, and is empowered to delegate on your behalf.
