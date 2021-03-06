vows test:
	@env PYTHONPATH=. python pyvows/console.py --cover --cover_package=pyvows --cover_package=pyvows.assertions --cover_threshold=80.0 --profile tests/

ci_test:
	@env PYTHONPATH=. python pyvows/console.py --cover --cover_package=pyvows --cover_package=pyvows.assertions --cover_threshold=80.0 -r pyvows.coverage.xml -x tests/

setup:
	@pip install --requirement=REQUIREMENTS

publish:
	python setup.py sdist upload

.PHONY: vows test setup publish ci_test
