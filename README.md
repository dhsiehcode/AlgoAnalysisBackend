# AlgoAnalysisBackend
Backend for Automatic Runtime Analysis

### Requirements

Must of the following installed
* Python >= 3.8
* Flask

### Running Project For Developement

#### Windows

Run the following in your anaconda prompt at your project's root
`flask --app flaskr --debug run` <br>
You should now see
```
 * Serving Flask app 'flaskr'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
```

Go to `http://127.0.0.1:5000/[url]` to see any of the pages

#### Mac


### Setting up database (if it doesn't exist)
A database should exist in `\instance` called `flaskr.sqlite`. If not, take the following steps. Run the server for developement. While the server is running, open another terminal (prompt) and run `flask --app flaskr init-db`. You should not see `Initialized the database.` and a file in `\instance` called `flaskr.sqlite`.
