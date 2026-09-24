# 🚌 BMTC Data Analysis — BlueFleet 2025

An end-to-end **data analysis and visualization project** focused on analyzing **BMTC bus operations, fuel consumption, bus models, speed limits, and monthly fuel trends**.

The project uses **Python, Excel, and Power BI** to transform raw BMTC operational data into meaningful insights and interactive visualizations.

---

## 📌 Project Overview

Public transportation systems generate large volumes of operational data. Analyzing this data can help identify patterns in fuel consumption, vehicle performance, and operational efficiency.

**BlueFleet 2025** focuses on analyzing BMTC bus data to understand:

* 🚌 Bus fleet composition
* ⛽ Fuel consumption
* 🚍 Bus model performance
* 📅 Monthly fuel trends
* 🚦 Speed-limit patterns
* 📊 Operational statistics
* 📈 Trends across 2024 and 2025

---

## 🎯 Objectives

* Analyze BMTC bus operational data.
* Understand fuel consumption patterns.
* Compare different bus models.
* Analyze monthly fuel consumption trends.
* Study speed-limit information.
* Identify patterns and variations in fleet performance.
* Build interactive dashboards for data visualization.
* Generate meaningful insights from transportation data.

---

## 🛠️ Technologies Used

| Technology              | Purpose                       |
| ----------------------- | ----------------------------- |
| 🐍 **Python**           | Data cleaning and analysis    |
| 🐼 **Pandas**           | Data manipulation             |
| 🔢 **NumPy**            | Numerical analysis            |
| 📊 **Power BI**         | Interactive dashboards        |
| 📗 **Excel**            | Data preparation and analysis |
| 📈 **DAX**              | Power BI calculations         |
| 📓 **Jupyter Notebook** | Exploratory analysis          |

---

## 🔄 Project Workflow

```text
                Raw BMTC Data
                      │
                      ▼
              Data Cleaning
              & Preprocessing
                      │
                      ▼
              Exploratory Data
                  Analysis
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
      Python / Excel          Power BI
          │                       │
          └───────────┬───────────┘
                      ▼
              Visual Analytics
                      │
                      ▼
                Key Insights
```

---

## 🔍 Analysis Performed

### 🚌 Fleet Analysis

Analyzed the BMTC fleet to understand:

* Number of buses
* Bus model distribution
* Model-wise operational characteristics
* Fleet composition

### ⛽ Fuel Consumption Analysis

Analyzed fuel-related data to understand:

* Total fuel consumption
* Average fuel consumption
* Model-wise fuel usage
* Monthly fuel trends
* Changes across different periods

### 📅 Monthly Trend Analysis

Analyzed monthly data to identify:

* Increasing or decreasing fuel trends
* Monthly variations
* Seasonal patterns
* Changes between 2024 and 2025

### 🚦 Speed Limit Analysis

Analyzed speed-limit information across the fleet to understand differences between bus types and operational configurations.

---

## 📊 Power BI Dashboard

The Power BI dashboard provides an interactive view of the BMTC dataset.

### Dashboard Areas

* 🚌 Fleet Overview
* ⛽ Fuel Consumption
* 📈 Monthly Trends
* 🚍 Bus Model Analysis
* 🚦 Speed Limit Analysis
* 📊 Comparative Analysis

The dashboard allows users to interact with the data through filters and visualizations.

---

## 📈 Key Visualizations

The project includes visualizations such as:

* Fuel consumption by month
* Fuel consumption by bus model
* Fleet distribution
* Bus model comparison
* Monthly trend charts
* Speed-limit distribution
* KPI cards
* Interactive Power BI charts

---

## 🧹 Data Cleaning

Before analysis, the dataset was processed to improve data quality.

The preprocessing workflow included:

* Handling missing values
* Removing duplicate records
* Correcting data types
* Standardizing values
* Checking inconsistent records
* Preparing data for visualization

---

## 📂 Project Structure

```text
bmtc-data-analysis/
│
├── data/
│   └── bmtc_data.*
│
├── python/
│   └── bmtc_analysis.ipynb
│
├── powerbi/
│   └── bmtc_dashboard.pbix
│
├── excel/
│   └── bmtc_analysis.xlsx
│
├── visualizations/
│   └── dashboard_images/
│
├── README.md
└── requirements.txt
```

> The exact structure may vary depending on the files included in the repository.

---

## 🚀 Getting Started

### Clone the Repository

```bash
git clone https://github.com/buildwithnirvan/bmtc-data-analysis.git
```

### Navigate to the Project

```bash
cd bmtc-data-analysis
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Python Analysis

```bash
jupyter notebook
```

Open the BMTC analysis notebook from the `python/` directory.

---

## 📦 Python Requirements

```text
pandas
numpy
matplotlib
seaborn
jupyter
```

Install them using:

```bash
pip install -r requirements.txt
```

---

## 💡 Skills Demonstrated

This project demonstrates practical experience in:

* Data Cleaning
* Exploratory Data Analysis
* Python
* Pandas
* NumPy
* Microsoft Excel
* Power BI
* DAX
* Data Visualization
* Dashboard Development
* Trend Analysis
* KPI Development
* Data Interpretation

---

## 🔮 Future Improvements

Potential improvements include:

* 📊 Real-time BMTC data integration
* ⛽ Fuel-efficiency prediction
* 🤖 Machine learning-based fuel consumption prediction
* 🚌 Bus-level performance scoring
* 📍 Route-wise analysis
* 🗺️ Geographic visualization of routes
* 📈 Automated Power BI data refresh
* 🔮 Predictive maintenance analysis

---

## 👨‍💻 Author

### Nirvan M

**Data Analyst | Python | SQL | Power BI | Machine Learning**

GitHub: [@buildwithnirvan](https://github.com/buildwithnirvan)

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐.

**Turning transportation data into actionable insights. 🚌📊**
