# Update the team compass

The Team Compass should be updated frequently as information about 2i2c changes.
Do not hesitate to propose a change!
This page contains instructions for how to build the Team Compass locally, and how to update the website.

The Team Compass is built using Sphinx, along with themes and extensions that are used by the [Jupyter Book project](https://jupyterbook.org). It is hosted via GitHub Pages and changes are auto-deployed via GitHub Actions.

## Propose a change to the team compass

If you'd like to update information in this book, you can do so via editing the book's source files. These are a collection of markdown files in [the book's repository](https://github.com/2i2c-org/team-compass).

To do so, you have two options

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
   pip install -r requirements.txt
   ```
2. **Make your changes**. Edit the markdown files in the Team Compass and the content will be updated.
3. **(optional) Preview your changes**. To preview the book locally, build it with Sphinx:

   ```
   make html
   ```

   This will build the book using Sphinx, and put HTML outputs in `_build/html`.
   You can then preview them by opening up one of the `.html` files in a web browser.
