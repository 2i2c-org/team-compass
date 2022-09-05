---
name: "👋🏻 Remove a team member from the Team Roles calendar and rota"
about: Steps to follow to remove a team member from our Team Roles calendar and rota
# labels: "type: offboard"
title: "Offboarding from Team Role: <name>"
---

**Role(s) this person will be stepping away from:**

- [ ] Meeting Facilitator
- [ ] Support Steward

### Checklist

- Remove them from the appropriate [Slack usergroup](https://2i2c.slack.com/admin/user_groups)
  - [ ] `@meeting-facilitators`
  - [ ] `@support-stewards`
- Delete all upcoming events for the appropriate role(s) using [code described here](https://github.com/2i2c-org/team-roles-geekbot-sweep/blob/HEAD/README.md#delete_events_bulkpy)
  - [ ] Run for `meeting-facilitator` role
  - [ ] Run for `support-steward` role
- Regenerate upcoming events for the appropriate role(s), without the new member in the roster, using [code described here](https://github.com/2i2c-org/team-roles-geekbot-sweep/blob/HEAD/README.md#create_events_bulkpy)
  - [ ] Run for `meeting-facilitator` role
  - [ ] Run for `support-steward` role

:sparkles: **Congratulations! This person is no longer on the rota for their role. Thank you for all your hard work!** :sparkles:
