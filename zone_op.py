#!/usr/bin/env python

import pexpect
import paramiko
import os
import re
import zone_info

def wwn_valid(wwns)
    pass

def zone_create_br(wwns, zone_name, vsan_id):
    ssh = parammiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=x86_br_rep_sw[ip],\
                username=x86_br_rep_sw[user],\
                password=x86_br_rep_sw[pass],\
                port=22)
    # return if ssh failed
    stdin, stdout, stderr = ssh.exec_command("cfgactvshow | grep cfg")
    
    command_line="zonecreate " + zone_name  + wwns

    stdin, stdout, stderr = ssh.exec_command(command_line)

def zone_create_ci(wwns, zone_name, vsan_id):
    pass

def zone_update_br(wwns, zone_name, op):
    pass

def zone_update_ci(wwns, zone_name, op):
    pass

if __name__=="__main__":
    if !(wwn_valid(wwns)):
        print ("wwn format error!")
        return -1

    
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="10.103.117.90", username="root", \
        password="#1Danger0us", port=22)
stdin, stdout, stderr = ssh.exec_command("hostname")
result=stdout.readlines()
print result
ssh.close()


