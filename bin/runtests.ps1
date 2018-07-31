mkdir -f -p tmp | Out-Null

py.test -rw --doctest-modules --junitxml=tmp/tests.xml --cov=intrinio --cov-report term-missing --cov-report xml:tmp/coverage.xml --cov-report html:tmp/coverage.html --ignore=setup.py .
