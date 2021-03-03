To run the tests first setup a virtual environment, activate it, and
install the required Python packages for this project:

	$ python3 -m venv env
	$ source env/bin/activate
	$ pip install -r requirements.txt

___Running the tests___

Ensure the appropriate _driver_ is in your path. For this excercise I'm using Firefox with the latest version of Geckodriver on MacOS. Detail my vary for
Windows and varients of Unix.

To run the tests, specify the browser you wish the tests to be executed against.
For more information, see the [pytest-selenium documentation]

	$ py.test --driver Firefox


[pytest-selenium documentation]: http://pytest-selenium.readthedocs.org/
