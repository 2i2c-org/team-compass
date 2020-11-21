# Active Projects

These are active projects that 2i2c is currently working on.

```{note}
Any time that you're asked to give a new email address for something related to your 2i2c work, use your 2i2c email address as a default. For example, if you're adding 2i2c team members as admin users to a hub with Google OAuth, use their 2i2c email addresses.
```

## Starting a new project?

A new project should be created for anything with a specific scope and set of deliverables that spans a reasonably long amount of time (e.g., something that will spawn multiple issues or to-do items). 2i2c projects should all feed into the [2i2c organizational strategy and goals](strategy.md).

When 2i2c embarks on a new project, create a new entry on this page. This will serve as a reference point where 2i2c team members can learn more about the project. Include the following information

We should document the following things:

1. **Summarize the project**. What is the overarching scope and deverables for the project? Who is it in collaboration with?
2. **Define the project's strategic goal**. What is the overarching purpose for working on this project? How does it fit in with the overarching [strategic goals of 2i2c](strategy.md)?
3. **Key Outcomes**. What are some concrete outcomes that we wish to get from this project? What are things we can use to define success?
4. **Project Information** What's the "source of truth" for this project? Where does project management and tracking take place? Where do we track progress? What about to-do items? Where does communication happen around this project? (e.g., in a GitHub repository, in Slack, in a Google doc).
5. **Project Shepherds**. Who ensures that this project is running smoothly, hitting its goals, and unblocking people?

## University of Toronto pilot hub

### Summary
A pilot educational hub for the University of Toronto. It will serve several educators in the university, including both Python and R users. This is a fairly vanilla JupyterHub setup but we will add modest customizations for the Toronto team.

### Strategic Goal
Use this pilot to learn about what needs a large, heterogeneous university like Toronto has, and use this to help build a sustainability model for 2i2c serving [large educational institutions](strategy:education).

### Key Outcomes

- Interviews with U. Toronto users about their experiences on the hub - what went well, what went wrong, etc
- Understanding about how to price educational hubs such as these for large institutions
- Future business with U. Toronto for running hub infrastructure

### Project Information

Project management for this collaboration is in two locations:

- [**The deployment repository**](https://github.com/utoronto-2i2c/jupyterhub-deploy) has further information about these deployments.
- **Microsoft teams**. This collaboration is using the Microsoft Teams account with U. Toronto. If you're working on this deployment, ask for MS Teams access in the Slack.

### Project Shepherds

- Chris Holdgraf
- Yuvi Panda
- Jim Colliander

(projects:hubs-for-all)=
## Hubs for All infrastructure pilot

### Summary
This is pilot infrastructure to minimize the human toil needed to deploy lightweight JupyterHub infrastructure with a standardized computing environment.

### Strategic Goal
The goal of this project is to get 2i2c closer to offering lightweight, "self-serve" hub infrastructure that requires minimal oversight and operation from 2i2c (and thus, lowers 2i2c's costs to providing this infrastructure). It will help make 2i2c hubs more affordable and [usable for smaller educational organizations](strategy:education).

### Key Outcomes

- JupyterHub deployment that is self-serve, can generate multiple hubs in a scalable fashion, meets the majority of educational needs for our users, and requires minimal human intervention.

### Project Information

Project management for this collaboration is in two locations:

- [JupyterHubs deploy repository](https://github.com/2i2c-org/pilot-hubs)
- [Pilot documentation](https://github.com/2i2c-org/pilot)

### Project Shepherds

- Chris Holdgraf
- Yuvi Panda

## Educational self-serve pilots

### Summary

In conjunction with [](projects:hubs-for-all), we are running several pilot hubs for educational institutions that we are connected with. Some of these are via a collaboration with UC Berkeley's Division of Data Science and Society, while others are connections we have made on our own.

### Strategic Goal

The main goal of these pilots is to learn more about how smaller organizations use hub infrastructure for education, as well as to build connections to these institutions to help grow our reach in the educational space.

### Key Outcomes

- Interviews and feedback from hub users about their experiences
- Understanding of the financial perspective of hub users that can feed into a sustainability model for self-serve hubs
- Satisfied users of these hubs that convert into paying hub customers

### Project Information

Most project management for these hubs takes place in the same place as the Pilot Hubs repositories:

- [JupyterHubs deploy repository](https://github.com/2i2c-org/pilot-hubs)
- [Pilot documentation](https://github.com/2i2c-org/pilot)

### Project Shepherds

- Chris Holdgraf
- Yuvi Panda
- Cathryn Carson

## Pan-foo hubs pilots

### Summary

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

All project management and support for this hub is in these two locations:

- [GitHub repository for hub deployments](https://github.com/2i2c-org/pangeo-hubs)
- [Gitter channel](https://gitter.im/pangeo-data/FI-hub)

#### Catalyst Cooperative

The [Catalyst Cooperative](https://catalyst.coop/) is a cooperative consultancy and advocacy group for climate change policy. They curate several large datasets and wish to provide easy interactive computing access to these datasets.

Currently, we are working with this team via the Pilot Hubs, though we expect to move them to a dedicated hub if they wish to pursue the collaboration further.

- [JupyterHubs deploy repository](https://github.com/2i2c-org/pilot-hubs)
- [Pilot documentation](https://github.com/2i2c-org/pilot)

### Project Shepherds

- Chris Holdgraf
- Yuvi Panda

## Jupyter Meets the Earth and Pangeo

### Summary

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

Conversation and deliverables for the Jupyter Meets the Earth grant are in [the `jupyter-earth` repository](https://github.com/pangeo-data/jupyter-earth).

Broader Pangeo conversation and engagement happen in [the Pangeo GitHub repository](https://github.com/pangeo-data/pangeo).

### Project Shepherds

- Ryan Abernathy
- Fernando Perez
- Lindsey Heagy
- Erik Sundell
- Chris Holdgraf
- Yuvi Panda

## Jupyter Book development

### Summary

Jupyter Book is an open source tool for building online interactive books in the Jupyter ecosystem. It has uses in both research and education. We are helping lead major development efforts on Jupyter Book in partnership with ANU via a Sloan Foundation grant.

### Strategic Goal

Jupyter Book has potential uses in both research and educational hubs, and improving the Jupyter Book experience and technology will make it more attractive for users of 2i2c Hubs that wish to use Jupyter Book integrations.

### Key Outcomes

- Achieve the deliverables set out in the original Jupyter Book grant
- Improve Jupyter Book's usefulness for educational or research use-cases
- Learn about how Jupyter Book could be used for research publishing, with the goal of integrating it i nto 2i2c Hubs

### Project Information

Most project discussion takes place in [github repositories in the `executablebooks/` organization](https://github.com/executablebooks) and project-wide conversations and discussion happen in [the `meta` repository](https://github.com/executablebooks/meta).

### Project Shepherds

- Chris Holdgraf
