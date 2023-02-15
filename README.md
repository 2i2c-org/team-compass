# 2i2c Team Compass

This repository contains the source files for the [2i2c Team Compass](https://team-compass.2i2c.org).
For more information, see [our Team Compass landing page](https://team-compass.2i2c.org).

## Build the team compass locally

The Team Compass is built with [the Sphinx documentation engine](https://sphinx-doc.org).
The easiest way to build the documentation in this repository is to use [the `nox` automation tool](https://nox.thea.codes/), a tool for quickly building environments and running commands within them.
This ensures that your environment has all the dependencies needed to build the documentation.

To do so, follow these steps:

1. Install `nox`

   ```console
   $ pip install nox
   ```
2. Build the documentation:

   ```console
   $ nox -s docs
   ```

This should create a local environment in a `.nox` folder, build the documentation (as specified in the `noxfile.py` configuration), and the output will be in `_build/dirhtml`.

To build live documentation that updates when you update local files, run the following command:

```console
$ nox -s docs-live
```
