(incidents:index)=
# Incident response

When an {term}`Incident` is declared, we follow a specific process in order to ensure that it is resolved quickly.
This section describes our incident response process, major roles and what to expect after an incident has been mitigated. We continually refine this process, taking lessons from our own experience and other experts. [^incident-refs][^google-sre][^acm-blog][^wikimedia-clinic-duty].

[^incident-refs]: The [PagerDuty Incident Response Guide](https://response.pagerduty.com/) describes a similar process with different roles.

[^google-sre]: The [Google SRE Incident response guide](https://sre.google/workbook/incident-response/) has a wealth of information about incident response and distributed SRE teams.

[^acm-blog]: This [ACM blog post](https://queue.acm.org/detail.cfm?id=3380779) describes the complexity of coordinating across a team of distributed responders during an incident, and notes a places where Incident Commander roles may actually hinder responsiveness. It is a good lesson in the complexity of incidents with distributed teams!

[^wikimedia-clinic-duty]: The [WikiMedia Clinic Duty](https://wikitech.wikimedia.org/wiki/SRE/Clinic_Duty#Responsibilities) process also inspired our process here, and is a great overall workflow around distributed SRE.

:::{admonition} In Beta!
:class: warning
We are currently working out our Incident Response process.
The content on this page might change over time, and we welcome suggested changes and pull requests!
:::


```{toctree}
before-incident
process
after-incident
```
