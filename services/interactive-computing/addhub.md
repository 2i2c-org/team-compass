# Adding an Additional Hub to an Existing Community

## Purpose
Describe the process for evaluating and rolling out an additional hub when a community already has an existing hub.

## When this applies
- The community already has at least one hub
- A new hub is requested due to capacity, use case, or operational needs

## Decision questions
The following questions must be answered before proceeding:

1. **Service agreement**
   - Can the additional hub be offered under the existing agreement?
   - Are amendments required?

2. **Engineering / Operations impact**
   - Does this introduce additional ongoing operational load?
   - Are there new reliability, support, or maintenance considerations?

3. **Cloud cost impact**
   - What incremental cloud costs are expected?
   - Who is responsible for these costs?

## Roles and responsibilities
- **Community**: participates in scoping and planning discussions
- **PS**: prepares and executes the hub rollout
- **BD**: informed of changes to number of hubs and scope

## Process overview
1. Community raises request for an additional hub
2. Initial scoping discussion with Community and PS
3. Assessment of operational and cloud cost impact
4. Confirmation of service agreement implications
5. Decision to proceed or not proceed
6. PS rolls out the hub with agreed technical details

## Outputs
- Decision record
- Cost and scope understanding
- Technical information sufficient for PS to deploy the hub


## Example: LEAP additional GPU hub

In the LEAP community, an additional hub was proposed to isolate expensive GPU workloads and allow stricter idle-culling policies without impacting other users.

Key considerations in this case:
- No increase to 2i2c engineering or operations costs
- No material change to the service agreement
- Clear benefit to the community in managing cloud spend
- BD informed of the additional hub as an expansion of support

**Decision:** Proceeded with deploying an additional GPU-focused hub for LEAP under the existing service agreement, as there was no increase to 2i2c engineering or operations costs and clear benefit to the community.

This example illustrates how the process can be applied in practice.

