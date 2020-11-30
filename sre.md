# Site Reliability best practices

The following are some best-practices that 2i2c has learned while running hub infrastructure for research and education.

## Roles needed to run a 2i2c hub

2i2c Hubs require a variety of expertise to design, deploy, and maintain.
This roughly breaks down along the following roles. They roughly follow a continuum of "user-focused" to "infrastructure-focused":

**Community Champions**
: The main connections to the community of users that a hub serves. They work with the hub architect and operator to ensure the hub meets the needs of each community. Their job is to translate the needs and perspectives of the users into design and development decisions for a hub. They are also often the first point-of-contact when users have issues, and elevate problems to the Hub Engineer if needed. They often have elevated abilities on the hub such as administrative and customization permissions.

**Hub Engineer**
: Keep a hub running from day to day and supports hub users with technical problems. The hub engineer is the first wave of defense when community champions have determined that something is technically wrong on the hub infrastructure. The engineer's job is to identify what is causing a disruption, and attempt to resolve the disruption through a combination of cluster maintenance as well as development on the hub infrastructure to resolve the issue now (and ideally in the future). Hub engineers should constantly try to solve problems (especially common ones) through developing programmatic solutions, rather than putting out the same fires many times. They also selectively escalate technical issues to Hub Architects if need be.

**Hub Architect**:
: Design the infrastructure underlying one or more hubs. They also often manage initial deployments and customizations for a particular community. They create the backbone of 2i2c Hub infrastructure and work with Hub Engineers and Community Champions to ensure that it meets the needs of the community. Hub architects have a deep knowledge of kubernetes, JupyterHub, and integrations with tools that are common for research and engineering. They spend the large majority of their time doing design and development, and only address major technical issues that require their attention (usually as determined by a hub engineer).

**Resource Provider**
: Provides the cloud resources to run the hub infrastructure. Sometimes this is a cloud provider providing credits, sometimes a community brings cloud resources it has purchased or been given, and other times it is 2i2c that handles purchasing for the community.
