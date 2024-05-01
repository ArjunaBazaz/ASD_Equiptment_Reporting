# Reporting Site Project

- Semester project for Advanced Software Development

- Teamates: Deyan Jani, Autin Mitra, Huarui Liu, Victor Pan

# Dependencies

Install dependencies using.
`pip install -r requirements.txt`

Add/remove dependencies to this file.

# Dev/Production

When developing on this app, use code default uses DEBUG mode. To use in PROD, add PROD to your environment.
This can be done on Linux/POSIX systems with `export PROD=true`.

Running this application in DEBUG means the application will use a local sqlite3 file.

# Setting up .env:

Create .env: In your project's root, make a .env file.
Add Variables: Define AWS_STORAGE_BUCKET_NAME as dev-computing_id-reportingsite in .env, replacing `computing_id` with your actual ID and replacing `your_computing_id` with your actual computing ID, and replacing `your_iam_user_access_key` and `your_iam_user_secret_access_key` with the credentials provided to you by AWS. This allows you to work with your own isolated storage bucket when developing.
Example:
AWS_STORAGE_BUCKET_NAME=dev-vmr8pg-reportingsite
AWS_ACCESS_KEY_ID=your_iam_user_access_key
AWS_SECRET_ACCESS_KEY=your_iam_user_secret_access_key
