# enable database engine
vault secrets enable database
# sql command basic
mysql -h XX.XXX.XXX.X -P3306 -uuser -ppass -e "show grants"
mysql -h XX.XXX.XXX.X  -P3306 -uroot -pPassword -e "show grants"
use mysql;
SELECT user FROM user;
#DROP USER 'user1'@'%';
SELECT user FROM user;


# example whec
########################################################################################################################################################################################
# login
export VAULT_ADDR=https://vault.myweb.com
export VAULT_CACERT=./rootCA.crt
vault login token=********

ip=11.179.207.196
port=3306
rootpassword=******
component=component1
region=whec
role=cdb-$component-$region


vault write database/config/$role\
    plugin_name=mysql-database-plugin \
    connection_url="{{username}}:{{password}}@tcp($ip:$port)/" \
    allowed_roles=$role \
    username="root" \
    password="$rootpassword"
vault read database/config/$role



# CREATE ROLE user1 WITH LOGIN PASSWORD Password123
# make sure this file is correctly added, in some shell `bus` will missing
cat > component1.sql << EOF 
CREATE USER '{{name}}' IDENTIFIED BY '{{password}}' ;
ALTER USER '{{name}}'@'%' PASSWORD EXPIRE INTERVAL 1 DAY;
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, INDEX, ALTER ON `bus`.* TO '{{name}}'@'%' ;
EOF

vault write database/static-roles/$role \
    username=$(echo component1 | awk -F '-' '{print $2;}') \
    db_name=$role \
    rotation_statements=@component1.sql \
    rotation_period=86400
    <!-- default_ttl=1h \
    max_ttl=24h -->
vault read database/static-roles/$role

=====
# setup app policy
# use policy database-manage-lease for all k8s cluster role, done in deploy_policies.sh already
 

# Get credentials from the database secrets engine
vault policy write database-cred-$role - <<EOF
path "database/static-creds/$role" {
  capabilities = [ "read" ]
}
# ... 
EOF

# login to permitted user or try k8s vault agent injector example
vault login -method=userpass username=user1 

# get cred
vault read database/static-creds/$role



# manage leases
vault login -method=userpass \
  username=admin \
  password=admin-password
vault list sys/leases/lookup/database/static-creds/$role

LEASE_ID=$(vault list -format=json sys/leases/lookup/database/static-creds/$role | jq -r ".[0]")

vault lease renew database/static-creds/$role/$LEASE_ID

vault lease revoke database/static-creds/$role/$LEASE_ID

vault list sys/leases/lookup/database/static-creds/$role

vault read database/static-creds/$role

vault lease revoke -prefix database/static-creds/$role
# revoke all
# vault list sys/leases/lookup/database/static-creds | xargs -I {} vault lease revoke -prefix database/static-creds/{}

vault list sys/leases/lookup/database/static-creds/$role


# password policy, login as admin required
tee password_complexity_policy.hcl <<EOF
length=20

rule "charset" {
  charset = "abcdefghijklmnopqrstuvwxyz"
  min-chars = 1
}

rule "charset" {
  charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  min-chars = 1
}

rule "charset" {
  charset = "0123456789"
  min-chars = 1
}

rule "charset" {
  charset = "!@#$%^&*"
  min-chars = 1
}
EOF

vault write sys/policies/password/passwordrule1 policy=@password_complexity_policy.hcl

vault read sys/policies/password/passwordrule1/generate

#Re-configure the database secrets engine with the connection credentials for the Postgres database.
vault write database/config/$role \
     plugin_name=mysql-database-plugin \
     connection_url="{{username}}:{{password}}@tcp($ip:$port)/" \
     allowed_roles=$role \
     username="root" \
     password="$rootpassword" \
     password_policy="passwordrule1"


vault read database/config/$role

vault login -method=userpass username=user1 
vault read database/static-creds/$role