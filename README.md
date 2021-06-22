## "Junior DevOps Engineer Assignment"
Provides Fibonacci, Factorial and Ackermann functions via a REST server.
### How to setup the project?
Command below creates the venv and installs required packages defined in requirements.txt.

    python helper.py --create


### How to run the server?
Command below will run the server.

    $ python helper.py --run
    
Alternatively you can activate venv and run below directly.

    (venv) $ python app.py


### Usage
Any browser can be used to access the server: http://127.0.0.1:5000/

    / 20210623063732
    // http://127.0.0.1:5000/
    
    {
      "definitions": {
        
      },
      "info": {
        "description": "Provides Fibonacci, Factorial and Ackermann functions.",
        "title": "Junior DevOps Engineer Assignment",
        "version": "1.0"
      },
      "paths": {
        "/ackermann?m=<number1>&n=<number2>": {
          "Sample": {
            "_url": "/ackermann?m=2&n=3",
            "response": "{'result':9}"
          }
        },
        "/factorial?n=<number>": {
          "Sample": {
            "_url": "/factorial?n=5",
            "response": "{'result':120}"
          }
        },
        "/fibonacci?n=<number>": {
          "Sample": {
            "_url": "/fibonacci?n=5",
            "response": "{'result':3}"
          }
        }
      },
      "swagger": "2.0"

#### Fibonacci
Url: http://127.0.0.1:5000/fibonacci?n=<number>

    // 20210623063636
    // http://127.0.0.1:5000/fibonacci?n=30
    
    {
      "result": 514229
    }

#### Factorial
Url: http://127.0.0.1:5000/factorial?<number>

    // 20210623063530
    // http://127.0.0.1:5000/factorial?n=3
    
    {
      "result": 6
    }

#### Ackermann
Url: http://127.0.0.1:5000/ackermann?m=<number>&n=<number>
    
    // 20210623063326
    // http://127.0.0.1:5000/ackermann?m=2&n=3
    
    {
      "result": 9
    }
    
#### Bad requests

    // 20210623063806
    // http://127.0.0.1:5000/fibonacci?n=asdf
    
    {
      "_status": "BAD_REQUEST",
      "errors": [
        [
          "ERROR - Non integer argument provided: 'asdf'."
        ]
      ]
    }
    
    
    // 20210623063948
    // http://127.0.0.1:5000/ackermann?
    
    {
      "_status": "BAD_REQUEST",
      "errors": [
        "'m' parameter is missing",
        "'n' parameter is missing"
      ]
    }
    
    // 20210623064021
    // http://127.0.0.1:5000/fibonacci?n=10000000
    
    {
      "_status": "BAD_REQUEST",
      "errors": [
        [
          "ERROR - Please provide a positive integer less than 100000 for arg1: '10000000'."
        ]
      ]
    }
    
    // 20210623064039
    // http://127.0.0.1:5000/fibonacci?n=1.6
    
    {
      "_status": "BAD_REQUEST",
      "errors": [
        [
          "ERROR - Non integer argument provided: '1.6'."
        ]
      ]
    }

### TODO
1. Helper script to check global Python version - minimum Python3.7.
2. Unit tests to be added.
3. Monitoring scripts to be extended.
4. REST API in yaml to be provided.# CaseStudy
