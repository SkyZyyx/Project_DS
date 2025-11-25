# Monthly Sales Analysis Project

A data science project analyzing monthly sales data for four products using NumPy, Pandas, Matplotlib, and Seaborn.

## 📋 Project Overview

This project generates synthetic monthly sales data for 4 products over 12 months and performs comprehensive analysis including:
- Data generation and validation
- Statistical analysis and metrics calculation
- Pivot tables for quarterly insights
- Data visualizations (line charts, bar charts, heatmaps, boxplots)
- Business insights extraction

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- UV package manager (recommended) or pip

### Installation

Using **UV** (recommended - faster):
```bash
# Install UV if you haven't
pip install uv

# Clone the repository
git clone <your-repo-url>
cd project_sales

# Install dependencies
uv pip install -r requirements.txt
```

Using **pip**:
```bash
pip install -r requirements.txt
```

### Running the Project

**Option 1: Python Script**
```bash
uv run python phase2_generate_data.py
```

**Option 2: Jupyter Notebook**
```bash
uv run jupyter lab
# Then open notebook.ipynb
```

## 📁 Project Structure

```
project_sales/
├── data/                      # Generated datasets
│   ├── initial.csv           # Raw generated data
│   ├── Final.csv            # Enhanced dataset with metrics
│   └── output.csv           # Final results with pivot tables
├── .agent/                   # Agent configuration
│   └── python_ml_rules.md   # Development rules and guidelines
├── utils.py                  # Utility functions
├── notebook.ipynb           # Main Jupyter notebook
├── phase2_generate_data.py  # Python script version
├── test_utils.py            # Unit tests for utilities
├── requirements.txt         # Project dependencies
└── README.md               # This file
```

## 🛠️ Technologies Used

- **NumPy**: Numerical operations and random data generation
- **Pandas**: DataFrame manipulation and analysis
- **Matplotlib**: Data visualization
- **Seaborn**: Statistical visualizations
- **Jupyter**: Interactive development environment

## 📊 Features

### Phase 1-2: Data Generation ✅
- Generate 12 monthly dates (Jan-Dec 2025)
- Random sales data for 4 products with different ranges
- Export to CSV format

### Phase 3: DataFrame Enhancement (In Progress)
- Calculate total and average sales
- Month-over-month growth analysis
- Quarterly categorization
- Identify max/min performing products

### Phase 4-7: Advanced Analysis (Planned)
- Pivot tables for quarterly summaries
- Key business insights
- Comprehensive visualizations
- Business recommendations

## 📈 Sample Output

```
Product A range: 56-100 (expected: 50-100) ✓
Product B range: 31-80 (expected: 30-80) ✓
Product C range: 22-48 (expected: 20-60) ✓
Product D range: 10-47 (expected: 10-50) ✓
```

## 🧪 Testing

Run tests for utility functions:
```bash
uv run python test_utils.py
```

## 📝 Development Guide

See `.agent/python_ml_rules.md` for:
- Package management best practices
- Code organization standards
- Data science workflow guidelines
- Performance optimization tips

## 🤝 Contributing

This is an educational project. Feel free to:
- Fork the repository
- Experiment with different data ranges
- Add new visualizations
- Improve analysis methods

## 📄 License

This project is for educational purposes.

## 👤 Author

Said - Data Science Student

---

**Note**: This project uses UV for faster package management. All commands shown use `uv run` prefix.
