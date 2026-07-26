# GitHub repository conventions

This page describes some common conventions and patterns that we follow in our GitHub repositories.

## Documentation

All of our team documentation is built with the [Sphinx documentation engine](https://www.sphinx-doc.org/en/master/).
We use a [shared Sphinx theme](https://github.com/2i2c-org/sphinx-2i2c-theme/blob/main/docs/index.md) across all of our repositories, in order to standardize the look and feel of our docs, and to ensure we have cross-references and navigation links across various documentation sites.
See [the Sphinx 2i2c theme documentation](https://github.com/2i2c-org/sphinx-2i2c-theme/blob/main/docs/index.md) for instructions about how to use and contribute to this theme.

## Issue templates

We use [Issue Templates](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository) to provide helpful prompts for common issues across all of our repositories.
These templates live [in our `.github/` repository](https://github.com/2i2c-org/.github) and are automatically synchronized with several other repositories [with this GitHub Workflow](https://github.com/2i2c-org/.github/blob/main/.github/workflows/sync-issue-templates.yaml).

When you update one of the issue templates in that repository, a PR will automatically be created for the other repositories that are defined in [the `sync.yml` file](https://github.com/2i2c-org/.github/blob/main/.github/sync.yml).
