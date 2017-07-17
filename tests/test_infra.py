def test_elasticsearch_zabbixagent_server_running_and_enabled(Command, Service):
    # Check that docker service is running and enabled
    docker_service = Service("docker")
    assert docker_service.is_running
    assert docker_service.is_enabled
    # Check that elasticsearch_zabbixagent service is running and enabled
    elasticsearch_zabbixagent_service = Service("elasticsearch_zabbixagent")
    assert elasticsearch_zabbixagent_service.is_running
    assert elasticsearch_zabbixagent_service.is_enabled


def test_elasticsearch_zabbixagent_start_stop(Command, Service):
    Command.run_expect([0], "systemctl stop elasticsearch_zabbixagent")
    elasticsearch_zabbixagent_service = Service("elasticsearch_zabbixagent")
    assert not elasticsearch_zabbixagent_service.is_running
    Command.run_expect([0], "systemctl start elasticsearch_zabbixagent")
    assert elasticsearch_zabbixagent_service.is_running
    Command.run_expect([0], "systemctl restart elasticsearch_zabbixagent")
    assert elasticsearch_zabbixagent_service.is_running
