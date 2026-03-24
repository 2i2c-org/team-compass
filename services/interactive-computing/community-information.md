# Community Information

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

These fields may be already known or discoverable during the sales process. This information is used downstream by the P&S team to accelerate the deployment of infrastructure on behalf of a community.

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
