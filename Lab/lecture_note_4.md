## Lecture Note 4
### pwd
shows the current path in a hierarchical directory

```
$ pwd
```
![images](https://github.com/leeseobin00/temp-repo/assets/70849467/4b044be6-8d31-4ace-94a8-fac40a086a61)

### cd
change directory

### ls
list files and directories

```
$ ls
```

| Command | Result |
| --- | --- |
| ls | List the files in the working directory |
| ls /bin | List the files in the /bin directory (or any other directory we care to specify) |
| ls -l | List the files in the working directory in long format |
| ls -l /etc /bin | List the files in the /bin directory and the /etc directory in long format |
| ls -la .. | List all files (even ones with names beginning with a period character, which are normally hidden) in the parent of the working directory in long format |

### cd and ls
| Arguments |  |
| --- | --- |
| / | root |
| . | current directory |
| .. | upper-level directory |
| ~ | home of current user |
| /[directory name] | absolute path |
| ./[directory name] | relative path |
| ../[directory name] | relative path |

| Options |  |
| --- | --- |
| -l | show detailed information (long format) |
| -lh | same as above, but size in units |

### cp
copy files and directories

| Command | Results |
| --- | --- |
| cp file1 file2 | Copies the contents of file1 into file2. If file2 does not exist, it is created; otherwise file2 is silently overwritten with the contents of file1. |
| cp -i file1 file2 | Like above however, since the “-i”(interactive) option is specified, if file2 exists, the user is prompted before it is overwritten with the contents of file1. |
| cp file1 dir1 | Copy the contents of file1 (into a file named file1) inside of directory dir1. |
| cp -R dir1 dir2 | Copy the contents of the directory dir1. If directory dir2 does not exist, it is created. Otherwise it creates a directory named dir1 within directory dir2. |
| cp *.txt text_files | Copy all files in the current working directory with names ending with the character “.txt” to an existing directory named text_files. |

### mv
move files and directories or rename them

| Command | Results |
| --- | --- |
| mv file1 file2 | If file2 does not exist, then file1 is renamed file2. If file2 exists, its contents are silently replaced with the contents of file1 |
| mv -i file1 file2 | Like above however, since the “-i”(interactive) option is specified, if the file2 exists, the user is prompted before it is overwritten with the contents of file1. |
| mv file1 file2 dir1 | The files file1 and file2 are moved to directory dir1. If dir1 does not exist, mv will exit with an error |
| mv dir1 dir2 | If dir2 does not exist, then dir1 is renamed dir2. If dir2 exists, the directory dir1 is moved within directory dir2. |
| mv dir1 ../*.bak dir2 | Move the subdirectory dir1 and all the files ending in “.bak” in the current working directory’s parent directory to an existing directory named dir2. |

### rm
delete files and directories *permantely and irreversevely*

| Command | Results |
| --- | --- |
| rm file1 file2 | Delete file1 and file2 |
| rm -i file1 file2 | Like above however, since the “-i”(interactive) option is specified, the user is prompted before each file is deleted. |
| rm -r dir1 dir2 | Directories dir1 and dir2 are deleted along with all of their contents |
| rm *~ | Delete all files in the current working directory that end the character “~”. Some applications create backup files using this naming scheme. Using this command will clean them out of a directory. |

### mkdir
make a new directory

```
$ mkdir new_directory
```

### Long Format
File_Permissions Owner Group Size(int_bytes) Modification_Time File_Name

### Clear
```
$ clear
```

### Manipulation: Wildcards
| Pattern | Matches |
| --- | --- |
| * | All filenames |
| g* | All filenames that begin with the character “g” |
| b*.txt | All filenames that begin the character “b” and end with the characters “.txt” |
| Data??? | Any filename that begins with the characters “Data” followed by exactly 3 more characters |

### help
```
$ help cd
```

### man
```
$ man cp
```
![images](https://github.com/leeseobin00/temp-repo/assets/70849467/97aefabf-809f-4ebd-949c-7cb1d28b270c)

### exit
```
$ exit
```
![images](https://github.com/leeseobin00/temp-repo/assets/70849467/801e5a34-3c53-49c6-b507-229631caddd2)

