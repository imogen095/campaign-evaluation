"""
WEEK 4 UPDATE (from Week 3)

1) We moved repeated code into FUNCTIONS
   - Why: so we don’t copy/paste the same “ask user / check input” code again and again.
   - This makes the program easier to read, fix and reuse.

2) We added a small TESTS function (run_tests) using assert
   - Why: so we can quickly check our maths works before a user types anything.
   - This helps catch mistakes early.

3) We separated jobs into clear parts:
   - get_int(...) = get a whole number safely (with validation)
   - calc_kpis(...) = do the KPI maths (CTR / CPC / CPM)
   - print_table(...) = show a neat results table
   - main() = runs the interactive program (the “main loop”)

4) We still store each campaign as a DICTIONARY
   - Why: a dictionary lets us label each piece of data (like "name", "CTR") with a key.

Roadmap words you should know here:
- function, list, dictionary, boolean, loop, input validation, return, assert, try/except
"""


# --------- FUNCTIONS (reusable blocks of code) ---------

def get_non_empty_string(prompt):
    # This function asks the user for text and makes sure it is not empty.
    while True:  # loop forever until we return a good answer
        value = input(prompt).strip()  # get text and remove extra spaces
        if value == "":  # check if user typed nothing
            print("Error - input required.")  # show error message
            continue  # go back to top of loop
        return value  # return the valid string


def get_int(prompt, min_value=None):
    # This function asks for a whole number (integer) and checks it is valid.
    while True:
        try:
            raw_text = input(prompt).strip()  # get text input
            value = int(raw_text)  # convert text to integer
        except ValueError:
            print("Error — enter a whole number.")  # if conversion fails
            continue

        if min_value is not None and value < min_value:
            # this checks rules like impressions must be at least 1
            print(f"Error — must be at least {min_value}.")
            continue

        return value  # return the valid number

def calc_kpis(record):
    # This function takes ONE campaign dictionary and calculates KPIs.
    # It returns another dictionary with CTR, CPC, and CPM.

    impressions = record["impressions"]  # get impressions from dictionary
    clicks = record["clicks"]  # get clicks from dictionary
    budget = record["budget"]  # get budget from dictionary

    ctr = clicks / impressions  # CTR formula
    cpm = (budget / impressions) * 1000  # CPM formula

    if clicks == 0:  # prevent divide-by-zero error
        cpc = None  # None means “not available”
    else:
        cpc = budget / clicks  # CPC formula

    return {
        "CTR": ctr,
        "CPC": cpc,
        "CPM": cpm
    }  # return results as a dictionary

def print_table(rows):
    # This function prints a summary table of all campaigns.

    print()
    print(f"{'Campaign Name':<20}{'CTR':>10}{'CPC (£)':>12}{'CPM (£)':>12}")
    print("-" * 54)

    for r in rows:  # loop through each campaign dictionary
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

def run_tests():
    # This function checks that our KPI maths works correctly.

    rec1 = {
        "name": "Test",
        "impressions": 1000,
        "clicks": 50,
        "budget": 100,
        "highest_post": "Example"
    }

    k1 = calc_kpis(rec1)
    assert abs(k1["CTR"] - 0.05) < 1e-9
    assert abs(k1["CPC"] - 2.0) < 1e-9
    assert abs(k1["CPM"] - 100.0) < 1e-9

    rec2 = {
        "name": "Zero Clicks",
        "impressions": 2000,
        "clicks": 0,
        "budget": 80,
        "highest_post": "Example"
    }

    k2 = calc_kpis(rec2)
    assert abs(k2["CTR"] - 0.0) < 1e-9
    assert k2["CPC"] is None
    assert abs(k2["CPM"] - 40.0) < 1e-9


# --------- MAIN PROGRAM ---------

def main():
    # This function runs the full interactive program.

    campaigns = []  # this is a list that will store campaign dictionaries
    running = True  # boolean that controls the main loop

    while running:
        name = get_non_empty_string("Enter campaign name:\n... ")
        impressions = get_int("Share campaign impressions:\n... ", min_value=1)
        clicks = get_int("Share campaign clicks:\n... ", min_value=0)
        budget = get_int("What was the campaign budget (£):\n... ", min_value=0)
        highest_post = input("What post performed best:\n... ").strip()

        base_record = {
            "name": name,
            "impressions": impressions,
            "clicks": clicks,
            "budget": budget,
            "highest_post": highest_post
        }  # dictionary storing campaign data

        metrics = calc_kpis(base_record)  # calculate KPIs

        print(f"CTR: {metrics['CTR']:.3f}")
        if metrics["CPC"] is None:
            print("CPC: N/A (0 clicks)")
        else:
            print(f"CPC: £ {metrics['CPC']:.2f}")
        print(f"CPM: £ {metrics['CPM']:.2f}")
        print("Length of highest performing post:", len(highest_post))

        full_record = {**base_record, **metrics}
        # merge two dictionaries into one bigger dictionary

        campaigns.append(full_record)  # add to the list

        while True:
            another = input("Add another campaign? (y/n)\n... ").strip().lower()
            if another == "y":
                break
            if another == "n":
                running = False
                break
            print("Error. Add another campaign? (y/n)")

    print_table(campaigns)  # show final summary table


if __name__ == "__main__":
    run_tests()  # run tests first
    main()  # then start program