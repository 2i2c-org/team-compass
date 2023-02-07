# Workflow

% We are still working out the workflow of the Partnerships team at 2i2c.
% Check out these issues for some conversations around this:

% - [System for planning and coordination](https://github.com/2i2c-org/team-compass/issues/510)
% - [System for leads and contacts](https://github.com/2i2c-org/leads/issues/99)
% - [System for monthly invoicing](https://github.com/2i2c-org/team-compass/issues/355)

## Standard Operating Procedures for Partnerships Business

2i2c provides interactive computing services to partner communities. These notes describe standard operating procedures used by 2i2c and CS&S to establish and cultivate business relationships with partner communities. The workflows orchestrate information exchanges (meetings, emails, negotiations) between 2i2c/CS&S and partners or prospective partners and produce documents (service agreements, quotes, statements of work, renewal notices, invoices, service descriptions, receipts).  

### Arc of Partnership Formation

The procedures describe action sequences our team will carry out as expression of interest in 2i2c evolves through phases Lead --> Prospect --> Partner: 

+ A _Lead_ is a contact with possible interest in a partnership with 2i2c. A lead is _qualified_ when the contact is connected to an organization that can enter agreements with CS&S/2i2c. 2i2c's main goal during the _lead phase_ is to empower the lead to decide whether to partner with 2i2c. The lead phase ends with a "verbal close" `no` or advances to the next phase with a `yes`. 
+ A qualified lead becomes a _Prospect_ after a "verbal close" `yes` to form a partnership. The _prospect phase_ involves two parallel activities: business terms of the partnership are negotiated in the service agreement and accompanying documents; technical exchanges specify details and the requested services are deployed. The prospect phase ends with an "executed close" when the service agreement is fully signed by all parties in the partnership. 
+ A _Partner_ is an organization that has a signed agreement with 2i2c/CS&S.

### Technology Context

2i2c/CS&S use a variety of technologies and subscription services in our overall operation. Personnel involved in supporting 2i2c's leads --> partnerships business processes need to have accounts and appropriate access to these resources. The technologies and servies used in the leads --> partnership procedures are described next: 

#### [Slack](https://2i2c.slack.com)

2i2c uses Slack for asynchronous team communications, often threaded by focus area. Discussions related to partnerships and the workflows described in this section of the Team Compass mostly take place in the `#leads-and-partnerships` channel in 2i2c's Slack. Questions about the implementation of procedures in the leads, prospects, and partnerships phases are likely best posed in the `#leads-and-partnerships` channel in Slack. 

#### [FreshDesk](https://2i2c.freshdesk.com)

2i2c uses FreshDesk ([https://2i2c.freshdesk.com](https://2i2c.freshdesk.com)) to manage leads and support requests. FreshDesk's ticketing system is used to track information exchanges around a particular lead or support request. FreshDesk's canned messaging support is used in some of the standard operating procedures described below.  

#### Google Drive

2i2c uses Google Drive and Google docs to process and store business documents. Most of the procedures described below involve action sequences that affect the `Partnerships` folder inside the `2i2c Team Drive`. Some of the procedures take place inside the `2i2c + CS&S Shared Drive`.

An exploded tree-view of the Partnerships folder:

```
2i2c Team Drive
|
|---Partnerships/ 
    |---Agreements/
        |---PartnerX/
        |---PartnerY/
        |...
    |---Assets/
        |---service description documents
    |---Invoices/
    |---Templates/
        |---[Template] -- service agreement
        |---[Template] -- Running - Notes - PartnerX + 2i2c
        |---2i2c-CS&S stationary template
    |---Running Notes -- 2i2c + CS&S
```

#### GitHub

2i2c uses GitHub to manage code and infrastructure with version control. 2i2c and partner communities collaborate on managed services, software development, documentation, and sharing of responsibilities using GitHub issues. 

Infrastructure services operated by 2i2c are managed through the [infrastructure repository](https://github.com/2i2c-org/infrastructure/). Technical exchanges leading to the deployment of new hubs for partner communities mostly take place in [issues in the infrastructure repo](https://github.com/2i2c-org/infrastructure/issues). 

#### AirTable

CS&S uses AirTable to process and store tabular data. Invoices and executed agreements with 2i2c's partners are stored and processed by CS&S using AirTable. 

#### DocuSign

CS&S uses DocuSign to execute agreements using digital signatures gathered from signatories to agreements between 2i2c/CS&S and partner organizations. 

### Lead Phase Procedures

#### SOP: Hail the Lead

A member of the 2i2c Partnerships Team sends an email to partnerships@2i2c.org requesting `Hail the Lead` action for **contact(s) with email addresses**. This message creates an issue in FreshDesk that will be used to track the lead as it progresses through the arc toward a singed partnership agreement.  2i2c's Partnerships Assistant carries out this action sequence:


1. Send Canned Response "Hail the Lead" from FreshDesk to contact email(s):
Start Email text:  
Hello!

Thank you for your interest in learning more about 2i2c. Please find a service description with pricing information attached to this email. If you have questions or wish to connect for a conversation, reach out to us by email using partnerships@2i2c.org or [schedule a virtual meeting by clicking here](https://calendly.com/colliand/25-minute-zoom-meeting). 

Best regards, 
2i2c's Partnerships Team
End Email text.
2. Change `From` field to `partnerships@2i2c.org`.
3. Add cc: partnerships@2i2c.org
4. Confirm that service description has been automatically attached
5. Confirm canned response includes a meeting invitation with 30 minute Calendly link

#### SOP: Running Notes for First Meeting with Lead

A lead confirmed an upcoming meeting with 2i2c. Calendly sends an automatic message with Zoom link to the contact and enters a calendar booking into Partnerships Lead's calendar. Partnerships Lead forwards email with meeting details to partnerships@2i2c.org triggering the following actions script:
 
1. Partnerships Lead specifies that the lead will be tracked under "PartnerX" (usually the name of the partner organization)
2. Create PartnerX folder inside 2i2c Team Drive >> Partnerships >> Agreements >> `PartnerX`
3. Copy 2i2c Team Drive >> Partnerships >> Templates >> [Template] Running Notes into PartnerX folder.
4. Rename [Template] -- Running Notes... to `Running notes -- PartnerX + 2i2c` (with PartnerX replaced by name of partner organization).
5. Replace `PartnerX` by partner name in the title of the running notes document.
6. Set sharing of running notes file (with editor rights) with lead contacts (meeting participants); Send message from Google notifying the availability of the shared running notes file. 


#### SOP: Meet with Lead

2i2c Partnerships and Community Teams will develop improved procedures for initial meetings with leads.

+ Answer questions
+ Right to replicate
+ Demo?
+ Target: "verbal close"
+ Forecast upcoming procurement/negotiation and technical/deployment stages
+ Record notes and exchanges in Running Notes file

### Prospect Phase Procedures

#### SOP: Send Draft Contract

A member of 2i2c Partnerships Team sends email to partnerships@2i2c.org requesting `Send Draft Contract` to PartnerX contact email(s). 2i2c's Partnerships Assistant carrys out the following actions script: 

1. Copy 2i2c Team Drive >> Partnerships >> Templates >> [Template] service agreement... into PartnerX folder
2. Replace `PartnerX` names by name of partner organization in draft service agreement
3. Remame [Template file] to `PartnerX - 2i2c - CS&S Services Agreement`
4. Set sharing of service agreement (with editor rights) with lead contacts
5. Add dated entry "YYYY-MM-DD Sent (Draft) Service Agreement as shared Google doc" to PartnerX >> Running Notes... file

#### SOP: Service Agreement Negotiation

2i2c's Partnerships Team works with the Prospect to upgrade the draft services agreement into an executable document that can be signed by all signatories. 

+ Answer questions
+ Negotiate; Adjust text
+ Specify addenda (statement of work; deliverables; ...)
+ Target: get to "ready to sign"

#### SOP: DocuSign Agreement

2i2c's Partnershps Team sends email to fsp@codeforscience.org requesting that the executable agreement be circulated for DocuSigning by all signatories.

CS&S arranges for DocuSign requests from signatories.

### Partnership Phase

#### SOP: Launch Meeting

2i2c's Community and Partnerships Teams will work to specify standard operating procedures for kickoff events to launch partnerships.

#### SOP: Invoicing 

Procedure to be specified better in collaboration with CS&S

#### SOP: Satisfaction Check-In

2i2c's Community and Partnerships Teams will work to specify standard operating procedures for checking in with partners.

#### SOP: Renewal Tickler System

2i2c's Community and Partnerships Teams, in collaboration with CS&S, will work to specify standard operating procedures for managing renewals of partnerships.



