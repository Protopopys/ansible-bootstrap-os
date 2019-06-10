
Ansible Role: ansible-bootstrap-os
=========

[![Build Status](https://travis-ci.org/Protopopys/ansible-bootstrap-os.svg?branch=master)](https://travis-ci.org/Protopopys/ansible-bootstrap-os)

An Ansible Role that installs Python and requirements packages.

Requirements
------------

None.

Role Variables
--------------

Available variables are listed below, along with default values (see defaults/main.yml):

```yaml
  install_required_packages: true
```

Dependencies
------------

None.

Example Playbook
----------------

```yaml
- hosts: all
  roles:
    - protopopys.ansible-bootstrap-os
```

License
-------

MIT

Author Information
------------------

This role was created in 2019 by Kirill Protopopov.
