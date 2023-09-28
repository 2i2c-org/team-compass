---
name: "🙌 Add a team member to the Support Triager Team Role, calendar and rota"
about: Steps to follow to add a team member into our Team Roles calendar and rota
labels: "type: onboard"
title: "Onboarding into Support Triager: <name>"
---

### Checklist

- Add them to the a`@support-stewards` [Slack usergroup](https://2i2c.slack.com/admin/user_groups)

The above action will automatically mean they will start to be added into rotation on the [Team Roles calendar](https://calendar.google.com/calendar/embed?src=c_nq8hl7qsm484g1p7mfkm29jpo8%40group.calendar.google.com&ctz=Etc%2FUTC) and be pinged by the Slackbot for reminders.
However, we keep the calendar populated ~1 year in advance (to assist with PTO scheduling), so it may be a long time before their first shift comes around!
To expedite this a little you can use code in the [`team-roles-geekbot-sweep` repo](https://github.com/2i2c-org/team-roles-geekbot-sweep) to update the calendar.

- [ ] Delete all upcoming events for the Support Triager using [code described here](https://github.com/2i2c-org/team-roles-geekbot-sweep/blob/HEAD/README.md#delete_events_bulkpy)
  - Command should look something like: `poetry run delete-bulk-events support-steward`
  - Use the `--date` flag to tweak when to begin deleting events from
- [ ] Regenerate upcoming events for the Support Triager, with the new member in the roster, using [code described here](https://github.com/2i2c-org/team-roles-geekbot-sweep/blob/HEAD/README.md#create_events_bulkpy)
  - Command should look something like: `poetry run create-bulk-events support-steward`
  - Use the `--date` flag to tweak when to begin creating events from, and the `--team-member` flag to indicate where in the team to begin cycling through from

:tada: **Congratulations! This person is now on the rota for their new role!** :tada:
