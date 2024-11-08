Whether you're trying to give back to the open source community or collaborating on your own projects, knowing how to properly fork and generate pull requests is essential. Unfortunately, it's quite easy to make mistakes or not know what you should do when you're initially learning the process. I know that I certainly had considerable initial trouble with it, and I found a lot of the information on GitHub and around the internet to be rather piecemeal and incomplete - part of the process described here, another there, common hangups in a different place, and so on.

This short tutorial is what I've found to be fairly standard procedure for creating a fork, doing your work, issuing a pull request, and merging that pull request back into the original project.

For the impatient, a short video: GitHub Pull Request in 100 Seconds, https://www.youtube.com/watch?v=8lGpZkjnkt4

## Creating a Fork

Just head over to the GitHub page and click the "Fork" button. It's just that simple. Once you've done that, you can use your favorite git client to clone your repo or just head straight to the command line:

```shell
# Clone your fork to your local machine
git clone git@github.com:USERNAME/FORKED-PROJECT.git
```

## Keeping Your Fork Up to Date

While this isn't an absolutely necessary step, if you plan on doing anything more than just a tiny quick fix, you'll want to make sure you keep your fork up to date by tracking the original "upstream" repo that you forked. To do this, you'll need to add a remote:

```shell
# Add 'upstream' repo to list of remotes
git remote add upstream https://github.com/UPSTREAM-USER/ORIGINAL-PROJECT.git

# Verify the new remote named 'upstream'; this displays all your remotes
git remote -v
```

Whenever you want to update your fork with the latest upstream changes, you'll need to first fetch the upstream repo's branches and latest commits to bring them into your repository:

```shell
# Fetch from upstream remote
git fetch upstream

# View all branches, including those from upstream
git branch -va
```

Now, checkout your own main branch and merge the upstream repo's main branch:

```shell
# Checkout your main branch and merge upstream
git checkout main
git merge upstream/main
```

If there are no unique commits on the local main branch, git will simply perform a fast-forward. However, if you have been making changes on main (in the vast majority of cases you probably shouldn't be - [see the next section](#doing-your-work), you may have to deal with conflicts. When doing so, be careful to respect the changes made upstream.

Now, your local main branch is up-to-date with everything modified upstream.

## Doing Your Work

### Create a Branch

Whenever you begin work on a new feature or bugfix, it's important that you create a new branch. Not only is it proper git workflow, but it also keeps your changes organized and separated from the main branch so that you can easily submit and manage multiple pull requests for every task you complete.

To create a new branch and start working on it:

```shell
# Checkout the main branch - you want your new branch to come from main
git switch main

# Create a new branch named newfeature (give your branch its own simple informative name)
# and switch to it
git switch -c newfeature
```

Now, go to town hacking away and making whatever changes you want to.

## Submitting a Pull Request

### Cleaning Up Your Work

Prior to submitting your pull request, you might want to do a few things to clean up your branch and make it as simple as possible for the original repo's maintainer to test, accept, and merge your work.

If any commits have been made to the upstream main branch, you should rebase your development branch so that merging it will be a simple fast-forward that won't require any conflict resolution work.

```shell
# Fetch upstream main and merge with your repo's main branch
git fetch upstream
git switch main
git merge upstream/main

# If there were any new commits, rebase your development branch (optional)
git switch newfeature
git rebase main
```

Optionally, it may be desirable to squash some of your smaller commits down into a small number of larger more cohesive commits. You can do this with an interactive rebase:

```shell
# Rebase all commits on your development branch
git checkout 
git rebase -i main
```

This will open up a text editor where you can specify which commits to squash. Feel free to skip this step when first going through this tutorial.

### Submitting

Once you've committed and pushed all of your changes to GitHub, go to the page for your fork on GitHub, select your development branch, and click the pull request button. If you need to make any adjustments to your pull request, just push the updates to GitHub. Your pull request will automatically track the changes on your development branch and update. 

When you create your PR, you should "Request a review" -- use the repository owner's github user ID. 

## Accepting and Merging a Pull Request

Take note that unlike the previous sections which were written from the perspective of someone that created a fork and generated a pull request (PR), this section is written from the perspective of the original repository owner who is handling an incoming pull request. Thus, where the "forker" was referring to the original repository as `upstream`, we're now looking at it as the owner of that original repository and the standard `origin` remote.

When the PR is created in your repository, you will first have to review it. To do that, in your repository's GitHub page, navigate to "Pull Requests", click on the pull request in the list, and go to "Files Changed", where you can comment on individual lines or ranges of lines. Alternatively, a prompt "review requested" will show up when you go to your repo (assuming the PR creator requested it as described in the previous section.)


Now that you're done with the development branch, you're free to delete it (optional step).

```shell
git branch -d newfeature
```

Based on: https://gist.github.com/Chaser324/ce0505fbed06b947d962
**Copyright**

Copyright 2017, Chase Pettit

MIT License, http://www.opensource.org/licenses/mit-license.php

**Additional Reading**

* [Atlassian - Merging vs. Rebasing](https://www.atlassian.com/git/tutorials/merging-vs-rebasing)

**Sources**

* [GitHub - Fork a Repo](https://help.github.com/articles/fork-a-repo)
* [GitHub - Syncing a Fork](https://help.github.com/articles/syncing-a-fork)
* [GitHub - Checking Out a Pull Request](https://help.github.com/articles/checking-out-pull-requests-locally)

```

```
