import numpy as np
import pandas as pd

# GIT COMMANDS
# git init 
# git add .
# git commit -m "Initial commit" 
# git remote add origin git@github.com:stucchistefano/mycode.git  (So the origin from which the files are taken, like the github repository, which are basically the HTTPS/SSH links that we have copied and past from git hub)
# git push -u origin main ("main" is the name of the branch)


# TO SAVE AND COMMIT CHANGES
# git add .
# git commit -m "changed Testpy"   (with the name in the "" of the specific thing changed)
# git push origin main   (where "main" is the branch name in which we want to commit into)

# To know the branch name in where we are, we could look at the bottom-left and see it. 
# Alternatively, we could run the command "git branch" and press enter and it will give the branch name


# ERROR RECOVERY
# When we need to come back to a certain version of the code, even after a commit that completely changed the code, 
# we could go on github and on our repo, click on "Commits" button, go on the commit that we are sure that has the right code, 
# and then on it copy the SHA code/link and do this command (or ask the chatbot to return to the original code (even doing a new branch)):
# $ git checkout SHA_LINK-COPIED-AND-PASTED
# $ git branch -f main SHA_LINK-COPIED-AND-PASTED (to force the main)
# $ git checkout main  (switch to the main branch)
# $ git push origin main --force  (force push into the main of the changes)
# Where the $ could not be present since it states the directory of the terminal


# PULL REQUEST (PR)
# It is basically a cross-reference between a branch and the main, so to connect the branch to the main
# In this case we could see if there are some "merge conflicts" (so if there is something in the branch code that conflict with the main one and prevent the merging)
# TO CREATE A NEW BRANCH (and switch to it):
# git checkout -b Rename   (where "Rename" is the name of the new branch)

# If we want to see in which branch we are, we could perform the command "git branch" and the branch in where we are
# This new branch could be seen only when a "git add ." and a "git commit -m "Commit"" are done (so that the branch is no more local)
# And then we could see that after the commit, we need to push the commit now into the branch "Rename" in this way "git push origin Rename"
# And then, after we have done it also with the buttons on the left column here, we could go on git hub, compare&accept the pull request and merge the results/branch changes into the main
# Even after the pull request (bit before the merge one) we could see tha changes and the SHA code correlated with the commit, that we could copy&paste to return to original code if we have made some mistakes
# Going into the Open PR, we could go on the "three dots" icon and click on "Edit" and write all the changes done
# Usually before the merging, all the developers will leave a "review" on the left column on github and then the boss will see the reviews and complete the "merge" operation

# To delete the branch "Rename" that we have used to make changes and merge them in "main" we will use the command "git branch -D Rename"  (where "Rename" is the name of the branch to delete)
# To confirm how many branches we have then, we could do the command "git branch" (and see if there is only "*main" as branch)
# But the changes that we have made could not be present into the files of the main, thus we need to do the command "git pull origin main" (used to pull the updated main from the github origin)

# If we want to enter/have a certain branch that another developer have performed, we could see the name of the branch on github, then use the command "git checkout NAME_WANTED_BRANCH"


# .GITIGNORE FILE
# In this file we will put all the information that should not be loaded publicly online/on github (ad for the ".env" file where the API key are placed; or the "error_log" errors and functions)
# Thus, in this .gitignore file, we should put the names (below "/coverage") of the files (like ".env") that should not be loaded online in the code repository

# Builder's Console Log --> It is the forum to look for examples