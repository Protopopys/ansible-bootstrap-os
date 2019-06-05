import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('epel_package', [
  'epel-release'
])
def test_is_epel_installed(host, epel_package):
    package = host.package(epel_package)

    assert package.is_installed


@pytest.mark.parametrize('base_package', [
  'sudo',
  'python',
  'python2-simplejson'
])
def test_is_base_package_installed(host, base_package):
    package = host.package(base_package)

    assert package.is_installed


@pytest.mark.parametrize('required_package', [
  'libselinux-python',
  'policycoreutils-python',
  'lvm2',
  'tar',
  'unzip',
  'gzip',
  'xz'
])
def test_is_required_package_installed(host, required_package):
    package = host.package(required_package)

    assert package.is_installed
