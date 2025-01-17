CONDA = $(shell which conda)
PYTHON = $(shell which python)

ENV_NAME = trainingenv

.PHONY: create-env install-deps run

create-env:
    @echo "Creating conda environment: $(ENV_NAME)"
    conda env create -f environment.yaml

install-deps:
    @echo "Activating environment: $(ENV_NAME) and installing dependencies"
    conda activate $(ENV_NAME) && pip install -r requirements.txt

update-deps:
    @echo "Updating requirements.txt and environment.yaml"
    pip freeze > requirements.txt
    conda list --export --no-builds > environment.yaml
    @echo "Dependencies updated in requirements.txt and environment.yaml"

run:
    @echo "Running main.py with environment: $(ENV_NAME)"
    python main.py

clean:
    @echo "Cleaning temporary files (excluding environment)..."
    rm -rf __pycache__ *.pyc *.pyo .pytest_cache

# USE WITH CAUTION!!!
clean-env:
    @echo "Removing conda environment: $(ENV_NAME)"
    conda env remove --name $(ENV_NAME)

env-info:
    @echo "Current Conda Environment: $(ENV_NAME)"
    conda info --envs

lint:
    @echo "Linting code..."
    pylint mymodule

format:
    @echo "Formatting code..."
    black .


