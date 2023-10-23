# Wargame

## Online Digital Mediation Tool

### About

### Architecture

**Architecture**: Cloud Native Layered / N-Tier Architecture

**Hosting**: The application is currently hosted on [Google App Engine](https://cloud.google.com/appengine) Google Apps Engine. App engine offers competitive [free quotas](https://cloud.google.com/appengine/quotas#Instances) and [extra charges](https://cloud.google.com/appengine/pricing#app-engine-pricing) if the quota is exceeded. It is highly scalable and will be more than enough to start off with to design a MVP. Independent hosting can be managed in a later stage.

**Security**: The Backend and Frontend are currently only accessible to rnd1@lugarit.com. A security plan will need to be identified and associated to the N-Tier Architecture.

**Language**: Python (Standard environment language) + Flask + Jinja + HTML + JavaScript + CSS. Custom script will initially be designed in house and commissioned in a latter stage to external consultants in such a way that the general Architecture stays protected.

**Off the Shelf Software**: It is inevitable to use custom coding to develop an MVP and/or clickable prototype. However, the software will initially rely heavily on external libraries and software. This includes the use of Open Source code and APIs:

**APIs**: (Application Programming Interface) Most APIs have interesting free quotas. We shouldn't need to worry about extra charges for a MVP.

- Zotero API
- Zoom API
- Google Calendar API
- Google Drive API
- Google Storage API

**Database Design**: The application currently runs off of Excel, but we will need to quickly migrate to a more sustainable solution such as Postgres or SQL. This will include extra charges and will need to be handled carefully. This needs to be orchestrated carefully with the rest of the data management strategy.  
