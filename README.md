# OpenAI API Text Completion Prediction for Generation Marketing Taglines

This is a marketing tagline generator [tutorial](). It may be setup as a [Cron](https://crontab.guru/) job on a system. Check out the tutorial or follow the instructions below to get set up.

## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/)

2. Clone this repository

3. Navigate into the project directory

   ```bash
   $ cd open_ai_cron_job
   ```

4. Create a new virtual environment

   ```bash
   $ python -m venv .
   $ . /bin/activate
   ```

5. Install the requirements

   ```bash
   $ pip install -r requirements.txt
   ```

6. Make a copy of the example environment variables file

   ```bash
   $ cp .env.example .env
   ```

7. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file

8. Run the script.

   ```bash
   $ python3 main.py
   ```
You should now be able to access  the output of the API response as a new line in the output.txt file in the same project directory.
For the full context behind this example app, check out the [tutorial](https://beta.openai.com/docs/quickstart).
