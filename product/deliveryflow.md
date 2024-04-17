# 2i2c's Product delivery flow

Since its formation, 2i2c has been successful in acquiring and maintaining a good number of client organizations that have benefited from its open, replicable cloud infrastructure services. 2i2c has maintained the ability to remain responsive to the needs of the communities it serves, but in doing so it has taken a somewhat reactive, ad-hoc approach to answering community partner or other customer requests.

As the organization is now more mature, and the breadth and complexity of its offerings and partnerships grow, it needs to shift to a more sustainable approach to the ongoing development of its products and services. This approach should allow it to make more effective use of its people and skills, and ensure that effort is always directed to the activities that are most valuable more closely aligned with its mission and value proposition.

## Identifying a Value Proposition as our North Star

A North Star is a core value, principle or goal that is used to help make decisions about what to do and when to do it. It starts with the organization’s mission, and is refined through a Value Proposition. Having a good understanding of what 2i2c’s North Star is will be key to ensuring that whatever we do is aligned with where we want the organization to be.

A Value Proposition is a clear, concise statement that communicates the specific benefits that a product or service offers to a target market segment. It succinctly explains how the product or service uniquely solves a problem or improves a situation for the community partner or customer, the value it adds, and why it is a better choice compared to competitors.

We are currently in the process of revising our value proposition to more accurately who we are and where we want to be, and will be sharing it for feedback in the coming months. 

## Becoming more intentional

As 2i2c scales up to meet its strategic goals, the way we decide what to put our efforts into will have to shift from a partially reactive approach to product development to a more intentional, careful approach that will allow us to carve out the space for our team to research and deploy the right solutions for the most important problems our communities face.

This will necessarily affect the interaction between Partnerships, Product and Engineering, to ensure that our external conversations with communities, both current and prospective, are carefully considered against what would deliver the most value for the most communities, and be most closely aligned with our strategic objectives as an organization.

The product delivery flow outlined herein is meant to provide a framework whereby input from community stakeholders can be recorded, assessed, triaged and prioritized in alignment with what it is we want to achieve as an organization. 

Here are some basic principles we need to keep in mind as we adopt a more intentional way of building product:

- Not all feature requests are equally important.
- Loud does not equate to urgent.
- It’s OK to say no. We will make no promises until we’re sure we can deliver.
- All non-critical feature requests will be triaged and prioritized according to the process.
- We will ensure our resources are not overtaxed, and create space for our work to be proactive, rather than reactive.
- We will limit the number of projects we run at any one time to ensure they can be adequately supported.
- We need to balance competing interests. What’s best for science? What’s best for this community? What’s best for 2i2c? What’s best for the upstream open source projects we contribute to?

By collectively signing up to these principles, we have given ourselves permission to say no to projects that are not aligned with our long term goals or those of the communities we serve, and preserve our ability to intentionally move towards those goals.

# Defining our product Delivery Flow

2i2c faces three key challenges in the coming years: expanding its community partner base, achieving a pricing model that fosters sustainable growth, and lessen our dependence on external funding.

In order to achieve these, we need to adopt a process that lets us balance pro-active tasks (e.g. developing new features for our products and services in line with our Value Proposition) against reactive tasks (e.g. community support tickets).

It’s key that this process be agreed upon by all stakeholders within the organization, but specifically the Product Lead and Delivery Manager, with the Product Lead being responsible for defining the priority of major strategic initiatives, projects and milestones, and the Delivery Manager being responsible for how those projects are broken down into tasks for our Engineering team to work on, and how progress and team performance is tracked.

As we are a small organization with a relatively large proportion of engineering talent, we will work wih a lightweight product and delivery flow, with an emphasis on up-front macro-level prioritization that empowers the Engineering team with the flexibility to define how to problem solve, break down and prioritize their work at the micro level.

The next part of this document outlines such a process, designed to be transparent to the organization about what’s been worked on at any time, and to provide clear communication and collaboration points between Product, Engineering and any stakeholders, internal or external, that have a vested interest in the outcome of a project.

## 1. The insights board

Any good product delivery flow starts with establishing a centralized repository for insights, a place to collect our knowledge of the wants and needs of the community partners and other customers we serve, and to record conversations we’ve had with partners about specific product enhancements we may want to consider. 

