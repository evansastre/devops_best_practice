@Evans Huang 
DevOps Roadmap  

# Programming languages
- Java - Swimlane, DevOps tool, Tekton task
- Python - Tekton tasks, gitlab jobs, automation
- Golang  - CR/CRD, helm template, terraform template
- Shell - general scripting 
- Javascript
- Ruby

# Server Administrator
## Linux/Unix 
- Permission, Log, Shell, DHCP, DNS, SMTP, SNMP, Cobbler, VPN, kernel tuning, 
- OS base image build and downstream application image merchain -- Machine learning scenario
## Windows  
- Group Policy, AD, WDS, WSUS, SCCM, Service, Registry, PowerShell

# Virtualization
- Vmware VShpere
- Hyper-v
- Citrix
- Vagrant
- VirtualBox

# Network 
- TCP/IP 
- Protocols: DNS, HTTP/s FTPm SSL
- Network configuration automation: Netconf, OPENCONFIG, GRPC, GNMI, Jinja
- Cloud network IaC
- VPC, Group Policy, subnet, gateway, VPN, firewall, load balancer

# Observability
- Permission group
- Better interface for development teams to use 
## Monitoring
- Prometheus
- Prometheus Operator and Prometheus Adapter for auto scaling 
- CR/CRD development for supporting customized metrics dealing requirement
- Grafana
- Zabbix
- DataDog
- IaC
- Resource usage monitoring and alerting
- New Relic
## Logging
- ELK
- Graylog
- Splunk

# Security
## The 4C's of Cloud Native security 
- Cloud
IAM, SCP
- Clusters
Kubeconfig role permission
Node instance security, OS level
- Containers
Resource limitation, pod network policy, credential injection 
- Code 
Gitleak, code quality, compliance, OPA(policy as code)

## Key elements 
- Inventory and classification
- Compliance management -- integrate to gitlab CI, FOSS scan
- Network security
- Identity and access management (IAM) security -- role&policy
- Data security
- Workload security
- Vulnerability management -- integrate to gitlab CI, fortify
- Automated investigation and response -- integrate to gitlab CI
- Policy-as-code 
a method of defining and managing security rules, criteria, and conditions through code. It is a way of enforcing security and risk policies programmatically, within a continuous integration / continuous delivery / continuous deployment (CI/CD) pipeline

# RBAC
- LDAP,  SSO, permission mapping to internal platforms 

# Servers
## Web server
- Apache
- Nginx
- Tomcat
- IIS
- Jetty
## Caching
- Redis
- ES
- MemCache
## Database
- NoSQL: Mongo DB, Cassandra, AWS DynamoDB, Google Datastore
- SQL: Oracle DB, MySQL/MariaDB, PostgreSQL, MS-SQL, RocketDB
- DB Deploy: Flyway
DB Deploy process gitops way -- helm chart for version statement, k8s CR drive flyway for action

# Cloud
## Provider
### AliCloud
- IaC ability,  usage of cloud infrastructure resources by cloud provider, one-click onboarding new environment, disaster recovery 
- Build Resource Module & Template 
- git MR as the review process for expanding/shrinking cloud infrastructure
- The test environment should be independent and cleaned up regularly
- Centralized load balancer management, with label/tag
- Generally, resources are divided into project groups
- Regularly clean up orphaned resources
### AWS
### GCP
### Azure
### OpenStack

# Cloud Native
## Cluster management
### Rancher
- IAC
- Cluster template 
- Rotate test cluster weekly
- cost saving, scalability, and flexibility 
- Autoscaling ability, KEDA or original auto-scaling, horizontal and vertical 
- Split clusters 
- Cluster hibernation
- Reserved instance
### Gardener
Alternative as the cluster management tool 

## Service Mesh 
- Istio
- Linkerd
- GRPC
- envoy

## Service Discovery
- Nacos
- Etcd
- consul

## Application Definition and Image Build
- Helm
- KubeVirt
- Kaniko
- Packer
- Skaffold

## Storage
- Rook
- Ceph
- Minio

## Container Registry
- ACR
- ECR
- Docker Hub

