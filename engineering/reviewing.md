(development:merge-policy)=
# Merge and Code Review policy

The sections below describe major policies around merging and reviewing depending on the kind of change being made.
There are some extra policies for changes that **affect actively-running infrastructure**.
See the section below for details.

Not all of them are followed strictly, though some are more important than others, and are marked with **REQUIRED**.

- **Always make a Pull Request**. (REQUIRED).
  All changes to 2i2c repositories should be made via a Pull Request.
  This should be enforced by setting the `main`/`master` branch of each repository to be "protected".
- **PRs should reference (and close) issues**.
  A pull request should almost always be related to an issue.
  Ideally, the issue should be tightly-scoped enough that the PR will close it when merged.
  If you have an idea that *doesn't* yet have an issue, open an issue first and then make the PR to close it.
  This ensures that the team has context around Pull Requests, and a chance to discuss before we implement.
- **Use GitHub's `Request Review` feature**.
  Add specific team members so that it is clear who is needed to review the PR.
- **Be explicit about what feedback you want**.
  When you open a PR, include some language about specific things you'd like feedback with, if applicable.
  This helps others focus their attention.
- **Use the review column on sprint boards**.
  When a PR needs review, move any relevant issues to the {kbd}`Review` column of the active [Sprint Board](coordination:deliverables-backlog) so others notice it.
- **Merge after one approval**.
  If there is at least one approval on a PR, then anybody, including the PR author, may merge the PR.
  PR authors should not hesitate to merge their own PR after an approval if they think it is ready to go!
- **Merging without review is discouraged, but not forbidden**.
  For changes that are minor, very straightforward, and do not affect actively-running infrastructure, it is acceptable to self-merge a PR without getting an approval.  
  If you don't believe that your PR requires an approval before merging, make it clear in your PR or in a comment that you plan to merge it in 24 hours.
- **Leave PRs open for at least 24 working hours**.
  This helps ensure that others on the team have a chance to look at the PR and give their thoughts (by working hours we mean hours during a weekday).


## Policy for changes to running infrastructure

Changing active infrastructure is a bit different from developing technology that is not immediately in production.
As such, we follow some more specific guidelines for these kinds of changes.
See {ref}`infra:infrastructure:review`.

## Policy for team compass changes

If a change affects the 2i2c team policies, or makes significant changes to our documentation or public-facing material, then you should also follow these extra policies:

- **Ensure that the team has consented**.
  For any major change, you should make sure that you have followed best-practices in consent-based decision making. See [](development:decisions) for more information.
