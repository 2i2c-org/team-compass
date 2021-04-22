# Active Projects at 2i2c

Projects are focused work that 2i2c conducts over a long-ish period of time.
They describe the major pieces work that drive our daily activities.

In general, projects should have:

1. A name / description
2. A location where deliverables and tasks are being tracked.

:::{seealso}
For more information about our workflow around projects and deliverables, see [](../practices/coordination.md).
:::

Below is a list of active projects for 2i2c.

## 2i2c organizational launch

As 2i2c is quite young, it must first build an organizational foundation for itself.
This is an ongoing effort to define structure, process, and governance of 2i2c so that it can grow and execute on its mission.

**Tracking deliverables**

There are a few places to track this project:

- [Issues in the 2i2c meta repository](https://github.com/2i2c-org/meta/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc) often contain actionable items towards this project.
- The [organizational projects backlog](https://github.com/2i2c-org/meta/projects/6?fullscreen=true) contains a list of deliverables we are currently working towards.

## Launch of the Managed JupyterHub Service

The Managed JupyterHub Service is an ongoing special project, with the goal of sustaining itself and providing JupyterHub infrastructure to others in research and education.

**Tracking deliverables**

Here's [a link to a table of currently-running hub deployment repositories](https://docs.google.com/spreadsheets/d/1cy10fLUhlXG3M_TLRdqinETQ6h0puEi8ovBYHDTu3Z0/edit?usp=sharing). The issues in those repositories contain the deliverables for each.

In addition, here's a view of that table for quick reference:

<div class="full-width">

```{csv-table}
:header-rows: 1
:file: ../tmp/hub-table.csv
```

</div>

<!-- DataTables to make the table above look nice -->
<link rel="stylesheet"
    href="https://cdn.datatables.net/1.10.24/css/jquery.dataTables.min.css">
<script type="text/javascript" src="https://cdn.datatables.net/1.10.24/js/jquery.dataTables.min.js"></script>

<script>
$(document).ready( function () {
    $('table').DataTable();
} );
</script>


(projects:jmte-pangeo)=
## Pangeo Hub Infrastructure development

The Pangeo project has considerable needs in both operating and developing hub infrastructure for their community.
We are collaborating with them to provide both daily operations of their hubs, as well as help them in evolvin and improving their infrastructure to better-suit their scientific mission.

**Tracking deliverables**

This project is just beginning, and currently does not have a location to track its deliverables.
However, you can find discussion of general Pangeo activity in [the Pangeo repository](https://github.com/pangeo-data/pangeo).

## Jupyter Meets the Earth

Jupyter Meets the Earth is an NSF EarthCube project to develop Jupyter infrastructure in service of the earth sciences.

**Tracking deliverables**

The [`pangeo-data/jupyter-earth` repository](https://github.com/pangeo-data/jupyter-earth) contains deliverables for this project. Look for [the {guilabel}`🏷 JupyterHub` label](https://github.com/pangeo-data/jupyter-earth/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc+label%3A%22%3Alabel%3A+JupyterHub%22).

## Jupyter Book development

The Executable Books Project is an international collaboration to build open source tools that facilitate publishing computational narratives using the Jupyter ecosystem.
Its activities are split across a variety of repositories in the [`executablebooks/` organization](https://github.com/executablebooks).

**Tracking deliverables**

- The [`meta/` repository](https://github.com/executablebooks/meta) contains high-level conversation and strategy in the project. Most project planning and execution is carried out in the issues in `executablebooks/` repositories.
- The [`jupyter-book` repository](https://github.com/executablebooks) contains many issues that are the best place to get started finding things of interest to work on.
- The [`executablebooks` feature voting board](https://executablebooks.org/en/latest/feature-vote.html) contains a table of issues users have "voted" for. It is a good guide for prioritizing work.
