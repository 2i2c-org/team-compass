(support:incident-response)=
# Incident response process

We prioritize the resolution of incidents above all other kinds of work, and have a special process we follow.

## Incident sources

1. [Automated Pagerduty alerts](https://infrastructure.2i2c.org/topic/monitoring-alerting/alerting)
2. [Support Freshdesk tickets](support:index)

## Steps
When an incident is identified via any of the above sources, the following steps must be taken:

### 1. Validate that we are dealing with an outage
   ````{tab-set}
   ```{tab-item} PagerDuty alert
   :sync: pagerduty
   - If the incident came via an automated PagerDuty alert and has a `take immediate action` tag, then **it is definitely an outage**.
   - If if doesn't have this tag, then based on the alert's type follow the [Manage Alerts guide](https://infrastructure.2i2c.org/howto/manage-alerts/#what-to-do-when-an-alert-fires-based-on-its-type-and-severity) and manually test the infrastructure to determine if it's matching the [definition of an outage](https://2i2c-pilot-documentation--272.org.readthedocs.build/admin/topics/outages/#outages) or not.
   ```

   ```{tab-item} Freshdesk ticket
   :sync: freshdesk
   - If the incident report was triggered via a Freshdesk ticket, then try to reproduce the issue.
   - If you cannot reproduce it, ask for more information from the community representative via Freshdesk. If the issue is reproducible and matching the [definition of an outage](https://2i2c-pilot-documentation--272.org.readthedocs.build/admin/topics/outages/#outages), then proceed with the next steps.
   ```
   ````

### 2. Officially mark the beginning of the incident
   ```{important}
   An incident officially starts when:
   - a **PagerDuty P1 incident** exists
   - someone has **acknowledged the incident** in PagerDuty
   - a separate **Slack channel** for this incident exists
   - the **community has been informed** via Freshdesk of the ongoing incident
   ```

   `````{tab-set}
   ````{tab-item} PagerDuty alert
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

### 3. Try resolving the issue
   At all times, try to communicate on the incident-specific channel while you gather information and perform actions - even if only to mark these as notes to yourself.

   ```{admonition} Do not use threaded Slack messages
   :class: warning

   Do **NOT** use threads when communicating in this Slack channel.
   When coming to write the [incident report](incidents:create-report) after the event, PagerDuty can import messages from the Slack channel in order to construct a timeline.
   However, it cannot import threaded messages, only those that are sent directly to the channel.
   Hence if the cause of an incident was established in a thread, this cannot be reflected automatically in the incident report.
   ```

### 4. Get all hands on deck
   If there are other Infrastructure Engineering team members available, pull them in as {term}`Subject Matter Experts` in order to investigate and resolve the inci
   dent quickly. When in doubt, delegate to the Tech Lead.[^note-on-delegation]

### 5. Communicate our status every few hours
   The {term}`Communication Liaison` is expected to communicate incident status and plan with the {term}`Community Representative`s.

   They should provide periodic updates that describe the current state of the incident, what we have tried, and our intended next steps. Here is a canned response to get started:

   ```{button-link} https://2i2c.freshdesk.com/a/admin/canned_responses/folders/80000143608/responses/80000247492/edit
   :color: primary

   Incident update template
   ```
### 6. Make sure the incident is resolved
   The {role}`Technology Lead` should be pulled in to validate and review the actions taken and suggested to be taken next.

### 7. Communicate when the incident is resolved
   When we believe the incident is resolved, communicate with the Community Representative that things should be back to normal.
   - Mark the incident as {guilabel}`Resolved` in PagerDuty.
   - Mark the FreshDesk ticket as {guilabel}`Resolved`

### 8. Take follow-up actions
   See [](incidents:after) for more information.

[^note-on-delegation]: If you cannot find somebody to take on this work, or feel uncomfortable delegating, the {role}`Technology Lead` should help you, and is empowered to delegate on your behalf.

## Handing off Incident Responder status

During an incident, it may be necessary to designate another person to be the Incident Responder.
For example, if it is getting late in the current IC's time zone, they feel burnt out from leading the incident response, or there is someone with better visibility or experience to be the Incident Responder.
This is encouraged and expected, especially for more complex or longer incidents!

To designate another team member as the Incident Responder, follow these steps:

1. **Confirm with them** that they are able and willing to serve as the Incident Responder
2. **Reassign the incident on PagerDuty** to the new Responder