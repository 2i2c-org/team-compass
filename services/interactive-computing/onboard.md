(onboard:index)=

# Onboard a Community

Scenario: A community is at the beginning of an Engagement with 2i2c for **Managed Interactive Computing hub**. This process assumes that the community is starting fresh with 2i2c but this process should also be used when a community is renewing a previous engagement.

Onboarding assumes there is already a Deal in HubSpot with with either the status of 'Contract Admin' or 'Closed Won'.

## Information collected about a community

BD fills in the following fields in the *Community* tab on a Deal in HubSpot:

Propery Label | Description
-- | --
Community Name | one word, will be used to create an machine-readable identifier for naming clusters, accounts, database keys, and other infrastructure internal to 2i2c
Community Long Name | Community Long Name (Long version, full formal name, for display on in public facing webpages )
Community Website | Community's Website URL
Community GitHub Organization  | Community's GitHub organization URL
Community Logo | Community's Logo URL
Community Representatives  | List of individual able to authorizes changes on behalf of this community
Community Context | Notes on community goals and technical contraints

These fields may be already known or discoverable during the sales process. This information is used downstream by the P&S team to accelerate the deployment of infrastructure on behalf of a commuity.

Under 'Community Context', here is information that is useful:

> Community Context questions: (use Markdown formatting)
>
> - Q: What do you want to achieve by working with 2i2c? Can you paint me a picture that describes the future you wish to materialize?(i.e. Do they have an existing image / environment they want us to use? )
>
> - Q: Can you describe this research community more? Is it segmented? Are there archetypes or personas? (i.e. How will users authenticate? If GitHub which GitHub Org or Teams? GitHub IDs of admins?)
>
> - Q: At a high level, what is your community trying to achieve and how open data/compute infrastructure will help advance toward your mission/vision? (i.e. Do they want GPUs? If so, what GitHub team should have access to GPUs? What's the maximum amount of RAM they want users to be able to spin up on the hub?  Default: 30G, generate with deployer generate resource-allocation choices r5.xlarge:4)
>
> - Q: Can you describe the data? Collaborating open science communities orbit around the heaviest objects in their science space -- their data. Where is it? (i.e. Do they have existing data in some cloud region or zone? Our default is AWS: us-west-2)


## Process to deploy a new hub

1. BD Acccount Manager initiates the converstion with the community to define the needs for a new hub.
  - PS engineering should be included in this sync call while we are learning and refining this process.

2. Use the Hub Configurator to capture information about the hub request. Capture additional additional information not in the Hub Configurator as free form notes.  With permission of the community, using Google Gemini to record a transcript of the request gathering meeting with the community.

  - The Hub Configurator is found at https://2i2c.org/hub-configurator

3. BD requests this new hub use the 'Hub Spot Order' workflow. This kicks off an automation that generates a 'BD request type ticket' that PS can then pick up. This automation has been used a few times so far. It is not yest perfect but the way to improve that process is to use it continuously iterate.

4. Follow [](technical-support:update-contacts) to ensure this community is set up in FreshDesk.

5. Once the new hub order is received, PS creates the new hub issue(s)
 - The means creating the New Hub GitHub issues (using the `New Hub Turnup - Setup` templates )
 - Use the information contained in
    - The Hub Configurator link with selections made.
    - HubSpot Deal information (see Community tab from on each HubSpot Deal).
    - Any additional free form notes attached to the Order.
    - The Gemini transcript from the meeting with the community in step 2.
- The ideal is that that there has already been sufficient information collected from the community to proceed without having to schedule a second technical meeting. If information is still missing blocking the creation of the New Hub Turnup issues, then:
    - Contact the community to request the missing information
    - Update the above process to collect this missing information to improve our process.

6. The New Hub Turnup issues are scheduled for the next P&S interation. The hub is deployed and configured.
 - *Bias towards action* and make a reasonable assumption if there is lack of explicit information. If something can be re-configured after deployment that is better to make a choice than blocking the deployment.
 - Once there is hub deployed it will be much easier to show a community what additional information is required and why.

7. The community is notified (via an email sent through Freshdesk) that the new hub is available

8. BD is notified that the hub has been delivered

9. BD confirms value is being received by this community by checking the Grafana [Engagement Details](https://grafana.pilot.2i2c.cloud/d/eb191919-5ca0-40b4-a696-a0415daf7c6a) dashboard. We expect at least 5 non-2i2c sessions of usage to declare that First Value is being received by a community for this new hub. (See [](communityvalue:tfv) for more information.)
