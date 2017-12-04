import paramiko
import sys



def run(machinename, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(machinename, username=username, password=password)
    channel = ssh.get_transport().open_session()
    channel.exec_command('sudo /usr/sbin/squid -k parse')
    sys.stdout.write('Validating Squid Syntax\n')

    if channel.recv_exit_status() == 0:
        channel = ssh.get_transport().open_session()
        channel.exec_command('sudo /etc/init.d/squid reload')
	sys.stdout.write("Reloading SQUID\n")
        ssh.close()
        return "OK"

    else:
        ssh.close()
	sys.stderr.write("Something went wrong , Aborting ....\n")
        return "NOK"

