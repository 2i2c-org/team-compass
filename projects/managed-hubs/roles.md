# Roles for the service

There are a few major roles that we define for the Managed JupyterHub Service.
These are outlined below.

:::{seealso}
They are also described in [the Hub Services diagrams slideshow](https://docs.google.com/presentation/d/1kqrviwVOoZfey_rujhIasdkKZmlYgxV-1J2AG-nr3VY/edit#slide=id.ge3f2127292_0_573) as well as in the [Managed Service Plan](https://docs.google.com/document/d/1Ka7tgJe7HR8EmS_MMakrYztgfkJT_iFksPsWHdQBqhM/edit?usp=sharing).
:::

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

The job of hub administrators is to support users and to perform common administrative operations on a hub that do not require intervention from a [Hub Engineer](roles:hub-engineer).
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

## Support Steward

:::{warning}
This is an experimental role and the details may change!
:::

The Support Steward is tasked with keeping track of ongoing support requests to `support@2i2c.org`.
They do not necessarily complete the request themselves, and should work with other engineers to ensure they are resolved.

The Support Steward rotates throughout the engineering team each sprint, in order to ensure that all team members share the load of supporting our communities.

See [the Support Process proposal](https://docs.google.com/document/d/17Kj_FbtVMl32TEcfvCp18fF1SEiBjVOhCswdidUytgM/edit?usp=sharing) for the latest version of our support process.

### Responsibilities

- Check the communication channels for support that we are using
- Respond to new support requests
- Communicate with community representatives throughout the support process
- Coordinate with engineering team members to ensure support requests are completed
- Pay attention to ongoing support efforts to ensure they are resolved in a timely manner

## Diagram of roles

Below is a diagram that summarizes the major roles described here, and their relationship to one another.

<iframe
  src="https://docs.google.com/presentation/d/e/2PACX-1vQ9P_0W-2IVqvPGM9nlgWZcJAdk7DNn_lK78R3eolr6JXYMaUTsMAlwAWcKZtNxqj8kNNDN7fiz3jVI/embed?start=false&loop=false&delayms=99999999"
  frameborder="0"
  width="960"
  height="569"
</iframe>
