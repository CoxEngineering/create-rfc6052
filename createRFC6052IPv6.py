#!/usr/bin/env python3

from ansible.module_utils.basic import *
#from mapalgs import * #When mapalgs is in PYTHONPATH (usually when installed such as setup.py or pip)
from ansible.module_utils.mapalgs import * #When mapalgs is in the module_utils dir
from ipaddress import IPv4Network

def main():

    fields = {
    "ipv6dmrs": { "required": True, "type": "list" },  
    "ipv4addrs": { "required": True, "type": "list" }  #Can be either 1.1.1.1/32 or 1.1.1.1 format - other mask will error
  }

    module = AnsibleModule(
    argument_spec=fields,
    supports_check_mode=True
  )
    dmrcalc_embedded_result = []
    for ipv4addr in module.params["ipv4addrs"]:
        net4 = IPv4Network(ipv4addr)
        ipv4 = net4[0]
        for ipv6dmr in module.params["ipv6dmrs"]:
            m = DmrCalc(ipv6dmr)
            dmrcalc_embedded_result = dmrcalc_embedded_result + [str(m.embed_6052addr(ipv4))]

    module.exit_json(changed=True, meta=dmrcalc_embedded_result)

if __name__ == '__main__':
  main()
