"""
WEEK 7 – Files (Persistence with JSON)

Goal:
- Store multiple campaigns in a LIST
- Each campaign is stored as a DICTIONARY
- Allow the user to interact with the program using a simple MENU
- Save campaign data to a JSON file
- Load campaign data back from a JSON file

New concepts this week:
- Files let programs save data permanently
- JSON stores structured data in a readable format
- json.dump() writes Python data to a file
- json.load() reads file data back into Python
- File handling allows data to persist after the program closes

Structure of the program:

1) Functions handle reusable tasks
   - get_non_empty_string() → safely get text
   - get_int() → safely get numbers
   - calc_kpis() → calculate campaign metrics
   - print_table() → display campaign results neatly
   - save_campaigns() → save campaign data to JSON
   - load_campaigns() → load campaign data from JSON

2) The main() function runs a MENU loop

3) Campaign data is stored in memory as:
   campaigns = [
       {campaign1 dictionary},
       {campaign2 dictionary}
   ]

4) Campaign data can also be stored in:
   data/campaigns.json
"""


import json

# -------- FUNCTIONS --------


def get_non_empty_string(prompt):
    # Ask the user for text input and ensure it is not empty.

    while True:  # repeat until valid input
        value = input(prompt).strip()  # remove extra spaces

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
            value = int(raw_text)  # convert text → integer

        except ValueError:
            print("Enter a valid whole number.")
            continue

        # Optional rule: enforce minimum value
        if min_value is not None and value < min_value:
            print(f"Number must be at least {min_value}.")
            continue

        return value


def calc_kpis(record):
    # Calculate CTR, CPC and CPM using campaign data.

    impressions = record["impressions"]
    clicks = record["clicks"]
    budget = record["budget"]

    # CTR = clicks ÷ impressions
    ctr = clicks / impressions

    # CPM = cost per thousand impressions
    cpm = (budget / impressions) * 1000

    # Prevent division-by-zero if clicks = 0
    if clicks == 0:
        cpc = None
    else:
        # CPC = cost ÷ clicks
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


def save_campaigns(campaigns):
    # Save the campaigns list to a JSON file.
    # "w" means write mode.
    # If the file does not exist yet, Python will create it.

    with open("data/campaigns.json", "w") as file:
        json.dump(campaigns, file, indent=2)

    print("Campaigns saved.")


def load_campaigns():
    # Load campaign data from a JSON file.
    # If the file does not exist yet, return an empty list instead of crashing.

    try:
        with open("data/campaigns.json", "r") as file:
            campaigns = json.load(file)

        print("Campaigns loaded.")
        return campaigns

    except FileNotFoundError:
        print("No saved campaigns found.")
        return []


# -------- MAIN PROGRAM --------


def main():
    """
    Main program loop.

    The menu allows the user to:
    1) Add campaigns
    2) View campaigns
    3) Show summary statistics
    4) Save campaigns to file
    5) Load campaigns from file
    6) Exit the program
    """

    campaigns = []  # list to store campaign dictionaries in memory

    while True:

        # ---- MENU ----
        print("\nCampaign Tracker")
        print("1. Add campaign")
        print("2. List campaigns")
        print("3. Summary")
        print("4. Save")
        print("5. Load")
        print("6. Exit")

        choice = input("Choose option:\n... ").strip()

        # ---- ADD CAMPAIGN ----
        if choice == "1":

            name = get_non_empty_string("Campaign name:\n... ")
            impressions = get_int("Impressions:\n... ", min_value=1)
            clicks = get_int("Clicks:\n... ", min_value=0)
            budget = get_int("Budget (£):\n... ", min_value=0)

            # Create dictionary storing campaign inputs
            record = {
                "name": name,
                "impressions": impressions,
                "clicks": clicks,
                "budget": budget
            }

            # Calculate performance metrics
            metrics = calc_kpis(record)

            # Merge campaign data + KPI metrics into one dictionary
            full_record = {**record, **metrics}

            # Store dictionary inside campaigns list
            campaigns.append(full_record)

            print("Campaign added successfully.")

        # ---- LIST CAMPAIGNS ----
        elif choice == "2":

            if len(campaigns) == 0:
                print("No campaigns stored yet.")
            else:
                print_table(campaigns)

        # ---- SUMMARY STATISTICS ----
        elif choice == "3":

            if len(campaigns) == 0:
                print("No campaigns to summarise.")
                continue

            # Aggregate campaign totals
            total_budget = sum(c["budget"] for c in campaigns)
            total_impressions = sum(c["impressions"] for c in campaigns)
            total_clicks = sum(c["clicks"] for c in campaigns)

            # Calculate average CTR
            avg_ctr = total_clicks / total_impressions

            print("\nSUMMARY")
            print("Campaign count:", len(campaigns))
            print("Total budget:", total_budget)
            print("Total impressions:", total_impressions)
            print("Total clicks:", total_clicks)
            print("Average CTR:", round(avg_ctr, 3))

        # ---- SAVE CAMPAIGNS ----
        elif choice == "4":
            # Save the current in-memory campaigns list to file
            save_campaigns(campaigns)

        # ---- LOAD CAMPAIGNS ----
        elif choice == "5":
            # Replace the current in-memory list with the loaded file data
            campaigns = load_campaigns()

        # ---- EXIT PROGRAM ----
        elif choice == "6":

            print("Exiting campaign tracker.")
            break

        else:
            print("Invalid option. Please choose 1–6.")


# Program entry point
if __name__ == "__main__":
    main()