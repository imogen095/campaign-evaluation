"""
WEEK 8 - CSV Export and Import

Goal:
- Keep the Week 7 JSON persistence version
- Add CSV export
- Add CSV import
- Convert CSV text values back to numbers after loading
- Keep the same menu-driven campaign tracker structure
"""

import csv
import json
import os

DATA_DIR = "data"
JSON_FILE = os.path.join(DATA_DIR, "campaigns.json")
CSV_FILE = os.path.join(DATA_DIR, "campaigns.csv")


# -------- FUNCTIONS --------

def ensure_data_dir():
    # Create the data folder if it does not already exist.
    os.makedirs(DATA_DIR, exist_ok=True)


def get_non_empty_string(prompt):
    # Ask the user for text input and ensure it is not empty.
    while True:
        value = input(prompt).strip()

        if value == "":
            print("Error - input required.")
            continue

        return value


def get_int(prompt, min_value=None):
    # Ask the user for a whole number (integer).
    # Prevent crashes if the user types text instead of numbers.
    # Optionally enforce a minimum allowed value.
    while True:
        try:
            raw_text = input(prompt).strip()
            value = int(raw_text)

        except ValueError:
            print("Enter a valid whole number.")
            continue

        if min_value is not None and value < min_value:
            print(f"Number must be at least {min_value}.")
            continue

        return value


def calc_kpis(record):
    # Calculate CTR, CPC and CPM using campaign data.
    impressions = record["impressions"]
    clicks = record["clicks"]
    budget = record["budget"]

    ctr = clicks / impressions
    cpm = (budget / impressions) * 1000

    if clicks == 0:
        cpc = None
    else:
        cpc = budget / clicks

    return {
        "CTR": ctr,
        "CPC": cpc,
        "CPM": cpm
    }


def print_table(rows):
    # Print a formatted summary table of all campaigns.
    print()
    print(f"{'Campaign Name':<20}{'CTR':>10}{'CPC (£)':>12}{'CPM (£)':>12}")
    print("-" * 54)

    for r in rows:
        if r["CPC"] is None:
            cpc_display = "N/A"
        else:
            cpc_display = f"{r['CPC']:.2f}"

        print(
            f"{r['name']:<20}"
            f"{r['CTR']:>10.3f}"
            f"{cpc_display:>12}"
            f"{r['CPM']:>12.2f}"
        )


def save_campaigns_json(campaigns):
    # Save the campaigns list to a JSON file.
    ensure_data_dir()

    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(campaigns, file, indent=2)

    print("Campaigns saved to JSON.")


def load_campaigns_json():
    # Load campaign data from a JSON file.
    # If the file does not exist yet, return an empty list instead of crashing.
    ensure_data_dir()

    try:
        with open(JSON_FILE, "r", encoding="utf-8") as file:
            campaigns = json.load(file)

        print("Campaigns loaded from JSON.")
        return campaigns

    except FileNotFoundError:
        print("No saved JSON campaigns found.")
        return []


def export_campaigns_csv(campaigns):
    # Export the campaigns list to a CSV file.
    ensure_data_dir()

    if len(campaigns) == 0:
        print("No campaigns available to export.")
        return

    fieldnames = ["name", "impressions", "clicks", "budget", "CTR", "CPC", "CPM"]

    with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(campaigns)

    print("Campaigns exported to CSV.")


def import_campaigns_csv():
    # Import campaign data from a CSV file.
    # CSV stores values as text, so convert numeric fields back to numbers.
    ensure_data_dir()

    try:
        campaigns = []

        with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row["CPC"] in ("", "N/A", "None"):
                    cpc_value = None
                else:
                    cpc_value = float(row["CPC"])

                campaign = {
                    "name": row["name"],
                    "impressions": int(row["impressions"]),
                    "clicks": int(row["clicks"]),
                    "budget": int(row["budget"]),
                    "CTR": float(row["CTR"]),
                    "CPC": cpc_value,
                    "CPM": float(row["CPM"])
                }

                campaigns.append(campaign)

        print("Campaigns imported from CSV.")
        return campaigns

    except FileNotFoundError:
        print("No CSV file found.")
        return []


def show_summary(campaigns):
    if len(campaigns) == 0:
        print("No campaigns to summarise.")
        return

    total_budget = sum(c["budget"] for c in campaigns)
    total_impressions = sum(c["impressions"] for c in campaigns)
    total_clicks = sum(c["clicks"] for c in campaigns)

    avg_ctr = total_clicks / total_impressions

    print("\nSUMMARY")
    print("Campaign count:", len(campaigns))
    print("Total budget:", total_budget)
    print("Total impressions:", total_impressions)
    print("Total clicks:", total_clicks)
    print("Average CTR:", round(avg_ctr, 3))


# -------- MAIN PROGRAM --------

def main():
    """
    Main program loop.

    The menu allows the user to:
    1) Add campaigns
    2) List campaigns
    3) Show summary statistics
    4) Save campaigns to JSON
    5) Load campaigns from JSON
    6) Export campaigns to CSV
    7) Import campaigns from CSV
    8) Exit the program
    """

    campaigns = []

    while True:
        print("\nCampaign Tracker")
        print("1. Add campaign")
        print("2. List campaigns")
        print("3. Summary")
        print("4. Save JSON")
        print("5. Load JSON")
        print("6. Export CSV")
        print("7. Import CSV")
        print("8. Exit")

        choice = input("Choose option:\n... ").strip()

        if choice == "1":
            name = get_non_empty_string("Campaign name:\n... ")
            impressions = get_int("Impressions:\n... ", min_value=1)
            clicks = get_int("Clicks:\n... ", min_value=0)
            budget = get_int("Budget (£):\n... ", min_value=0)

            record = {
                "name": name,
                "impressions": impressions,
                "clicks": clicks,
                "budget": budget
            }

            metrics = calc_kpis(record)
            full_record = {**record, **metrics}

            campaigns.append(full_record)

            print("Campaign added successfully.")

        elif choice == "2":
            if len(campaigns) == 0:
                print("No campaigns stored yet.")
            else:
                print_table(campaigns)

        elif choice == "3":
            show_summary(campaigns)

        elif choice == "4":
            save_campaigns_json(campaigns)

        elif choice == "5":
            campaigns = load_campaigns_json()

        elif choice == "6":
            export_campaigns_csv(campaigns)

        elif choice == "7":
            campaigns = import_campaigns_csv()

        elif choice == "8":
            print("Exiting campaign tracker.")
            break

        else:
            print("Invalid option. Please choose 1–8.")


if __name__ == "__main__":
    main()