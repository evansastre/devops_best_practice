CREATE USER  IF NOT EXISTS '{{name}}' IDENTIFIED BY '{{password}}' ;
ALTER USER '{{name}}'@'%' PASSWORD EXPIRE INTERVAL 1 DAY;
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, INDEX, ALTER ON `bus`.* TO '{{name}}'@'%' ;