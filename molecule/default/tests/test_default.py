import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_transmission(host):
    h = host.run(
        'curl -L http://transmission:transmission@localhost/transmission'
    ).stdout

    'Transmission' in h


def test_nzbget(host):
    h = host.run(
        'curl -L http://nzbget:tegbzn6789@localhost/nzbget'
    ).stdout

    assert 'NZBGet' in h


def test_sonarr(host):
    h = host.run(
        'curl -L http://localhost/sonarr'
    ).stdout

    'Sonarr' in h


def test_radarr(host):
    h = host.run(
        'curl -L http://localhost/radarr'
    ).stdout

    'Radarr' in h
