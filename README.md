# create-rfc6052
A small (ansible) python library for use generating RFC6052 addresses in a MAP-T environment 

This is a small ansible module created by the team at Cox to generate RFC6052 addresses for MAP-T deployments. It can be used (for example) to generate IPv6 endpoint addresses to configure listening services in the MAP-T DMR range.

This is useful as it allows a provider to offload common customer MAP-T traffic patterns (DNS, NTP, etc.) onto a dual-stack capable service endpoint. This functionally reduces the workload on MAP-T BRs for well-known (on-net) IPv4 endpoints.

## Dependancies ##
This code was inspired by (and requires):

* python3
* pyswmap

  https://github.com/ejordangottlieb/pyswmap

## Use ##

### Installation Steps ###

Install pysmap in one of two ways:
- using python pip or similar
- placing mapalgs.py in your preferred ansible module_utils location

Copy the createRFC6052IPv6.py to your ansbile library location.

### Sample Playbook ###

```yaml
- name: Create RFC6052 IPv6 address list
  connection: local
  hosts: localhost
  gather_facts: False
  vars:
    dmrIPs: [ "2600:1234:bfff:fffe::/64", "2600:1234:bfff:ffff::/64" ]
    ipv4s: [ "8.8.8.8", "8.8.4.4" ]

  tasks:
    - name: Get list using pyswmap
      createRFC6052IPv6:
        ipv6dmrs: "{{ dmrIPs }}"
        ipv4addrs: "{{ ipv4s }}"
      register: dmrcalc_output

    - debug: var=dmrcalc_output.meta

```

With the following output that can be leveraged in your other plays and roles:

```json
PLAY [Create RFC6052 IPv6 address list] ************************************************************************

TASK [Get list using pyswmap] **********************************************************************************
changed: [localhost]

TASK [debug] ***************************************************************************************************
ok: [localhost] => {
    "dmrcalc_output.meta": [
        "2600:1234:bfff:fffe:8:808:800:0",
        "2600:1234:bfff:ffff:8:808:800:0",
        "2600:1234:bfff:fffe:8:804:400:0",
        "2600:1234:bfff:ffff:8:804:400:0"
    ]
}
```
