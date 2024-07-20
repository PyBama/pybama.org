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
	@rye run app run --debug

docs-serve:
	@echo "not implemented"\
