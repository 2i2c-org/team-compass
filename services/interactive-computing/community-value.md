(communityvalue)=

# Community Value

We want ensure that our communities are receiving **value** from our interactive community service.  Our proxy for measuring that value is multiple members of a community are actively logging in and engaging in interactive sessions.

We measure MAUs (Month Active Users) as the number of account that have *logged in* to JupyterHub in the preceeding 30 days but this is not equivalent to the number of users who have started and engaged in an interactive sessions. As well, we want to ensure that value is being delivered to community members and that we are not only measuring activity by 2i2c staff and the community representatives.

A community is *receiving value* if at least five separate, non-2i2c users, have engaged with the platform in the proceeding two week period. 

To measure value, here are two Grafana dashboards that can be used:

## Engagement - Details

[Grafana - Engagement Details](https://grafana.pilot.2i2c.cloud/d/eb191919-5ca0-40b4-a696-a0415daf7c6a)

```{figure} images/engagement-detail.png

Selecte the *cluster* and *hub* in the top left. Adjust the time range (top-right) to the period of interest.

This dashboard shows the number of individual sessions and the total number user used by each user.  The Images table in the bottom left shows which docker image is is most commonly used for this hub.

```

## Engagement - Summary

[Grafana - Engagement Summary](https://grafana.pilot.2i2c.cloud/d/44d7cc5b-ea43-4c44-98c5-0598693c928b)

```{figure} images/engagement-summary.png
```

(communityvalue:tfv)=

## Time to First Value

We define *Time to First Value (TFV)* for a hub as the number of days between when the hub request was made to P&S and at least five separate, non-2i2c, account have engaged in an interactive session.