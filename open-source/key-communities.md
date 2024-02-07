---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.13.8
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Key open source communities

Key open source communities are those that align with 2i2c's values and that are central to 2i2c's mission.
They build technology that is essential for the infrastructure that 2i2c offers.

```{admonition} This is not exclusive!
Team members are encouraged to make upstream contributions to communities other than those listed here.
This section just describes the communities to which we devote extra resources and time.
```

## Ways to support key communities

While we try to make upstream contributions wherever we can, we make extra effort to support key communities.
Here are a few examples of this:

- Seek leadership positions within key communities and help guide their strategy and policy.
- Perform ongoing maintenance as part of our 2i2c time (not nights and weekends).
- Put extra time into doing community work and support, not just code.
- Put extra time into reviewing pull requests from others, not just our own.
- Seek funding that we can use to make improvements and give support (see [](open-source:funding))
- Track our efforts in these communities and include them in our self-assessments about impact.

## List of key communities

Currently, the following communities are considered "key communities" for 2i2c.
It is pulled from [this source of truth](data/key-communities.toml).

```{code-cell} ipython3
---
mystnb:
  markdown_format: myst
tags: [remove-input]
---
from tomlkit import parse
from pathlib import Path
from IPython.display import Markdown
with Path("data/key-communities.toml").open() as ff:
  communities = parse(ff.read())["communities"]

communities = [f"- [@{cc}](https://github.com/{cc})" for cc in communities]
communities = "\n".join(communities)
Markdown(communities)
```