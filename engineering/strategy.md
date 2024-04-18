# Technical strategy

We make a few base assumptions about the kind of infrastructure we will focus on in this pilot.
Here are several major components.

## Where to deploy the infrastructure

We'll focus our deployments on **major commercial cloud providers**.
These are the most likely places for organizations to want to run cloud infrastructure, and are the most scalable and sustainable.
In addition, getting Jupyter infrastructure to run well on all of the major cloud providers will have a large impact on a community's right to replicate.

We'll focus on the following cloud providers:

- Google Cloud
- Amazon Web Services
- Microsoft Azure

In the short term, we favor deploying hubs on Google Cloud Platform.
This is because GCP has the most stable Kubernetes offering of all of the cloud providers.
We follow {external+infra:ref}`team guidelines for when to deploy new Kubernetes clusters <cluster:when-to-deploy>`.
For new hubs that don't require their own Kubernetes cluster, we plan to run them on Google Cloud until our team has capacity to run more infrastructure across Azure and AWS.

## Why Jupyter and JupyterHub?

- The Jupyter ecosystem is a collection of building blocks that are highly customizable and composable. They are popular and useful for many use-cases, but still require expertise to customize for a particular need. This is well-suited for 2i2c's skillset and the kind of service it wishes to provide.
- Jupyter is a community-led and multi-stakeholder ecosystem that aligns well with 2i2c's commitment to vendor-agnosticity and the [Right to Replicate](https://2i2c.org/right-to-replicate/).
- JupyterHub allows you to access centralized infrastructure for a community, but in a way that gives that community a lot of control over the details. It is a good balance between "SaaS" and "Fully bespoke community infrastructure". JupyterHub can be deployed via a single repository, but is also deployable by individual people or communities, providing them a clear off-ramp.

## Deployment and operations strategy

Our goal is to provide a service that minimizes infrastructural complexity while providing JupyterHubs that can be used my Communities of Practice independently of one another.
We wish to minimize the amount of engineering labor needed to develop and operate these deployments.
Below are a few major aspects of the service that we believe provide a good chance of accomplishing these goals:

- Deploy independent JupyterHubs from a centralized deployment system
- Use Terraform to build Kubernetes clusters on cloud providers, and Kubernetes as a base to run the actual JupyterHub infrastructure.
- JupyterHubs should be pre-configured for a use-case, but customizable by the community
- JupyterHubs will respect the Community's [Right to Replicate](https://2i2c.org/right-to-replicate/)
- JupyterHubs may be more bespoke than is sustainable provided we can learn from them.
- JupyterHubs should be able to connect with external datasets and services, as the community needs.
- JupyterHubs should be customizable by the communities they serve, ideally without intervention from a 2i2c Engineer.