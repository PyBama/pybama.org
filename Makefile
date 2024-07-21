install:
	@rye sync --force
	@rye run app assets build
	@rye run app assets install

lint:
	@rye lint --fix
	@rye fmt

fmt:
	@rye fmt

fmt-check:
	@rye fmt --check

test:
	@rye test

run:
	@rye run app run --debug --reload

docs-serve:
	@echo "not implemented"\

applet:
	@echo "Generating new applet in 'src/pybama_org/components/'..."
	@rye run copier copy gh:JacobCoffee/applet-template src/pybama_org/components/
