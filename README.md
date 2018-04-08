# Homework 01
The purpose of this exercise is mainly to get you all set up, install python and git the correct way, and practice some git. You can follow the instructions in this file without downloading the repository yet, as you'll probably need to get git and python first.

## Installation instructions
Download  Miniconda https://conda.io/miniconda.html with Python 3.6.

##### For Linux/Mac OS
To start the installer run

    bash Miniconda3-latest-Linux-x86_64.sh

Most options can just be answered with yes, however you should insist on adding conda to your path when the installer asks you.

#### For Windows
Start the graphical installer, it should guide through the installation process. If you don't have another pyhton-installation already installed, you can savely add python to your %PATH%, such that you can it from your normal ``cmd``-shell. In any case, you should have a programm named "Anaconda prompt" installed afterward, which you can find with the start menu. If you didn't add it to your %PATH% as instructed above, you need to run all `conda`-commands in the Anaconda prompt, otherwise you can use the normal `cmd` or `Powershell`.

 You can test if you have the correct python-version there by typing ``python --version``, which should tell you it's Python 3.6.x

### git

Next, download the git VCS from https://git-scm.com/downloads, if you don't have it already.

##### For Linux/Mac OS

To install, open a terminal and run

    sudo apt-get install git

#### For Windows

In the install wizard, make sure that git **can** be used from the command promt, otherwise you'd have to switch between shells when coding and committing to git. To make sure your solution will be accepted once pushed, you need to set one of the two *commit unix style* options. Other than that, you'll probably go for the *openSSL* as well as *Windows default console as terminal emulator* options.

## Working on the exercise

Clone the repository by entering a terminal and using `git clone URL` in it, where URL means the link the `Clone or download` button to the top right of this webpage hints you at. Afterwards, open the directory in the terminal. It should contain a file `requirements.txt`. In the terminal, run

    conda create -n sheet1 --file requirements.txt python=3.6

Afterwards, you need to activate the environment.

##### For Linux/Mac OS

To activate the environment, run

    source activate sheet1

#### For Windows

Open the program Anaconda prompt, it will give you a typical Windows `cmd`-style shell. The command to activate the environment is

    activate sheet1

on Windows. Your shell should indicate the envionment you are in if it worked.

You should follow these steps for every new exercise sheet, as it creates the virtual environment containing all packages you need to solve the exercise.
This will create a new environment and install without anything else.
Always activate the enviornment when you work on the homework. To deactivate the
environment again, run `source deactivate` on Linux/Mac OS, or `deactivate` in Windows.

To open the python interpreter run

    python

the prompt should start with something like

    Python 3.6.3 |Anaconda, Inc.|


## Your first homework assignment
Open the file `hello_world.py` and modify the function `say_hello` in such a
way that it says hello to the world. The docstring should give you a hint.

Then run

    pytest

to see whether your function passes the test. If not, `pytest` should give
you a helpful message on what to change.
Once all test are passing, `add` and `commit` your changes and `push` them to github.
Look in the lecture slides, if you need help with git.

Make sure you create your repository at least 15 minutes before the deadline, and to push your last changes also enough in advance such that you can be sure your changes are considered. To be certain everything is okay, check if there is a green mark next to your latest commit.
