# Project Euler Notebooks

Automatically load each Project Euler problem into its own notebook. The idea of this is to create a repository which is always up-to-date with the latest problems, so that a person can easily make a private fork of the repository and pull in new problems with git. The problems folder has a directory for each Project Euler problem, and if I have configured this correctly, a new commit will automatically add more whenever new problems are available.

To update the problems manually, run `python -m euler_binder`. Any missing problems will be populated, including any which have been deleted.

To get started on solving the problems, make a private fork of this repository and hop to it. Do make sure you keep it private, since the team at Project Euler would prefer you not share a solution with anyone who has not solved the problem already.

There is more which could be done on this project to handle the more exotic formatting in some of the problems. For example, some problems (such as problem 18) contain links to other problems which are not correctly resolved yet in the notebooks. That will be a project for another day.

# Copyright

I am putting my original code up here under the MIT license, so you are free to use it. The Project Euler problems, however, are covered by a much stricter creative commons license. [Have a look at it here.](https://projecteuler.net/copyright) All the problems are the original work of Project Euler and should be credited as such.
