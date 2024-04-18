(engineering:definition-of-ready)=
# Engineering work definition of ready

The engineering team gets many different kinds of work from many different sources. An important question for solving these work items is: _**is something ready to be worked on?**_

Answering this question, requires at least the following information:

- [What kind of work item something is](dor:categorization)
- [Does it have all the information needed for a member of the engineering team to start working on?](dor:ready)
- If it does not, what exactly is the information needed? And who is responsible for providing it?
- Once all the information is provided, is there explicit documentation on what actually needs to be done?

(dor:categorization)=
## Work categorization

The following non-exhaustive initial list of the different kinds of tasks that the engineering team performs during a sprint cycle.

1. [](ready:feature-enablement)
2. [](ready:routine-maintenance)
3. [](ready:new-hub)
4. [](ready:config-change)
5. [](ready:fault-fixing)
6. [](ready:community-review)
7. [](ready:incident-Response)
8. [](ready:routing)

(dor:ready)=
## Definition of ready

The following describes what is the information needed for a member of the engineering team to start working on a specific type of work item.

(ready:feature-enablement)=
### Feature enablement

Some features for hubs require 2i2c engineering effort to be enabled, and usually this is requested via
the support process. Before a feature enablement request is considered ready to be worked on, it must
have the following information:

- [ ] Link to 2i2c documentation on how to enable this feature. This is to be found under
      [infrastructure.2i2c.org](https://infrastructure.2i2c.org) documentation site.
- [ ] Any additional information needed for this specific feature. This should be listed in the 2i2c
      documentation for how to enable this feature.

Functionally, this means that anything that doesn't have an explicit documentation on how to enable it
should not be considered a feature we currently support!

(ready:routine-maintenance)=
### Routine maintenance

These are tasks that must happen on some *predefined cadence* (every month, every quarter, etc).
It's important that these get done **consistently**, so the cadence must be adjusted so we can
in fact consistently do these given our actual capacity.

Before a routine maintenance task can be considered ready to be worked on, it should have:

- [ ] Link to 2i2c documentation that describes the cadence this should be performed in,
      and how it should be done. The latter can just be links to upstream, as often these
      tasks are not 2i2c specific.
- [ ] A time period during which this maintenance should be performed.

(ready:new-hub)=
### New hub

(ready:config-change)=
### Config change

(ready:fault-fixing)=
### Fault fixing

(ready:community-review)=
### Community config change review

(ready:incident-response)=
### Incident response

(ready:routing)=
### Routing