(product-delivery-flow)=
# Product delivery flow

As we are a small organization with a relatively large proportion of engineering talent, we work with a lightweight product and delivery flow, with an emphasis on up-front macro-level prioritization that empowers the Engineering team with the flexibility to define how to problem solve, break down, and prioritize their work at the micro level.

:::{figure} images/delivery-flow.jpg

Process diagram of 2i2c's [Product Delivery Flow](https://miro.com/app/board/uXjVNvlBa6E=/?share_link_id=253320305785).
:::

This document outlines such a process, designed to be transparent to the organization about what’s been worked on at any time, and to provide clear communication and collaboration points between Product, Engineering and any stakeholders, internal or external, that have a vested interest in the outcome of a project.

## How most team members participate in this process

All team members are encouraged to participate in the Product process by **providing, refining, and discussing suggestions, needs and pain points with the Head of Product**. Suggestions for new streams of work to be prioritized can come from anywhere, and we encourage all team members to proactively engage with the product delivery flow to ensure their input and expertise contributes to our direction of travel.

## Our product operations principles

First off, read [the Product overview and principles section](overview.md) to understand the high-level goals and principles that drive this work, and lead to the system below.

While insights naturally trickle in from our partnership support and sales efforts, community building initiatives, conferences, and other organic means, the most actionable and valuable insights come from intentional, active and engaged customer and UX research.

Insights are not tasks. They are not the basis of a backlog. They are knowledge that may be leveraged into feature ideas, projects, initiatives, or whole new products… Or not. 

At 2i2c, we should always ensure that we are dedicating our skills, people and resources to fully understanding, capturing and responding to our communities’ most pressing needs, separating the signal from the noise and ensuring our efforts are always aligned with the most value with the widest community impact.

When it's clear that conversations and insights point towards a particular need, pain point or solution that may be worth capturing and implementing, we use Initiatives as a way of capturing that information. 

## Product Initiatives

