# Goals and strategy

This is the 2-3 year challenge we must overcome as an organization, and the major policies and actions we must take to solve it[^gsbs].

Our [theory of impact](./theory-of-impact.md) describes a flywheel in which we **develop** open technology with open source communities, and **operate** standardized community infrastructure that uses this technology.

This means running **two lines of business**:

1. **A managed infrastructure service** that is rooted in reliability, stability, flexibility, and access.
2. **A development service** that is rooted in innovation, new development, and iteration.

These two services are in tension:

- Operations focuses on standardization, stability, and scale. It draws from practices like "Site Reliability Engineering". It requires upstream communities to fix bugs quickly, to be stable, and to be responsive.
- Development work focuses on short-term improvements that tend towards bespoke solutions. It is more uncertain because you're building new things. It requires upstream communities to efficiently design, prioritize, and iterate.

[^gsbs]: This is inspired by the [Good Strategy, Bad Strategy framework](https://www.amazon.com/Good-Strategy-Bad-Difference-Matters/dp/0307886239).

## Our big challenge

We must ensure these two services are strongly aligned with one another, instead of being independent lines of business that compete for the same organizational resources, while maintaining a healthy upstream relationship for each. 

## Our guiding policy

Our service offers a centralized technical system that serves a network of independent communities. Our unique value is the way in which we improve that system by engaging member communities to learn, identify problems, and develop solutions together with the open source community.

- Managed infrastructure
  - Provides a stable base that our member communities can rely on
  - Provides upstream support to provide a similar level of stability
  - Rapidly benefits from development work
- Development work
  - Provides a steady stream of _improvements_ to open technology
  - Provides upstream support that drives innovation
  - Always benefits our managed infrastructure

## Operating principles

Here are several principles that follow this policy:

1. **Scalable agency and collaboration is the unique value of Membership**. The unique value of our membership is in the ability to interact with our team, other member communities, and open source communities. This should be where we spend most of our time. We must make it clear how membership is a way to direct support to open source tools, influence our roadmap, and make their own contributions.

2. **Efficiently operate infrastructure to have more cycles for development**. Communities will not use infrastructure that is fundamentally unreliable, though it it is not our core value. Our site reliability team must be efficient to ensure our infrastructure is reliable, while recognizing that most of our time should go towards collaboration and new development.


3. **ONLY develop improvements that benefit MANY member communities.** This ensures we develop broadly useful and flexible technology that is designed for an ecosystem rather than a single client. We must identify problems shared by many communities and build solutions that bring value to many of our customers and many others through our platform services operation.

4. **Be selective about our member communities to ensure they are aligned**. To share a single network-wide roadmap, we must ensure all members have heavily overlapping needs and use cases. We must be precise in the communities we'll support to ensure they are a good fit for co-development and operations with our standard platform.

5. **Actively engage members on our own terms to be scalable.** To make community engagement scalable, we must do so on our own terms. We must design systems that ensure commmunities have visibility and agency in our work, so that we don't default to bespoke consulting. We must actively define a narrative for the work we do, share credit with the members that made it happen, and share it with others in a discoverable and digestible form.

## Target end-state

These are the targets we're currently aiming for:

- Each service (membership and development) sustains a dedicated staff.
- Each service generates margin we re-invest in open source communities.
- We're seen as a healthy leader and contributor in each open source community we work with.

If we achieve these goals, here are a few targets we're interested in achieving:

- There is an accessible infrastructure option for communities that cannot pay. (subsidized by the two lines of business above)
- We have multiple operations and development teams co-located geographically or by domain.

(service-model)=
## Our service model

Our primary engagement model is **membership**.
This centers our mission-driven nature, and builds a feeling of mutual support and status between our member organizations.

All members have the option to participate in **co-funded project work**, which is a way for them to pool their resources to support open source development.

### Membership tiers

Membership should:

- **Framing**: Membership is a way to pool resources on a shared service team (operations, development, and community engagement).
- **Cost recovery**: Membership covers core costs in operations, engagement, and upstream support.
- **Benefit**:
  - Comes with managed infrastructure. This ensures we have a cycle between operations and development work.
  - Access to spaces and conversations communities otherwise would not have.
  - A way for communities to pool resources to contribute upstream.

Our target business model includes three membership tiers:

**General Membership**
- **For**: Discrete communities with a homogeneous user base (e.g., a single research group or collaboration).
- **Impact**: The core loop that sustains 2i2c and covers the cost of making open infrastructure accessible and supported with foundational contributions.
- **Offers**:
  - Site Reliability Engineering for managed infrastructure.
  - Basic guidance in usage.
  - Participation in roadmapping exercises and co-funding opportunities.

**Premier Membership**
- **For**: Strategic partners that want deeper engagement or investment in open source development. Usually serve more than one community that fits our membership profile.
- **Impact**: Drives deeper engagement and investment in open source, strategic guidance for 2i2c, and larger-scale growth within a community.
- **Offers**:
  - Strategic-level engagement from 2i2c, with more direction over our roadmap.
  - Coordination and guidance in planning and delivering technical improvements.
  - Tighter feedback loops and reporting between development and operations.

**Essential Membership** (TDB, not currently prioritized)
- **For**: Communities that need standardized, commodity infrastructure with minimal customization.
- **Offers**: Commodified SRE evolving with open source. Automated operations with community-driven support.
- **Impact**: Makes open infrastructure largely accessible, even to communities that cannot cover the costs of foundational contributions and development.

### Co-funded projects with members

Project-based work gives members a way to influence our new development, and make it possible with funding. It is the engine that drives innovation and enhancement of our shared technical system.

- **For**: Any member organization that wants their infrastructure to be better (we do not distinguish between "premier" and "general" members for co-funding).
- **Cost recovery**: Covers all R&D-style costs for new development. 
- **Benefits**:
  - A mechanism to fund fractions of new development work to make it more likely to happen faster.
  - Engages communities to talk about shared problems, and to learn from one another.
  - A way to get credit for supporting open source infrastructure development.

### How membership and project work feed into one another

Each line of business benefits from network effects, and crucially depends on our development work and our operations work feeding into one another. As the number of member communities grows:

- They share more of the cost of operations, which decreases cost of service or increases support for open infrastructure.
- They increase the resources available for new development, which benefits the entire network.
- They have a larger group of communities to learn from, which increases learning and adoption of new workflows.

(strategic-priorities)=
## Our strategic priorities

To carry this out we must make strategic progress in a few key functional areas, defined below.

### Platform and infrastructure

- Automate our commodity infrastructure baseline: Minimize the manual effort required to operate our network of hubs.
- Use the extra capacity to engage communities in a scalable way, and to develop improvements for our network. 

**We will know this is working when** our platform team spends 80% of its time engaging with our communities and developing new enhancements for our infrastructure, rather than toil and reacting to problems.

### Services and community relationships

- Make our community engagement scalable. Create shared spaces that allow us to efficiently share information, invite feedback, and engage in collaboration. Minimize reactive and one-off work in favor of shared resources.
- Build an excellent feedback loop of design, development, and recognition that encourages communities to engage with us in improving our infrastructure.

**We will know this is working when** we spend our time _orchestrating_ and _facilitating_ learning from our communities, rather than reacting to their requests.

### Business Development

- Build a sales system that engages member communities to generate funded development.
- Grow a baseline of member organizations so that we can reliably generate enough co-funding opportunities to cover our costs.

**We will know this is working when** a combination of memberships and co-development work reliably covers our costs, and we bring on more member communities only if we want to scale.
