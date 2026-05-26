# git commands


## Do this **once** when you first start working on the project

`git clone <URL>` 

this will download everything in the lastest repo

---

## sanity check
`git status` : check if anything is wrong, check for things like "error, fault, fatal etc"

`git branch` : check what branch you're on

`git checkout <exsiting_branch_name>` : (if you're not on the branch you want to commit, usually you should NOT commit to the default branch (main) )

`git checkout -b <new_branchName>` : if you want to make a new branch

## Error handling
`git branch -u origin/<remote-branch-name>` : Set the upstream remote  branch for the local branch you are on to track

`git reflog` : show commit history and hashes (dense)

`git log` : show commit history and hashes (verbose), press q to quit

`git reset --soft <commit-hash>` : Revert to a specific past commit, uncommitted changes are saved

**Dangerous**<br>
`git reset --hard <commit-hash>` : Revert to a specific past commit, all uncommitted changes are deleted forever


## fetching new updates
`git fetch origin` : fetch all the new updates from other branch in github website (no merge)

`git pull origin main` : fetch and merge from the remote main branch

`git rebase --autostash origin/main` : use the current remote main as the new base to work on your new changes, conflict might occur

`git merge origin/<branch>` : merge the new changes, merge conflict might happen, don't panic if so, if not sure ask Sean

## adding your changes locally
`git add -A` : add all new changes to local git branch (local history)

`git add -u` : add update/deleteion and modification only (no untrack files)

`git reset <file>` : unstage the file

## commit
`git commit -m "<message>"` : commit the change to your local branch , <message> is the description of this commit, single lined.

## pushing
before running this
pls make sure you're not on the default branch, run `git branch` to check

`git push` : push to the remote branch

Use `git push -u origin <new branch name>` if you want to push to a new remote branch. 

if everything went well
in github website 
submit a pull request
Sean will check it