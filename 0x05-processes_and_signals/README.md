# 0x05. Processes and Signals

Tasks related to processes and signals in the ALX System Engineering & DevOps curriculum.

## Task 0: What is my PID
* File: [0-what-is-my-pid](0-what-is-my-pid)
* Description: Write a Bash script that displays its own PID.

## Task 1: List your processes
* File: [1-list_your_processes](1-list_your_processes)
* Description: Write a Bash script that displays a list of currently running processes. The script should show all processes for all users, including those without a TTY, display the information in a user-oriented format, and show the process hierarchy.

## Task 2: Show your Bash PID
* File: [2-show_your_bash_pid](2-show_your_bash_pid)
* Description: Write a Bash script that displays lines containing the word "bash" and their corresponding PIDs, allowing you to easily get the PID of your Bash process.

## Task 3: Show your Bash PID made easy
* File: [3-show_your_bash_pid_made_easy](3-show_your_bash_pid_made_easy)
* Description: Write a Bash script that displays the PID and process name of processes containing the word "bash" in their name.

## Task 4: To infinity and beyond
* File: [4-to_infinity_and_beyond](4-to_infinity_and_beyond)
* Description: Write a Bash script that displays "To infinity and beyond" indefinitely with a 2-second pause between each iteration.

## Task 5: Don't stop me now!
* File: [5-dont_stop_me_now](5-dont_stop_me_now)
* Description: Write a Bash script that stops the process created in Task 4 ("4-to_infinity_and_beyond") using the "kill" command.

## Task 6: Stop me if you can
* File: [6-stop_me_if_you_can](6-stop_me_if_you_can)
* Description: Write a Bash script that stops the process created in Task 4 ("4-to_infinity_and_beyond") without using the "kill" or "killall" commands.

## Task 7: Highlander
* File: [7-highlander](7-highlander)
* Description: Write a Bash script that displays "To infinity and beyond" indefinitely and responds with "I am invincible!!!" when receiving a SIGTERM signal. Create a copy of the script from Task 6 and name it "67-stop_me_if_you_can" to kill the "7-highlander" process.

## Task 8: Beheaded process
* File: [8-beheaded_process](8-beheaded_process)
* Description: Write a Bash script that kills the process created in Task 7 ("7-highlander").

## Task 9: Process and PID file
* File: [100-process_and_pid_file](100-process_and_pid_file)
* Description: Write a Bash script that creates a PID file, displays messages, and responds to signals. The script should create the file /var/run/myscript.pid, display messages, and delete the PID file when receiving SIGQUIT or SIGTERM signals.

## Task 10: Manage my process
* Files: [101-manage_my_process](101-manage_my_process), [manage_my_process](manage_my_process)
* Description: Write a Bash script (manage_my_process) that manages another Bash script (manage_my_process) which writes "I am alive!" to a file, /tmp/my_process, with a 2-second pause between each message. The manager script allows starting, stopping, and restarting the process and creates/deletes a PID file.

## Task 11: Zombie
* File: [102-zombie.c](102-zombie.c)
* Description: Write a C program that creates 5 zombie processes and displays messages for each. The program should create zombie processes and demonstrate how to check for zombie processes using the "ps" command.

