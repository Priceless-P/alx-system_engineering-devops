#0x1B. Web stack debugging #4

## Tasks

1. [0. Sky is the limit, let's bring that limit higher](./0-the_sky_is_the_limit_not.pp)
I wrote a puppet script to fix nginx not being able to handle a large number of request as a result of the ULIMIT

2. [1. User limit](./1-user_limit.pp)
I wrote another puppet script to `fix Too many open files error for user 'holberton'` by increasing the user's hard and soft file limit
