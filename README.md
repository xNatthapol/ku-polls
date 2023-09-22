## KU Polls: Online Survey Questions 
[![Unittest](https://github.com/xNatthapol/ku-polls/actions/workflows/python-app.yml/badge.svg)](https://github.com/xNatthapol/ku-polls/actions/workflows/python-app.yml)

An application to conduct online polls and surveys based
on the [Django Tutorial project][django-tutorial], with
additional features.

This app was created as part of the [Individual Software Process](
https://cpske.github.io/ISP) course at Kasetsart University.


## Requirements

Requires Python 3.8 and later.  Required Python packages are listed in [requirements.txt](./requirements.txt). 


## Install and Run

### How to Install and Configure

You can install and configure the project by following the [Installation](Installation.md).

### How to Run

1. Activate the Virtual Environment
- On MacOS or Linux
    ```bash
    source venv/bin/activate
    ```
- On Windows
    ```cmd
    venv\Scripts\activate
    ```

2. Start the Django Development Server
    ```bash
    python manage.py runserver
    ```
    If you receive an error message indicating that the port is unavailable, try running the server on a different port (1024 thru 65535), such as
    ```bash
    python manage.py runserver 12345
    ```

3. Navigate to http://localhost:8000 in your web browser.
   
4. To stop the server, press **Ctrl-C** / **control-C** in the terminal window.

5. Exit the virtual environment by closing the window or typing
    ```bash
    deactivate
    ```

## Demo Accounts

### Demo Admin

| Username  |    Password    |
|:---------:|:--------------:|
|   admin   |  istudyisp123  |

This is the admin we generated as a demo. You can use this to login to the admin page of KU Polls.

### Demo User

| Username  |    Password     |
|:---------:|:---------------:|
|  user001  |  nopassword001  |
|  user002  |  nopassword002  |

This is the user we generated as a demo. You can use this to login to KU Polls.

## Project Documents

All project documents are in the [Project Wiki](../../wiki/Home).

- [Vision Statement](../../wiki/Vision%20Statement)
- [Requirements](../../wiki/Requirements)
- [Development Plan](../../wiki/Development%20Plan)
- [Domain Model](../../wiki/Domain%20Model)
- [Iteration 1 Plan](../../wiki/Iteration%201%20Plan)
- [Iteration 2 Plan](../../wiki/Iteration%202%20Plan)
- [Iteration 3 Plan](../../wiki/Iteration%203%20Plan)
- [Iteration 4 Plan](../../wiki/Iteration%204%20Plan)

[django-tutorial]: https://docs.djangoproject.com/en/4.2/intro/tutorial01/
