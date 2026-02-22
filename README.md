# Campaign Evaluation System
Command line Python application for evaluating B2B campaign performance using standard digital marketing KPIs.

The application allows users to input campaign performance data, calculate efficiency metrics, interpret results against benchmarks, and compare multiple campaigns in a structured output table.

This repository forms part of a practical data engineering portfolio project. It demonstrates incremental development from a simple calculator to a structured multi campaign reporting tool. The system is designed as a foundation for future work involving data persistence, warehousing, and pipeline automation.

---

## Nomenclature

**CTR (Click Through Rate)**
Clicks divided by impressions.

**CPC (Cost per Click)**
Campaign spend divided by traffic uplift.

**CPM (Cost per 1,000 impressions)**
Campaign spend divided by impressions.

**Campaign record**
A structured collection of campaign inputs and calculated metrics stored in memory using Python dictionaries.

---

## Technical documentation

### Before running the application

Requirements:

* Python 3.9 or higher installed
* Command line or terminal access

No external libraries are required.

---

### Running the application

From the project root directory:

```bash
python src/week03_multi_campaign.py
```

Follow the prompts to enter campaign data.

---

### Project structure

```
src/
  week01_single_campaign.py
  week02_validation.py
  week03_multi_campaign.py
```

Week 1
Single campaign KPI calculator.

Week 2
Input validation and benchmark interpretation.

Week 3
Multi campaign data entry and comparison reporting using in memory data structures.

---

### Application design

* command line interface for user interaction
* procedural processing of campaign inputs
* in memory storage using Python lists and dictionaries
* incremental feature development across versions

---

### Further documentation

Future technical documentation will be added as the project expands.

Planned areas include:

* data persistence
* CSV and JSON handling
* SQL database integration
* data warehousing
* workflow orchestration

---

## Licence

This project is provided for portfolio and educational purposes.
