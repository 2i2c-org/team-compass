(sales-operations:index)=

# Sales Operations Overview (2025)

## Purpose & Philosophy

2i2c's sales operations convert prospects into General Members through a **learning-driven sales system**. Unlike traditional sales processes that execute a fixed playbook, our approach treats each deal as an opportunity to validate and refine our understanding of the market.

**Key principles:**
- **Iterative ICP development**: We systematically test hypotheses about which institutions make ideal members and why
- **Metrics as experiments**: Conversion rates, pipeline velocity, and activity metrics guide strategic pivots
- **Structured flexibility**: Deal stages provide scaffolding for consistent execution while allowing experimentation within each stage

Our members are typically universities, research institutions, and educational organizations (the *buyers*), while the communities they serve are the researchers, students, and practitioners who use our interactive computing infrastructure (the *community of users*).

## Current Strategic Focus (2025)

**General Membership sales**: We are focused on validating a scalable sales motion for General Membership, which provides up to 3 community hubs with standardized configurations and support.

**Premier tier deferred**: Prospects interested in Premier Membership (10+ hubs, custom configurations, dedicated consulting) are kept warm for follow-up in 2026Q3. This allows us to focus learning efforts on one offering at a time.

## Sales Pipeline Stages

Our Customer Relationship Manager (CRM) pipeline (managed in HubSpot) consists of the following stages:

### **1. Enrichment**
- **Purpose**: Research and qualify prospects before outreach
- **Activities**: Validate Ideal Customer Persona (ICP) fit, assess budget signals, map decision-makers
- **Exit criteria**: Sales-qualified (need + budget + ICP fit) → moves to Outreach, OR disqualified → moves to Closed Lost, OR Premier interest → parked for 2026Q3
- **Learning focus**: Which prospect signals predict successful conversion?

### **2. Outreach**
- **Purpose**: Initiate contact with sales-qualified prospects
- **Activities**: Execute outreach strategy (email, warm intro, conference follow-up), track response patterns
- **Exit criteria**: Prospect engages → moves to Discovery, OR unresponsive after follow-up sequence → moves to Closed Lost
- **Learning focus**: Which messaging, channels, and value propositions drive engagement?

### **3. Discovery**
- **Purpose**: Understand prospect needs and validate General Membership fit
- **Activities**: Discovery calls document jobs-to-be-done, assess technical requirements
- **Exit criteria**: Prospect requests pricing → moves to Proposal, OR deal stalls/no fit → moves to Closed Lost
- **Learning focus**: Do prospect needs align with our offering assumptions? Should we adjust ICP?

### **4. Renewals**
- **Purpose**: Re-engage existing members for contract renewal or expansion
- **Activities**: Customer health check, explore expansion opportunities, validate renewal intent
- **Exit criteria**: Renewal confirmed → moves to Proposal, OR not renewing → moves to Closed Lost with learnings
- **Learning focus**: What do renewing members value most about 2i2c? Will renewing members make referrals to new prospective members?

### **5. Proposal**
- **Purpose**: Present pricing and negotiate terms
- **Activities**: Draft General Membership proposal, present to prospect, address objections, finalize service agreement
- **Exit criteria**: Contract signed → moves to Closed Won, OR negotiation fails → moves to Closed Lost
- **Learning focus**: What objections arise? How do we overcome them?

### **6. Closed Won**
- **Purpose**: Hand off to delivery and begin onboarding
- **Activities**: Update HubSpot deal data (contract dates, MRR), initiate Ordering process, handoff to Delivery Manager
- **Exit criteria**: Engagement operational, customer actively using hubs
- **Learning capture**: What ICP signals and sales approaches led to this win?

### **7. Closed Lost**
- **Purpose**: Analyze failure and evolve ICP/process
- **Activities**: Document specific loss reason (price, timing, competitor, feature gap, wrong ICP), assess re-engagement potential
- **Exit criteria**: Learnings documented, Sales Playbook updated if needed
- **Learning focus**: Was ICP definition wrong, or was execution poor?

## Key Metrics (Tracked Weekly)

Our learning-driven approach requires visibility into pipeline health and conversion effectiveness.

Deals in HubSpot are labeled with `Deal Type` ("existing business", "new business"). Renewals are "existing business". Net new business opportunities are "new business". The `Deal Type` is used to filter deals to enable tracking of new business and renewal business opportunities in our pipeline. 

New business is tracked with these metrics (**implemented**, _planned_):

- **Sales Qualified Deals (SQD)**: Count of deals in Outreach + Discovery + Renewals + Proposal stages
- **SQD Net New**: Deals that entered SQD stages in the last 7 days (leading indicator of pipeline growth)
- **Meetings Per Week (MPW)**: Discovery, renewal, and proposal meetings held (activity indicator)
- _Outreach Email Open Rates_: Do the emails we send get opened? Which emails get opened and which don't?
- _Outreach → Discovery conversion rate_: Validates outreach quality and ICP targeting
- _Discovery → Proposal conversion rate_: Validates qualification effectiveness
- _Days in Pipeline_: Average time from Enrichment to Closed Won (velocity indicator)
- _Days in Discovery_: Average time in Discovery stage (identifies stalled deals)

Existing business flowing into the Renewals stage are tracked with these metrics (**implemented, _planned_):

- **Existing Business Active**: Count of current active deals (Closed Won, and Now is after contract start and before contract end).
- **Overdue Renewal**: Count of deals with ongoing service with Now after contract end.
- **[0,30] Renewal**: Count of deals with Now before but within 30 days of contract end.
- **[31,90] Renewal**: Count of deals with Now before but within 31 to 90 days of contract end.
- **[91,180] Renewal**: Count of deals with Now before but within 91 to 180 days of contract end.

