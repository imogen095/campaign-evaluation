# Campaign Evaluation System

Command line Python application for evaluating B2B campaign performance using standard digital marketing KPIs.

The application allows users to input campaign performance data, calculate efficiency metrics, interpret results against benchmarks, and compare multiple campaigns in a structured output table.

This repository forms part of a practical **data engineering portfolio project**. It demonstrates incremental development from a simple calculator to a structured multi-campaign reporting tool. The system is designed as a foundation for future work involving data persistence, data pipelines, warehousing, and workflow automation.

---

# Example output

Example CLI output when listing campaign performance:

```
Campaign Name           CTR       CPC (£)      CPM (£)
------------------------------------------------------
Spring Launch          0.045        2.31        13.20
Summer Promotion       0.038        2.90        11.75
Autumn Webinar         0.051        1.98        14.50
```

Example summary output:

```
SUMMARY
Campaign count: 3
Total budget: £2200
Total impressions: 75000
Total clicks: 3120
Average CTR: 0.042
```

---

# Nomenclature

**CTR (Click Through Rate)**
Clicks divided by impressions.

**CPC (Cost per Click)**
Campaign spend divided by clicks.

**CPM (Cost per 1,000 impressions)**
Campaign spend divided by impressions multiplied by 1000.

**Campaign record**
A structured collection of campaign inputs and calculated metrics stored in memory using Python dictionaries.

---

# Technical documentation

## Requirements

Before running the application ensure you have:

* Python **3.9 or higher**
* Command line or terminal access

No external libraries are required. The project uses only the Python standard library.

---

# Running the application

From the project root directory:

```bash
python week08_csv.py
```

Follow the menu prompts to:

* add campaign performance data
* calculate campaign KPIs
* compare campaign results
* save campaign data to JSON
* export and import campaign data as CSV files

---

# Project structure

```
week01_single_campaign.py
week02_validation.py
week03_multi_campaign.py
week04_functions.py
week05_defensive_input.py
week06_campaign_tracker.py
week07_persistence.py
week08_csv.py

data/
  campaigns.json
  campaigns.csv
```

---

# Development progression

This project demonstrates structured incremental development across multiple versions.

### Week 1 – Single campaign KPI calculator

A simple script that calculates CTR, CPC, and CPM for a single campaign.

### Week 2 – Input validation

Improved user input validation and interpretation of KPI results against benchmarks.

### Week 3 – Multi campaign comparison

Support for multiple campaigns using Python lists and dictionaries with formatted reporting tables.

### Week 4 – Functions and modularisation

Refactoring logic into reusable functions for improved structure and maintainability.

### Week 5 – Defensive input handling

Robust validation and error handling to prevent application crashes from incorrect input.

### Week 6 – Campaign tracker interface

Introduction of a menu-driven command line interface to manage campaigns interactively.

### Week 7 – JSON persistence

Campaign records can be saved and loaded using JSON files via the Python `json` module.

### Week 8 – CSV export and import

Campaign data can be exported to and imported from CSV files using the Python `csv` module.

This introduces a simple **file-based data pipeline** and basic **ETL concepts**.

---

# Application design

The application uses a simple procedural architecture:

* command line interface for user interaction
* campaign records stored as Python dictionaries
* collections of campaigns stored in lists
* modular functions for calculations and file operations
* incremental feature development across versions

The project intentionally avoids external dependencies to focus on core Python and data processing fundamentals.

---

# Future development

Planned future expansions include:

* SQL database storage
* automated ETL pipelines
* campaign reporting dashboards
* workflow orchestration
* integration with marketing analytics data sources
* basic data warehouse modelling

---

# Licence

This project is provided for **portfolio and educational purposes**.
