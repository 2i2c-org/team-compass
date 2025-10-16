(support:timeboxed-evaluation)=
# Initial timeboxed (30m) ticket resolution checklist

In the [non-incident support response process](https://compass.2i2c.org/projects/managed-hubs/support/#non-incident-response-process), an initial 30m time-boxed ticket resolution process is documented.

The support triagers use these 30m time interval to try an resolve a ticket, before opening a follow-up issue about it.

The next sections represents an incomplete initial checklist that the support triager can follow in order to resolve the ticket or decide on opening a tracking issue about it, with the context they gained during this investigation.

The steps to follow depend greatly on the type of ticket. To simplify, only three big ticket categories will be addressed.

## Category 1: Something is not working

```{important}
If something is not working, you might be dealing with an incident, so depending on the scale of the issue and its nature, you might want to consider following the [Incident Response Process](https://compass.2i2c.org/projects/managed-hubs/incidents/process).
```

1. ✅ Ask for any additional info that might be needed
1. ✅ Check if the errors being reported are listed in this incomplete list of [the most common seen errors](https://infrastructure.2i2c.org/howto/troubleshoot/logs/common-errors/).
1. ✅ Depending on the issue being experienced, you should check the relevant logs:

    🟡 via cloud-agnostic tools like [kubectl or the deployer](https://infrastructure.2i2c.org/howto/troubleshoot/logs/kubectl-logs), which provide details about the current running components

    🟡 or search [the logs via the console](https://infrastructure.2i2c.org/howto/troubleshoot/logs/cloud-logs) which can be useful for digging out information about components, persisted for a longer time span (30d in GCP's case).

1. ✅ Save any of the logs that look useful
1. ✅ Check if you are dealing with any of [the most common seen problems](https://infrastructure.2i2c.org/sre-guide/common-problems-solutions/) and try and fix it.
  1. ❌ If not, then open a new GitHub issue, sharing as much context from the previous steps as possible and continue with the [non-incident response process](https://compass.2i2c.org/projects/managed-hubs/support/#non-incident-response-process)

## Category 2: New feature requested
```{list-table}
:widths: 30
:header-rows: 1

*   - Is the feature requested documented at [](hub-features)?
*   - ✅ Yes? Then enable it after checking it is in the scope of the contract.
*   - ❌ No? Then open a GitHub tracking issue about it and continue following the non-incident process.
```

## Category 3: Technical advice
```{list-table}
:widths: 30
:header-rows: 1

*   - Is the question about an area where the support triager has insight into?
*   - ✅ Yes? Then answer the ticket.
*   - ❌ No? Then open a GitHub tracking issue about it and continue following the non-incident process
```
