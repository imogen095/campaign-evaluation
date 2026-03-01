"""
WEEK 5 – Debugging & Defensive Input

Goal:
- Prevent crashes from bad user input
- Practice reading error messages (tracebacks)
- Document 3 bugs and fixes in a separate .md file
"""

# --------- FUNCTIONS ---------

def get_non_empty_string(prompt):
    # Ask for text and make sure it is not empty.
    while True:
        value = input(prompt).strip()
        if value == "":
            print("Error - input required.")
            continue
        return value


def get_int(prompt, min_value=None):
    # Ask for a whole number and safely handle bad input.
    while True:
        try:
            raw_text = input(prompt).strip()
            value = int(raw_text)  # this can fail if user types letters
        except ValueError:
            # If conversion fails, we catch the error instead of crashing.
            print("Enter a valid whole number.")
            continue

        if min_value is not None and value < min_value:
            print(f"Number must be at least {min_value}.")
            continue

        return value


def calc_kpis(record):
    # Calculate CTR, CPC, CPM from campaign dictionary.

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


# --------- MAIN PROGRAM ---------

def main():
    campaigns = []
    running = True

    while running:
        name = get_non_empty_string("Enter campaign name:\n... ")
        impressions = get_int("Impressions:\n... ", min_value=1)
        clicks = get_int("Clicks:\n... ", min_value=0)
        budget = get_int("Budget (£):\n... ", min_value=0)
        highest_post = input("Best performing post:\n... ").strip()

        record = {
            "name": name,
            "impressions": impressions,
            "clicks": clicks,
            "budget": budget,
            "highest_post": highest_post
        }

        metrics = calc_kpis(record)

        print(f"CTR: {metrics['CTR']:.3f}")
        if metrics["CPC"] is None:
            print("CPC: N/A (0 clicks)")
        else:
            print(f"CPC: £ {metrics['CPC']:.2f}")
        print(f"CPM: £ {metrics['CPM']:.2f}")

        campaigns.append({**record, **metrics})

        while True:
            another = input("Add another campaign? (y/n)\n... ").strip().lower()
            if another == "y":
                break
            if another == "n":
                running = False
                break
            print("Error. Type y or n.")

    print_table(campaigns)


if __name__ == "__main__":
    main()