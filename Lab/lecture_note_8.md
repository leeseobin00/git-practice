## Lecture Note 8
### Git Branching and Merging

- Branching: Diverge from the “main” development stream and
work without interrupting the main branch 

- Merging: Uniting two branches to one branch 

- Why matters? 
  - Developing without messing with the deployed “main” branch 
  - Testing a new feature, issue resolving, error fixing, … 
  - Test sufficiently before you deploy
  - (Remote branch) Collaboration

### Making a new git repository
```
$ git branch-test/
$ git init

$ echo "# practicing git branching and merging" >> README.md
$ cat README.md
# practing git branching and merging

$ echo "first edition" >> edition.txt
$ cat edition.txt
first edition

$ ls -lha
```

### Commit the new repository
```
$ git status
$ git add .
$ git commit -m "first commit"
```

```
$ nano edition.txt
$ cat edition.txt
$ git add edition.txt
$ git commit -m "second commit"
```

### Checking commit log
```
$ git log
```

### Making and Switching to a new branch
```
$ git branch
$ git branch testing
$ git log --oneline --decorate
$ git checkout testing
```

### Commit at the new branch
```
$ echo "add a new feature" >> new_feature.txt
$ git add new_feature.txt
$ git commit -m "new feature"
$ ls - lha
$ git log --oneline --decorate
```

### Switching to master branch
```
$ git checkout master
$ ls - lha
```

### Resolving an issue at master branch
```
$ nano edition.txt
$ cat edition.txt
$ git add edition.txt
$ git commit -m "issue closed"
$ git log --oneline --decorate --graph --all
```

### git merge
```
$ git merge testing
$ git log --oneline --decorate --graph --all
$ git branch -d testing
$ git branch
```

### Check merged repository
```
$ ls -lha
$ cat edition.txt
```
