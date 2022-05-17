# Roles for the service

There are a few major roles that we define for the Managed JupyterHub Service.
Unless specified otherwise, they may not require a dedicated person to fill each role.

(roles:community-representative)=
## Community Representative

The job of a Community Representative is to ensure that the interests of the {term}`Hub Community` are represented in the infrastructure, and that the hub serves their needs.
There must be **one or two community representatives for a given community**.
This role is usually filled by someone that is a member of the hub's community of practice.

### Responsibilities

- The main point of contact between the hub engineer and the {term}`Hub Community`.
- Collect feedback and questions from users on a hub.
- Surface questions and requests to Hub Engineers via support tickets.
- Oversee the [Hub Administrators](roles:hub-administrator)

(roles:hub-administrator)=
## Hub Administrator

Community members that support users and perform common administrative operations on a hub that do not require intervention from a [Hub Engineer](roles:hub-engineer).
[Community Representatives](roles:community-representative) are the first Hub Administrators, and they may add new Hub Administrators via the JupyterHub interface.
They are able to add users, start/stop servers, and generally have more control over operations on the hub.

:::{seealso}
See the [Community Hub Administrator documentation](https://docs.2i2c.org) for helpful information for Hub Administrators.
:::

:::{warning}
While there may be any number of Hub Administrators on a hub (any administrator can add other administrators), make sure to give this role to people you trust, as they can perform disruptive actions for other users.
:::

### Responsibilities

- Provide support to users of a hub for common problems that don't require a Hub Engineer to resolve.
- Add new users to a hub, including administrative users.
- Surface major issues or requests to the Community Representative(s).

(roles:hub-engineer)=
## Hub Engineer

The job of a Hub Engineer is to develop and operate deployment infrastructure for a hub, and to perform major upgrades or improvements to resolve issues that cannot be solved by a [Hub Administrator](roles:hub-administrator).
Hub engineers regularly work on the JupyterHub infrastructure and provide open source development for the technology that powers each hub.
People in these roles are generally affiliated with 2i2c.

### Responsibilities

- Respond to support requests from the Community Representative(s)
- Perform major upgrades on hub infrastructure
- Debug and resolve major issues with a hub that require intervention from a Hub Engineer
- Perform open source development on technologies that are in use by the hubs

(roles:support-steward)=
## Support Stewards

The primary external point of contact for all support-related issues.
See [](support:process) for more information.

(roles:incident-commander)=
## Incident commander

The Source of Truth for status and action plan around any {term}`Incident`s.
See [](support:process) for more information.

(roles:project-manager)=
## Project Manager

We are piloting the use of a dedicated Project Manager to help our team plan and coordinate with one another.
See [this GitHub issue](https://github.com/2i2c-org/team-compass/issues/398) for our plans and experience with this pilot thus far.

## Diagram of roles

Below is a diagram that summarizes the major roles described here, and their relationship to one another.

<iframe
  src="https://docs.google.com/presentation/d/e/2PACX-1vQ9P_0W-2IVqvPGM9nlgWZcJAdk7DNn_lK78R3eolr6JXYMaUTsMAlwAWcKZtNxqj8kNNDN7fiz3jVI/embed?start=false&loop=false&delayms=99999999"
  frameborder="0"
  width="960"
  height="569"
</iframe>
