# Active Projects

These are active projects that 2i2c is currently working on.

```{note}
Any time that you're asked to give a new email address for something related to your 2i2c work, use your 2i2c email address as a default. For example, if you're adding 2i2c team members as admin users to a hub with Google OAuth, use their 2i2c email addresses.
```

Here is a list of active projects:

```{contents}
:depth: 2
```

## Starting a new project?

A new project should be created for anything with a specific scope and set of deliverables that spans a reasonably long amount of time (e.g., something that will spawn multiple issues or to-do items). 2i2c projects should all feed into the [2i2c organizational strategy and goals](strategy.md).

When 2i2c embarks on a new project, create a new entry on this page. This will serve as a reference point where 2i2c team members can learn more about the project. Include the following information

We should document the following things:

1. **Summarize the project**. What is the overarching scope and deverables for the project? Who is it in collaboration with?
2. **Define the project's strategic goal**. What is the overarching purpose for working on this project? How does it fit in with the overarching [strategic goals of 2i2c](strategy.md)?
3. **Key Outcomes**. What are some concrete outcomes that we wish to get from this project? What are things we can use to define success?
4. **Project Information** What's the "source of truth" for this project? Where does project management and tracking take place? Where do we track progress? What about to-do items? Where does communication happen around this project? (e.g., in a GitHub repository, in Slack, in a Google doc).

(projects:organization-building)=
## Organization-building

As 2i2c is quite young, a major first step will be to build out our organizational infrastruture, team processes, and culture.

### Strategic Goal

Building a good organizational and team structure is an important first step in being successful for the next 3 / 6 / 12 / 24 months.

### Key outcomes

- Team members understand the goals and mission of the organization, and are aligned with them
- Team members understand how their role and workstreams fit into those goals
- We have healthy practices in communication and information-sharing
- We follow best-practices at remote teamwork and inclusivity
- We have a process to improve our team practices moving forward

### Project information

