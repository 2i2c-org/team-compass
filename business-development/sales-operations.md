(sales-operations:index)=

# Sales playbook

Our [Sales Playbook](https://app.asana.com/1/1200524400901350/project/1212757516638013/list/1212758290889099) is an Asana project that describes common actions that must be taken throughout the sales process.



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

Sales operations are documented in our [Sales Playbook](https://app.asana.com/1/1200524400901350/project/1212757516638013/list/1212758290889099). If you're working on deals, have insights from member interactions, or want to propose experiments, reach out to James Colliander (Business Development Lead) or use the Lead - Opportunity - Capture workflow in the business-development channel in Slack. 
