---
name: "🙌 Onboard a team member"
about: Steps to follow to bring on a new team member
labels: "type: onboard"
title: "Onboarding <name>"
---

- Onboarding champion: `@INSERT_HANDLE`
- New person's name: `INSERT NAME`
- New person's GitHub handle: `@INSERT_HANDLE`

### Onboarding checklist

The **Onboarding champion** should follow the checklist below to onboard a new team member. Don't hesitate to delegate some actions to others (e.g. if another person needs to give access to an account because you aren't able to).

**First steps**

- [ ] Send them a welcome e-mail to introduce yourself and mention that you'll be onboarding them.
- [ ] Point them to [our onboarding documentation](https://compass.2i2c.org/en/latest/operations/onboarding.html)

**Accounts**

- [ ] Get member's GitHub.com account
- [ ] Get member's ReadTheDocs.org account
- [ ] Get member's Quay.io account
- [ ] Get member's NameCheap.com account
- [ ] Get member's PagerDuty account

- [ ] Create a @2i2c.org Google account for them
	- Note that this requires [access to the Admin Panel](https://compass.2i2c.org/en/latest/administration/google-workspace.html?highlight=workspaces#access-and-permissions), a permission held by any 2i2c team lead
- [ ] Add them to the proper Google group in our Google Admin space.
- [ ] Add to the proper [2i2c GitHub teams](https://github.com/orgs/2i2c-org/teams/)
- [ ] Add to the proper [Slack groups](https://2i2c.slack.com/admin/user_groups)
- [ ] Add to the proper [FreshDesk group](https://2i2c.freshdesk.com/a/admin/groups)
- [ ] Add to propoer [PagerDuty Users group](https://2i2c-org.pagerduty.com/users-new)

**Communication**

- [ ] Send them a link to the [2i2c Team Compass](https://team-compass.2i2c.org/en/latest/) and its [Team Operations section](https://team-compass.2i2c.org/en/latest/operations/index.html)
- [ ] Send them a link to the [2i2c calendars and meetings](https://team-compass.2i2c.org/en/latest/reference/calendar.html)
- [ ] Send them a link to the [2i2c Team Google Drive](https://drive.google.com/drive/u/1/folders/0AJcabtB-T0LnUk9PVA)
- [ ] Schedule an onboarding meeting for after they've read through the docs

**Documentation**

- [ ] Grant appropriate permissions on [ReadTheDocs projects](https://readthedocs.org/)
  - [ ] https://readthedocs.org/dashboard/2i2c-pilot-hubs/users/
  - [ ] https://readthedocs.org/dashboard/2i2c-team-compass/users/
  - [ ] https://readthedocs.org/dashboard/2i2c-pilot-documentation/users/

**Cloud engineering permissions**

_This is only relevant for others that are joining our Engineering team._

- [ ] Add to 2i2c hubs as an admin
- [ ] Add to appropriate GCP organizations and projects
  - [ ] Organization `2i2c.org`'s [admin group](https://console.cloud.google.com/iam-admin/groups/03znysh73qbio4n?organizationId=184174754493)
  - [ ] Organization `2i2c.org`s [engineering group](https://console.cloud.google.com/iam-admin/groups/01opuj5n2qnifml?organizationId=184174754493)
  - [ ] Outside-organization project for [`cloudbank`](https://console.cloud.google.com/iam-admin/iam?project=cb-1003-1696)
  - [ ] Outside-organization project for [`meom-ige`](https://console.cloud.google.com/iam-admin/iam?project=meom-ige-cnrs)
  - [ ] Outside-organization project for [`callysto`](https://console.cloud.google.com/iam-admin/iam?project=callysto-202316)
  - [ ] (optional) Outside-organization project for [`pange-hubs`](https://console.cloud.google.com/iam-admin/iam?project=columbia)
    - An agreement has to be signed first, and they require a copy of our passports, see (TODO: clarify this)

- [ ] Add to appropriate AWS projects
  - [ ] Management account [`2i2c-sandbox`](https://2i2c.awsapps.com/start/#/) (Grants SSO access at https://2i2c.awsapps.com/start#/)
  - [ ] Outside-SSO account [`carbonplan`](https://631969445205.signin.aws.amazon.com/console)
  - [ ] Outside-SSO account [`openscapes`](https://783616723547.signin.aws.amazon.com/console)
  - [ ] Outside-SSO account [`nasa-veda`](https://smce-veda.signin.aws.amazon.com/console)
    - An agreement has to be signed first, see https://github.com/2i2c-org/leads/issues/104
- [ ] Add to appropriate Azure projects
  - [ ] Outside-organization subscription for `utoronto` (TODO: figure out details here)
- [ ] Add to the [auth0 2i2c tenant](https://manage.auth0.com/dashboard/us/2i2c/tenant/admins)
- [ ] Add to [quay.io 2i2c team](https://quay.io/organization/2i2c/teams/owners)
- [ ] NameCheap administration privileges to `2i2c.org` and `2i2c.cloud`

**Roles**

- [ ] Onboard into the [Support Steward Role](https://github.com/2i2c-org/team-compass/issues/new?assignees=&labels=type%3A+onboard&template=new-team-member.md&title=Onboarding+%3Cname%3E)

**External**

- [ ] Add to [2i2c website](https://2i2c.org/organization/)
- [ ] Celebrate their arrival on social media! (Twitter, Mastodon, LinkedIn)

**Wrap up**

- [ ] Have a one-on-one with the new team member to answer any questions they may have
- [ ] Announce in the `#general` Slack channel about our new team member
- [ ] Celebrate, they are now onboarded! 🎉
