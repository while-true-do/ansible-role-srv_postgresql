<!--
name: README.md
description: This file contains important information for the repository.
author: while-true-do.io
contact: hello@while-true-do.io
license: BSD-3-Clause
-->

<!-- github shields -->
[![Github (tag)](https://img.shields.io/github/tag/while-true-do/ansible-role-srv_postgresql.svg)](https://github.com/while-true-do/ansible-role-srv_postgresql/tags)
[![Github (license)](https://img.shields.io/github/license/while-true-do/ansible-role-srv_postgresql.svg)](https://github.com/while-true-do/ansible-role-srv_postgresql/blob/master/LICENSE)
[![Github (issues)](https://img.shields.io/github/issues/while-true-do/ansible-role-srv_postgresql.svg)](https://github.com/while-true-do/ansible-role-srv_postgresql/issues)
[![Github (pull requests)](https://img.shields.io/github/issues-pr/while-true-do/ansible-role-srv_postgresql.svg)](https://github.com/while-true-do/ansible-role-srv_postgresql/pulls)
<!-- travis shields -->
[![Travis (com)](https://img.shields.io/travis/com/while-true-do/ansible-role-srv_postgresql.svg)](https://travis-ci.com/while-true-do/ansible-role-srv_postgresql)
<!-- ansible shields -->
[![Ansible (min. version)](https://img.shields.io/badge/dynamic/yaml.svg?label=Min.%20Ansible%20Version&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-srv_postgresql%2Fmaster%2Fmeta%2Fmain.yml&query=%24.galaxy_info.min_ansible_version&colorB=black)](https://galaxy.ansible.com/while_true_do/srv_postgresql)
[![Ansible (platforms)](https://img.shields.io/badge/dynamic/yaml.svg?label=Supported%20OS&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-srv_postgresql%2Fmaster%2Fmeta%2Fmain.yml&query=galaxy_info.platforms%5B*%5D.name&colorB=black)](https://galaxy.ansible.com/while_true_do/srv_postgresql)
[![Ansible (tags)](https://img.shields.io/badge/dynamic/yaml.svg?label=Galaxy%20Tags&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-srv_postgresql%2Fmaster%2Fmeta%2Fmain.yml&query=%24.galaxy_info.galaxy_tags%5B*%5D&colorB=black)](https://galaxy.ansible.com/while_true_do/srv_postgresql)

# Ansible Role: srv_postgresql

An Ansible Role to install and configure postgresql.

## Motivation

[Postgresql](https://www.postgresql.org/) is a very common database server, used
by many applications, teams and companies.

## Description

This role installs and configures postgresql.

-   install postgresql
-   configure postgresql user
-   configure hba access

## Requirements

Used Modules:

-   [Ansible Package Module](https://docs.ansible.com/ansible/latest/modules/package_module.html)
-   [Ansible Service Module](https://docs.ansible.com/ansible/latest/modules/service_module.html)
-   [Ansible package_facts Module](https://docs.ansible.com/ansible/latest/modules/package_facts_module.html)
-   [Ansible User Module](https://docs.ansible.com/ansible/latest/modules/user_module.html)
-   [Ansible File Module](https://docs.ansible.com/ansible/latest/modules/file_module.html)
-   [Ansible Stat Module](https://docs.ansible.com/ansible/latest/modules/stat_module.html)
-   [Ansible Command Module](https://docs.ansible.com/ansible/latest/modules/command_module.html)
-   [Ansible Template Module](https://docs.ansible.com/ansible/latest/modules/template_module.html)
-   [Ansible Firewalld Module](https://docs.ansible.com/ansible/latest/modules/firewalld_module.html)

## Installation

Install from [Ansible Galaxy](https://galaxy.ansible.com/while_true_do/srv_postgresql)
```
ansible-galaxy install while_true_do.srv_postgresql
```

Install from [Github](https://github.com/while-true-do/ansible-role-srv_postgresql)
```
git clone https://github.com/while-true-do/ansible-role-srv_postgresql.git while_true_do.srv_postgresql
```

## Usage

### Role Variables

```
---
# defaults file for while_true_do.srv_postgresql

## Package Management
wtd_srv_postgresql_package:
  - postgresql-server
  - postgresql-contrib
# State can be present|latest|absent
wtd_srv_postgresql_package_state: "present"

## User Management
# This user will also be ths postgres super user
wtd_srv_postgresql_user:
  name: "postgres"
  group: "postgres"

## Configuration Management
wtd_srv_postgresql_conf_data: "/var/lib/pgsql/data"
# For local connections via postgres_user defaults will be set
wtd_srv_postgresql_conf_hba: []
# - type: "local"
#   database: "all"
#   user: "all"
#   method: "peer"
# - type: "host"
#   database: "somedatabase"
#   user: "someuser"
#   address: "192.168.10.0/24"
#   method: "ident"

## Service Management
wtd_srv_postgresql_service: "postgresql"
# State can be started|stopped
wtd_srv_postgresql_service_state: "started"
wtd_srv_postgresql_service_enabled: true

## Firewalld Management
wtd_srv_postgresql_fw_mgmt: true
wtd_srv_postgresql_fw_service: "postgresql"
# State can be enabled|disabled
wtd_srv_postgresql_fw_state: "enabled"
# Zone can be according to defined zones on your machine.
wtd_srv_postgresql_fw_zone: "public"
```

### Example Playbook

Running Ansible
[Roles](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html)
can be done in a
[playbook](https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html).

#### Simple

```
---
- hosts: all
  roles:
    - role: while_true_do.srv_postgresql
```

## Known Issues

1.  RedHat Testing is currently not possible in public, due to limitations
    in subscriptions.
2.  Some services and features cannot be tested properly, due to limitations
    in docker.

## Testing

Most of the "generic" tests are located in the
[Test Library](https://github.com/while-true-do/test-library).

Ansible specific testing is done with
[Molecule](https://molecule.readthedocs.io/en/stable/).

Infrastructure testing is done with
[testinfra](https://testinfra.readthedocs.io/en/stable/).

Automated testing is done with [Travis CI](https://travis-ci.com/while-true-do).

## Contribute

Thank you so much for considering to contribute. We are very happy, when somebody
is joining the hard work. Please fell free to open
[Bugs, Feature Requests](https://github.com/while-true-do/ansible-role-srv_postgresql/issues)
or [Pull Requests](https://github.com/while-true-do/ansible-role-srv_postgresql/pulls) after
reading the [Contribution Guideline](https://github.com/while-true-do/doc-library/blob/master/docs/CONTRIBUTING.md).

See who has contributed already in the [kudos.txt](./kudos.txt).

## License

This work is licensed under a [BSD-3-Clause License](https://opensource.org/licenses/BSD-3-Clause).

## Contact

-   Site <https://while-true-do.io>
-   Twitter <https://twitter.com/wtd_news>
-   Code <https://github.com/while-true-do>
-   Mail [hello@while-true-do.io](mailto:hello@while-true-do.io)
-   IRC [freenode, #while-true-do](https://webchat.freenode.net/?channels=while-true-do)
-   Telegram <https://t.me/while_true_do>
