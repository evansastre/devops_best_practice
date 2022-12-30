Q: zombie process vs orphan processs
A: An orphan process is formed when it's parent dies while the process continues to execute, while zombie process is a process which has terminated but it's entry is there in the system.



Q: port and pid
A:
linux:
```
netstat -tlp | grep -i http 
netstat -anpe | grep "1234" | grep "LISTEN"
ps aux | grep [pid]
```

windows:
```
netstat -ano  | findstr  "8080" | findstr "LISTEN"
tasklist | findstr [pid]
```

disk space

shows disk space in human-readable format
`df -h`

shows disk usage in human-readable format for all directories and subdirectories
`du -h`  

show kernel version
`uname -r` 


lsof
List All the Open Files Belonging to a Particular Directory in Linux
`sudo lsof +D directorypath`

List All the Open Files Belonging to a Particular User in Linux
`lsof –u username`

List All the Open Files Belonging to a Particular Internet Protocol 
`lsof –i 6`

List All the Open Files Belonging to a Particular File System in Linux 
`lsof /proc`

grep exclude specify work
`grep -vw "word" filename`


Type .sudo route add default gw IP Address Adapter. For example, to change the default gateway of the eth0 adapter to 192.168.1.254, you would type `sudo route add default gw 192.168.1.254 eth0.[3]` You'll be prompted for your user password in order to complete the command.

available interface
`tcpdump -D`

`tcpdump -c 4 -i wlo1 -A`

Docker
docker pid
docker ps 
docker container top <container id / name>

