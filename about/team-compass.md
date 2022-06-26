# About the Team Compass

This is about our Team Compass, how to understand and read it, and how to make changes if you need.

## Why have a Team Compass?

There are a few major reasons why we use a Team Compass:

- **Asynchronous coordination**. 2i2c is a distributed organization with team members across the world.
  Some are full-time, some are part-time, some are collaborators that work closely with us.
  Having a {term}`Source of Truth` that is available to all team members helps us stay aligned and prevent information silos from popping up.
- **Transparency**. 2i2c collaborates with many external stakeholders, and wishes to be a model organization for transparent and inclusive organizational dynamics.
  We believe this builds trust and connections with communities we serve.
  The Team Compass is a record of everything we're up to, and how we do it.
- **Provenance**. Almost all organizational decisions are made via edits to the Team Compass, or in documentation that we link to from the Team Compass.
  Because we conduct most discussions in GitHub repositories and issues, we have a historical record of the evolution of 2i2c, as well as provenance behind its decisions.

## What is a Source of Truth

The Team Compass is a {term}`Single Source of Truth`, meaning that it is the definitive answer for questions about 2i2c's policy and state.
Below is a quick definition of "Source of Truth":

```{glossary}
Source of Truth
Single Source of Truth
  Distributed teams and open communities need to balance information across team members, and ensure that everyone is on the same page. For this reason, it is recommended to adopt a "single source of truth" for anything important. This is an authoritative source that everyone can look to in order to know the current status and plan for anything we do at 2i2c[^source-of-truth].
```

[^source-of-truth]: **References for Single Source of Truth**: For a few examples, see [this Bitergia post](https://blog.bitergia.com/2020/08/25/why-ospo-teams-need-a-single-source-of-truth/) and [the GitLab SSOT section](https://about.gitlab.com/handbook/values/#single-source-of-truth).


## How to update the team compass

The Team Compass should be updated frequently as information about 2i2c changes.
Do not hesitate to propose a change!
This page contains instructions for how to build the Team Compass locally, and how to update the website.

The Team Compass is built using Sphinx, along with themes and extensions that are used by the [Jupyter Book project](https://jupyterbook.org). It is hosted via GitHub Pages and changes are auto-deployed via GitHub Actions.

## Propose a change to the team compass

If you'd like to update information in this book, you can do so via editing the book's source files. These are a collection of markdown files in [the book's repository](https://github.com/2i2c-org/team-compass).

To propose an edit directly from the documentation, click {fab}`github` -> {fas}`pencil-alt`.

### Option 1: Use the GitHub UI

The easiest way to propose a change to the Team Compass is by using the GitHub User Interface.
To do so, navigate to the GitHub page for a file that you'd like to edit, and click on the pencil ({fa}`pencil-alt`) icon.

Make whatever changes you like using the GitHub interactive editor, and then click `Create a new branch for this commit and start a pull request.`.
This will create a Pull Request with your proposed changes.

### Option 2: Make the change locally

The other option is to make the change locally on your computer, push it to GitHub, and then propose a Pull Request.
To do this, you should be familiar with `git`.
To do so, follow these steps:

1. **Clone the source files**. First, clone the source files for the Team Compass:

   ```
   git clone https://github.com/2i2c-org/team-compass
   cd team-compass
   ```
2. **Make your changes**. Edit the markdown files in the Team Compass and the content will be updated.
3. **(optional) Preview your changes**. To preview the book locally, build it with `nox`:

   ```
   pip install nox
   nox -s docs-live
   ```

   This will build the book using Sphinx, and put HTML outputs in `_build/html`.
   You can then preview them by opening up one of the `.html` files in a web browser.

(team-compass:structure)=
## Structure of the Team Compass

This team compass is organized into a few major sections.

### Getting started material

Should be a small number of top-level pages that help folks get started with the most important information about 2i2c, assuming they are a newcomer.

### Topic areas

Several top-level sections that roughly map onto **major functional areas** of 2i2c.
There should be no more than around 10 topic areas here.
Each topic area has a number of sub-topics with more information.

### Reference material

Reference material contains factual and more structured information about 2i2c.
It is meant as a quick reference and doesn't go into as much explanation and depth.
