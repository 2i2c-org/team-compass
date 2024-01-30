---
name: "👋🏻 Remove a team member from the Support Triager Team Role, calendar and rota"
about: Steps to follow to remove a team member from our Team Roles calendar and rota
# labels: "type: offboard"
title: "Offboarding from Support Triager: <name>"
---

### Checklist

- [ ] Remove them from the `@support-triagers` [Slack usergroup](https://2i2c.slack.com/admin/user_groups)
- [ ] Delete all upcoming events for the Support Triager using [code described here](https://github.com/2i2c-org/team-roles-geekbot-sweep/blob/HEAD/README.md#delete_events_bulkpy)
  - Command should look something like: `poetry run delete-bulk-events support-triager`
  - Use the `--date` flag to tweak when to begin deleting events from
- [ ] Regenerate upcoming events for the Support Triager, without the specified member in the roster, using [code described here](https://github.com/2i2c-org/team-roles-geekbot-sweep/blob/HEAD/README.md#create_events_bulkpy)
  - Command should look something like: `poetry run create-bulk-events support-triager`
  - Use the `--date` flag to tweak when to begin creating events from, and the `--team-member` flag to indicate where in the team to begin cycling through from

:sparkles: **Congratulations! This person is no longer on the rota for their role. Thank you for all your hard work!** :sparkles:
