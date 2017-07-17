Welcome to elasticsearch\_zabbixagent Ansible Role’s documentation!
===================================================================

Role Name
---------

Ansible role to install and configure elasticsearch\_zabbixagent as
container

### Requirements

Docker engine up and runnig

### Dependencies

N/A

### Example Playbook

    - hosts: servers
      roles:
        - { role: elasticsearch_zabbixagent }

pip ansible role default variables
----------------------------------

#### Sections

-   elasticsearch\_zabbixagent packaging
-   elasticsearch\_zabbixagent configuration

### elasticsearch\_zabbixagent packaging

`elasticsearch_zabbixagent_docker_imagen`

> elasticsearch\_zabbixagent docker image

    elasticsearch_zabbixagent_docker_image: melodous/zabbix-agent

`elasticsearch_zabbixagent_version`

> elasticsearch\_zabbixagent docker image version (TAG)

    elasticsearch_zabbixagent_version: 3.2.6

`elasticsearch_zabbixagent_docker_labels`

> Yaml dictionary which maps Docker labels. os\_environment: Name of the
> environment, example: Production, by default “default”.
> os\_contianer\_type: Type of the container, by default
> elasticsearch\_zabbixagent.

    elasticsearch_zabbixagent_docker_labels:
      os_environment: "{{ docker_os_environment | default('default') }}"
      os_container_type: elasticsearch_zabbixagent

### elasticsearch\_zabbixagent configuration

`elasticsearch_zabbixagent_port`

> Zabbix Agent port

    elasticsearch_zabbixagent_port: 10060

`elasticsearch_zabbixagent_hostname`

> host to send traps

    elasticsearch_zabbixagent_hostname: elasticsearch

`elasticsearch_zabbixagent_server`

> zabbix server to send traps

    elasticsearch_zabbixagent_server: localhost

Changelog
---------

**elasticsearch\_zabbixagent**

This project adheres to Semantic Versioning and human-readable
changelog.

### elasticsearch\_zabbixagent master - unrelease

##### Added

-   First addition

##### Changed

-   First change

### elasticsearch\_zabbixagent v0.0.1 - 2017/07/17

##### Added

-   Initial version

Copyright
---------

elasticsearch\_zabbixagent

Copyright (C) 2017/07/13 Raúl Melo
&lt;<raul.melo@opensolutions.cloud>&gt;

LICENSE
