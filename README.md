# PoC of DASLog: Decentralized Auditable SecurityLogging for UAV Ecosystems

# AWS EC2 Instance Configuration

* In the demonstration, we have fure AWS EC2 instances as blockchain nodes and three AWS EC2 instances as 
Operator (EC2-LS), Data Consumer (EC2-DC) and Data Source (EC2-LG).

##General setting up process of AWS EC2 instance is defined as following:
* Login to `aws.amazon.com`
* Click on `EC2 Dashboard`
* Click on `Launch Instances`
* Select Type `Amazon Linux`
* Select `t2.micro`
* Configure Instance Details
* Create new VPC
* Configure Security Group
  * Add inbound configurations
* Review Instance Launch
* Select `Launch`
* Select a key pair (e.g., RSA)
* Lunch Instance

## Blockchain node instance (bootnode)

In our demonstration, the bootnode should have the below minimum inbound configurations.

| Type | Protocol | Port range | Source |
| --- | --- | --- | --- |
| Custom TCP | TCP | 30303 | 0.0.0.0/0 |
| Custom UDP | UDP | 30303 | 0.0.0.0/0 |
| Custom UDP | UDP | 8545 | 0.0.0.0/0 |
| Custom TCP | TCP | 8545 | 0.0.0.0/0 |
| SSH | TCP | 22 | 0.0.0.0/0 |

## Blockchain node instance (bootnode)

In our demonstration, all other nodes except the bootnode should have the below minimum inbound configurations.

| Type | Protocol | Port range | Source |
| --- | --- | --- | --- |
| Custom TCP | TCP | 30303 | 0.0.0.0/0 |
| Custom UDP | UDP | 30303 | 0.0.0.0/0 |
| SSH | TCP | 22 | 0.0.0.0/0 |

## Installing Hyperledger BESU on blockchain nodes EC2 instances

* `wget https://hyperledger.jfrog.io/artifactory/besu-binaries/besu/21.7.2/besu-21.7.2.zip`
* `unzip besu-21.7.2.zip`
* `sudo amazon-linux-extras install java-openjdk11 -y`
* `sudo ln -s /home/ec2-user/besu-21.7.2/bin/besu /usr/local/bin`

## Installing Truffle on Operator, and Data Consumer EC2 instances
* `curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.34.0/install.sh | bash`
* `. ~/.nvm/nvm.sh`
* `nvm install node`
* `npm install -g truffle`
* `npm install --save @truffle/hdwallet-provider`
# Steps must be done in the Operator, Data Consumer and Data Source components
## Operator
* Copy files and folders in this instance
* Execute bash script `./W_R_Log.sh` in terminal
* From now onwards, the instance waits for the Write and Read requests
 
## Data Source
* Copy files and folders in this instance
### Signing the address of the node that wants to be added as a validator
* Execute bash script `./gen_keypair.sh` in terminal: it generates `public-key.pem` and `private-key.pem` pair for signing and validation process.
* Handover `public-key.pem` to other validators that want to validate this address.
* Execute bash script `./addsig.sh` in terminal: it asks node address and puts the signed address into `Data.sign` file. The new node will give this file to the other validators to validate and add this address to the `accounts-allowlist`.
* In other validators: 
  * Copy `public-key.pem`
  * Copy `addver.sh`
  * Copy `Data.sign` file.
  * Execute bash script `./addver.sh` in terminal: it asks node address and will give the message "verified OK" if valid.
*  add this address to the `accounts-allowlist`.
### Writing process
* Execute bash script `./write_to_LS.sh` in terminal: it sends write request including log records to Secure Logging component and waits for the acknowledgment.
## Data Consumer
* Copy files and folders in this instance
### Reading process
* Execute bash script `./read_from_LS.sh` in terminal: it first sends the token request to Keycloak and then sends the log record read request to the 
Secure Logging component and waits for the log records.
### Verification process
* Execute bash script `./VerifyLog.sh` in terminal: it communicates with blockchain and verifies all records.
 
# Keycloak configuration
Setting up process of Keycloak on AWS RDS is defined as following:
* Run `wget https://github.com/keycloak/keycloak/releases/download/15.0.2/keycloak-15.0.2.tar.gz`
* Run `tar -xvzf keycloak-15.0.2.tar.gz`
* Install java `sudo amazon-linux-extras install java-openjdk11`
* In bin directory run `./standalone.sh -b=0.0.0.0`

# RDS configuration
Setting up process of MySQL database on AWS RDS is defined as following:
* Login to AWS account
* Type “RDS” in the search console and click
* Click on “Create database”
* Choose “Standard create” and “Mysql”
* Create a master username and master password
* Click on create database
* Wait for 5 minutes to open up
* When it is run, be sure that database is located in a VPC that has a security group which accepts traffic to TCP port 3306.
* run `python3 RDS-tables-config.py` to create a database and table.
