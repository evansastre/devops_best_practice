# TODO: setup policy and vault authenticate
# refer https://www.vaultproject.io/docs/concepts/policies


# enable users to change own password
# read the mount accessor via `vault auth list | awk '/^userpass/ {print $3}'`
vault policy write userpass - <<EOF
path "auth/userpass/users/{{identity.entity.aliases.auth_userpass_27621967.name}}" {
  capabilities = [ "update" ]
  allowed_parameters = {
    "password" = []
  }
}
EOF

# genral system level admin permission, e.g. allow change policy and allow update policy associate to users 
vault policy write admin-policy - <<EOF
# Create and manage ACL policies
path  "sys/policies/acl" {
  capabilities = ["create", "read", "update", "delete", "list", "sudo"]
}
# allow to update policy associate to users
path "auth/userpass/users/*" {
  capabilities = [ "update" ]
  allowed_parameters = {
    "policy" = []
  }
}
# Read system health check
path "sys/health"
{
  capabilities = ["read", "sudo"]
}
# Manage auth methods broadly across Vault  !!!to validate
path "auth/*"
{
  capabilities = ["create", "read", "update", "delete", "list", "sudo"]
}
path "auth/kubernetes/login"
{
  capabilities = ["create", "read", "update", "delete", "list", "sudo"]
}
path "sys/auth/kubernetes/login"
{
  capabilities = ["create", "update", "delete", "sudo"]
}
# Create, update, and delete auth methods
path "sys/auth/*"
{
  capabilities = ["create", "update", "delete", "sudo"]
}
# List auth methods
path "sys/auth"
{
  capabilities = ["read"]
}
# Manage secrets engines
path "sys/mounts/*"
{
  capabilities = ["create", "read", "update", "delete", "list", "sudo"]
}
# List existing secrets engines.
path "sys/mounts"
{
  capabilities = ["read"]
}
EOF

# ops-admin for managing secret and user password, e.g. allow changes all secrets, and change password for all users
vault policy write admin-secrets-upassowrd - <<EOF
path "secret/*" {
  capabilities = ["create", "read", "update", "delete", "list"]
}
path "auth/userpass/users/*" {
  capabilities = [ "update" ]
  allowed_parameters = {
    "password" = []
  }
}
EOF


###### secrets policy ###### 
# bus admin
vault policy write bus-admin - <<EOF
path "secret/data/bus/*" {
  capabilities = ["create", "read", "update", "delete", "list"]
}
EOF

# root user for bus cdb
vault policy write bus-cdb-root - <<EOF
path "secret/data/bus/bus-cdb-root" {
  capabilities = ["read"]
}
EOF


vault policy write bus-component1-cdb - <<EOF
path "secret/data/bus/bus-component1/cdb" {
  capabilities = ["read"]
}
EOF

vault policy write bus-component2-cdb - <<EOF
path "secret/data/bus/bus-component2/redis" {
  capabilities = ["read"]
}
EOF





vault policy write dbpolicy - <<EOF
path "sys/mounts/*" {
  capabilities = [ "create", "read", "update", "delete", "list" ]
}

# Configure the database secrets engine and create roles
path "database/*" {
  capabilities = [ "create", "read", "update", "delete", "list" ]
}

# Manage the leases
path "sys/leases/+/database/static-creds/readonly/*" {
  capabilities = [ "create", "read", "update", "delete", "list", "sudo" ]
}

path "sys/leases/+/database/static-creds/readonly" {
  capabilities = [ "create", "read", "update", "delete", "list", "sudo" ]
}

# Write ACL policies
path "sys/policies/acl/*" {
  capabilities = [ "create", "read", "update", "delete", "list" ]
}

# Manage tokens for verification
path "auth/token/create" {
  capabilities = [ "create", "read", "update", "delete", "list", "sudo" ]
}

# Create a password policy
path "sys/policies/password/*" {
  capabilities = [ "create", "read", "update", "delete", "list", "sudo" ]
}
EOF

#!!!!!!!!!!!!!
vault policy write database-manage-lease - <<EOF
 # Manage the leases
path "sys/leases/+/database/static-creds/+/*" {
    capabilities = [ "create", "read", "update", "delete", "list", "sudo" ]
}

path "sys/leases/+/database/static-creds/*" {
    capabilities = [ "create", "read", "update", "delete", "list", "sudo" ]
}
EOF



# example for create policy and generate token
# vault policy write user1-policy user1-policy.hcl
# vault token create -policy=user1-policy

# ##### user1-policy.hcl
# path "secret/data/bus/DB/cdb" {
#   capabilities = ["read"]
# }
# path "secret/data/bus/DB/redis" {
#   capabilities = ["read"]
# }