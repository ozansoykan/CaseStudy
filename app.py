from flask import Flask, request, jsonify
from flask_swagger import swagger

from calculations.utils import fib, fact, ack

app = Flask(__name__)


@app.route('/')
def index():
    """
    Root endpoint. Provides usage.
    Note: Not using standards API descriptions.

    :return: api usage in json
    """
    swag = swagger(app)
    swag['info']['description'] = "Provides Fibonacci, Factorial and Ackermann functions."
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "Junior DevOps Engineer Assignment"
    swag['paths']['/fibonacci?n=<number>'] = {"Sample": {"_url": "/fibonacci?n=5", "response": "{'result':3}"}}
    swag['paths']['/factorial?n=<number>'] = {"Sample": {"_url": "/factorial?n=5", "response": "{'result':120}"}}
    swag['paths']['/ackermann?m=<number1>&n=<number2>'] = \
        {"Sample": {"_url": "/ackermann?m=2&n=3", "response": "{'result':9}"}}
    return jsonify(swag)


def run_method(func, *args):
    """
    Runs given method with url arguments.
    Returns 400 BAD_REQUEST if args are missing or not valid.

    :param func: function to run
    :param args: url args provided
    :return: response json
    """
    errors = []
    error_status = 400
    func_args = []
    try:
        for arg in args:
            # Find whether arguments are provided
            arg_in_request = request.args.get(arg)
            if arg_in_request:
                # Argument provided -> Add to function args
                func_args.append(arg_in_request)
            else:
                # Argument missing -> Append to error messages
                errors.append(f"'{arg}' parameter is missing")
        if not errors:
            # All required arguments provided -> Run the function adn return response
            return jsonify({"result": func(*func_args)})
    except ValueError as e:
        errors.append([str(e)])
    except Exception as e:
        # This is for demoing. Better not to expose error message to user.
        errors.append([str(e)])
        error_status = 500
    finally:
        # Check whether any error raised when running the function
        if errors:
            # Errors raised -> Return error response
            return jsonify({"_status": "BAD_REQUEST", "errors": errors}), error_status


@app.route('/fibonacci')
def calculate_fibonacci():
    """
    Calculates nth Fibonacci number.

    n comes from url args.

    :return: nth Fibonacci number
    """
    return run_method(fib, "n")


@app.route('/factorial')
def calculate_factorial():
    """
    Calculates n factorial.
    n comes from url args.

    :return:
    """
    return run_method(fact, "n")


@app.route('/ackermann')
def calculate_ackermann():
    """
    Calculates Ackerman function with given args.
    m and n comes from url args.

    :return: result of Ackerman(m,n)
    """
    return run_method(ack, "m", "n")


if __name__ == '__main__':
    app.run()
