import paramiko
import threading

# with python module paramiko access to server and check health status of network interface, using multiple thread, structure code in a class

class NetworkMonitor:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password
        self.ssh = None
        self.connected = False

    def connect(self):
        """Connect to the server using SSH."""
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            self.ssh.connect(self.host, username=self.username, password=self.password)
            self.connected = True
        except Exception as e:
            print(f"Failed to connect to {self.host}: {e}")

    def check_interface(self, interface):
        """Check the health status of the specified network interface."""
        if not self.connected:
            print(f"Not connected to {self.host}")
            return
        stdin, stdout, stderr = self.ssh.exec_command(f"ifconfig {interface}")
        output = stdout.read().decode()
        if "UP" in output:
            print(f"{interface} is up on {self.host}")
        else:
            print(f"{interface} is down on {self.host}")

    def check_interfaces(self, interfaces):
        """Check the health status of multiple network interfaces in parallel using threads."""
        threads = []
        for interface in interfaces:
            t = threading.Thread(target=self.check_interface, args=(interface,))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()

# usage example
monitor = NetworkMonitor("192.168.1.100", "user", "password")
monitor.connect()
monitor.check_interfaces(["eth0", "eth1"])
