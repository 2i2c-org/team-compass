---
name: "🙌 Add a team member to the Team Roles calendar and rota"
about: Steps to follow to add a team member into our Team Roles calendar and rota
labels: "type: onboard"
title: "Onboarding into Team Role: <name>"
---

**Role(s) this person will be taking on:**

- [ ] Meeting Facilitator
- [ ] Support Steward

### Checklist

- Add them to the appropriate [Slack usergroup](https://2i2c.slack.com/admin/user_groups)
  - [ ] `@meeting-facilitators`
  - [ ] `@support-stewards`

The above action will automatically mean they will start to be added into rotation on the [Team Roles calendar](https://calendar.google.com/calendar/embed?src=c_nq8hl7qsm484g1p7mfkm29jpo8%40group.calendar.google.com&ctz=Etc%2FUTC) and be pinged by the Slackbot for reminders.
However, we keep the calendar populated ~1 year in advance (to assist with PTO scheduling), so it may be a long time before their first shift comes around!
To expedite this a little you can use code in the [`team-roles-geekbot-sweep` repo](https://github.com/2i2c-org/team-roles-geekbot-sweep) to update the calendar.

- Delete all upcoming events for the appropriate role(s) using [code described here](https://github.com/2i2c-org/team-roles-geekbot-sweep/blob/HEAD/README.md#delete_events_bulkpy)
  - [ ] Run for `meeting-facilitator` role
  - [ ] Run for `support-steward` role
- Regenerate upcoming events for the appropriate role(s), with the new member in the roster, using [code described here](https://github.com/2i2c-org/team-roles-geekbot-sweep/blob/HEAD/README.md#create_events_bulkpy)
  - [ ] Run for `meeting-facilitator` role
  - [ ] Run for `support-steward` role

:tada: **Congratulations! This person is now on the rota for their new role!** :tada:
