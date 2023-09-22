## Installation and Configuration

You can install and configure the KU Polls app by following these steps.

1. Open a command-line interface
    - MacOS or Linux: Open the Terminal.
    - Windows: Open the Command Prompt, PowerShell, or Windows Terminal, depending on which you prefer.

2. Check Python is installed
    ```bash
    python --version
    ```
    > If Python is installed, it should show the version.

3. Clone the repository from GitHub
    ```bash
    git clone https://github.com/xNatthapol/ku-polls.git
    ```

4. Change the directory to the ku-polls project
    ```bash
    cd ku-polls
    ```

5. Create a Virtual Environment
    ```bash
    python -m venv venv
    ```

6. Activate the Virtual Environment
- On MacOS or Linux
    ```bash
    source venv/bin/activate
    ```
- On Windows
    ```cmd
    venv\Scripts\activate
    ```

7. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```

8. Create .env file and copy the content from sample.env file
- On MacOS or Linux
    ```bash
    cp sample.env .env
    ```
- On Windows
    ```cmd
    copy sample.env .env
    ```

9. Run migrations
    ```bash
    python manage.py migrate
    ```

10. Load data from the data fixtures
    ```bash
    python manage.py loaddata data/polls_no_votes.json
    python manage.py loaddata data/users.json
    ```

11. Run tests
    ```bash
    python manage.py test
    ```

12. Run server
    ```bash
    python manage.py runserver
    ```
    > If CSS is not loading on your website, you can try to clear the browser cache.<br>
    >
    > If you're using Google Chrome, follow these steps:
    > 1. Open Chrome's Settings
    > 2. Search for "cache"
    > 3. Click on "Clear browsing data"
    > 4. Select "Cached images and files"
    > 5. Click "Clear data"
    > 6. Reload the web page
