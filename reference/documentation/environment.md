# Set up a local documentation environment

To create your documentation environment locally, you'll need a **Python environment** as well as **Nox** installed.
If you wish to build Sphinx by-hand without **Nox**, you'll also need to install the dependencies for a given repository.

:::{note}
The easiest way to edit our documentation is to [use GitHub's UI editor](documentation:edit:github).
Setting up your documentation environment locally is not required.
:::

(docs:install:python)=
## Install Python

First, you'll need to install **Python 3**.
The easiest way to do this is by [installing `minioconda`](https://conda.io/projects/conda/en/stable/user-guide/install/index.html).
This will give you a lightweight Python installation on your machine.

## Install `git`

We use [the `git` command line tool](https://git-scm.com/docs/user-manual) to manage "Version Control" for our repositories, and to keep track of changes.
Install `git` locally with the following command:

```shell
conda install -c conda-forge git
```

(docs:install:nox)=
## Install `nox`

Most of our documentation is buildable with [the `nox` automation tool](https://nox.thea.codes/).
This is a lightway way to execute commands in an isolated environment.
It will let you both install the dependencies for your documentation and build it with a single command.

To install `nox`, first [confirm you have installed Python](docs:install:python) then type:

```shell
pip install nox
```

To list all available options to use with `nox`, run:

```shell
nox -l
```

To build documentation locally, run:

```shell
nox -s docs
```

To build documentation with a live server that previews your changes, run:

```shell
nox -s docs -- live
```

### Clear the `nox` environment cache

When you run a job with `nox`, it will automatically install the necessary dependencies for you and place them in a local folder called `.nox`.
This is folder is usually _hidden_, and it contains all of the files needed to run a Nox build.

To delete the environment and force Nox to re-install things from scratch, deleted this folder.
For example, on `*nix` platforms, run:

```shell
rm -rf .nox
```

## Manually install the environment for documentation

Normally, [Nox](docs:install:nox) will handle all of the environment installation for you.
However if you prefer to install the environment manually and runs Sphinx yourself, you may do so.
This differs slightly depending on the repository, but it usually works like this:

1. **Find the environment files for the repository documentation**. These define the dependencies needed to build the documentation. It is usually in a file called `requirements.txt` or `environment.yml`. It is sometimes in `docs/requirements.txt`.
2. **Install the environment for the documentation**. Manually install the dependencies with `pip` or `conda`. For example:

   ```shell
   pip install -r requirements.txt
   ```
3. **Build the documentation with Sphinx**. Finally, you can build the documentation locally with Sphinx using a command like so:

   ```shell
   sphinx-build docs docs/_build/html
   ```

See [the Sphinx documentation](https://www.sphinx-doc.org/en/master/) for more details.
