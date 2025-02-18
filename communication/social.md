# Social media

We use social media to signal boost and broadcast 2i2c's impact to the broader community.
Currently, we do not have a dedicated Social Media manager, so the responsibility for managing these accounts is spread amongst the team.

(socialmedia:topics)=
## What to post on social media

We use social media to signal-boost our efforts in 2i2c and upstream communities.
Here are a few things to post:

- Links to blog posts
- Major announcements
- Advertising job posts and other items we want to draw attention to
- Re-tweeting and boosting other team members and their accounts

We don't usually use 2i2c's social media accounts to engage directly with other individuals or organizations, though we encourage individual team members to interact as themselves. 
We have not had the resources to plan extensive social engagement as an organization.

(social:scheduling)=
## Scheduling social media campaigns with AirTable

A social media campaign can be optionally scheduled via the [AirTable Form](blog:airtable-form) to submit content, or the communications team can manually schedule campaigns according to perceived priority. This is scheduled in the *Content* table of the [Content Planning and Scheduling](https://airtable.com/appM2L2x1uglMU0hy?ao=cmVjZW50) AirTable base by checking a box in the *Social media campaign?* field and specifying a *Social media campaign date*.

:::{figure} images/social-airtable-content.png
:alt: Content table with focus on social media fields.
The *Content* table showing the social media fields.
:::

This triggers an AirTable automation to populate the *Campaigns* table, with a row per social media channel ([Twitter](social:twitter), [Mastodon](social:mastodon) and [LinkedIn](social:linkedin)) for each content piece.

:::{figure} images/social-airtable-campaigns.png
:alt: Campaigns table.
The *Campaigns* table automatically populated with 3 social media channels per content piece.
:::

The *Campaigns* table contains the following important fields the the communications team needs to pay attention to:

- Status
- URL

### Status

There are 4 possible states: {bdg-secondary}`Unplanned` (default), {bdg-muted}`Planned`, {bdg-primary}`Scheduled`, and {bdg-success}`Published`. The workflow is as follows:

- When a social media campaign is ready to be executed, it should be marked as {bdg-primary}`Planned`.
- This triggers an AirTable automation that opens a [GitHub issue](https://github.com/2i2c-org/2i2c-org.github.io/issues) in our website repository to track work to schedule on [Buffer](social:buffer).
- Once the post is scheduled, the status can be changed to {bdg-primary}`Scheduled`.
- Once the social media post is published, the communications team should mark the item as {bdg-success}`Published` and proceed to update the [URL](social:url) field.

(social:url)=
### URL

For the purposes of tracking metrics, links to the public social media posts should be recorded in this field for future reference.

(social:twitter)=
## Twitter

Our Twitter handle is ([@2i2c_org](https://twitter.com/2i2c_org)).
Currently, there is nobody actively monitoring the Twitter account.

**How to access**: See [](account:bitwarden).

(social:mastodon)=
## Mastodon

Our Mastodon handle is ([@2i2c_org](https://hachyderm.io/@2i2c_org)).
Currently, there is nobody actively monitoring the Mastodon account.

**How to access**: See [](account:bitwarden).

(social:linkedin)=
## LinkedIn

Here is [our LinkedIn page](https://www.linkedin.com/company/70495902/).
We use LinkedIn roughly the same way that we use Twitter, though focus it more on signal-boosting blog posts and updates because fewer team members regularly use LinkedIn.

**How to access**: We can add **page admins** to our LinkedIn account, which gives others the ability to manage the account and post content.
If you'd like to be added, ask one of [the pre-existing account admins](https://www.linkedin.com/company/70495902/admin/manage-admins/).

(social:buffer)=
## Buffer

This is a productivity tool for posting across our Twitter, Mastodon and LinkedIn channels simultaneously and scheduling social media campaigns with a content calendar.

**How to access**: See [](account:bitwarden).
