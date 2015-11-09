.venv:
	virtualenv -p python2.7 `pwd`/.venv
	. .venv/bin/activate && pip install -r requirements/development.txt

test: .venv
	. .venv/bin/activate && coverage run -a runtests.py
