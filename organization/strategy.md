# Goals and strategy

The 1-2 year challenge we must overcome as an organization, and the major policies and actions we must take to solve it[^gsbs].

[^gsbs]: This is inspired by the [Good Strategy, Bad Strategy framework](https://www.amazon.com/Good-Strategy-Bad-Difference-Matters/dp/0307886239).

## Our big challenge

- Integrate two business lines that are in fundamental tension: project-based work (that tends to provide bespoke solutions) with SRE operations (that provides a standardized and scalable platform).
- ...for communities that must retain their unique identities and needs.
- ...using open technology we do not solely control.

## Our guiding policy

> Build efficient, reliable infrastructure as a baseline. Use freed capacity to identify shared needs and develop technology that advances the entire network.

By combining a **shared platform** with a **service team deeply embedded in the ecosystem**, we bring communities into close technical and social proximity. This proximity enables a virtuous cycle where shared platforms create leverage, service facilitates connection, connection enables collaboration, and collaboration fuels the ecosystem.

## Operating principles

To execute our guiding policy of standardizing infrastructure, reinvesting through member co-funding, and orchestrating ecosystem advancements, we follow these principles:

1. **Infrastructure reliability provides a foundation for innovation**. Communities will not use infrastructure that is fundamentally unreliable. Unreliable infrastructure takes time and energy to maintain. Our site reliability must be reliable and stable to provide us a foundation that frees up time for community engagement and development.

2. **We control our roadmap.** We must be in charge of our roadmap to avoid the bespoke consultancy trap. 2i2c does not have the flexibility to build reactively in response to each customer's requests and must instead proactively define what we think should be built and sell that.


3. **We prioritize network-wide benefits.** We only develop infrastructure that serves the network of communities for whom we manage infrastructure. This ensures we develop broadly useful and flexible technology that is designed for an ecosystem rather than a single client. We must identify problems shared by many communities and build solutions that bring value to many of our customers and many others through our platform services operation.

4. **We scope our service to community archetypes**. To share a single network-wide roadmap, we must ensure all members have heavily overlapping needs and use cases. We must be precise in the communities we'll support to ensure they are a good fit for co-development and operations with our standard platform.

5. **We invite structured participation.** To build trust and buy-in from member communities, we must define structured ways to get their feedback and guide our priorities.

6. **We turn participation into fundraising.** We must nurture member communities into coalitions of buyers for new development. Driven by our shared roadmap, this will reduce the cost of new development to any one member community.

7. **We say NO to distractions.** We must say NO to requests to build the wrong solutions. Solutions are wrong for 2i2c when they do not advance *our* roadmap and when they go beyond our delivery capacity.

## Target end-state

We aim to create a self-sustaining service model in which each line of business is net-sustainable (membership, consultative work, and basic access for non-members). This will allow us to scale our base support for open source communities and infrastructure (via membership), to use this base to make strategic development investments in the ecosystem (via co-funding), and to make open infrastructure massively accessible (via basic access service). We want to be seen as a key strategic leader in the open source communities in which we participate that represents the needs of the research and education communities, with a participatory model that ensures their interests are represented, and a sustainable model that provides reliability.


(service-model)=
## Our service model

We operate between bespoke consultancy (doesn't scale) and commodified SRE (crushed by big vendors). Our challenge is to blend these two business types through a tiered membership model that integrates operational services with strategic development.

### Membership tiers

Our target business model includes three membership tiers:

**General Membership**
- **For**: Discrete communities with a homogeneous user base (e.g., a single research group or collaboration).
- **Offers**: Site Reliability Engineering for managed infrastructure. Basic guidance in usage. Participation in roadmapping exercises and co-funding opportunities.
- **Impact**: The core loop that sustains 2i2c and covers the cost of making open infrastructure accessible and supported with foundational contributions.

**Premier Membership**
- **For**: Strategic partners that want deeper engagement or investment in open source development. Usually serve more than one community that fits our membership profile.
- **Offers**: Strategic-level engagement from 2i2c and direction over our roadmap. Coordination and guidance in planning and delivering technical improvements. Tighter feedback loop between development and operations.
- **Impact**: Drives deeper engagement and investment in open source, as well as larger-scale deployments.

**Essential Membership** (not yet developed)
- **For**: Communities that need standardized, commodity infrastructure with minimal customization.
- **Offers**: Commodified SRE evolving with open source. Automated operations with community-driven support.
- **Impact**: Makes open infrastructure largely accessible, even to communities that cannot cover the costs of foundational contributions and development.

### Integrating consulting with membership

Frame "membership" as participating in a shared dev-ops service, where member funds cover the operational costs of infrastructure, and project-based funds give members a voice in where we improve the commodity infrastructure that the network uses.

This integration model allows us to:
- **Control our roadmap** by proactively defining development directions rather than building reactively for individual customers
- **Leverage our network** by nurturing member communities into coalitions of buyers for new development, reducing costs for any single member
- **Fund ecosystem improvements** by aggregating demand for new capabilities across our membership base

(strategic-priorities)=
## Our strategic priorities

To carry this out we must make strategic progress in a few key functional areas, defined below.

### Platform and infrastructure

> Automate the commodity infrastructure to focus on network-wide enhancements.

- Automate our commodity infrastructure baseline: Minimize the manual effort required to operate our network of hubs. Automate repetitive tasks. De-prioritize enhancements that do not benefit most of our member network. Develop tools that allow communities to self-serve their own customization.
- Focus our freed-up engineering capacity to solve problems that benefit everyone. This means improving the shared platform's capabilities and contributing features directly to upstream projects. We measure success by how much we grow the ceiling for all of our community members.

**We will know this is working when** our platform team spends 80% of its time engaging with our communities and developing new enhancements for our infrastructure, rather than toil and reacting to problems.

### Services and community relationships

> Minimize reactive support to focus on proactively connecting with our community network.

- Reduce the volume of basic technical support (e.g., login issues, basic usage, etc). Prioritize documentation, self-service tools, and community peer-support channels to handle routine inquiries.
- Focus our freed-up time on actively connecting our members to identify shared needs. Help researchers navigate open source dynamics, translate their needs into technical roadmaps, and facilitate cross-community learning. Focus on interactions that help communities leverage the platform and one another's learning to achieve their mission.

**We will know this is working when** we spend our time _orchestrating_ and _facilitating_ learning from our communities, rather than reacting to their requests.

### Business Development:

> Standardize recurring revenue with a model that naturally leads to high-impact contracts.

- Memberships cover our core services: Price memberships to be fully self-sustaining. This revenue must cover our critical infrastructure, our open source support, and our core investment in community relationships. This is our core cost of doing business, ensuring that the basic existence of our network funds the mission of the organization.
- Make ecosystem improvements with co-funding: Because we have an engaged membership base with similar needs, we can aggregate demand for new capabilities, allowing multiple members to split the cost of strategic enhancements. Use this leverage to fund targeted improvements that advance our platform or services in new ways.

**We will know this is working when** the majority of our revenue comes from contracts, and the majority of our contract revenue is recurring.

## Appendix: Things that are not our unique value

**We are not solely a commodity-level infrastructure provider**. Reliably running a hub service is a commodity. By treating it as a commodity layer you can take for granted, we minimize the "drag" on research and education and allow them to focus on their work. While it must provide a high degree of reliability and trust, the true value of this technical infrastructure is not in its existence alone.

**We are not a bespoke consultancy**. While we do consultative work, we do so in a way that benefits our entire member network rather than an individual client. This ensures consultative work feeds into our membership benefits, and ensures that we develop technology that is broadly useful.
