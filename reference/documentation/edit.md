# Edit the documentation

2i2c's documentation should be dynamic and constantly changing.
It is important that our documentation reflect our current practices, so that other team members know how to contribute and what to expect.

These sections cover the major ways that you can make edits to our documentation.

(documentation:edit:github)=
## Make edits with the GitHub UI

The easiest way to edit documentation is to use GitHub's user-interface directly.
This will allow you to make changes in your browser, and propose them via a **Pull Request**.

To do so here are some basic steps:

### Navigate to the repository for the documentation you wish to edit

Navigate to the documentation in the repository of your choice.
If the repository is purely for documentation, then our documentation is usually in the root of the repository.
If the repository also contains code, then our documentation is usually in a `docs/` folder.

For example, [the repository for our Team Compass is at this URL](https://github.com/2i2c-org/team-compass).

### Navigate to the file you wish to edit

In the Github UI, open the file that you wish to edit by clicking on it.
For example, [here is the URL for the page you are currently reading](https://github.com/2i2c-org/team-compass/blob/main/reference/documentation/edit.md).

### Trigger "Edit Mode" in the GitHub UI

There is a little pencil icon ({fas}`pencil-alt`) in the the top-right of the page.
Click on it, and it will turn on "editing mode".

### Make your edits

Make edits to the page's markdown as you wish.
For information about how to write MyST Markdown in our documentation, see [](content.md).

### Create a Pull Request

When you're done making your edits, click `Create a new branch for this commit and start a pull request`.
This will create a Pull Request with your proposed changes.

In the Pull Request, give it a title and description that describe the changes you've made.
If the edits are very minor, don't hesitate to merge them yourself (e.g., correcting a typo).
If they are more complex, ping a team member for a review.

## Edit documentation locally

If you are comfortable with or interested in learning Sphinx-based documentation workflows, you can also make changes to documentation locally on your computer, push it to GitHub, and then propose a Pull Request.

:::{admonition} Learn ahead of time
This section assumes you have a basic knowledge of how to use `git`.
See [the Software Carpentry training on `git`](https://swcarpentry.github.io/git-novice/) to learn how to use this tool.
:::

### Set up a local documentation environment

To do so, see [](environment.md).

### Clone the repository source files

First, clone the source files for the repository you wish to edit.
For example, to clone the source files of the Team Compass:

```
git clone https://github.com/2i2c-org/team-compass
cd team-compass
```

### Make your changes

Edit the markdown files in the Team Compass and the content will be updated.
For guidance on how to write MyST Markdown, see [](content.md).

### Preview your changes (optional)

To preview your documentation locally, [see the instructions on installing and using `nox`](docs:install:nox).

This will build the book using Sphinx, and put HTML outputs in an output folder in `_build/`.
You can then preview them by opening up one of the `.html` files in a web browser.

### Push your changes to GitHub and make a Pull Request

Once you've made your local changes, commit them to the repository, push it to GitHub, and open a Pull Request.
