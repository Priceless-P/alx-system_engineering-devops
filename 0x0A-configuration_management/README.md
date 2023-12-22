# 0x0A. Configuration management

This folder contains Puppet manifests for various configuration management tasks.

## Tasks

- [Create a file](0x0A-configuration_management/0-create_a_file.pp)
  - **Description:** Using Puppet, create a file in `/tmp`.
  - **Requirements:**
    - File path: `/tmp/school`
    - File permission: 0744
    - File owner: www-data
    - File group: www-data
    - File content: "I love Puppet"

- [Install a package](0x0A-configuration_management/1-install_a_package.pp)
  - **Description:** Using Puppet, install Flask from pip3.
  - **Requirements:**
    - Install Flask
    - Version: 2.1.0

- [Execute a command](0x0A-configuration_management/2-execute_a_command.pp)
  - **Description:** Using Puppet, create a manifest that kills a process named `killmenow`.
  - **Requirements:**
    - Use the `exec` Puppet resource
    - Use `pkill` to terminate the process
