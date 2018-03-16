### Python Machine Learning Example

based on this [tutorial](https://machinelearningmastery.com/machine-learning-in-python-step-by-step/)

### Setting up Python on Mac OSX

1. Install [pyenv](https://github.com/pyenv/pyenv) python version manager by following the instructions for installing with [brew](https://github.com/pyenv/pyenv#homebrew-on-mac-os-x).

2. Install a recent version of python with pyenv (as of March 15, 2018 - `3.6.4` is latest)

3. Make a directory and setup a pyenv instance

    a. Set version of python to use for this project

        ```
        mkdir my-project
        cd my-project

        # this is like generating an .nvmrc file for nvm
        pyenv local 3.6.4

        # check that your local python version is equal to version set above
        python --version
        > Python 3.6.4
        ```

    b. set up private packages

        ```
        # from inside project directory `my-project/`
        # this is like running npm init
        python -m venv .

        # start the python virtual environment
        source bin/activate

        # add a package
        pip install numpy

        # list your packages
        pip list

        # deactivate the python virtual environment
        deactivate

        # check that the packages were only installed on the virtual environment
        pip list
            # list should not contain numpy
        ```

4. Install your required packages

 
    This tutorial required the packages listed below. If you followed along above, you will need to reactivate your python virtual environment with `source bin/activate` and then run `pip install` for each of the packages below.

    * sklearn
    * matplotlib
    * scipy
    * numpy (you should already have this install if you follow along above)
    * pandas

5. Save required packages so you can install them easily on another machine

    ```
    pip freeze > requirements.txt
    ```

6. Install packages from a requirements.txt file

    ```
    pip install -r requirements.txt
    ```
