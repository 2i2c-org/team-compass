# Documentating product features

(product:documentation-sources)=
## Sources of documentation

- [2i2c Service Guide](https://docs.2i2c.org/): **what** our product is, **why** it is useful, and **how to use** our features and services.
- [2i2c Infrastructure repository](https://infrastructure.2i2c.org): **how to operate** our infrastructure.
- [2i2c Services guide](https://github.com/2i2c-org/services): **how to operate** our services.

(minimally-documented)=
## Our minimal definition of "documented"

The following things must exist to meet our definition of **Minimum Viable Documentation**. Product initiatives are not complete until these criteria are met. This applies equally to platform functionality and services.

### User and value documentation

In a [source of truth for user documentation](../operations/documentation.md), provide information along the following template:

```md
(a-myst-label)=
# A short, discoverable page title or section header

A few sentences answering: What does this allow you to do? Why is it useful? When should you use it? Who is it for?

## How it works

A few sentences describing how to use it, and what what it looks like when it works. What should you expect to happen as a user?

## Who can access it?

(optional) if this is only available to subsets of communities or users, state which users/tiers/etc can use it.
```

### Team operations documentation

In a [source of truth for team documentation](../operations/documentation.md), provide information for others on the team to operate, maintain, and enhance this functionality. Here's a template you can use:


```md
(a-myst-label)=
# A short, discoverable page title or section header

A sentence explaining the functionality [that is documented here](<link to the user documentation>)

## How to set-up / operate / deliver / etc

All the necessary information for a member of the same team to learn more about how to perform, maintain, or understand the feature / service. It should be enough for another team member to get started and figure it out themselves without requiring the author to give missing context.
```