Initiatives are tracked in [our Initiatives Repo](https://github.com/2i2c-org/initiatives/issues) as well as [our Public Roadmap](https://2i2c.org/roadmap).

Product Initiatives are ideas that we have decided to take a deeper look at, with a view to implementing them to produce value for 2i2c or its communities. The Product Lead, in collaboration with any relevant stakeholders and 2i2c’s Leadership team, will normally determine when an idea is worth taking forward to the Initiative stage. 

**Initiatives form the basis of the Product Roadmap**, the list of tasks we are or soon expect to be working on. As such, unlike Ideas, Initiatives are deemed to be “on deck”, requiring stakeholder input to actively triage, scope, and potentially implement.

**Initiatives within the scope of Product should have a software component, but do not have to be purely about software**, they can and often will contain activities that are complementary to the building of tangible software outputs. These could include, but not be limited to, the creation of training materials, copy, content, visual assets, or other non-software activities. 

Initiatives that are related to the technical aspects of our platform are labelled as **"platform initiatives"**, whereas initiatives of a more general, non-software specific nature are labelled as **"P&S Initiatives"**. Our public roadmap only shows platform initiatives. 

**Initiatives need to be finite and have tangible deliverables.** Indefinite partnership commitments or policy efforts do not fit within the Delivery Flow, and will need to be prioritized and handled at the strategic level.

**All initiatives default to the status of "Candidate initiative."**  They only officially enter our roadmap when they are promoted to the **"Upcoming P&S Initatives"** status in the [P&S backlog](https://github.com/orgs/2i2c-org/projects/57/views/1).

## Scoping initiatives

### Goals

Scoping an Initiative has two goals:

1. Defining the specification of an Initiative to ensure a shared and thorough understanding of what needs to be built, from both an internal and cusstomer perspective (as our initiatives are public).
2. Establishing the level of effort required to implement it, usually in terms of days or engineering points. This task normally falls to the engineers who are most likely to be working on an Initiative’s implementation, and it is up to the Delivery Manager to ensure there is a process in place to carve time for scoping new Initiatives as they hit the backlog.

The scoping stage requires active involvement and collaboration from a mix of stakeholders, product, designers and engineers, who all contribute their expertise to ensure a shared understanding of the task at hand. Scoping an Initiative is not a waterfall process.

### Creating a valid initiative

Initatives are written following a [strict template](https://github.com/2i2c-org/initiatives/blob/main/.github/ISSUE_TEMPLATE/01_new-initiative.yaml) that ensures a minimum acceptable level of detail. **Anyone can write an initiative**, but it's the the **Tech Lead** and **Head of Product** who are ultimately responsible for ensuring the content of all initiatives on the roadmap meet this minimum level of detail.

#### Prioritizing initiatives

Having a collection of candidate initiatives is not very useful if they are all treated equally. We need a way to rapidly get a sense of which initiatives are likely to produce the most value. 

To that end, each candidate initiative is evaluated against a set of drivers to decide which should make it to our roadmap:

- **Impact**: How wide ranging is the impact of this feature on 2i2c or the entities it serves.
- **Request frequency** : how many individual community partners or other customers have mentioned this, or outright requested it. The more requests, the more we should pay attention.
- **Strategic alignment** : How close is this idea to the goals of the organization, 	its mission, and value proposition? We should always aim to prioritize ideas that are closely aligned with those guiding principles.
- **Effort**: How much effort would this take to implement (relative sizing, very guess-based).
- **Co-funding interest**: Candidate initiatives that have received a commitment for funding by one or more communities are usually fast-tracked into the Roadmap for accelerated development. The ability to co-fund platform initiatives is one of the key benefits of our Premier Membership tier.  

### Statements of Work (SOWs) and Software Design Documents (SDDs)

We use Statements of Work (SOWs) or Software Design Documents (SDDs) as a tool to refine the scope of an Initiative, and to ensure that all parties involved have a shared understanding of why, what and how a project is delivered. This is not a waterfall design process, but is intended to provide just enough detail for collaborators to align on the goal, design approach and technical deliverables.

The difference between an SOW and SDD is that an SOW is written for an external buyer that could potentially commission the work and hence require more rigorous timeline estimates, while an SDD is written for internal review and alignment without the same rigour for timeline estimates (but still recommended).

SDDs and SOWs are usually only defined when an initiative has received interest from a community, and can be used to drive conversations around funding of that initiative. 

The following table summarises the relevant parties that can sign off on an SOW/SDD before implementation:

| | SOW | SDD |
|--|--|--|
| Head of Product | ✅ | ✅ | 
| Tech Lead | ✅ | ✅ |
| Business Development Lead | ✅ | ❌ |

Once an SOW or SDD is signed off, it can be used to break down an initiative into tasks with [GitHub sub-issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/adding-sub-issues). A single document is easier to read and review than a collection of GitHub issues while the initiative is being scoped, but once the initiative is ready to be built, work in progress is tracked in GitHub issues on the [P&S board](/operations/workflow.md#product-and-services-board).


- [SOW/SDD template](https://hackmd.io/boBV8E_kSJOo_tkMCU29Eg?both)
- [Example of an SOW](https://github.com/2i2c-org/infrastructure/issues/6150)
- [Example of an SDD](https://github.com/2i2c-org/infrastructure/issues/6315)

## Building

Scoped Initiatives are now ready to be executed upon, and be broken down into tasks that will allow for the right skill sets to contribute to the outcome. Engineering tasks will be broken down and assigned to the Engineering backlog, and non-engineering tasks (e.g. the production of training materials,content, or documentation) will be assigned to individuals within the relevant disciplines.

### Engineering breakdown

Any software related tasks within the initiative needs to be broken down before entering the Engineering backlog. This breakdown, and the subsequent implementation of the software components of the Initiative, is fully within the responsibility of the Engineering team, in consultation with any relevant stakeholders and product owners, until the output of the Initiative is ready to be tested at the Review stage.

As more detail is added to a Initiative through these activities, the Initiative will also be broken down into the following work item types, in close collaboration with Engineering and any relevant stakeholders:

- Initiatives
- Epics
- User Stories
- Tasks
- Sub-tasks

### User stories

User stories describing an Initiative should be in the format of:

**As a ______ I want to ______ in order to ______**

For example, an idea to provide a self-service menu of add-ons for our platform would contain the following user story:

_“As a community leader I want to have a list of all available add-ons, and their prices, in order to select what I want from my deployment and know exactly how much extra that will cost me.”_

User stories in this format are extremely helpful in ensuring all stakeholders have a common understanding of what the goal of a particular idea might be. These user stories can also form the basis of engineering tasks. 

Initiatives are moved through these stages while they are with Engineering, and will remain there until they are ready to be moved to the next stage, Review.

### Documenting new features and services

All new platform features and services must meet our [definition of minimally documented](#minimally-documented) before a product initiative is complete.

## Review

At this stage, the Product Lead and/or any relevant internal or community partner stakeholders take the output of Engineering and validate it against the Initiative’s original user story, established Scope, relevant designs or blueprints, and/or documented customer requirements. 

If the Initiative was assigned a Key Stone Flag or Feature Flag release, that release will fall under the scope of this Review stage until the Initiative has been adequately validated with the entities or users who have access to the flagged feature. For major projects, this could include a lengthy beta testing phase.

Successful testing will move the Initiative to the next stage, Release, while unsuccessful testing will bump it back to the Building stage.


By default, the Engineering Lead will be responsible for signing off the Initiative’s code quality and implementation robustness, while the Product Lead will take responsibility for signing off that the Initiative’s implementation meets the intended use case and business value, taking in input from any relevant stakeholders, as needed. 

## Done
Successful release of a Initiative effectively concludes a Initiative’s lifecycle. Any new bugs or issues found after the release will be treated as new Ideas.

## Learn from what we have done
After every delivery, the team should have the space to reflect on what was achieved, celebrate the milestone, and record any learnings that could lead to improvements in the process for the next deliverable. Alongside regular iteration retrospectives, major milestones should be capped by a Milestone Retrospective, a ceremony designed to provide a safe and open environment for the team to express what they liked, didn’t like, and would improve about the process of delivering that milestone.

## Communicate what we have done

While it’s important to have a process that takes a concept from idea to release, it is just as important to make sure that we actively communicate what’s been done to our community.

The product delivery flow therefore must be extended to ensure action is taken to clearly communicate the release of major milestones to our communities, highlighting the value we have delivered and how it is aligned with their needs.

We should ensure that we have a process in place to follow up major releases with relevant community announcements, above and beyond the regular updates provided by Chris. 

These announcements should be broadcast on [the 2i2c.org blog](https://2i2c.org/blog) as well as any relevant social media channels, to ensure we keep engaging our community with our progress, while giving new or prospective community partners or other customers an opportunity to learn more about the kinds of features and services we could provide them.

## Outcomes

A scalable, sustainable product delivery flow helps to provide us with the tools we need to sift through ideas and community partner, customer or end user requests in a more intentional way.

Additionally, as we prioritize Initiatives according to their drivers, we naturally gain a roadmap that will focus our efforts as an organization, ensure we are spending our effort and skills where they can generate the most value for our community partners and our strategic goals, and provide us with a clearer view of projects and activities they can communicate to our network of partners.