These metrics guide weekly sales reviews where we identify experiments to run, diagnose bottlenecks, and decide when to pivot strategy.

## Team Roles (Current Bootstrap Phase)

2i2c's sales operation is currently carried out by:

- **James Colliander (Business Development Lead / Account Manager)**: Leads sales strategy, conducts discovery calls, owns ICP evolution
- **Harold Campbell (Chief of Staff / Account Manager)**: Supports deal execution in burst capacity, contributes to qualification and proposal development
- **April Johnson (Delivery Manager)**: Manages post-sale onboarding and ongoing service delivery, provides critical insights on member health that inform renewals and ICP refinement

As the sales system matures, these activities will likely evolve into distinct roles:
- **Business Development Lead**: Strategy, partnerships, ICP development
- **Account Manager - New Sales** ("Hunter"): Outreach through proposal for net-new members
- **Account Manager - Renewals** ("Farmer"): Customer success and renewal/expansion sales

## Tools & Systems

- **HubSpot**: CRM for pipeline tracking, deal stages, metrics dashboards, order creation
- **Asana**: Deal strategy iteration, sales playbook development, experiment tracking
- **Google Drive**: Proposal drafting, service agreement templates, shared documentation
- **Dropbox Sign** (formerly HelloSign): Contract execution
- **Hub Configurator**: Web-based tool for specifying hub configurations (up to 3 hubs for General Members)

## Key Artifacts

Throughout the sales process, we generate:

- **ICP hypothesis documents**: Evolving definition of ideal member characteristics in Asana
- **Outreach experiments log**: Testing messaging, channels, and value propositions in Google Drive
- **Discovery notes**: Jobs-to-be-done, technical requirements, decision-maker mapping in Asana
- **Service agreements**: Template-based contracts customized for member needs (managed via Code for Science & Society, 2i2c's fiscal sponsor) in Google Drive (drafts), SAGE and HubSpot (executed)
- **HubSpot Orders**: Generated post-Closed Won using Hub Configurator URL, triggers delivery process
- **Win/loss analysis**: Captured learnings from every closed deal in Asana and Google Drive

## Integration with Delivery

When a deal reaches **Closed Won**, the handoff to delivery follows this sequence:

1. **Account Manager updates HubSpot**: Ensures contract dates, MRR, and member details are accurate
2. **Ordering process initiated**: Account Manager guides member through [Hub Configurator](https://2i2c.org/hub-configurator) to specify hub requirements (authentication, computing environment, storage, etc.)
3. **Order created in HubSpot**: Uses Hub Configurator URL as initial specification
4. **Automation triggers**: HubSpot → GitHub issues created automatically for P&S (Product & Services) team
5. **Delivery Manager takes ownership**: April Johnson coordinates provisioning, ongoing services, and member success
6. **Feedback loop established**: Delivery insights on member health, usage patterns, and satisfaction inform ICP refinement and renewal strategies

## Learning & Iteration Rhythm

**Weekly Sales Review** (30 minutes):
- Review SQD metrics and pipeline health
- Discuss stalled deals and determine action
- Share closed deal learnings (wins and losses)
- Select 1-2 experiments to run next week

**Monthly Template Evolution**:
- Review 10-20 closed deals for patterns
- Propose ICP refinements based on conversion data
- Update Asana deal template and Sales Playbook based on validated learnings
- Version template (v1 → v2 → v3) with changelog

**Pivot Decision Points**:
We've defined "red line" metrics that trigger fundamental strategy reassessment:
- Outreach → Discovery conversion <15% after 20+ attempts → ICP or messaging broken
- Discovery → Proposal conversion <25% after 10+ calls → Offering/market fit issue
- Zero wins after 10 proposals → Pricing, positioning, or product-market fit problem

## Service Agreements & Legal Structure

2i2c operates under the fiscal sponsorship of **Code for Science & Society (CS&S)**, a 501(c)(3) nonprofit organization. CS&S is the legal entity that enters into service agreements with our members.

Service agreements are based on the [Outbound Services Agreement template](https://docs.google.com/document/d/1kPgSddJ_Sob0XcTbkDy5UShIAVKPmm04P9ZLsYiOV20/edit?usp=sharing) developed collaboratively with CS&S. Agreements include:
- Scope of services (hub specifications, support levels, consulting hours if applicable)
- Pricing structure (annual membership fee + monthly usage fees)
- Contract term and renewal provisions
- Service level commitments

Agreements are finalized through Dropbox Sign and trigger the delivery handoff process.

## What Makes This System Different

**Traditional sales process**: Execute a playbook → measure adherence → optimize for efficiency

**2i2c's learning-driven system**: Test hypotheses → measure outcomes → evolve strategy based on evidence

Every deal contributes to our understanding of:
- Who makes an ideal 2i2c member (ICP evolution)
- What messaging resonates with prospects (outreach experiments)
- Which needs General Membership solves well vs. poorly (product-market fit)
- How to predict which prospects will convert (qualification refinement)

This approach allows us to build a scalable, repeatable sales motion while operating in an evolving market with a maturing product offering.

---

## Questions or Want to Contribute?

Sales operations are documented in our Sales Playbook (Asana). If you're working on deals, have insights from member interactions, or want to propose experiments, reach out to James Colliander (Business Development Lead) or use the Lead - Opportunity - Capture workflow in the business-development channel in Slack. 
