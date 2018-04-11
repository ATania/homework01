# Homework 01
The purpose of this exercise is mainly to get you all set up, install python and git the correct way, and practice some git. You can follow the instructions in this file without downloading the repository yet, as you'll probably need to get git and Python first.

To get this exercise done, you need to be able to use your terminal. If you are not 
comfortable with using the terminal try one of these tutorial

* https://www.codecademy.com/learn/learn-the-command-line
* https://de.udacity.com/course/shell-workshop--ud206

In the following, if you are asked to *run* a command like

    $ run this command

it means that you should type `run this command` in the terminal and press <kbd>Enter</kbd>.

## Installation instructions

### conda

Download  Miniconda https://conda.io/miniconda.html with Python 3.6.

##### For Linux/Mac OS
To start the installer run

    $ bash Miniconda3-latest-Linux-x86_64.sh

Most options can just be answered with yes, however you should insist on adding `conda` to your PATH when the installer asks you.

#### For Windows
Start the graphical installer, it should guide through the installation process. If you don't have another python-installation already installed, you can safely add python to your %PATH%, such that you can it from your normal `cmd`-shell. In any case, you should have a program named "Anaconda prompt" installed afterward, which you can find with the start menu. If you didn't add it to your %PATH% as instructed above, you need to run all `conda`-commands in the Anaconda prompt, otherwise you can use the normal `cmd` or `Powershell`.

 You can test if you have the correct python-version there by typing ``python --version``, which should tell you it's Python 3.6.x

### git

#### For Linux

To install, open a terminal and run

    $ sudo apt-get install git
    
#### For Mac
Install Homebrew if you don't have it already from https://brew.sh/. Then run

    $ brew install git

#### For Windows

Download the `.exe` from https://git-scm.com/download/win and run the installer.


#### For Windows

In the install wizard, make sure that git **can** be used from the command prompt, otherwise you'd have to switch between shells when coding and committing to git. To make sure your solution will be accepted once pushed, you need to set one of the two *commit unix style* options. Other than that, you'll probably go for the *openSSL* as well as *Windows default console as terminal emulator* options.

## Working on the exercise

### Clone your repository
Enter the terminal and navigate to a directory where you want to put your homework. Run
    
    $ git clone <URL>
    
where `<URL>` is the link you get from clicking the `Clone or download` button to the top right of your github repository web page (most probably the page you are on right now). 

### Create a new environment
Next you have to create a virtual environment for working on your homework, run

    $ conda create -n scientific python=3.6

This will create a new environment and install without anything else.


Afterwards, you need to activate the environment.

##### For Linux/Mac OS

To activate the environment, run

    $ source activate scientific

#### For Windows

Open the program Anaconda prompt, it will give you a typical Windows `cmd`-style shell. The command to activate the environment is

    $ activate scientific

on Windows. Your shell should indicate the environment you are in if it worked.


Always activate the environment when you work on the homework. To deactivate the
environment again, run `source deactivate` on Linux/Mac OS, or `deactivate` in Windows.

To open the Python interpreter run

    $ python

the prompt should start with something like

    Python 3.6.3 |Anaconda, Inc.|

close the interpreter again by running

    >>> quit()

## Your first homework assignment
After activating the `scientific` environment, run 

    $ pip install pytest
    
`pip` is the Python package manager that is used to install new packages (**p**ip **i**nstalls 
**p**ackages). `pip install <package-name>` is a universal command that can used to install any package 
you need. The packages will always the installed into the environment that is currently active,
so make sure to activate your environment.

`pytest` will automatically collect all test from the directory you run it in. 
It will give you feedback on all tests that your homework has to pass.
In order for this to happen you need to navigate to the directory where
you put your homework and run

    $ pytest
    
to see how the tests are currently failing.     

Open the file `hello_world.py` and modify the function `say_hello` in such a
way that it says hello to the world. The docstring should give you a hint.

Then run

    $ pytest

again to see whether your function passes the test. If not, `pytest` should give
you a helpful message on what to change.
Once all test are passing, `add` and `commit` your changes and `push` them to github.
Look in the lecture slides, if you need help with git.


## Important note
Make sure you create your repository at least 15 minutes before the deadline, and to push your last changes also enough in advance such that you can be sure your changes are considered. To be certain everything is okay, check if there is a green mark next to your latest commit.
