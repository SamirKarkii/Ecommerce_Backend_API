## PostgreSQL Setup on Windows

If `psql` is not recognized:

1. Find `psql.exe` inside:
   `C:\Program Files\PostgreSQL\<version>\bin`

2. Add that `bin` folder to the Windows PATH.

3. Restart PowerShell.

4. Verify:

   `psql --version`


## Environment variables

1. Install python-dotenv
2. Import os and load_dotenv
3. Define BASE_DIR
4. Run load_dotenv(BASE_DIR / ".env")
5. Read values with os.environ["VARIABLE_NAME"]