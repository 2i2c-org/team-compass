# The 2i2c Handbook

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
people
benefits
sre
projects
```

```{toctree}
:hidden:
:caption: Projects and Strategy
projects
strategy
```

## How to use the handbook

As a general rule, 2i2c team members should document everything relevant to operating the organization in the 2i2c handbook, and give it precedence over all other kinds of documentation unless explicitly stated otherwise in the handbook.

Use it for both high- and low-level things - this book describes the culture, aspirations, operations, and activities of 2i2c at any moment in time. It should have enough information for any newcomer or team member to get up-to-speed with any question they may have about 2i2c.

The handbook should not be the *only* place for information in 2i2c, but it should contain pointers to other sources of truth, updates, etc as needed. For example, it should not contain much project-specific information as this is better suited for project repositories, but it should have information about *where to find* information for any given project.

## This is the source of truth

Any information that is in this handbook should be considered the **source of truth** for 2i2c. Its information should be complete and updated frequently.

If you see information here that is out of date, please propose an edit in [the handbook repository](https://github.com/2i2c-org/handbook).

## Propose a change to the handbook

If you'd like to update information in this book, you can do so via editing the book's source files. These are a collection of markdown files in [the book's repository](https://github.com/2i2c-org/handbook).

Do not hesitate to propose changes to this book - you may do so either via forking and cloning the book's repo, or simply by proposing changes via GitHub's interactive markdown editor.

As a general rule, this book should be updated as open as possible, in order to ensure that its content is accurate and up to date!

## Build the handbook

This handbook is built using Sphinx, along with themes and extensions that are used by the [Jupyter Book project](https://jupyterbook.org). It is hosted via GitHub Pages and changes are auto-deployed via GitHub Actions.

To preview the book locally:

Get your own copy of the book:

```
git clone https://github.com/2i2c-org/handbook
cd handbook
```
Install the requirements to build this handbook:

```
pip install -r requirements.txt
```

Build the book with Sphinx:

```
make html
```

This will build the book using Sphinx, and put HTML outputs in `_build/html`. You can preview them by opening up one of the `.html` files in a web browser.

## Inspiration

This handbook is inspired by several open company handbooks from companies and organizations dedicated to transparency. In particular:

- [The GitLab Company handbook](https://about.gitlab.com/handbook/)
- [The Basecamp Company handbook](https://basecamp.com/handbook)
- [The Valve company handbook](https://steamcdn-a.akamaihd.net/apps/valve/Valve_NewEmployeeHandbook.pdf)
