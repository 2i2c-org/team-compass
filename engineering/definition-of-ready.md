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

(ready:new-hub)=
### New hub

(ready:config-change)=
### Configuration change

This is usually about *modifying* a feature that was enabled via a
[feature enablement](ready:feature-enablement) request earlier. So the definition of ready should
be very similar.

- [ ] Link to documentation about this feature, which has at least some mention of the possible
      ways to make configuration changes. Since 2i2c documentation may not cover all the possible
      options (as that would be too unweildy), this could be either a link to 2i2c documentation on
      [infrastructure.2i2c.org](https://infrastructure.2i2c.org) or a link to upstream documentation
      about various configuration options for this feature.
- [ ] Any additional information needed for this specific configuration change.

Functionally, this means that if we are requested to change config for something that we can't
find any documentation for, we should

(ready:community-review)=
### Community config change review

This should be codified once [this issue](https://github.com/2i2c-org/infrastructure/issues/3912)
is resolved.

(ready:incident-response)=
### Incident response

This should be handled according to our [incident response](support:incident-response) process.

(ready:fault-fixing)=
### Fault fixing

Usually a user reports 'something is not working', but it is not urgent in the same way an
incident response is. These cases are a mix of incident response and configuration change. But
because the timeline pressure of an incident response is not present, these should be handled
exactly the same way as a [configuration change](ready:config-change).