While insights will naturally trickle in from our partnership support and sales efforts, community building initiatives, conferences, and other organic means, the most actionable and valuable insights come from intentional, active and engaged customer and UX research.

Insights are not tasks. They are not the basis of a backlog. They are knowledge that may be leveraged into feature ideas, projects, initiatives, or whole new products… Or not. 

At 2i2c, we should always ensure that we are dedicating our skills, people and resources to fully understanding, capturing and responding to our communities’ most pressing needs, separating the signal from the noise and ensuring our efforts are always aligned with the most value with the widest community impact.

Formerly, insights relevant to product improvements were captured on GitHub as conversations around projects, on Slack as casual conversations, or as emails between community partners and Partnership leads. As queries and comments on FreshDesk. They could easily get lost. 

While those tools are still very much in use at 2i2c, we have now adopted a tool called [Productboard](https://www.productboard.com/) to provide us with a centralized place for storing, tagging and later mining this type of knowledge, benefiting our ability to fully consider, prioritize, and potentially action the most important ideas. 

## 2. The Ideas board

### What is an idea

Any single insight, or collections of related insights, can give rise to an idea, which is an actionable and well formulated suggestion of a project we may want to look into. Ideas are the individual items in the Ideas board. 

What typically is considered an idea that will go into the product’s ideas board:

- Suggestions from community partners, other customers, partnership discussions, stakeholders, or community members that seem worth doing at some point.
- Internally-sourced features that form the backbone of what we want to do to achieve our value proposition (e.g. a push towards a self-service interface for customization)
- Big, strategically important projects spanning a collection of features (These will typically be broken down into multiple Initiatives later)
- Non urgent user experience shortcomings that are likely to need acting on at some points
- Technical debt reductions

What is not an Idea and should not be included in the product backlog:

Urgent or critical bugs - these will typically be short-cutted to the Build stage and sped through Testing and Release.
Bugs that can be dealt with in the normal course of community support efforts.
Day-to day partnership support requests that require relatively rapid response.

#### Prioritization drivers

Having a collection of ideas is not very useful if they are all treated equally. We need a way to rapidly get a sense of which ideas are likely to produce the most value. 

To that end, each idea should be submitted with a set of drivers, which will help us prioritize our backlog of ideas, and decide which ideas we should look into more closely with a view to potentially implementing them  (see Initiatives).


- **Impact**: How wide ranging is the impact of this feature on 2i2c or the entities it serves.
- **Request frequency** (0, 1-4, 5+): how many individual community partners or other customers have mentioned this, or outright requested it. The more requests, the more we should pay attention.
- **Strategic alignment** (Low, Med, High): How close is this idea to the goals of the organization, 	its mission, and value proposition? We should always aim to prioritize ideas that are closely aligned with those guiding principles.
- **Effort** (Low, Med, High): How much effort would this take to implement (relative sizing, very guess-based).

### Types of idea

Ideas should be classified as one of the following, each with its own ticket template:

- **Bug** - Something not working as it should. Non critical, not timely.
- **Feature Request** - An enhancement to our product that has specifically originated from a community partner or other customer. The requester who raised it should be noted in the ticket.
- **Feature Enhancement** - A proposal for improving the functionality of our product
- **Technical Debt** - An Idea that will reduce our technical debt moving forward

## 3. Product Initiatives

Product Initiatives are ideas that we have decided to take a deeper look at, with a view to implementing them to produce value for 2i2c or its communities. The Product Lead, in collaboration with any relevant stakeholders and 2i2c’s Leadership team, will normally determine when an idea is worth taking forward to the Initiative stage. 

**Initiatives form the basis of the Product Backlog**, the list of tasks we are or soon expect to be working on. As such, unlike Ideas, Initiatives are deemed to be “on deck”, requiring stakeholder input to actively triage, scope, and potentially implement.

**Initiatives within the scope of Product should have a software component, but do not have to be purely about software**, they can and often will contain activities that are complementary to the building of tangible software outputs. These could include, but not be limited to, the creation of training materials, copy, content, visual assets, or other non-software activities. 

**Initiatives need to be finite and have tangible deliverables.** Indefinite partnership commitments or policy efforts do not fit within the Delivery Flow, and will need to be prioritized and handled at the strategic level.

## 4. Scoping

### Goals

Scoping an Initiative has two goals:

1. Defining the specification of an Initiative to ensure a shared and thorough understanding of what needs to be built
2. Establishing the level of effort required to implement it, usually in terms of days or engineering points. This task normally falls to the engineers who are most likely to be working on an Initiative’s implementation, and it is up to the Delivery Manager to ensure there is a process in place to carve time for scoping new Initiatives as they hit the backlog.

The scoping stage requires active involvement and collaboration from a mix of stakeholders, product, designers and engineers, who all contribute their expertise to ensure a shared understanding of the task at hand. Scoping an Initiative is not a waterfall process.

### Activities

The up-front investment in thoroughly scoping an Initiative pays dividends in maximizing the chances of developing the right solution the first time round.

Typical activities that may be conducted during the scoping stage include, but are not limited to:

- UX research
- Customer research
- Design sprints
- Specification writing
- UX wireframes 
- Prototype building
- User testing 
- Engineering feasibility assessment
- Engineering points estimation (a.k.a. hard scoping) 

## 5. Building

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

User stories describing a Initiative should be in the format of:

**As a ______ I want to ______ in order to ______**

For example, an idea to provide a self-service menu of add-ons for our platform would contain the following user story:

_“As a community leader I want to have a list of all available add-ons, and their prices, in order to select what I want from my deployment and know exactly how much extra that will cost me.”_

User stories in this format are extremely helpful in ensuring all stakeholders have a common understanding of what the goal of a particular idea might be. These user stories can also form the basis of engineering tasks. 

Initiatives are moved through these stages while they are with Engineering, and will remain there until they are ready to be moved to the next stage, Review.

## 6. Review

At this stage, the Product Lead and/or any relevant internal or community partner stakeholders take the output of Engineering and validate it against the Initiative’s original user story, established Scope, relevant designs or blueprints, and/or documented customer requirements. 

If the Initiative was assigned a Key Stone Flag or Feature Flag release, that release will fall under the scope of this Review stage until the Initiative has been adequately validated with the entities or users who have access to the flagged feature. For major projects, this could include a lengthy beta testing phase.

Successful testing will move the Initiative to the next stage, Release, while unsuccessful testing will bump it back to the Building stage.


By default, the Engineering Lead will be responsible for signing off the Initiative’s code quality and implementation robustness, while the Product Lead will take responsibility for signing off that the Initiative’s implementation meets the intended use case and business value, taking in input from any relevant stakeholders, as needed. 

## 7. Done
Successful release of a Initiative effectively concludes a Initiative’s lifecycle. Any new bugs or issues found after the release will be treated as new Ideas.

# Learning from what we have done
After every delivery, the team should have the space to reflect on what was achieved, celebrate the milestone, and record any learnings that could lead to improvements in the process for the next deliverable. Alongside regular iteration retrospectives, major milestones should be capped by a Milestone Retrospective, a ceremony designed to provide a safe and open environment for the team to express what they liked, didn’t like, and would improve about the process of delivering that milestone.

# Communicating what we have done

While it’s important to have a process that takes a concept from idea to release, it is just as important to make sure that we actively communicate what’s been done to our community.

The product delivery flow therefore must be extended to ensure action is taken to clearly communicate the release of major milestones to our communities, highlighting the value we have delivered and how it is aligned with their needs.

We should ensure that we have a process in place to follow up major releases with relevant community announcements, above and beyond the regular updates provided by Chris. 

These announcements should be broadcast on the 2i2c’s site as well as any relevant social media channels, to ensure we keep engaging our community with our progress, while giving new or prospective community partners or other customers an opportunity to learn more about the kinds of features and services we could provide them.

# Outcomes

A scalable, sustainable product delivery flow helps to provide us with the tools we need to sift through ideas and community partner, customer or end user requests in a more intentional way.

Additionally, as we prioritize Initiatives according to their drivers, we naturally gain a roadmap that will focus our efforts as an organization, ensure we are spending our effort and skills where they can generate the most value for our community partners and our strategic goals, and provide us with a clearer view of projects and activities they can communicate to our network of partners.
