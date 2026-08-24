# Handling events

Sometimes, communities will want to run events like workshops, exams or even conferences on their hubs. The hubs might be specifically deployed to serve this purpose, or they might be their day to day hubs. In either case, there are infrastructure updates that need to happen to ensure that the hub can sustain the increased load and change in workflow.

```{tip}
The infrastructure guide for events is available at https://infrastructure.2i2c.org/howto/prepare-for-events/.
The community facing guide for events is available at https://docs.2i2c.org/admin/community/events/.
```

## Process for handing over event technical context

Event requests come in as support tickets and are then turned into actionable GitHub issues, tracked in our planning board. The process is described in more details in the [support guide](https://compass.2i2c.org/services/technical-support/process/#overview-of-the-support-process).

```{important}
From this point on, the GitHub issue becomes the single source of technical context.
```

This issue must track _all_ changes that were performed to support the event. The information must be detailed enough so that, if another engineer needs to take on the event support work, they will refer to this info to understand what was done and why.

The event tracking issue must reference:
- the support ticket link
- pull requests updating the infrastructure to support the event
- any other external GitHub issues that are relevant to the event (e.g. an issue tracking the event on the community's side)
- links to all Slack conversations about the event (e.g. conversations happening in the `#support-freshdesk` channel, or in the community's Slack workspace)
