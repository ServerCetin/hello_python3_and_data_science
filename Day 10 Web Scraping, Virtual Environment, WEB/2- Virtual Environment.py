# To start with project, it would be better to have a virtual environment. Virtual environment can help
# us to create an isolated or separate environment. This will help us to avoid conflicts in dependencies
# across projects. If you write pip freeze on your terminal you will see all the installed packages on your
# computer. If we use virtualenv, we will access only packages which are specific for that project. Open your
# terminal and install virtualenv

# Inside a folder create a flask_project folder.

# After installing the virtualenv package go to your project folder and create a virtual env by writing:
# python -m venv project  # for windows {project} is dynamic name that you can name

# activating on powershell
# project\Scripts\activate

# After you write the activation command, your project directory will start with project.

# let's install flask in this project
# pip install Flask
# pip freeze # checking packages

# When you finish you should deactivate active project using deactivate.
# deactivate