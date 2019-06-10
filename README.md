# Python & Oracle Autonomous Transaction Processing

This project is a flask api built with Python, Flask and Oracle Autonomous Data Warehouse to be used as a starter template.

## Built with

* [Python 3](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Oracle Instant Client](https://docs.oracle.com/en/cloud/paas/atp-cloud/atpug/connecting-nodejs.html#GUID-AB1E323A-65B9-47C4-840B-EC3453F3AD53)

## Prerequisites

You will need the following:

* [Git](http://git-scm.com/)
* [Oracle Autonomous Transaction Processing Instance](https://cloud.oracle.com/atp)
* [Oracle Instant Client](https://docs.oracle.com/en/cloud/paas/atp-cloud/atpug/connecting-nodejs.html#GUID-AB1E323A-65B9-47C4-840B-EC3453F3AD53)


## Installation

* On Oracle Cloud Infrastructure, spin up a compute instance with the [Oracle Cloud Developer Image on OCI](https://blogs.oracle.com/linux/announcing-the-oracle-cloud-developer-image-for-oracle-cloud-infrastructure)
** This image comes with the Oracle Instant client and Python, effectively removing the need for a docker image.
* Run `git clone https://github.com/GaryHostt/HubsterDatabase.git`

## Setup

Getting the Autonomous Transaction Processing Wallet files
* Navigate to your ATP instance on the Oracle Cloud Infrastructure Console
* Click 'DB Connection'
* Download the Client Credentials (Wallet)
* Then you have 2 options

1. Unzip the wallet, copy the multiple files within the wallet and place them in a directory in this project /HubsterDatabase/wallet/network/admin
2. If you are trying to configure this for a compute instance running in the cloud:

###You need to add your wallet to instant client directory

sudo find . -wholename "*/network/admin*"
./usr/lib/oracle/18.3/client64/lib/network/admin
./usr/lib/oracle/18.3/client64/lib/network/admin/README
./usr/lib/oracle/18.5/client64/lib/network/admin
./usr/lib/oracle/18.5/client64/lib/network/admin/README

### To configure compute instance with wallet:
sudo chmod 777 /usr/lib/oracle/18.3/client64/lib/network/admin
sudo chmod 777 /usr/lib/oracle/18.5/client64/lib/network/admin

Sudo scp - r /Users/aamacdon/Desktop/autonomous_coaching/Wallet_AutoDB opc@132.145.172.19:/usr/lib/oracle/18.5/client64/lib/network/admin

Sudo scp - r /Users/aamacdon/Desktop/autonomous_coaching/Wallet_AutoDB opc@132.145.172.19:/usr/lib/oracle/18.3/client64/lib/network/admin


Updating Python API
* Update `app.py` with the ATP credentials
* Or create a passwords.py file in the project directory with your information
* Update the endpoints to pull relevant data using SQL
