(operations:activity-log)=
# Activity log

We keep a log of the work we do for our communities in [Asana](https://app.asana.com/).
Its purpose is to understand where our effort goes and to generate reports for team members, communities, and funders.

Each activity records:

- **What we did** - a short task title and description.
- **Effort in hours** - see [](#activity-log:time-fields).
- **The type of action** - mapped to our major areas of work: delivery, operations, connecting, and stewardship.
- **Who it was for** - the contract, consortium, or member group the work supported.

(activity-log:how-to-log)=
## How to log activity

There are two ways to log activity.
Use whichever fits your workflow, but log a given task in only one of them so hours aren't double-counted.

### Via GitHub (automatic sync)

Best if you're already tracking the work in a GitHub issue.

- Label the issue with one of the sync labels, like `asana-sync`. The [data-sync repository](https://github.com/2i2c-org/data-sync) has the current list of labels.
- A [data-sync automation](#operations:data-sync) creates a matching Asana task and syncs the title, description, assignee, `GitHub Hours`, and status one-directionally from GitHub to Asana. **Changes you manually make in Asana are overwritten**.
- Sub-issues sync automatically as sub-tasks; you don't need to label each one.
- Close the issue as **Completed** to mark the Asana task done. Closing it for any other reason (Not planned, Duplicate) *removes* the Asana task, since the work wasn't delivered.

### Directly in Asana

Best for logging work retroactively, or work that isn't tied to a GitHub issue.

- Add a task to the **Activity Log** project in Asana.
- Link the engagement the work supported in the task's project column.
- Set the action type, and log your time in `Actual time` (Asana's built-in timer works well).

(activity-log:time-fields)=
## Time fields

Tasks share a standard set of time fields, and `Total Time` adds them up:

- `Actual time` - time logged directly in Asana, for work not tracked in a GitHub issue.
- `GitHub Hours` - hours logged on the linked GitHub issue, synced automatically. Don't edit it in Asana; the sync overwrites it.
- `Total Time` - `GitHub Hours` plus `Actual time`. This is the figure we report against an engagement.
- `Estimated time` - hours a task is expected to take, used for planning.

(activity-log:time-principles)=
## Principles for logging time

- **Count hours per person.** If two team members attend a 1-hour meeting, log 2 hours total.
- **Include the work around the work.** Preparation, follow-up (like writing a summary), and code review from other team members all count for time.
- **Be generous.** People tend to underestimate how long a task takes. Account for context-switching and the on/off-ramp around the task itself.
- **Times are best effort.** Use reasonable judgement rather than trying to account for every minute.