- Most information for this one uses [issues with the {badge}`strategy,badge-danger` badge](https://github.com/2i2c-org/meta/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc+label%3Astrategy).

(projects:product-building)=
## Business model and product design

First and foremost, 2i2c is meant to be a sustinable organization that generates revenue through services that it provides to others. We must define what these services are (SaaS, support, development, etc), how users may access them (one-off collaborations, web-forms, umbrella grants, etc), and what pricing model we wish to follow (e.g., hourly rates, tiered products and support, etc).

### Strategic goal

Defining a specific set of products and pricing will allow us to engage new collaborators (or customers) in a more structured fashion with less time and labor associated with it. It will also give us something concrete that begin iterating on as we continue working towards sustainability.

### Key outcomes

- We have a publicly-defined menu of options for how others can access hub infrastructure via 2i2c
- These options have prices attached to them, and those prices are flexible enough to be attractive for the variety of organizations we wish to fund
- We have a financial model that predicts 2i2c revenue over time using these options as input
- We have decision-making mechanisms for when to grow the 2i2c team

### Project Information

- [this google folder](https://drive.google.com/drive/folders/1HEEfyT2h_fKeqKdsz9Ftiw9Be1Uj48D6?usp=sharing) has most information and brainstorms regarding this project
- [this github issue](https://github.com/2i2c-org/meta/issues/94) also has several relevant links and discussion points

(projects:utoronto-hub)=
## University of Toronto pilot hub

 pilot educational hub for the University of Toronto. It will serve several educators in the university, including both Python and R users. This is a fairly vanilla JupyterHub setup but we will add modest customizations for the Toronto team.

### Strategic Goal
Use this pilot to learn about what needs a large, heterogeneous university like Toronto has, and use this to help build a sustainability model for 2i2c serving [large educational institutions](strategy:education).

### Key Outcomes

- Interviews with U. Toronto users about their experiences on the hub - what went well, what went wrong, etc
- Understanding about how to price educational hubs such as these for large institutions
- Future business with U. Toronto for running hub infrastructure

### Project Information

Project management for this collaboration is in two locations:

- Project management: [the deployment repository](https://github.com/utoronto-2i2c/jupyterhub-deploy) has further information about these deployments.
- Communication: **Microsoft teams**. This collaboration is using the Microsoft Teams account with U. Toronto. If you're working on this deployment, ask for MS Teams access in the Slack.


(projects:hubs-for-all)=
## Hubs for All infrastructure pilot

his is pilot infrastructure to minimize the human toil needed to deploy lightweight JupyterHub infrastructure with a standardized computing environment. Some of these are via a collaboration with UC Berkeley's Division of Data Science and Society, while others are connections we have made on our own.

### Strategic Goal
The goal of this project is to get 2i2c closer to offering lightweight, "self-serve" hub infrastructure that requires minimal oversight and operation from 2i2c (and thus, lowers 2i2c's costs to providing this infrastructure). It will help make 2i2c hubs more affordable and [usable for smaller educational organizations](strategy:education).

Another strategic goal is to begin building bridges to educational institutions that would benefit from lightweight hub infrastructure, with the goal of strengthening these connections in the future.

### Key Outcomes

- JupyterHub deployment that is self-serve, can generate multiple hubs in a scalable fashion, meets the majority of educational needs for our users, and requires minimal human intervention.
- Interviews and feedback from hub users about their experiences
- Understanding of the financial perspective of hub users that can feed into a sustainability model for self-serve hubs
- Satisfied users of these hubs that convert into paying hub customers

### Project Information

Project management for this collaboration is in two locations:

- Project management in two locations:
  - [JupyterHubs deploy repository](https://github.com/2i2c-org/pilot-hubs)
  - [Pilot documentation](https://github.com/2i2c-org/pilot)


(projects:panfoo-pilots)=
## Pan-foo hubs pilots

We are deploying several customized JupyterHubs for research communities that are related to the Pangeo project. These will generally be a bit more hands-on than the "self-serve" JupyterHub infrastructure.

### Strategic Goal

Our primary goal for these pilots is to learn how we can adapt the Pangeo infrastructure model to new use-cases, and to find patterns and technology that we can make easier to replicate and maintain. We also wish to have some research use-cases under our belt to better-understand their needs, and to make inroads into some research communities.

### Key outcomes

- Technology and documentation for deploying a Pangeo-style hub infrastructure with minimal toil and maintenance
- Documentation about the "pan-foo" model and the tools that it uses
- Feedback from our hub users about their experience, both good and bad.
- An understanding of financial perspective from hub users and their institutions that can fit into a sustainability model.
- Institutional buy-in and conversions to paying customers.

### Project Information

There are currently two organizations for which we are deploying these hubs, and these are being managed in two different places.

#### Farallon Institute

The [Farallon Institute](http://www.faralloninstitute.org/) is a research institute associated with NASA, they are running a Pangeo-like hub for their community.

- project management:
  - [GitHub repository for hub deployments](https://github.com/2i2c-org/pangeo-hubs)
  - [Gitter channel](https://gitter.im/pangeo-data/FI-hub)

#### Catalyst Cooperative

The [Catalyst Cooperative](https://catalyst.coop/) is a cooperative consultancy and advocacy group for climate change policy. They curate several large datasets and wish to provide easy interactive computing access to these datasets.

Currently, we are working with this team via the Pilot Hubs, though we expect to move them to a dedicated hub if they wish to pursue the collaboration further.

- Project management: [Meta issue for collaboration](https://github.com/2i2c-org/meta/issues/80)

(projects:jmte-pangeo)=
## Dev/ops for Jupyter Meets the Earth and Pangeo

The Pangeo project has considerable needs in both operating and developing hub infrastructure for their community. We are collaborating with them to provide both daily operations of their hubs, as well as help them in evolvin and improving their infrastructure to better-suit their scientific mission.

### Strategic Goal

Pangeo is a key partner of 2i2c and has collaborated with 2i2c founders for many years - it is a standard-bearer for science in the cloud, and an opportunity for 2i2c to both learn from and support their use-cases. We hope to use this partnership to both move Pangeo closer to sustainability, as well as to highlight how 2i2c infrastructure can be used for large-scale scientific analysis and communities. It is also an opportunity to support a scientific use-case that is within the mission of 2i2c's research goals.

### Key Outcomes

The key outcomes for this project are largely defined by the Pangeo community, as this will be an ongoing engagement. That said, we have a few core goals for 2i2c:

- Meet the deliverables from the NSF JMTE grant
- Improve JupyterHub technology for research through this collaboration
- Minimize toil and maintenance costs for deploying Pangeo-like hubs
- Learn more about the Pangeo deployments and document them so we can replicate them easily
- Make the Pangeo community happy with their collaboration with 2i2c. Convert this into an ongoing relationship of development support.

### Project Information

- Project management: [the `jupyter-earth` repository](https://github.com/pangeo-data/jupyter-earth)
- Meeting notes and updates: [the `jupyter-earth` meeting google doc](https://docs.google.com/document/d/1Od-7_FK1M9kLUkTiSMvAl2tmMwRJEdh-EySCMx5kndg/edit)

(projects:open-source)=
## Open source support

One of 2i2c's core missions is to support open communities and tools that underlie the infrastructure that we deploy. Here we list open source projects that we are devoting particular attention to. This means that "official 2i2c work" can include doing maintenance, feature building, and engagement within these projects / communities.

[Jupyter Book](https://jupyterbook.org)
: An open source tool for building online interactive books in the Jupyter ecosystem. It has uses in both research and education. We are helping lead major development efforts on Jupyter Book in partnership with ANU via a Sloan Foundation grant.

The [JupyterHub project](https://jupyter.org/hub)
: supports a variety of technology projects that facilitate access, customization, and deployment of *shared infrastructure for interactive computing*.

[Jupyter-wide support](https://jupyter.org)
: In addition to the more focused projects listed above, the Jupyter Project also has a variety of project-wide initiatives and communities that we also support. For example, the [community forum](https://discourse.jupyter.org) or the [governance refactoring process](https://discourse.jupyter.org/c/meta/governance/23).