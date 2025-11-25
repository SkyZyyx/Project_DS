# Python ML/DS Development Rules

## Package Management

### Use UV for Package Setup
- **ALWAYS use `uv` for package installation and management** - it's significantly faster than pip
- Install packages with: `uv pip install <package>`
- Create virtual environments with: `uv venv`
- Sync dependencies with: `uv pip sync requirements.txt`
- Add packages with: `uv add <package>` (if using uv's project management)

### Common ML/DS Packages
```bash
# Data manipulation and analysis
uv pip install numpy pandas polars

# Visualization
uv pip install matplotlib seaborn plotly

# Machine Learning
uv pip install scikit-learn xgboost lightgbm catboost

# Deep Learning
uv pip install torch torchvision tensorflow keras

# Model evaluation and deployment
uv pip install mlflow optuna wandb

# Jupyter and notebooks
uv pip install jupyter ipykernel jupyterlab
```

## Best Practices

### Code Organization
- Use clear, descriptive variable names
- Follow PEP 8 style guidelines
- Organize projects with standard structure:
  ```
  project/
  ├── data/
  │   ├── raw/
  │   ├── processed/
  │   └── external/
  ├── notebooks/
  ├── src/
  │   ├── data/
  │   ├── features/
  │   ├── models/
  │   └── visualization/
  ├── models/
  ├── reports/
  └── requirements.txt
  ```

### Data Science Workflow
1. **Exploratory Data Analysis (EDA)**: Always start with thorough data exploration
2. **Data Validation**: Check for missing values, outliers, data types
3. **Feature Engineering**: Document all transformations
4. **Model Selection**: Compare multiple models with consistent metrics
5. **Evaluation**: Use appropriate metrics for the problem type
6. **Reproducibility**: Set random seeds, save model configurations

### Performance Optimization
- Use vectorized operations with NumPy/Pandas instead of loops
- Leverage `polars` for large datasets (faster than pandas)
- Use `joblib` or `multiprocessing` for parallel processing
- Profile code with `cProfile` or `line_profiler` when needed

### Documentation
- Document data sources and assumptions
- Comment complex transformations
- Keep a changelog of experiments and results
- Use docstrings for functions and classes

### Version Control
- Track model versions and hyperparameters
- Use `.gitignore` for large data files and models
- Commit notebooks with cleared outputs
- Track dependencies in requirements.txt or pyproject.toml

## Technical Standards

### Jupyter Notebooks
- Clear markdown explanations between code cells
- Restart kernel and run all cells before sharing
- Keep notebooks focused on single tasks
- Export key functions to .py modules for reusability

### Model Development
- Always split data: train/validation/test
- Use cross-validation for robust evaluation
- Track experiments (manually or with MLflow/Weights & Biases)
- Save preprocessing pipelines with models

### Code Quality
- Write unit tests for data processing functions
- Use type hints for function signatures
- Handle exceptions appropriately
- Validate input data types and shapes

## Environment Setup

### Creating New Project
```bash
# Initialize UV project
uv venv .venv
source .venv/bin/activate  # On Linux/Mac
# .venv\Scripts\activate  # On Windows

# Install dependencies
uv pip install -r requirements.txt
```

### Jupyter Setup
```bash
# Install Jupyter with UV
uv pip install jupyter ipykernel

# Add virtual environment to Jupyter
python -m ipykernel install --user --name=project_name
```

---

**Last Updated**: 2025-11-24
**Priority**: ALWAYS use UV for package management
