install:
	@rye sync --force
	@npm install

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
	@npm run dev

run-api:
	@rye run app run --debug --reload

run-frontend:
	@npm run next-dev

docs-serve:
	@echo "not implemented"\

applet:
	@echo "Generating new applet in 'src/pybama_org/components/'..."
	@rye run copier copy gh:JacobCoffee/applet-template src/pybama_org/components/
