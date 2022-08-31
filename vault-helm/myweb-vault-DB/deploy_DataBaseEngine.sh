## setup

# script for apply all env

function login_vault()
{
# login
    export VAULT_ADDR=https://vault.myweb.com
    export VAULT_CACERT=./rootCA.crt
    read -p "token: " mytoken
    vault login token=$mytoken
}

function password_complexity()
{
password_complexity_rule=$1
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

vault write sys/policies/password/$password_complexity_rule policy=@password_complexity_policy.hcl

# vault read sys/policies/password/$password_complexity_rule/generate
}


function database_config()
{
    role=$1
    ip=$2
    rootpassword=$3
    password_complexity_rule=$4
    vault write database/config/$role \
        plugin_name=mysql-database-plugin \
        connection_url="{{username}}:{{password}}@tcp($ip:$port)/" \
        allowed_roles=$role \
        username="root" \
        password="$rootpassword" \
        password_policy="$password_complexity_rule"

    vault read database/config/$role
}

function creat_cdb_user()
{
    vault write database/static-roles/$role \
        username=$(echo $1 | awk -F '-' '{print "v-"$2;}') \
        db_name=$role \
        rotation_statements=@$1.sql \
        rotation_period=86400
        # default_ttl=1h \
        # max_ttl=24h
    vault read database/static-roles/$role
}

function database_creds_role_readable()
{
    # Get credentials from the database secrets engine
    vault policy write database-cred-$role - <<EOF
    path "database/static-creds/$role" {
        capabilities = [ "read" ]
    }
EOF

    # validate:
    # login to permitted user or try k8s agent injector example 
    # vault login -method=kubernetes username=user1 
    # get cred
    # vault read database/static-creds/$role
}



function main()
{
    input="cdb_bus.txt" 
    # login
    login_vault

    

    while IFS= read -r line
    do
    ip=$(echo $line | awk '{print $1}')
    port=$(echo $line | awk '{print $2}')
    rootpassword=$(echo $line | awk '{print $4}')
    component=$(echo $line | awk '{print $6}')
    region=$(echo $line | awk '{print $5}')
    role=cdb-$component-$region
    cdb_user_sql=cdb-$component
    cdb_user_policy=cdb-$component
    password_complexity_rule="passwordrule1"

    #set password_complexity
    password_complexity  $password_complexity_rule

    # write database config
    database_config $role $ip $rootpassword $password_complexity_rule

    
    #create cdb user
    creat_cdb_user $cdb_user_sql
    
    # use policy database-manage-lease for all k8s cluster role, done in deploy_policies.sh already

    #add database_creds_role_readable policies
    database_creds_role_readable


    done < "$input"
}



main

# echo "" > vault_DB.sh && vim vault_DB.sh 