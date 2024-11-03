# Makefile for Rust Project
all: install check build format lint test

rust-version:
	@echo "Rust command-line utility versions:"
	rustc --version 			#rust compiler
	cargo --version 			#rust package manager
	rustfmt --version			#rust code formatter
	rustup --version			#rust toolchain manager
	clippy-driver --version		#rust linter

check:
	cargo check

install:
	# Install if needed
	#@echo "Updating rust toolchain"
	#rustup update stable
	#rustup default stable

build:
	cargo build

format:
	cargo fmt

lint:
	cargo clippy

test:
	cargo test

release:
	cargo build --release

python_install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

python_test:
	python -m pytest -vv --cov=main --cov=mylib test_*.py

python_format:	
	black *.py 

python_lint:
	ruff check *.py mylib/*.py

python_container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

python_refactor: format lint

python_deploy:
	#deploy goes here
		
python_all: install lint test format deploy

#Debug mode: binary is found at target/debug/
#release mode: binary is found at target/release. Uses full optimisations.
generate_and_push:
	# Add, commit, and push the generated files to GitHub
	@if [ -n "$$(git status --porcelain)" ]; then \
		git config --local user.email "action@github.com"; \
		git config --local user.name "GitHub Action"; \
		git add .; \
		git commit -m "Add metric log"; \
		git push; \
	else \
		echo "No changes to commit. Skipping commit and push."; \
	fi