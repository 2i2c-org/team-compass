# Workflows

% We are still working out the workflow of the Partnerships team at 2i2c.
% Check out these issues for some conversations around this:

% - [System for planning and coordination](https://github.com/2i2c-org/team-compass/issues/510)
% - [System for leads and contacts](https://github.com/2i2c-org/leads/issues/99)
% - [System for monthly invoicing](https://github.com/2i2c-org/team-compass/issues/355)

These sections describe Standard Operating Procedures (SOPs) around the creation, maintenance, and closure of the **Partnership Lifecycle**.

The table of contents below links to the workflows for various types of Partnerships activities.

```{toctree}
:maxdepth: 2
workflow/hub-service.md
workflow/grants-and-projects.md
```

## Technology Context

2i2c/CS&S use a variety of technologies and subscription services in our overall operation. Personnel involved in supporting 2i2c's leads --> partnerships business processes need to have accounts and appropriate access to these resources. The technologies and servies used in the leads --> partnership procedures are described next: 


### AirTable

We use AirTable as a source of truth for some important information in Partnerships.
See the workflows above for specific examples.

In addition, CS&S stores a record of **all invoices and executed agreements** with 2i2c's partners in AirTable.
See [our Invoices and Contracts section](../finance/contracts.md) for information about this table.

(slack:partnerships)=
### The Partnerships Slack channel

The [`#partnerships` Slack channel](https://2i2c.slack.com/archives/G015W2KSBCP) is for discussions around the partnerships and community lifecycle.
It is primarily used by the Partnerships team in planning, coordinating, and discussing their work.

### [FreshDesk](https://2i2c.freshdesk.com)

2i2c uses FreshDesk ([https://2i2c.freshdesk.com](https://2i2c.freshdesk.com)) to manage leads and support requests. FreshDesk's ticketing system is used to track information exchanges around a particular lead or support request. FreshDesk's canned messaging support is used in some of the standard operating procedures described below.  

(workflow:google-drive)=
### Google Drive

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
    |---Technical Content/
        |---README
        |---ArtifactX
        |...
    |---Templates/
        |---[Template] -- service agreement
        |---[Template] -- Running - Notes - PartnerX + 2i2c
        |---2i2c-CS&S stationary template
    |---Running Notes -- 2i2c + CS&S
```

#### Technical Content

The `Technical Content` folder is a collection of artifacts, such as reports, drafts, or any such piece of technical writing, to be stored in our Team {ref}`Google Drive<workflow:google-drive>` for future reference.

Materials are usually produced as a result of a task within a GitHub issue. Once the GitHub issue is closed, artefacts become difficult to trace. We therefore

- [ ] Store in the top comment of the GitHub issue a link to the artefact stored in the `Technical Content` folder
- [ ] Update the contents of the `README` file in the Google drive to capture the originating GitHub issue and the linked artefact.

Team members looking for technical content are directed to the `Technical Content` folder from here in the Team Compass. 

### GitHub

2i2c uses GitHub to manage code and infrastructure with version control. 2i2c and partner communities collaborate on managed services, software development, documentation, and sharing of responsibilities using GitHub issues. 

Infrastructure services operated by 2i2c are managed through the [infrastructure repository](https://github.com/2i2c-org/infrastructure/). Technical exchanges leading to the deployment of new hubs for partner communities mostly take place in [issues in the infrastructure repo](https://github.com/2i2c-org/infrastructure/issues). 

### DocuSign

CS&S uses DocuSign to execute agreements using digital signatures gathered from signatories to agreements between 2i2c/CS&S and partner organizations. 
