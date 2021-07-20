# Roles for the Managed JupyterHub Service

There are a few major roles that we define for the Managed JupyterHub Service.
These are outlined below.

:::{seealso}
They are also described in [the Hub Services diagrams slideshow](https://docs.google.com/presentation/d/1kqrviwVOoZfey_rujhIasdkKZmlYgxV-1J2AG-nr3VY/edit#slide=id.ge3f2127292_0_573) as well as in the [Managed Service Plan](https://docs.google.com/document/d/1Ka7tgJe7HR8EmS_MMakrYztgfkJT_iFksPsWHdQBqhM/edit?usp=sharing).
:::

Hub Community
: The community of practice that a Managed JupyterHub serves.
  This includes leadership of the community as well as users of the hub.
Community Representative
: The Community Representative is the main point of contact between the hub engineer and the users on a hub.
  They are the primary escalation pathway when issues arise that can not be debugged on their own, or for customization requests that require an engineer.
  This person is usually part of the community that uses the hub.
Hub Administrators
: Hub Administrators have special status and permissions on a hub.
  They are able to add users, start/stop servers, and generally have more control over operations on the hub.
  When a new hub is deployed, the Community Representative is added as a Hub Administrator, along with 2i2c Engineers.
  The Community Representative may then add other users as administrators if they wish.
Hub Engineer
: Keeps a hub running from day to day.
  The hub engineer is the first wave of defense when a Community Representative has determined that something is technically wrong on the hub infrastructure.
  They also perform development and upgrades on hub infrastructure.
  This person is generally employed by 2i2c.
