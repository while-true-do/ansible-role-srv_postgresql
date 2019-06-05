import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_postgresql_package(host):
    pkg = host.package('postgresql-server')

    assert pkg.is_installed


def test_postgresql_service(host):
    srv = host.service('postgresql')

    assert srv.is_running
    assert srv.is_enabled
