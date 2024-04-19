(support:expected-time-off)=
# Expected time off and downtime

There are some cases when we intentionally reduce our operations and support capacity.
See [](time-off:annual-expected) for our broader policies and support commitments during this time.

(support:expected-time-off:policy)=
## Expected time off support policy

Below is our policy for support during expected time off:

- We monitor our support e-mail for major incidents, but do not guarantee a response for non-essential requests or questions.
  % NOTE: In the future we may define a policy for support if a community knows and
  %   tells us they are doing essential work during expected time off.
  %   We can update this policy when we discuss and make a decision on this.
  %
  %   Some conversation in: https://github.com/2i2c-org/meta/issues/435
- We will take steps to minimize harm and avoid catastrophic problems (e.g. incidents that drastically increase costs), but will not perform non-essential actions. We will assume there is _no essential work happening on any of our hubs for all communities_.
- If there is a catastrophic incident, we will take the minimal number of actions to reduce risk and damage to a reasonable level.
- For non-catastrophic incidents and general change requests, we will wait until _after this period_ to resolve them.

## Support process during expected time off

Here are the steps we take to set expectations for our team and for other organizations during expected time off:

- **One month before the start of time off**. Add footer content to our `support@2i2c.org` and `hello@2i2c.org` responses that communicates our intent.
  See [](freshdesk:footer) for instructions on doing this.

  Example text:

  > **Note:** the 2i2c team will have **expected reduced capacity** from `STARTDATE` to `ENDDATE`.
  > During this time, we will provide operational support for significant cloud incidents and outages, but not for non-essential questions or change requests.
  > We will be less responsive than normal, and will return to answer your questions and resolve issues after the time off.
- **During the time off**. Add an auto-responder to our FreshDesk accounts with a message like the following:

  > **Note:** the 2i2c team is operating at an **expected reduced capacity** until `ENDDATE`.
  > We will provide operational support for significant cloud incidents and outages, but not for non-essential questions or change requests.
  > We will be less responsive than normal, and will return to answer your questions and resolve issues after the time off.

% TODO: In the future, we want to add two extra steps:
%
% 1. Send an e-mail to our mailing list for Community Representatives communicating our intent to be on expected reduced capacity.
%    ref: https://github.com/2i2c-org/team-compass/issues/579
%
% 2. Add a banner announcement to each of our community hubs.
%    ref: https://github.com/2i2c-org/infrastructure/issues/1501

## Rotating team members during expected time off

Because team members continue to serve as support triagers during this time, we should take care to avoid the same person serving in this role across multiple periods of expected time off.
