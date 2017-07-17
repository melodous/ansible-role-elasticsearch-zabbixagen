.. vim: foldmarker=[[[,]]]:foldmethod=marker

pip ansible role default variables
==================================

.. contents:: Sections
   :local:

elasticsearch_zabbixagent packaging
-----------------------------------

.. envvar:: elasticsearch_zabbixagent_docker_imagen

   elasticsearch_zabbixagent docker image

::

  elasticsearch_zabbixagent_docker_image: melodous/zabbix-agent




.. envvar:: elasticsearch_zabbixagent_version

   elasticsearch_zabbixagent docker image version (TAG)

::

  elasticsearch_zabbixagent_version: 3.2.6




.. envvar:: elasticsearch_zabbixagent_docker_labels

   Yaml dictionary which maps Docker labels.
   os_environment: Name of the environment, example: Production, by default "default".
   os_contianer_type: Type of the container, by default elasticsearch_zabbixagent.

::

  elasticsearch_zabbixagent_docker_labels:
    os_environment: "{{ docker_os_environment | default('default') }}"
    os_container_type: elasticsearch_zabbixagent




elasticsearch_zabbixagent configuration
---------------------------------------

.. envvar:: elasticsearch_zabbixagent_port

   Zabbix Agent port

::

  elasticsearch_zabbixagent_port: 10060




.. envvar:: elasticsearch_zabbixagent_hostname

   host to send traps

::

  elasticsearch_zabbixagent_hostname: elasticsearch




.. envvar:: elasticsearch_zabbixagent_server

   zabbix server to send traps

::

  elasticsearch_zabbixagent_server: localhost



