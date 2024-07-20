install:
	@rye sync --force

lint:
	@rye lint --fix
	@rye fmt

fmt:
	@rye fmt

fmt-check:
	@rye fmt --check

test:
	@rye test
