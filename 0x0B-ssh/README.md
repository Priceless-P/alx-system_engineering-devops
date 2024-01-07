# SSH Tasks

## Task 0: [Use a private key](./0-use_a_private_key)
Write a Bash script that uses SSH to connect to your server using the private key `~/.ssh/school` with the user `ubuntu`.

## Task 1: [Create an SSH key pair](./1-create_ssh_key_pair)
Write a Bash script that creates an RSA key pair:
- The name of the private key must be `school`
- Number of bits in the key to be created: `4096`
- The created key must be protected by the passphrase `betty`

## Task 2: [Client configuration file](./2-ssh_config)
Configure your machine's SSH client configuration file to connect to a server without typing a password:
- Configuration to use the private key `~/.ssh/school`
- Configuration to refuse authentication using a password

## Task 3: [Let me in!](./)
Add the provided SSH public key to your server's `ubuntu` user to enable access.

## Task 4: [Client configuration file (w/ Puppet)](./100-puppet_ssh_config.pp)
Use Puppet to set up your SSH client configuration file:
- Configuration to use the private key `~/.ssh/school`
- Configuration to refuse authentication using a password
