# Needs Assessment Guide

*Steps 4–5 of the Hub Rollout Process*

## Your Role

You are the engineer assigned to this community. BD has closed the contract and you have context from the sales engineering call. Your job is to confirm what this community actually needs and turn that into an executable technical plan.

## What You Need to Do

### Confirm and validate requirements

Start from what the sales engineer learned, but verify it directly with the community. Things shift between "interested" and "signed contract."

- Review the sales engineering notes. What was promised? What was left open?
- Reach out to the community (sync or async) to confirm their priorities and fill any gaps.
- Watch for scope that has grown, shrunk, or changed since the sales conversation.

### Pin down the technical specifics

Walk through each of these with the community. Don't assume — ask.

- **Environment**: What software stack do users need? (Python/conda, R, Julia, custom Docker images?)
- **Resources**: What compute profiles? (CPU/RAM tiers, GPU access, shared vs. dedicated storage?)
- **Data access**: Do users need to reach external data sources, object storage, or institutional systems?
- **User management**: Confirm auth method and understand admin needs — who manages users, who can see what?
- **Usage patterns**: Is this a semester course with predictable spikes, an always-on research lab, or something in between?

### Propose the technical plan

Translate the community's needs into a concrete plan. This is where you apply 2i2c's platform knowledge.

- Map requirements to 2i2c's supported configurations. Flag anything non-standard early.
- If requirements conflict with platform capabilities, propose alternatives — same XY problem mindset from the sales call, but now with more detail.
- Share the plan with the community for sign-off before writing any issues.

### Write the GitHub issue

Create a **New Hub Deployment** issue (or equivalent) that captures the full plan. This is your handoff to execution — it should be self-contained.

The issue should include:

- **Community context**: Who they are, what they're trying to do, and any relevant constraints.
- **Technical decisions**: Cloud provider, auth method, environment specs, resource profiles.
- **Subtasks**: Break the work into discrete, actionable items (e.g., configure auth, build custom image, set up storage, test with community admin).

Each subtask should be something an engineer can pick up and complete independently.

## What Success Looks Like

By the end of this step:

- **The community** has reviewed and agreed to the technical plan.
- **The GitHub issue** is ready to execute — an engineer unfamiliar with the community could pick it up and know exactly what to build.
