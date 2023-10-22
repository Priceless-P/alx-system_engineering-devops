# Uploading Screenshots to a Remote Server using SFTP

## Step 1: Taking Screenshots
I started by taking the required screenshots for the completed tasks.

## Step 2: Opening a Terminal
I opened a terminal on my local machine.

## Step 3: Connecting to the Sandbox Environment
I used the SFTP command-line tool to connect to the remote sandbox environment provided to me. Here's the command:

```bash
sftp my_username@hostname
```

Replace `my_username` with your actual username and `hostname` with the provided server address.

## Step 4: Navigating to the Destination Directory
After connecting, I was in my home directory on the remote server. I used the `cd` command to navigate to the directory where I wanted to upload the screenshots:

```bash
cd /root/alx-system_engineering-devops/command_line_for_the_win/
```

## Step 5: Uploading Screenshots
In the destination directory, I used the `put` command to upload the screenshots from my local machine to the remote server:

```bash
put /path/to/local/0-first_9_tasks.png.png
```

Replace `/path/to/local/0-first_9_tasks.png.png` with the actual file path of the screenshot on your local machine.

## Step 6: Confirming File Transfer
To confirm that the screenshots were successfully transferred, I used the `ls` command to list the files in the remote directory:

```bash
ls
```
