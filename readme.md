# Australia Toilet Data Serverless API

A sample Azure Functions-based API written in Python that uses a MySQL backend database to surface the public toilet dataset. 

This code is used as part of a demonstration on how you can move from running code on Virtual Machines or on-premises, to containers and finally [Azure Serverless](https://github.com/sjwaight/ServerlessDownunderDunnies).

In order to run the code you will need a MySQL database that is populated with the data contained in the [toiletdata_short.csv](https://github.com/sjwaight/PythonAussieDunnyDataAPI/blob/main/toiletdata_short.csv) file contained in the [original implementation repository](https://github.com/sjwaight/PythonAussieDunnyDataAPI). This data is based on the Australian [National Public Toilet Map](https://data.gov.au/data/dataset/activity/national-public-toilet-map) dataset.

See the local.settings.sample.json file for how to get this up and running. You will need to set four App Settings in Azure in order to have the Function connect to the appropriate MySQL database.

Check out Microsoft Australia and New Zealand's cloud developer show [New Breakpoint](https://aka.ms/new-breakpoint/) on which this demo was used (Series 2, Show 9).
