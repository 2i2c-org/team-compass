# Delivering and logging Community Success Hours

2i2c team members deliver Community Success Hours by:
- Responding to complex support questions, which we track on GitHub.
- Attending and supporting community planning meetings.
- Offering ongoing Slack-based consultation.
- Providing expert guidance on JupyterHub, image management, and open science workflows.
- Supporting grant co-writing and open science governance structures.

Community Success Hours can be proactively recommended to a community by any team member. Most commonly a community asks for help via a FreshDesk ticket or a question in a meeting.

(csh:logging)=
## How to log CSH activity

There are two ways to log CSH activity - use whichever fits your workflow, but log a given task in only one of them (see [](#delivery:tracking-time)):

- **GitHub** - best if you're already tracking work in GitHub (e.g., engineering work). The instructions below show how to set it up to automatically sync the issue to Asana.
- **Asana** - best if you need to log something retroactively or your work isn't tied to a GitHub issue.

Before logging new activity with either method, check that the engagement's `Total Time` has not already significantly exceeded the community's contracted hours.

### Logging via GitHub

- Create a new issue in GitHub.
- Include the community's name and specific contact people for the request; if the request came from FreshDesk, add the FreshDesk link.
- Mark GitHub issues on the P&S Project Board with the label `CSH` to indicate this is Community Success Hours activity.
- A [GitHub automation](#operations:data-sync) will automatically create a corresponding task in Asana. Updates to the title, description, assignee, `GitHub Hours`, and issue status sync one-directionally from GitHub to Asana (changes made in Asana will be overwritten).
- If the issue has **sub-issues**, they sync automatically as subtasks of the Asana task. You don't need to label each sub-issue.
- Close the issue as **Completed** to mark the Asana task done. Closing it for any other reason (Not planned, Duplicate) removes the Asana task instead, since the work wasn't delivered.

### Logging via Asana

- Go to [Active Engagements](https://app.asana.com/0/portfolio/1211914502801258/1211914511709245) in Asana.
- Find the community you're doing CSH for and click it. Find the `Community Success Hours` sub-task for that community.
- Create a new sub-task directly undern the `Community Success Hours` task.
- Log your time on the sub-task with Asana's built-in timer (the `Actual time` field).
- Ignore the other fields (e.g., `GitHub URL` is just for the automated workflow above)

## How to deliver Community Success Hours

- Read any context about the community's problem and questions in the GitHub card.
- Reach out to the community contact to offer your time; that typically requires scheduling a call with the community - sending them your Cal.com link is helpful.
- When you meet or exchange emails, listen to the community contact's problem and offer advice. That can include existing solutions or conversations about future solutions on our [public roadmap](https://2i2c.org/roadmap/).
- After you meet, add notes about any outcome or follow up action to the GitHub card.
- When the task is complete, follow [](#csh:logging).

### Counting hours

- **Hours are counted per-person.** If two staff members attend a 1-hour meeting, log 2 hours total.
- **Include follow-up work** (e.g., writing a summary, drafting a blog post) in the same GitHub issue and add that time to the hours you log there.

## Managing CSH work (Engagement Management and Community Relations)

- Ensure New Engagements are created in Asana
- Validate that CSH tasks are associated with the correct community and correct `Community Success Hours` task.
- Confirm tasks that have been completed but have no time logged (`Total Time` is empty). If needed, estimate the time based on the description of the task.
- Flag communities to BD that are either exceeding or underusing their expected Community Success Hours

## Reporting back to the community (BD)

- Review the list of sub-tasks completed under `Community Success Hours` will be information on the community-specific delivery work that 2i2c has completed.
- Ensure that the `Hours Total` associated with the each `Community Success Hours` task is consistent with any service agreement or contract 2i2c has with a community.
- Communicate with the community about what has been accomplished under Community Success Hours and identify future opportunities.
