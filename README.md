## Package Management

1. **Install packages from requirements.txt:**
    
    ```bash
    pip install -r requirements.txt
    ```
    
2. **List installed packages:**
    
    ```bash
    pip list
    ```
    
3. **Generate requirements.txt:**
    
    ```bash
    pip freeze > requirements.txt
    ```
    

## Conda Environment Management

1. **Create new environment:**
    
    ```bash
    conda create --name myenv python=3.9
    ```
    
2. **Activate environment:**
    
    ```bash
    conda activate myenv
    ```
    
3. **Deactivate environment:**
    
    ```bash
    conda deactivate
    ```
    
4. **List all environments:**
    
    ```bash
    conda env list
    ```
    
5. **Remove environment:**
    
    ```bash
    conda env remove --name myenv
    ```
    
6. **Export environment:**
    
    ```bash
    conda env export > environment.yml
    ```
    
7. **Create environment from file:**
    
    ```bash
    conda env create -f environment.yml
    ```
    

## Running Python Projects

1. **Run Python file:**
    
    ```bash
    python script.py
    ```
    
2. **Run Python module:**
    
    ```bash
    python -m module_name
    ```
    
3. **Run with arguments:**
    
    ```bash
    python script.py arg1 arg2
    ```
    
4. **Run interactive Python:**
    
    ```bash
    python
    ```
    

## Virtual Environment (venv) Commands

1. **Create virtual environment:**
    
    ```bash
    python -m venv myenv
    ```
    
2. **Activate virtual environment:**
    
    ```bash
    source myenv/bin/activate
    ```
    
3. **Deactivate virtual environment:**
    
    ```bash
    deactivate
    ```
    

## Useful Development Commands

1. **Check Python version:**
    
    ```bash
    python --version
    ```
    
2. **Update pip:**
    
    ```bash
    python -m pip install --upgrade pip
    ```
    
3. **Install package in editable mode:**
    
    ```bash
    pip install -e .
    ```
    
4. **Run tests:**
    
    ```bash
    python -m pytest
    ```
    

Note: Replace 'myenv' with your desired environment name and '[script.py](http://script.py)' with your actual Python file name.

### **Computer**

On your coworker’s machine:

1. **Clone the Repository**:
    
    ```bash
    git clone https://github.com/StechQ/your-repo-name.git
    cd your-repo-name
    ```
    
2. **Create the Environment from the `environment.yml` File**:
    
    ```bash
    conda env create -f environment.yml
    
    ```
    
3. **Activate the New Environment**:
    
    ```bash
    conda activate myenv
    ```
    
    Note: The environment name will be the same as specified in the `environment.yml` file.