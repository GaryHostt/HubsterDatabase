# Python & Oracle Autonomous Transaction Processing

This project is a flask api built with Python, Flask and Oracle Autonomous Data Warehouse to be used as a starter template.

## Built with

* [Python 3](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Oracle Autonomous Transaction Processing](https://www.oracle.com/database/autonomous-transaction-processing.html)

## Prerequisites

You will need the following things properly installed on your computer:

* [Git](http://git-scm.com/)
* [Oracle Autonomous Data Warehouse Instance](https://cloud.oracle.com/en_US/datawarehouse)

## Installation

* run `git clone XXX`

## Setup

Getting the Autonomous Transaction Processing Wallet files
* Navigate to your ADW instance on the Oracle Cloud Infrastructure Console
* Click 'DB Connection'
* Download the Client Credentials (Wallet)
* Unzip the files and place them in the `wallet` folder in this project

Updating Python API
* Update `app.py` with the ATP credentials
* Update the `api/test` and other endpoints to pull relevant data using SQL

## Running

To run the project locally follow the following steps:

To run the project on a compute instance in the cloud:

## JSON API

The JSON API has sample endpoints to start development
Must configure `app.py` to connect to your Oracle DB and update the SQL query

* `http://localhost:5000/api/version`
(returns current database version)

* `http://localhost:5000/api/test`
(returns data from Oracle DB connection)
