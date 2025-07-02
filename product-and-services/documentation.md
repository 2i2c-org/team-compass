# Product documentation guide

## Sources of documentation

> The published version of a 2i2c service will be released using the following sites:
> 
> - [2i2c Team Compass](https://compass.2i2c.org/) As 2i2c's primary source of truth, the operational details and procedures of all services will be published to the Team Compass. Pushing to the Team Compass indicates that a particular version of a service has been released and can be trusted both internally and externally as the official documentation of **how** a service is intended to work. For services, the Team Compass defines how a service is implemented. The intended audience is the 2i2c Team. The Team Compass also needs to explicitly delegate the descriptions of both existing services and potential future services to where that information should be found.
> - [2i2c Service Guide](https://docs.2i2c.org/) This is the documentation that 2i2c makes available to its communities and users about what they should expect from our interactive computing platform. As services are integral to the socio-technical platform that are made available to communities, they need to be fully described in the Service Guide. For services, the Service Guide define **what** a service is and what should be expected by communities. The primary intended audience is 2i2c communities and users. The Service Guide should also describe **why** a service is offered and describes intended value to communities. A secondary intended audience is 2i2c sub-teams so there is alignment on available 2i2c services and how to they are intended to be experienced.
>
> A service needs to be consistently described and documented both sites to be considered done. For practically, this [repository](https://github.com/2i2c-org/services) may host the content describing both the how and the what and why for services. The Team Compass and Service Guide can delegate out the content to this repository.

## Our minimal definition of "documented"

The following things must exist to meet our definition of **Minimum Viable Documentation**. We will not accept product initiatives and tasks as complete until these criteria are met. This applies equally to platform functionality and services.

### User and value documentation

In a [source of truth for user documentation](../operations/documentation.md), provide information for users and for our BD team to create marketing and sales materials:

1. **A linkable page or section**. It should have at least the following.
2. **A short, discoverable title or section header**. It should have a descriptive title that is easy to discover and search for.
3. **Value and outcomes**. Why is it useful? When should you use it? Who is it for?
4. **Expected behavior**. What does it look like when it works? What should you expect to happen as a user?
5. **Who can access it?** For example, is it only for certain tiers? Is it only for certain user roles within a tier (e.g. community rep)?

Here's a template with an example:

```
# A short and recognizeable title about feature X

Feature X allows you to cool things A, B, and C. It works by A, B, C. As a result, you can accomplish A, B, and C outcomes / goals. This is useful because of A, B, C.

To use Feature X, do `A, B, C`. You'll know it's working when A, B, C.

**Available for**: Premier tier, Advanced tier communities. Available to all community members.
```

:::{admonition} Ways to make better documentation
The following things extend above-and-beyond our minimal viable documentation:

- Examples describing the most common use-cases for users to learn from.
- Tutorials that take users step by step through the actions needed to get value out of the feature / service.
- Sub-sections for "how-tos" with snippets of instructions for specific outcomes.
- Explanatory sections describing the theory / decisions behind a feature, and where to learn more.
:::

### Team and operations documentation

In a [source of truth for team documentation](../operations/documentation.md), provide information for others on the team to operate, maintain, and enhance this functionality.

1. **A linkable page or section**. It should have at least the following.
2. **Operator documentation**. All the necessary information for a member of the same team to learn more about how to perform, maintain, or understand the feature / service. It should be enough for another team member to get started and figure it out themselves without requiring the author to give missing context.

Examples:

- A short section with the most common gotchas and steps needed to learn.
- A short slide deck showing the outline and major structure of running a service.
