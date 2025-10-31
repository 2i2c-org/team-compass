# Dedicated and Shared clusters for hubs

## How we approach clusters
Our original architecture used shared clusters (multiple communities on a single cluster) to maximize efficiency of the cloud resources communities use. We've since built in features like Grafana reporting, to help each community monitor cost and usage. Communities can only directly view their Grafana data if they're on a dedicated cluster. 

## Policy for new hubs: 
All new hubs start on dedicated clusters. Any hub deployed in mid-2025 or later will be on a dedicated cluster, giving hub administrators direct access to their own Grafana monitoring

## Policy for existing hubs: 
We recommend moving to dedicated clusters once an institution reaches an amount of usage/spend where they would benefit from more direct access to the data in Grafana, so they can better manage usage and cost. 

Being on a dedicated cluster is desirable but not absolutely necessary. We can share usage details with communities on demand, with a 1-2 day turnaround. 

## Process for migration: 
When we do plan a migration, we actively communicate ahead of time with the community, and plan a time frame for migration that minimizes disruption to their work. 

Currently running hubs on shared clusters have stored home directories. These home directories will need to be migrated from the shared cluster over to the new dedicated cluster, and that transition needs to be carefully planned to minimize impact on users.

We also communicate migration plans to our Business Development team. 

