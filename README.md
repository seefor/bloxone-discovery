# bloxone-discovery
Good Enough Discovery Tool for Infoblox BloxOne DDI

## Table of contents

- [Quick start](#quick-start)
- [Status](#status)
- [What's included](#whats-included)
- [Creators](#creators)
- [Thanks](#thanks)
- [Copyright and license](#copyright-and-license)


## Quick start

This is an initial discovery script for Infoblox BloxOne DDI
Needs python3.6+ and NMAP install

### Installation:  
> pip3 install bloxone  
> pip3 install nmap  
> git clone this repo you will need the nmap folder included here

### Before running the script
You will need to edit the `csp.ini` file to add your API key and IP Space
> [BloxOne]  
> url = 'https://csp.infoblox.com'  
> api_version = 'v1'  
> api_key = 'mykey'  
>  
> [space]  
> ip_space = sbaksh-ip-space  

After we save the `csp.ini` file we need to edit the `networks.txt` file, it's basically a single column of networks with CIDRs  
> 192.168.0.0/24  
> 10.10.1.0/24  

### Running the Script
>sudo python3 scan2ddi.py  
>[+] sbaksh-ip-space id is ipam/ip_space/93c26245-b0e2-11ea-a9fa-f68df6f70235  
>[+] Created - Subnet 192.168.0.0/24 in ipam/ip_space/93c26245-b0e2-11ea-a9fa-f68df6f70235  
>[+] Created - 192.168.0.1 in sbaksh-ip-space  
>[+] Created - 192.168.0.103 in sbaksh-ip-space  
>[+] Created - 192.168.0.106 in sbaksh-ip-space  
>[+] Created - 192.168.0.107 in sbaksh-ip-space  
>[+] Created - 192.168.0.109 in sbaksh-ip-space  
>[+] Created - 192.168.0.80 in sbaksh-ip-space  
>[+] Created - 192.168.0.82 in sbaksh-ip-space  
>[+] Created - 192.168.0.84 in sbaksh-ip-space  
>[+] Created - 192.168.0.94 in sbaksh-ip-space  
>[+] Created - 192.168.0.95 in sbaksh-ip-space  
>[+] Created - 192.168.0.96 in sbaksh-ip-space  
>[-] Error : 400 - {"error":[{"message":"The ipam/subnet(10.10.1.0 - 10.10.1.255) already exists."}]}  
>[+] Updated 10.10.1.1 in sbaksh-ip-space  
>[+] Updated 10.10.1.250 in sbaksh-ip-space  

## Status

Phases of the script
- ~~Phase 1 - Initial Discovery~~  
- Phase 2 - Update what we discovery  
- Phase 3 - Docker Image  

## What's included

Here is the 
```text
discovery/
    ├── csp.ini
    ├── networks.txt
    ├── nmap
    │   ├── __init__.py
    │   ├── nmap.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-38.pyc
    │   │   └── nmap.cpython-38.pyc
    │   └── test_nmap.py
    └──scan2ddi.py
```

## Creators

**Creator 1**

- [Sif Baksh](https://github.com/seefor)

## Thanks

[Chris Marrison](https://github.com/ccmarris) for his [python-bloxone](https://github.com/ccmarris/python-bloxone) module.

## Copyright and license

Code and documentation copyright 2020-2021 the authors. Code released under the [MIT License](https://github.com/seefor/bloxone-discovery/blob/main/LICENSE).

Enjoy :metal:
