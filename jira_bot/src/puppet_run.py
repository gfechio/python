import paramiko
import sys

import send_email

def put_file(machinename, username, password, dirname, filename, data):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(machinename, username=username, password=password)
    sftp = ssh.open_sftp()
    f = sftp.open("/etc/squid/blacklist", 'r')
    checked = check(f, data)

    if str(checked) == "OK":
        sys.stdout.write("Opening file -> /etc/squid/blacklist \n")
        f = sftp.open("/etc/squid/blacklist", 'a')
        f.write(data)
        f.close()
        ssh.close()
        return "OK"

    else:
        ssh.close()
        return str(checked)

def send_file(machinename, username, password, dirname, filename):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(machinename, username=username, password=password)
    sftp = ssh.open_sftp()
    f = sftp.open("/etc/squid/blacklist", 'r')
    send_email.send_email(f.read(data))

def kick(machinename, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(machinename, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command('puppetize"')
    ssh.close()

def check(filename, url):
    datafile = filename.read()

    if url in datafile:
        sys.stdout.write("URL already blacklisted\n")
        return "NOK"

    return "OK"

def rollback(machinename, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(machinename, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command('sudo puppet agent -t ')
    sys.stderr.write("Rolling Back, problems testing\n")
    print stdout.read()
    exit_status = stdout.channel.recv_exit_status()

    if exit_status == 0:
        ssh.close()
        return "OK"
