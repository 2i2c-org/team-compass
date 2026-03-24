# Validation Guide

*Step 7 of the Hub Rollout Process*

## Your Role

You built the hub. Now you need to confirm the community can actually use it. Validation is the gate between "deployed" and "delivering value." Your job is to verify real users are accessing the hub and determine whether the rollout is complete or needs more work.

## What You Need to Do

### Confirm community representatives can log in

Start with the people you've been working with directly. They should be your first testers.

- Share the hub URL and confirm they can authenticate using the configured method.
- Have them verify they can access the expected environment (correct software stack, storage, resource profiles).
- Ask them to flag anything that doesn't match what was agreed in the technical plan.

### Verify broader community access

Representative access isn't enough. You need evidence that the hub works for regular users, not just the people who helped design it.

- At least **5 community members** (including representatives) should have successfully logged in and used the service.
- Confirm that authentication works across the user base — not just for admins or power users.
- Watch for access issues that only surface at scale (e.g., institutional SSO edge cases, CILogon group membership problems).

### Make the call

Based on what you see, decide:

1. **Needs more work** → Identify what's broken or missing, loop back to the Needs Assessment step, and update the GitHub issue with new subtasks.
2. **Rollout complete** → The community is receiving value. Confirm this with the community representatives and hand off to BD for ongoing value tracking.

Don't declare complete prematurely. If users can log in but the environment doesn't serve their actual workflow, that's not validation — that's a working front door to an empty room.

## What Success Looks Like

By the end of this step:

- **The community** has confirmed that real users can log in and do meaningful work on the hub.
- **You** can confidently say the hub delivers what was promised in the technical plan — or you know exactly what still needs to be done.
