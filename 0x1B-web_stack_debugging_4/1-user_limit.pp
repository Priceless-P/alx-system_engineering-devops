# Fix Too many open files error for user 'holberton'

exec { 'increase-hard-file-limit-holberton':
  command => 'sed -i "/holberton hard/s/5/40960/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'increase-soft-file-limit-holberton':
  command => 'sed -i "/holberton soft/s/4/40960/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
