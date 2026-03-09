## Internal Details Implementation of CSH (Asana)

We track all all of our engagements in Asana.

When creating a New Membership Engagement, the template comes prepopluated with a `Community Success Hours` task.

After creating the new engagement, Configure the following in Asana:
- Set the 'Community' drop down to the correct community label. Create a new Community label if needed.
- Change the start and end dates for the `Community Success Hours` task to be the same as the start and end dates of the engagement.
- Only if needed, duplicate and create new `Community Success Hours` tasks for different periods within the same engagement. (For example, an engagement may specify 10 hours per quarter of CSH)
- Every `Community Success Hours` tasks also co-owned by a special `Community Success Hours` project.

Each `Community Success Hours` tasks represents the collection of all community success hours tasks listed as sub-tasks.  

## How to track Community Success Hours activity (sync from GitHub, automatic)

- CSH tasks are tracked in the [Product and Services Github Project board](https://github.com/orgs/2i2c-org/projects/57) with the issue label `CSH`. This label is configured for the `infrastructure` and `meta` repositories.
- There are GitHub workflow automations ([csh-sync](https://github.com/2i2c-org/csh-sync)) which automatically copy any open issue marked with the label `CSH` into Asana.  
- Updates to the title, top comment, and hours spent, issue status are automatically updated replicated in Asana.
- This sync is one-directional from GitHub to Asana only. Changing the title, descriptions, or hours spent in Asana will be overwritten by the GitHub issue.
- The workflow checks for duplicates based on the GitHub issue URL.

## How to record a Community Success Hour activity (Asana only, manual)

- Create a new sub-task under the corresponding `Community Success Hours` task






