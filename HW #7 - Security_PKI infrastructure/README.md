# PKI Infrastructure and TLS Certificate Setup

## Overview
This repository documents the process of designing and building a PKI (Public Key Infrastructure) that includes a Root CA (Certificate Authority), a Signing CA, and a TLS (Transport Layer Security) certificate. Additionally, it details using the TLS certificate to install and configure a web server, specifically Apache Tomcat.

## Steps Summary

### Step 1: Creating Root CA
- Cloning the repository and setting up the necessary directories for Root CA.
- Initializing the database and generating the Root CA's private key and CSR (Certificate Signing Request).
- Self-signing the Root CA certificate.

### Step 2: Creating and Setting Up the Signing CA
- Creating directories for the Signing CA and initializing its database.
- Generating the CSR for the Signing CA and signing it to create the Signing CA Certificate.

### Step 3: Creating the TLS Certificate
- Generating the private key and CSR for the web server.
- Signing the web server's CSR with the Signing CA.
- Converting the TLS Certificate to PKCS#12 format.

### Step 4: Configuring Apache Tomcat for HTTPS
- Modifying the `server.xml` configuration file in Tomcat to enable HTTPS connections.
- Testing the HTTPS connection to ensure proper setup.

## Repository Contents
- Scripts for creating Root CA, Signing CA, and TLS certificate.
- Configuration details for setting up Apache Tomcat with the TLS certificate.

For detailed scripts and configuration steps, please refer to the documentation in the repository: [Security Documentation](https://github.com/joash-muganda/SJSU-CMPE-272-Enterprise-SW-Plat-Projects/tree/main/HW%20%237%20-%20Security_PKI%20infrastructure).


