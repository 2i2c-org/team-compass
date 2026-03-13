(technical-support:update-contacts)=

# Add or update community representatives

Scenario: A community has an engagement with 2i2c for **Technical Support**. Community Representative information is missing in FreshDesk.

During the sales or renewal process, BD is asked to associate *Contacts* with each *Community* in HubSpot.

HubSpot is the source of truth for this Community-Contact information. There is a GitHub action (see https://github.com/2i2c-org/hubspot-communities) that run four times a day to sync information from HubSpot to FreshDesk.

If information about Community Representatives (CRs) or Technical Contacts (TCs) is missing or outdated in FreshDesk, we need to update this information HubSpot.

1. Create a new Contact in HubSpot. Key fields: Name, email, GitHubID (if known)
2. Look up the corresponding Community in [HubSpot->Communities](https://app-na2.hubspot.com/contacts/242496330/objects/0-410)
3. Associate the Contact with the Community
4. Add/remove assocation labels (Community Representative, Technical Contact) to indicate the role(s) for this contact in this community.

You can manual sync this information by triggering the [HubSpot → Freshdesk Sync](https://github.com/2i2c-org/hubspot-communities/actions/workflows/sync_community_contacts.yml) workflow action in GitHub.

:::{admonition} Freshdesk Communities and Contacts
FreshDesk has the concept of a 'Company' that can be associated independently with both tickets and contacts. We interpret the 'Company' in Freshdesk to mean the 2i2c Community that is being served.

When a ticket comes into FreshDesk is automatically associated with the Community based on the 'Company' of the Community Representative submitting the ticket.
:::
