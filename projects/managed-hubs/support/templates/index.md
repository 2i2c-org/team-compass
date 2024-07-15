(support:templates)=
# Support Templates

Here are a collection of templates you can use when communicating with a community
in a support capacity. Ensure the values enclosed by `{{ }}` are filled in before
sending.

(support:templates:budget-alerts)
## Notifying a community champion of a budget alert trigger

> **Subject line:** Notice of increased usage on JupyterHub cluster {{ cluser_name }}
> 
> Hello {{ community_champion }},
> 
> We are writing to inform you that your JupyterHub cluster  in {{ cloud_vendor }}
> project {{ project_id }} is experiencing unusually high usage. It is currently on
> track to cost you a high bill for {{ next billing month }}. We're contacting you
> because you're in our records as the community champion for {{ community_name }}.
> 
> **Details**
> 
> Your forecasted usage for {{ month }} would be {{ cost }}. This is above the budget
> alert threshold we set of {{ alert_threshold }}. We set thresholds using a forecasting
> model that averages the past three months of costs and adds a 20% buffer. If you
> would like to change this threshold, please let us know by emailing support@2i2c.org.
> 
> Remember, you can always track usage of your hubs with your Grafana instance at
> {{ grafana_url }}.
> 
> **What you should do next**
> 
> If you are expecting this increase because of high usage that you know about, you
> don't need to do anything! But if this is unexpected, we'd like to talk with you
> to collaboratively understand why the costs have gone up, and resolve the issue.
> 
> If you have any questions, please let us know by replying to this email.
> 
> As usual, you can expect your next bill by {{ latest possible date of next bill }}.
> 
> Thank you,
> 
> {{ name of customer service rep }}
