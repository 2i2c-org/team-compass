(engineering:structure)=
# Structure and responsibilities

This page describes the structure and roles of our Engineering team.

## Responsibilities

Below is a summary of the major responsibilities for this team.

### Oversee our technical strategy

- Define our major objectives and priorities.
- Make major architectural decisions about our cloud infrastructure.

### Operate our cloud infrastructure

- Perform daily operation of ongoing cloud services, addressing technical problems as-needed.
- Resolve operational issues related to our cloud infrastructure.
- Oversee our [Incident Response process](../projects/managed-hubs/incidents.md).

### Develop our cloud infrastructure

- Improve the reliability and uptime of our infrastructure
- Improve the scalability of our infrastructure to more users and more communities
- Minimize toil and automate processes as much as possible

```{team} Engineering Team
```

## Team structure

This team operates similarly to a **Site Reliability Engineering** team.
It focuses most development efforts on improving the cloud infrastructure that supports our partner communities, rather than developing new features and technology for the use-cases we support.
It balances a combination of **operations** and **development** focused around our cloud infrastructure.

Our **Technical Lead** and **Team Lead** define our technical priorities at any moment, and communicate these priorities to others on the team.
They are expected to coordinate with other leads within 2i2c in order to ensure that our technical priorities reflect our organizational priorities for impact.
Our **Project Manager** ensures that we have an efficient system for coordinating and planning our work, and **our engineering team** carries out most technical implementaitons and operations for 2i2c.

(engineering:roles)=
## Team roles

```{role} Engineering Manager
```

### Engineering Manager

:::{note}
This role is a work-in-progress,
:::

Responsible for overseeing our engineering team, ensuring that it is operating in an effective and equitable manner, and ensuring that each team member's work is aligned with their goals and interests.

This role is currently un-filled.

```{role} Technology Lead
```

### Technology Lead

The Senior Open Source Infrastructure Engineer (SOSIE) role is designed to help guide our team and cultivate a healthy and productive culture.
It is heavily inspired by [On being a senior engineer](https://www.kitchensoap.com/2012/10/25/on-being-a-senior-engineer/).

This role focuses their efforts on our infrastructure, but spends a lot of their time guiding others, focusing on particularly complex infrastructure design and development, and interfacing with other teams and stakeholder communities to help guide our development. Below is a short list of expectations for this role.

- Solve complex technical problems with **broad, cross-project scope**, often
  involving co-ordination with multiple teams across different open source
  projects.

- Acts as a point of escalation for complex technical problems, preferring to
  solve them with collaborative guidance rather than 'just doing it'.

- Coordinate with product/business teams on roadmap priorities, and provide
  implementation suggestions and effort estimates.

- Provide guidance on major strategic questions in infrastructure and
  engineering team strategy

- Helps grow other engineers via mentorship, code & design review, and
  sponsorship to find opportunities for them

- Act as a role model for positive, inclusive, and constructive team dynamics.

**Membership**: This role is currently filled by `@yuvipanda` on a volunteer basis.

```{role} Open Source Infrastructure Engineer
```
```{role} Engineer
```

### Open Source Infrastructure Engineer

An Open Source Infrastructure (OSIE) focuses on infrastructure that supports interactive computing.
It intersects job titles such as “dev-ops engineer”, “site reliability engineer”, “software engineer”, and “cloud engineer”.

#### Key responsibilities

- Ensure the reliable operation of the 2i2c infrastructure (leveraging production-ready cloud-based tools such as JupyterHub, BinderHub and Dask).
- Resolve operational issues that are surfaced by our support team
- Explore emerging technologies in the Cloud / DevOps space, design and implement cloud computing architecture in partnership with our team.
- Participate in upstream open source communities we rely on (such as JupyterHub, BinderHub, Dask, etc) in partnership with the established leaders of those communities and collaborate with the Community Lead in the education and outreach around cloud computing.
- Work with a distributed and global team - team members are given a lot of autonomy, and expected to be proactive at communicating with one another and working with others to allocate effort that will maximize our impact.

#### Necessary qualities

- Experience with deploying applications on cloud infrastructure.
- Experience deploying and developing with Linux container-based technologies, such as Docker and Kubernetes.
- Experience with continuous integration services (e.g. Circle CI, GitHub Actions).
- Experience developing tools in a general purpose programming language (eg. Python).
- Experience collaborating and coordinating work via online platforms, such as GitHub, GitLab, or BitBucket, and distributed revision control.
- Experience working with distributed service teams that use asynchronous methods of communication

#### Useful qualities

- Experience with major cloud providers.
- Experience in programming and software engineering with a track record of leadership in open, collaborative projects with broad community adoption.
- Experience working on geographically distributed open-source projects.
- Experience with the Jupyter ecosystem and other tools for interactive computing.
- Evidence of existing connections and relationships in the worldwide ecosystem of open source software for data-intensive research and ability to establish new ones.
- Experience with common data science methods, platforms, workflows, and infrastructures; with data management systems, practices, and standards; and the capacity to gain familiarity with new related topics.
- Experience engaging with highly technical researchers across a variety of methodological fields, research domains, and computational platforms.
- Experience building and maintaining continuous deployment pipelines.
- Interpersonal skills to work with researchers and students. Including the skills to communicate complex information in a clear and concise manner both verbally and in writing

## Membership

Our engineering team is listed on our [list of team members](../reference/team.md).
