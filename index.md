# The 2i2c Team Compass

This Team Compass is a guide for team members of 2i2c to navigate our organization and community[^team-compass].
It is our team's primary knowledge base.

**The Team Compass is the {term}`Source of Truth`!**

If you see information that is out of date, propose an edit in [the team compass repository](https://github.com/2i2c-org/team-compass).
To propose an edit directly from the documentation, click {fab}`github` -> {fas}`pencil-alt`.

[^team-compass]: For more about the Team Compass itself, see [](operations/team-compass.md).

## Structure of the Team Compass

### Major sections

The team compass is roughly divided into four sections:

- [Organizational documents](index:organizational-documents) are relevant to the entire organization.
  Everything from our mission and values, to our processes for administration.
- [Functional Areas](index:functional-areas) are major focus areas of 2i2c that have their own practices and roles.
- [Managed JupyterHub Service](index:hubs-service) is cross-functional documentation aimed at describing our Managed JupyterHub Service processes.
- [Reference](index:reference) collects reference material, lists, and guides for doing many things across 2i2c.

### Common pages in each section

Each of our top-level sections tends to have one or more of the same four pages:

- **Scope and responsibilities** (`overview.md`) describes the major focus areas and responsibility for this area.
- **Structure and roles** (`structure.md`) describes any formal roles, job titles, and team structures for this area.
- **Workflow** (`workflow.md`) describes how this area coordinates and works with one another.
- **Governance** (`governance.md`) how this area makes decisions, and what roles have decision-making authority if any non-standard structure is used.
- **Strategy** (`strategy.md`) describes the major approach that this area takes towards its work and accomplishing its goals.

Below you'll find a list of the sections in our Team Compass.

(index:organizational-documents)=
## Organizational documents

These documents cover the whole organization and are relevant to everybody at 2i2c.

```{toctree}
:caption: Organization wide
:maxdepth: 2

organization/index
operations/index
people/index
open-source/index
finance/index
product/index
administration/index
```

(index:functional-areas)=
## Functional Areas

Functional areas each have their own leads, goals, and structures.

```{toctree}
:caption: Functional Areas
:maxdepth: 2

leads/index
engineering/index
partnerships/index
```

(index:hubs-service)=
## Managed JupyterHubs Service

2i2c oversees a single major effort, which is building a sustainable service to make interactive computing with open source infrastructure more accessible and scalable.
We act as a cross-functional team around this service, and share many responsibilities and duties.
We document some major aspects of this service in the sections below.

```{toctree}
:caption: Managed JupyterHub Service
:maxdepth: 2
:glob:
projects/managed-hubs/index
projects/managed-hubs/*
List of running hubs <https://infrastructure.2i2c.org/en/latest/reference/hubs.html>
```

(index:reference)=
## Team Reference

Reference and archival information for our teams.

```{toctree}
:caption: Reference Material
:maxdepth: 2
reference/calendar.md
reference/team.md
reference/documentation/overview.md
reference/terminology.md
reference/inspiration.md
```
