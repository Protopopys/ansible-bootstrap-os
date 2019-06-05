import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('base_package', [
  'sudo',
  'aptitude',
  'python3-minimal',
  'python3-apt',
  'python3-simplejson'
])
def test_is_base_package_installed(host, base_package):
    package = host.package(base_package)

    assert package.is_installed


@pytest.mark.parametrize('required_package', [
  'dbus',
  'acl',
  'ca-certificates',
  'module-init-tools',
  'apt-transport-https',
  'gzip',
  'lvm2',
  'tar',
  'unzip',
  'xz-utils'
])
def test_is_required_package_installed(host, required_package):
    package = host.package(required_package)

    assert package.is_installed
