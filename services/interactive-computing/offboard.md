(offboard:index)=

# Offboard a Community

Assuming an engagement has not been renewed, here is a process to gracefully offboard a community from the Mangaged Interactive Computing Service.

1. 60 days before the end of an engagement BD initiates a renewal process to determine if the community wants to continue with a the Managed Interactive Computing Service.
   - _Each engagement needs to have a task defined to make this explicit._

2. If the community decides to end the service, continue this process.

3. 2 weeks before the end of the engagement, email the Community Representatives (CRs) that 2i2c is planning process of shutting down their hub.
   - Use FreshDesk to send out email:
     - Click {guilabel}`New ticket`.
     - Choose at least one community representative as the **Contact**.
     - Select the {guilabel}`Offboard a Community` ticket template.
     - Click {guilabel}`Create`. This creates a ticket without notifying the community.
     - Follow the instructions in the body of the created ticket.

4. 2 days before the date of decomissioning, a reminder email should be sent to the CRs confirming that we intended to shut down the hub. If we have not already received confirmation that the user data has been migrated off, we should seek that confirmation in this email.

5. Delete the hub(s). Follow https://infrastructure.2i2c.org/hub-deployment-guide/hubs/delete-hub/#delete-a-hub for the steps.

6. Email the CRs confirming that the hub has been deleted. The FreshDesk ticket can be marked as closed. If the community responsed it will be automatically reopened.

7. Finalize and record the Cloud Billing and MAUs usage. Costs incurred up this point can be allocated to the community. Cost incurred after this point need to be covered by 2i2c.

8. Delete the cluster.
   - Before deleting the cluster, verify that `federated-prometheus` has the MAU data for the hubs that are being deleted for the full duration of the engagement.
   - Removing the cluster also removes the data for support services such as Grafana and Prometheus.
     % - _Add a link to infrastructure docs to delete the cluster_

9. If applicable, close the cloud provider account.
   - For AWS: The cloud billing data is retained in the `2i2c-sandbox account`. See https://infrastructure.2i2c.org/howto/budgeting-billing/bill/#get-a-community-dedicated-aws-accounts-s-costs
   - For GCP: The cloud billing data is the `2i2c Billing` account. See https://infrastructure.2i2c.org/howto/budgeting-billing/bill/#get-a-community-dedicated-gcp-projects-costs

The community has been offboarded from the Managed Interactive Computing Service.