# Infrastructure as code
## Server instance Configuration Management 
- Ansible
- Puppet
- Chef
- Saltstack
## Platform Configuration as code
### Gitlab configuration as code 
- Apply branch/tag specification rules
- Manage group/project 
### Vault configuration as code 
- Role
- Policy 
- integrate Engines 
### Datadog configuration as code 
- Dashboard
- Cloud provider integration
- log
- monitor
- security
## Policy as code
- Dependencies
- Code changes
- Business criticality of application
- Sentitive data, significant risk to downtime,
- checkov
- OPA

## Container
- Docker
- Rkt
- LXC
- runC
- CRI-O
- containerd

## Container Orchestrator
- Kubernetess
- OpenShift
- NoMad
- Docker Swarm

## Infrastructure Provisioning
### Terraform/Terragrunt
- Module: Resource types, security rules, label specification 
- Template: resource group binding
### Pulumi/CDKTF
### AWS Cloudformation
### Azure template
### Google Development Manger 
### Boto3 - AWS
### OpenAPI explorer - AliCloud
### Crossplane & ArgoCD - Could be part of OAM 
Module & Template 


# CI/CD
## CI tool
- Jenkins
- Gitlab CI
- Tekton 
- Github Action
- TeamCity
- Travis CI
- Circle CI
- Bitbucket CI
- AWS Code Pipeline
- Google Cloud Build
## Gitlab CI
- CI Library
Build a complete CICD library, the most concise reference for user projects
- Branch Specification/Tag Specification
- GitLab flow, for development and release 
- Project management -- integration with Jira
- Get through the whole link of code quality, build, deploy, testing, security, compliance, and release pipeline
- Standard pipeline template by build type

## CD tool
### ArgoCD
- Continuously deploy
- Gitops
- Observability
- Blue/Green
- Custimization
- SealedSecret
- Helm/Kustomize
- integration with the swimlane system
### Kubevela (OAM)
### Spinnaker
### Weave flux
### Octopus Deploy

## Scans 
- Sonarscan
- Fortify
- black duck
- Checkmarx
- WhiteSource scan
- protecode

# DevOps CLI 
- Context Switch, ops on swimlane
- Git flow specification commands 
- Build, Release 

# Artifact management
- Nexus
- JFrog

# Test Environment System
- automated deployment and release management -- Swimlane system 
- Scenarios of test environment
- SDN, Tag, Label, Kong, Nacos, tenant conception, form routing link
- Monitoring for performance
- Autoscaling for resources allocation 

# Data
## Apollo -- Configuration for Application 
## Vault -- configs & secrets 
- Certification, environmental variables
- Cloud account and DB Credential rotation, enhance security 
- Easy to use, API, yaml definition, k8s injection 
- Time-Limited Temporary Authorization Scenarios

## Flyway -- DB script deploy
## Veloro 
- Disaster Recovery
- Data Migration
- Data Protection

## Use cloud services
- Original data protection method along with cloud infrastructure resource

# Project management 
- Integration of Jira and gitlab
- Best practice for the workflow

# DevOps Princinple
## Cloud and Cloud Native
- Enjoy the benefit of the cloud, and practice the principle
- Keep up with the cloud-native ecology, and find the best technical path

## X as code
### Infrastructure as code 
- servers, databases, networks 
- Terraform, Pulumi, Crossplane
### Configuration as code
- Ansible
- Puppet
### Policy as code
### Security as code
- AWS Security Hub 
- OPA
### Compliance as code 
 - Chef InSpec 
 - Terraform Complianc
### ChatOps as code 
- Hubot
- Lita

## GitOps
### ArgoCD
- Setup ArgoCD 
- For devops team, tekton
- Public components: Certificate manager, Prometheus, Istio, 
- For development teams, application components
- Helm 
- Convert projects to be release with helm chart 
- Monorepo for ArgoCD to manage released component helm chart
### Git-based Workflow

## Automate everything
- self-service
- Reduce manual operations
- Minimize parameters as much as possible
- Event-driven
- Git-based 

## Consider Multi-Tenancy
Use Distributed Software Architectures and Containerization
Grant necessary permission to the user
- Design your policy and role mapping 

## Keep Simple 
- Avoid over-design, the back end can be complicated, keep the user side simple 
-  Embrace open source, extensions and custom development
- Template reuse, clear hierarchical structure
- Write clean code and handle your exceptions
- Release Small and Release Regularly
- Make code easy to roll back and consider using feature flags

## Chaos Engineering
- Hit the weakness of the platform

## Decoupling data and computation
- Immutable infrastructure

## Exploration
- AIOps
