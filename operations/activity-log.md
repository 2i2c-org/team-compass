(operations:activity-log)=
# Activity log

We keep a log of the work we do for our communities in [Asana](https://app.asana.com/).
Its purpose is to understand where our effort goes and to generate reports for team members, communities, and funders.

Each activity records:

- **What we did** - a short task title and description.
- **Effort in hours** - see [](#activity-log:time-fields).
- **Activity Area** - which of our [DOCS service areas](#service-model:docs) describes the work (or, an internal area like `Admin`).
- **Who it was for** - the contract, consortium, or member group the work supported.

(activity-log:how-to-log)=
## How to log activity

There are two ways to log activity.
Use whichever fits your workflow, but log a given task in only one of them so hours aren't double-counted.

### Via GitHub (automatic sync)

Best if you're already tracking the work in a GitHub issue.

- Tag the issue with its {gui}`Activity Area`, in either of these ways:
  - Add a label named after the area, like {gui}`Operate Infrastructure` or {gui}`Connect and Advise`.
  - Set {gui}`Area of Work` on the [Operations board](https://github.com/orgs/2i2c-org/projects/64), or {gui}`Allocation` on the [Product and Services board](https://github.com/orgs/2i2c-org/projects/57). This is the only option for issues in repositories outside `2i2c-org`.

  This will set the {gui}`Activity Area` in Asana as well.[^others]
- A [data-sync automation](#operations:data-sync) creates a matching Asana task and syncs the title, description, {gui}`GitHub Hours`, and status from GitHub to Asana (this is one-directional!). **Changes to most things in Asana will be overwritten**, except the {gui}`Activity Area` and {gui}`assignee`, which you can set in Asana.
- Sub-issues sync automatically as sub-tasks, so you don't need to label each one. They'll generally "inherit" the labels or engagement assignments from their parent.
- Close the issue as {gui}`Completed` to mark the Asana task done. Closing it for any other reason ({gui}`Not planned`, {gui}`Duplicate`) *removes* the Asana task, since the work wasn't delivered.

[^others]: A few other labels trigger the sync too (like `support`, `CSH`, or `asana-sync`); see the [full list in data-sync](https://github.com/2i2c-org/data-sync/blob/main/scripts/issues/README.md).

### Directly in Asana

Best for logging work retroactively, or work that isn't tied to a GitHub issue.

- Add a task to the {gui}`Activity Log` project in Asana.
- Link the engagement the work supported in the task's project column.
- Set {gui}`Activity Area`, and log your time in {gui}`Actual time` (Asana's built-in timer works well).

(activity-log:time-fields)=
## Time fields

Tasks share a standard set of time fields, and {gui}`Total Time` adds them up:

- {gui}`Actual time` - time logged directly in Asana, for work not tracked in a GitHub issue.
- {gui}`GitHub Hours` - hours logged on the linked GitHub issue, synced automatically. Don't edit it in Asana; the sync overwrites it.
- {gui}`Total Time` - {gui}`GitHub Hours` plus {gui}`Actual time`. This is the figure we report against an engagement.
- {gui}`Estimated time` - hours a task is expected to take, used for planning.

(activity-log:time-principles)=
## Principles for logging time

- **Count hours per person.** If two team members attend a 1-hour meeting, log 2 hours total.
- **Include the work around the work.** Preparation, follow-up (like writing a summary), and code review from other team members all count for time.
- **Be generous.** People tend to underestimate how long a task takes. Account for context-switching and the on/off-ramp around the task itself.
- **Times are best effort.** Use reasonable judgement rather than trying to account for every minute.
