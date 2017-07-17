Role Name
=========

Ansible role to install and configure elasticsearch_zabbixagent as container

Requirements
------------

Docker engine up and runnig

Dependencies
------------

N/A

Example Playbook
----------------

.. code::

  - hosts: servers
    roles:
      - { role: elasticsearch_zabbixagent }
