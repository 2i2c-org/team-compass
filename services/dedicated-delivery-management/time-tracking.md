# Time Tracking

Dedicated delivery may operate within the context of a contract that is billed hourly. In such circumstances, it is important that contributors accurately and consistently report their time spent on delivery associated tasks, such as software development, code review, client management, and planning. In order to keep this process non-intrusive, we employ a simple Asana-based workflow.

## Task Planning

Typically, delivery can be decomposed into a discrete set of tasks, e.g. `Build feature X` or `Meet with client Y`. We can use an Asana Project to enumerate these tasks. Given that Asana can record connections to GitHub, our day-to-day project management tool, it is often useful to define Asana tasks such that they directly correspond to their GitHub counterparts. This simplifies the process of accurately reporting hours by ensuring that the high level task tracking aligns with the practical execution of these tasks on a day-to-day basis.

```{figure} ./images/asana-table.png
:name: fig:ddm-asana-table

A screenshot of the Asana table view for a typical statement of work. The "Estimated time" and "Actual time" columns help to track the expected vs delivered hours. GitHub Issues are l inked directly to subtasks, whilst high-level deliverables are defined as parent tasks.
```

## Time Tracking
To track time spent on delivery (e.g. authoring a pull-request and steering it through code review), we use Asana to track both estimated and actual (delivered) hours. See [](fig:ddm-asana-table) for an example built from our [Canvas Authentication and Authorization statement of work](https://2i2c.org/statements-of-work/sow/canvas-authentication/). Asana tracks time at minute-level granularity. These times should be recorded as best-effort — in practice, the time spent working on task is subject to interpretation and 2i2c team members should exercise reasonable judgement.

```{figure} ./images/asana-timer.png
:name: fig:ddm-asana-timer

A screenshot o fthe Asana timer widget that can be used to help keep track of time spent on particular tasks.
```

Asana ships with a timer widget (see [](fig:ddm-asana-timer) that makes it easy to keep track of time spent on a particular task (just as long as one remembers to pause it!) It can also be useful to make use of timing information like shell history e.g. [`atuin`](https://atuin.sh/) to derive time spent on a task from an auxiliary source of truth.

Anything outside of regular day-to-day 2i2c activities that is associated with a particular community deliverable should be tracked. This includes code-review from other team members, or work around project management in preparation for a meeting.
