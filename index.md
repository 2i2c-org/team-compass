# The 2i2c Team Compass

```{toctree}
:hidden:
:caption: 2i2c Information
about
positions
reference
```
```{toctree}
:caption: Team Information

get-started
practices
sre
projects
```

```{toctree}
:hidden:
:caption: Projects and Strategy
projects
strategy
```

## How to use the team compass

As a general rule, 2i2c team members should document everything relevant to operating the organization in the 2i2c team compass, and give it precedence over all other kinds of documentation unless explicitly stated otherwise in the team compass.

Use it for both high- and low-level things - this book describes the culture, aspirations, operations, and activities of 2i2c at any moment in time. It should have enough information for any newcomer or team member to get up-to-speed with any question they may have about 2i2c.

The team compass should not be the *only* place for information in 2i2c, but it should contain pointers to other sources of truth, updates, etc as needed. For example, it should not contain much project-specific information as this is better suited for project repositories, but it should have information about *where to find* information for any given project.

## This is the source of truth

Any information that is in this team compass should be considered the **source of truth** for 2i2c. Its information should be complete and updated frequently.

If you see information here that is out of date, please propose an edit in [the team compass repository](https://github.com/2i2c-org/team-compass).

## Propose a change to the team compass

If you'd like to update information in this book, you can do so via editing the book's source files. These are a collection of markdown files in [the book's repository](https://github.com/2i2c-org/team-compass).

Do not hesitate to propose changes to this book - you may do so either via forking and cloning the book's repo, or simply by proposing changes via GitHub's interactive markdown editor.

As a general rule, this book should be updated as open as possible, in order to ensure that its content is accurate and up to date!

## Build the team compass

This book is built using Sphinx, along with themes and extensions that are used by the [Jupyter Book project](https://jupyterbook.org). It is hosted via GitHub Pages and changes are auto-deployed via GitHub Actions.

To preview the book locally:

Get your own copy of the book:

```
git clone https://github.com/2i2c-org/team-compass
cd team-compass
```
Install the requirements to build this book:

```
pip install -r requirements.txt
```

Build the book with Sphinx:

```
make html
```

This will build the book using Sphinx, and put HTML outputs in `_build/html`. You can preview them by opening up one of the `.html` files in a web browser.

## Inspiration

This team-compass is inspired by the team compass repositories used across the Jupyter ecosystem. For example:

- [The JupyterHub team compass](https://jupyterhub-team-compass.readthedocs.io/)
- [The JupyterLab team compass](https://github.com/jupyterlab/team-compass)

In addition, it is inspired by several open company handbooks from companies and organizations dedicated to transparency. In particular:

- [The GitLab Company handbook](https://about.gitlab.com/handbook/)
- [The Basecamp Company handbook](https://basecamp.com/handbook)
- [The Valve company handbook](https://steamcdn-a.akamaihd.net/apps/valve/Valve_NewEmployeeHandbook.pdf)
