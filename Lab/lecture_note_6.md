# Lecture Note 6


## Version Control and Collaboration
- It’s essential to use a version control system for software development
and other documentation works.
- Basic solution: Making copies
- We need a systematic management system for version control and collaboration


## Changes vs. Snapshots
- Storing data as changes to the base version
![image](https://github.com/leeseobin00/temp-repo/assets/70849467/e1af8166-6e47-4a67-a642-95e76a0acaf4")
- Storing data as snapshots (Git)
  - Record a particular event/moment
![image](https://github.com/leeseobin00/temp-repo/assets/70849467/f8886dc8-ff73-4cb2-80e8-b0f37a0d9c7c)


## Local, Centralized, and Distributed Version Control
![image](https://github.com/leeseobin00/temp-repo/assets/70849467/5f8a401d-ecd6-4b71-b70f-6f8933c07627)
- Local
  - Controlling the version within your personal computer
  - Difficulty collaborating with others

- Centralized
  - Central server is present
  - The server records multiple versions and requests the central server if necessary
  - Get it and work on the local computer
  - Convenient in collaboration
  - Cons: If the central server goes down, it cannot be imported at that point & problems with uploading work from the local computer to the central computer
  
- Distributed (Git)
  - have a server computer
  - Each local computer has a copy of the database that the central computer has
  - Easy to recover even if files are corrupted or down
  - Also, when collaborating, you can merge and reflect it centrally
  - No need to communicate with the server until needed


## Three Staes in Git
![image](https://github.com/leeseobin00/temp-repo/assets/70849467/8866c0a1-6fff-43be-8023-813388fb3f21)
- Modified
  - Working Directory - Directory to contain common projects
- Staged
  - Staging Area - Intermediate steps to get to the Commit stage
- Committed
  - .git directory (Repository) 

## Installing Git
- Linux / Mac / Windows (check pre-installed version)
```
$ git --version
```
![image](https://github.com/leeseobin00/temp-repo/assets/70849467/75ab0425-ca0c-4544-9cf2-c27fdf812626)

- Linux (install on a Debian-based distribution)
- Mac
- Windows – Run “Git Bash”


## Git config: First-time setup
- Git configurations are stored in three levels:
- (1) System level: --system option. Affects all uses and repositories on the system (administrative)
  - file: /etc/gitconfig
- (2) Global (user) level: --global option. Affects all repositories of a current user
  - file: ~/.config/git/config
- (3) Local level: --local option. Specific to the current repository
  - file: .git/gitconfig
- * Each level overrides values in the previous level: system -> global -> local

```
$ git config --global user.name "leeseobin00"

$ git config --global user.email "leeseobin000709@gmail.com"

$ git config --global init.defaultBranch "main"

$ git config --list

$ git config --list --show-origin

$ git config user.name
```
![image](https://github.com/leeseobin00/temp-repo/assets/70849467/83e9dddb-0b4a-4e73-ac1f-efc81661b33a)


## Initializing a Repository in an Existing Directory

```
$ git init 
```
Initializes a Git repository. When you run this command, the current directory becomes a Git repository.

```
$ git status
```
Checks the status of your current working directory. It shows any changes like modified files or new files.

```
$ git add [file_name]
```
Adds a specific file to the staging area. This file will be included in the next commit.

```
$ git add .
```
Adds all modified files and new files to the staging area. This command stages all changes at once.

```
$ git rm -cached [file_name]
```
Stops tracking a file in Git, and the file will remain untracked. This file is treated similarly to files listed in .gitignore.   

```
$ git commit -m “commit message”
```
Commits the changes in the staging area. You provide a commit message to describe the commit.   


## Ignoring a file
.gitignore file
The .gitignore file is used to specify which files and directories should be excluded from being tracked in a Git repository.
```
# ignore all .a files
*.a

#but do track lib.a, even though you're ignoring .a files above
!lib.a

# only ignore the TODO file in the current directory, not subdir/T
ODO
/TODO

# ignore all files in any directory named build
build/

# ignore doc/notes.txt, but not doc/server/arch.txt
doc/*.txt

# ignore all .pdf files in the doc/ directory and any of its subdirectories
doc/**/*.pdf
```
- Exclude Unnecessary Files
- Security and Confidentiality
- Efficiency in Version Control


## Change branch name
The provided code snippet demonstrates how to change the name of the current branch in a Git repository. 
```
$ git branch

$ git branch -m master main

$ git branch 

$ git status
```















