# Lecture Note 5
# CLI (Command Line Interface)
## I/O Redirection: Standard Output
- By default, standard output is screen.
- You can redirect output using “>” after a command (e.g., ls) to create and save the output in a file
- Command “cat” displays the content of a text file.
![image](https://github.com/leeseobin00/temp-repo/assets/70849467/9ec85af1-aae8-4d4e-98d0-58173fe51deb)
- Using “>>” appends output to an extising file (if it already exitsts), or create and write to a new file if it doesn’t exist.
![image](https://github.com/leeseobin00/temp-repo/assets/70849467/49c7e641-0702-4c6b-acac-b8a8bb55df54)


## I/O Redirection: Standard Input
- By default, standard input is from keyboard.
- You can redirecct input from a file using “<”.
- You can mix “<“ and “>” together in a single line.

## Pipelines “|”
- Pipeline feeds output of previous command to input of next command.
- command1 | command2 | command3 | ...
- Press “q” key to exit the screen.
![image](https://github.com/leeseobin00/temp-repo/assets/70849467/8a15198a-b09f-4bd7-9cc3-24f09c2fd635)
- Number of files currently in the directory
![image](https://github.com/leeseobin00/temp-repo/assets/70849467/5f2b14be-d7a2-4245-9ceb-780bd13d45a9)


## Expansion
- Special characters expand its meaning when given to shell commands.
- Extends to a specific meaning
![images](https://github.com/leeseobin00/temp-repo/assets/70849467/bb466ca7-1037-4b11-8617-d5e49412228c)
![images](https://github.com/leeseobin00/temp-repo/assets/70849467/0a7a3f5e-f8f1-493b-a9ab-e7ffc501c017)


## Tip: Backslash
- Backslah can be used to ignore line change in command (“enter”), to enter a long command in multiple lines.

## Permissions
- Linux is a multi-user system.
- Files and directories have a permission assigned differently to owner / group / others.
![image](https://github.com/leeseobin00/temp-repo/assets/70849467/db1c7f18-5553-443f-944e-9f6e5c2b3465)

## Changing Permissions
- “chmod” changes permissions.
- Change the permission of a file “word.txt” that only the owner (you) can read and write, but all the others (including others in the group) can only read it. No execution is needed for all users.

| Value | Meaning |
| --- | --- |
|**777**|**(rwxrwxrwx)** No restrictions on permissions. Anybody may do anything. Generally not a desirable setting.|
|**755**|**(rwxr-xr-x)** The file's owner may read, write, and execute the file. All others may read and execute the file. The setting is common for programs that are used by all users.|
|**700**|**(rwx------)** The file's owner may read, write, and execute the file. Nobody else has any rights. The setting is useful for programs that only the owner may use and must be kept private from others.|
|**666**|**(rw-rw-rw-)** All users may read and write the file.|
|**644**|**(rw-r--r--)** The owner may read and write a file, while all others may only read the file. A common setting for data files that everybody may read, but only the owner may change.|
|**600**|**(rw-------)** The owner may read and write a file. All others have no rights. A common setting for data files that the owner wants to keep private.|


## Superuser
- A superuser has all system administation authority.
- Some commands need superuser’s privilleges.
- Put “sudo” before the command if you are a superuser.
- Type “exit” to get out of a superuser session.

## Text Editors
- In Linux, you can choose CLI-based or GUI-based text editors.
  
| Name | Description | Interface |
| --- | --- | --- |
| **vi, vim** | The granddaddy of Unix text editors, **vi**, is infamous for its obtuse user interface. On the bright side, **vi**, is powerful, lightweight, and fast. Learning **vi** is a Unix rite of passage, since it is universally available on Unix-like systems. On most Linux distributions, an enhanced version of **vi** called **vim** is providedin place of vi. **vim** is a remarkable editor and well worth taking the time to learn it. | command line |
| **Emacs** | The true giant in the world of text editors in Emacs orginally written by Richard Stallman. **Emacs** contains (or can be made to contain) every feature ever conceived of for a text editor. It should be noted that **vi** and Emacs fancs fight bitter religious wars over which is better. | command line |
| **nano** | **nano** is a free clone of the text editor supplied with the **pine** email program. **nano** is very easy to user but is very short on features compared to vim and **emacs**. **nano** is recommended for first-time users who need a command line editor. | command line |
| **gedit** | **gedit** is the editor supplied with the GNOME desktop environment. gedit is easy to use and contains enough features to be a good beginners-level editor. | graphical |
| **kwrite** | **kwrite** is the "advanced editor" supplied with KDE. It has syntax highlighting, a helpful feature for programmers and script writers. | graphical |

## Shell Script
- Write and run a shell script

## Tip: History
- Type “history” to see previous command history.
- Or, save it to a text file.
