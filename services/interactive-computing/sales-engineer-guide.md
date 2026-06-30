# Sales Engineer Guide

*Step 2 of the Hub Rollout Process*

## Your Role

You are the technical voice in the sales call. Your job is to understand the community's goals and provide expert guidance on how to accomplish those goals, not to close the deal (that's BD). You're there to make the community feel confident that 2i2c understands their problem and can solve it.

## What You Need to Do

### Listen first, then guide

- Understand the community's objectives — what are they trying to accomplish with interactive computing?
- Identify who the users are (researchers, students, analysts) and how many.
- Let the community describe their X (what they want) and their Y (how they think it should work). Your value is validating that approach or proposing a better Z that fits 2i2c's platform.

### Key questions to ask
- Who are the users? Administrators? Groups?
- Do some of your users have technical expertise? What kind of expertise?
- What do the usage scenarios look like?
- How do your users identify themselves as members of your community?
- What does success look like for your community leadership and members?

### Gather key technical context

- **Hubs**: Based on their activities, does this community need one hub or many? What workloads (notebooks, RStudio, GPUs, large datasets) should they be ready for?
- **Data**: Data is a gravitational object in the cloud, so critical data may set direction for cloud provider choice. Where is the data stored? What kinds of workflows do you want to carry out with the data? 
- **Cloud provider**: Which is appropriate — AWS, GCP, Azure, one of those but using a CloudBank allocation, JetStream2, OVH, NRP? Consider cost, data locality (see above), and institutional constraints.
- **Authentication**: How will users log in — CILogon, GitHub, Google Auth, institutional SSO?

### Solve the XY Problem

Communities often arrive with a preconceived solution. Your job:

1. Validate if their approach works on 2i2c's platform, **or**
2. Propose an alternative that better fits their actual need (which can include referencing the 2i2c roadmap)

Be direct but collaborative. The goal is upstream technical judgment — "Are we building the right thing the right way?"

## What Success Looks Like

By the end of the call:

- **The community** walks away feeling that 2i2c will be a trusted expert partner.
- **You** have enough context about the community to deploy a hub if BD closes the contract.
