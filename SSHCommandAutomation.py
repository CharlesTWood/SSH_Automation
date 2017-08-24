# Author: Charles Wood
# ========================
# Prerequisites
#
# Visual C++ Build Tools 2015 (for SSH): http://landinghub.visualstudio.com/visual-cpp-build-tools
# paramiko: easy-install paramiko
#
# This script will run a command in an SSH session and then record the output from the console
# to a text file and then appends a date string to the file for organization purposes

import sys
import paramiko
from contextlib import redirect_stdout
import time

ip = input('Host IP:')
username = input('Username:')
password = input('Password:')
sleep_time = 1
ssh = paramiko.SSHClient()


def main():

    if __name__ == '__main__':
        def login(username, password, host, i):
            print("Trying connection as: ", username)

            try:

                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(host, username=username, password=password)
                print("Connected to %s" % host)
                run_commands()

            except paramiko.AuthenticationException:
                print("Authentication failed when connecting to %s" % host)
                sys.exit(1)

        def run_commands():

            time_string = time.strftime("%Y%m%d-%H%M%S")
            # (stdin, stdout, stderr) = ssh.exec_command('Command_Here', get_pty=True)
            (stdin, stdout, stderr) = ssh.exec_command('ifconfig', get_pty=True)
            type(stdin)
            with open('PDU Log_'+time_string, 'w') as f:
                with redirect_stdout(f):
                    for output in stdout:
                        print(output)

        login(username, password, ip, sleep_time)
main()
