# Starting Off with Git

## What is Git?
Git is a version control system that locally stores the versions and changes to a project.
These changes can then be merged with the original after testing and review.<br>
It can be installed by downloading it from https://git-scm.com/downloads/win and going though the normal executions you would do with any other application.

## Configuring your device
Changing name/email: ```git config --global user.[name/email] "*Name*"```<br>
Setting default branch: ```git config --global init.defaultbranch main ```

## Working with directories
Check which directory you are in: ```pwd```<br>
Creating a new directory: ```mkdir "*Name*"```<br>
Change directory:``` cd "*Name*"```<br>
Look at the files within the directory: ```ls``` (use ```-al``` for more information)

## Working with local repositories
There are 3 stages: Working (short term memory) --> Staging (working memory) --> Repo (long term memory)<br>
Create a new repo: ```git init```<br>
New file: Notepad ```*Name*.md```<br>
Check the status of repo (whether any changes need to be added to repo): ```git status```<br>
Working --> Staging:``` git add [*filename* / .]```<br>
Staging --> Repo:``` git commit -m "*My message"```<br>
Check differences in file and repo file: ```git diff```<br>
Check log: ```git log```

## Working with network repositories
Connect local to GitHub: ```git remote add origin (*URL*)```<br>
Local to network: ```git push origin "*Branch Name*"```<br>
Entire network repo to local: ```git clone (*URL*)```<br>
Pull modified repo (already on local): ```git pull origin```

## Branches
A branch is a way of editing the documents before the changes are implimented in the main file.<br>
See the branch: ```git branch```<br>
Create new branch: ```git checkout -b "*BranchName*"```<br>
Change branch: ```git checkout "*BranchName*"```<br>
Merge branches: ```git merge "*BranchName*"```<br>
[If there are conflicts in merging, open the file!]

## Summary
Git is like a brain:
- the working stage being your short term memory where you add or change information
- the staging stage is the working memory pushing information back and forth
- the repo stage is the long term memory, a large collection of everything you knew and the changes made
- these 'memories' can then be uploaded to GitHub for everyone to see<br>
The main commands are to do with managing file location and are summarised here:
!["Stages of Git"](https://blog.isquaredsoftware.com/images/2021-01-career-advice-git-usage/git-staging-workflow.png)

