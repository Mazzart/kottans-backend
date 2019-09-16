# Stage 0
## 1. Git and Github
I have gained new and expand existing knowledge of Git version control system. The Udacity course [How to use Git and Github](https://www.udacity.com/course/how-to-use-git-and-github--ud775) was a good starting point and gave a good overview of basic Git usage (create a repo, commit changes, review the history of commits, etc). I learned new commands, how to use them and what information they provide for example:

`git log —oneline` list one commit per line, shows the first 7 characters of the commit’s SHA and the commit message;

`git log —stat` displays the file(s) that have been modified, the number of lines that have been added/removed and a summary line with the total number of modified files and lines that have been added/removed;

`git log -p` or `git log —patch` displays the files that have been modified, the location of the lines that have been added/removed and the actual changes that have been made;

`git tag` add a marker on a specific commit;

`git commit --amend` alter the most-recent commit;

`git revert` reverses given commit (you have to provide SHA).

Other materials help to further improve skills and can be used in the future.

## 2. Unix Shell

[Linux Survival](https://linuxsurvival.com/linux-tutorial-introduction/) completion:

| Quiz                               | End of module                       |
| ---------------------------------- | ----------------------------------- |
|[Quiz 1](task_unix_shell/quiz_1.png)|[Module 1](task_unix_shell/end_1.png)|
|[Quiz 2](task_unix_shell/quiz_2.png)|[Module 2](task_unix_shell/end_2.png)|
|[Quiz 3](task_unix_shell/quiz_3.png)|[Module 3](task_unix_shell/end_3.png)|
|[Quiz 4](task_unix_shell/quiz_4.png)|[Module 4](task_unix_shell/end_4.png)|

Notes from the learned materials:
* The command `cd` followed by nothing, will change the working directory to your home directory;
* Useful additional options for some commands, for example: `ls -a` shows hidden files, `ls -l` shows files in long format, `ls -hlt` shows files in human readable, long form and sorted by time;
* In unix there are three spheres of permission — user, group, and other — as well as three particular types for each sphere — read, write, and execute. Use `chmod` command to change the permission of a file or directory;
* `cat` command prints the contents of the files;
* [Unix pipeline](https://en.wikipedia.org/wiki/Pipeline_(Unix));
* `man` command shows the manual pages;
* I/O redirection: use `>` to send output to file or `>>` to append to file;
* `ps` command displays process information, `ps aux` - shows all system processes;
* `grep` command searches for text in a file and returns the line(s) where it finds a match
