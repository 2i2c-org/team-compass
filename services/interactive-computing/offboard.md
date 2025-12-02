(offboard:index)=

# Offboard a Community

Assuming an engagement has not been renewed, here is a process to gracefully offboard a community from the Mangaged Interactive Computing Service.

1. 60 days before the end of an engagement BD initiates a renewal process to determine if the community wants to continue with a the Managed Interactive Computing Service.
  - _Each engagement has a task defined to make this explicit_

2. If the community decides to end the service, continue this process.

3. 2 weeks before the end of the engagement, email the Community Representatives CRs that 2i2c is planning process of shutting down their hub.
  - Use FreshDesk to send out all emails (use Canned Repsonses to standardize those emails *these need to be drafted*)
  - The email should thank the CRs for the opportunity to provide value to their community and summarize statistics on how much usage (e.g. number of users, number of sessions) they community has used.
  - Tell the CRs how much user storage is currrently being consumed by their community.  CRs need to work internally within their community to ensure that the data is backed up or migrated.
  - The community does not need to delete data themselves but is responsible for ensuring the data is backed up and migrated.
  - The email should include specific date then the hub will be decommissioned (recommendation: the day the engagement ends or very soon thereafter)

4. 2 days before the date of decomissioning, a reminder email should be sent to the CRs confirming that we intended to shut down the hub. If we have not already received confirmation that the user data has been migrated off, we should seek that confirmation in this email.

5. Delete the hub(s). Follow https://infrastructure.2i2c.org/hub-deployment-guide/hubs/delete-hub/#delete-a-hub for the steps.

6. Email the CRs confirming that the hub has been deleted.

7. Finalize and record the Cloud Billing and MAUs usage. Costs incurred up this point can be allocated to the community.  Cost incurred after this point need to be covered by 2i2c.

8. Delete the cluster.
  - Removing the cluster also removes the support services such as a the Grafana/Prometheus data.
  - Before deleting the cluster, verify that `federated-prometheus` has the MAU data for the hubs that are being deleted for the full duration of the engagement.
  - _Add a link to infrastructure docs to delete the cluster_

9. If applicable, close the cloud provider account.
  - For AWS: The cloud billing data is retained in the `2i2c-sandbox account`. See https://infrastructure.2i2c.org/howto/budgeting-billing/bill/#get-a-community-dedicated-aws-accounts-s-costs
  - For GCP: The cloud billing data is the `2i2c Billing` account. See https://infrastructure.2i2c.org/howto/budgeting-billing/bill/#get-a-community-dedicated-gcp-projects-costs

The community has been offboarded from the Managed Interactive Computing Service.  
