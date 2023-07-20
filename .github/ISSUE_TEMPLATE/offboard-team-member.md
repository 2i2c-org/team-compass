---
name: "👋🏻 Offboard a departing team member"
about: Steps to follow for a departing team member
labels: "type: offboard"
title: "Departing <name>"
---

- Departing person's name: `INSERT NAME`
- Departing person's manager: `@INSERT_HANDLE`

### Departure checklist

The manager should follow the checklist below to offboard a departing team member after exit.
Don't hesitate to delegate some actions to others (e.g. if another person needs to give access to an account because you aren't able to).

**First steps**

- [ ] Schedule a 2i2c offboarding meeting
- [ ] Arrange with CS&S HR team to do formal exit interview


**Accounts**

Document accounts:

- [ ] Get member's [GitHub.com account](https://github.com)
- [ ] Get member's [ReadTheDocs.org account](https://readthedocs.org)
- [ ] Get member's [Quay.io account](https://quay.io)
- [ ] Get member's [NameCheap.com account](https://namecheap.com)
- [ ] Get member's [PagerDuty account](https://pagerduty.com)


** After Departure**

Remove 2i2c accounts and remove from team accounts:

- [ ] Deactivate a @2i2c.org Google account for them
	- Note that this requires [access to the Admin Panel](https://compass.2i2c.org/en/latest/administration/google-workspace.html?highlight=workspaces#access-and-permissions), a permission held by any 2i2c team lead
- [ ] Remove them from the proper Google group in our Google Admin space.
- [ ] Remove them from [2i2c GitHub teams](https://github.com/orgs/2i2c-org/teams/)
- [ ] Remove them from [Slack groups](https://2i2c.slack.com/admin/user_groups)
  - Note that as 2i2c slack is open check to see if they are going to continue to be part of broader 2i2c community and their slack email address is changed
- [ ] Remove from the proper [FreshDesk group](https://2i2c.freshdesk.com/a/admin/groups)
- [ ] Remove from [PagerDuty Users group](https://2i2c-org.pagerduty.com/users-new)
- [ ] Remove from our [bitwarden organization](https://vault.bitwarden.com/#/organizations/11313781-4b83-41a3-9d35-afe200c8e9f1/vault) and remove from "Default collection"
- [ ] Remove a team member from the Support Steward Team Role, calendar and rota [Role Offboarding Ticket](https://github.com/2i2c-org/team-compass/issues)


**Documentation**

- [ ] Revoke appropriate permissions on [ReadTheDocs projects](https://readthedocs.org/)
  - [ ] https://readthedocs.org/dashboard/2i2c-pilot-hubs/users/
  - [ ] https://readthedocs.org/dashboard/2i2c-team-compass/users/
  - [ ] https://readthedocs.org/dashboard/2i2c-pilot-documentation/users/

**Cloud engineering permissions**

_This is only relevant for others that are leaving our Engineering team._

- [ ] Remove from 2i2c hubs as an admin
- [ ] Remove from appropriate GCP organizations and projects
  - [ ] Organization `2i2c.org`'s [admin group](https://console.cloud.google.com/iam-admin/groups/03znysh73qbio4n?organizationId=184174754493)
  - [ ] Organization `2i2c.org`s [engineering group](https://console.cloud.google.com/iam-admin/groups/01opuj5n2qnifml?organizationId=184174754493)
  - [ ] Outside-organization project for [`cloudbank`](https://console.cloud.google.com/iam-admin/iam?project=cb-1003-1696)
  - [ ] Outside-organization project for [`meom-ige`](https://console.cloud.google.com/iam-admin/iam?project=meom-ige-cnrs)
  - [ ] Outside-organization project for [`callysto`](https://console.cloud.google.com/iam-admin/iam?project=callysto-202316)
  - [ ] (optional) Outside-organization project for [`pangeo-hubs`](https://console.cloud.google.com/iam-admin/iam?project=columbia)

- [ ] Remove from appropriate AWS projects
  - [ ] Management account [`2i2c-sandbox`](https://2i2c.awsapps.com/start/#/) (Grants SSO access at https://2i2c.awsapps.com/start#/)
  - [ ] Outside-SSO account [`carbonplan`](https://631969445205.signin.aws.amazon.com/console)
  - [ ] Outside-SSO account [`openscapes`](https://783616723547.signin.aws.amazon.com/console)
  - [ ] Outside-SSO account [`nasa-veda`](https://smce-veda.signin.aws.amazon.com/console)
    - An agreement has to be signed first, see https://github.com/2i2c-org/leads/issues/104
- [ ] Remove from appropriate Azure projects
  - [ ] Outside-organization `utoronto` contact them for removal 
- [ ] Remove from [quay.io 2i2c team](https://quay.io/organization/2i2c/teams/owners)
- [ ] Remove NameCheap administration privileges to `2i2c.org` and `2i2c.cloud`

**External**

- [ ] Remove from [2i2c website](https://2i2c.org/organization/)

