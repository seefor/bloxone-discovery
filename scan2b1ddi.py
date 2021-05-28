#!/usr/local/bin/python3
'''
 Description:
    Discovery for networks to add to BloxOne DDI

 Requirements:
   Python3 with requests,nmap, bloxone,

 Author: Sif Baksh
 Date Last Updated: 20210524
 Todo:
 Copyright (c) 2021 Sif Baksh
 Redistribution and use in source and binary forms,
 with or without modification, are permitted provided
 that the following conditions are met:
 1. Redistributions of source code must retain the above copyright
 notice, this list of conditions and the following disclaimer.
 2. Redistributions in binary form must reproduce the above copyright
 notice, this list of conditions and the following disclaimer in the
 documentation and/or other materials provided with the distribution.
 THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
 FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
 INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
 BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
 ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 POSSIBILITY OF SUCH DAMAGE.
'''
__version__ = '0.1.1'
__author__ = 'Sif Baksh'
__author_email__ = 'sifbaksh@gmail.com'

import nmap
import bloxone
import datetime
import json

nm = nmap.PortScanner()
csp_token = 'csp.ini'

d = {}
def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()
d = datetime.datetime.now()

# Create a BloxOne DDI Object
b1ddi = bloxone.b1ddi(csp_token)
r1 = b1ddi.get_id('/ipam/ip_space', key="name", value="sbaksh-ip-space", include_path=True)

def create_host(address):
    payload = json.dumps({
    "addresses": [
        {
        "address": address,
        "space": r1
        }
    ],
    "tags": {
        "disco_First_Seen": (json.dumps(d, default = myconverter)),
        "disco_Name_of_Scanner" : "Inital Script"
    }
    })
    #print(payload)
    filter = f'address=="{address}" and space=="{r1}"'
    id = b1ddi.get('/ipam/address', _filter=filter).json()
    print(id['results'][0]['host'])
    new = b1ddi.create('/ipam/host', body=payload)
    return new

def create_subnet(address):
    body = ( '{ "address": "' + address + '", '
                #+ '"cidr": "' + cidr + '", '
                + '"space": "' + r1 + '", '
                #+ '"name": "' + address_name + '", '
                + '"comment": "Discovered by scan2b1ddi" '
                ' }' )
    new = b1ddi.create('/ipam/subnet', body=body)
    if new.status_code in b1ddi.return_codes_ok:
        print(f"Subnet {address} in {r1} was created")
    else:
        print(f"[bold red][-] Error : [/bold red]{new.status_code} - {new.text}")
        
def networks_to_scan(ini_networks):
    # If you want to do a pingsweep on network 192.168.0.0/24:
    sif = nm.scan(hosts=ini_networks, arguments='-sn')
    for x in nm.all_hosts():
        try:
            if len(nm[x]['vendor'])==0:
                #print(x + "," + nm[x]['status']['state'] + "," + " NA,NA")
                create_host(x)
                # payload = '{"ipaddress": "' + x + '", "status": "' + nm[x]['status']['state'] + '", "mac": "' + nm[x]['addresses']['mac'] + '","vendor":"'>
                # response = requests.request("POST", url, headers=headers, data=payload)
                #print(response.text)
            else:
                #vendor = nm[x]['vendor']
                create_host(x)
                #mac, vendor = zip(*vendor.items())
                #print(x + "," + nm[x]['status']['state'] + "," + nm[x]['addresses']['mac'] + "," + str(vendor[0]))
                
        except KeyError as error:
            print(x + "," + nm[x]['status']['state'] + "," + " NA,NA")
            # payload='{"ipaddress": "' + x + '", "status": "' + nm[x]['status']['state'] + '", "mac":"NA", "vendor":"NA"}'
            # response = requests.request("POST", url, headers=headers, data=payload)
            #print(response.text)


# 
# This will read the networks from "networks.txt"
# Add one network per a line
file1 = open('networks.txt', 'r')
Lines = file1.readlines()

# Strips the newline character
for line in Lines:
    create_subnet(line.rstrip())
    networks_to_scan(line)
