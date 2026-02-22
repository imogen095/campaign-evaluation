# This programme helps B2B campaign leads evaluate LinkedIn campaigns
# using simple performance metrics

campaigns = []  # empty box to store campaigns

running = True  # keep program going
while running:  # repeat until told to stop

    while True:  # keep asking for name
        print('Enter campaign name:')  # ask for name
        name = input("...").strip()  # get name, remove spaces
        if name == "":  # if nothing typed
            print('Error - name required')  # say no
            continue  # ask again
        else:
            break  # name ok, move on

    # --- impressions ---
    while True:  # keep asking
        try:  # try number
            campaign_impressions = int(input("Share campaign impressions:\n"))  # get number
            if campaign_impressions <= 0:  # if bad number
                print("Error, too few impressions to analyse meaningful results.")  # say no
                continue  # ask again
            break  # number ok
        except ValueError:  # if not a number
            print("Error — enter a whole number.")  # say no

    # --- clicks ---
    while True:  # keep asking
        try:
            campaign_clicks = int(input("Share campaign clicks:\n"))  # get number
            if campaign_clicks <= 0:  # if bad
                print("Error, campaign website clicks required to deliver meaningful results.")
                continue
            break
        except ValueError:
            print("Error — enter a whole number.")

    # --- budget ---
    while True:
        try:
            campaign_budget = int(input("What was the campaign budget:\n"))  # get number
            if campaign_budget < 0:  # if bad
                print("Error, budget required to analyse results.")
                continue
            break
        except ValueError:
            print("Error — enter a whole number.")

    highest_post = input("What post performed best:\n")  # get best post text

    # --- CTR ---
    CTR = campaign_clicks / campaign_impressions  # clicks ÷ views
    print("CTR:", round(CTR, 3))  # show CTR

    # --- CPC ---
    CPC = campaign_budget / campaign_clicks  # cost ÷ clicks
    print("CPC: £", round(CPC, 2))  # show CPC

    # --- CPM ---
    CPM = (campaign_budget / campaign_impressions) * 1000  # cost per 1000 views
    print("CPM: £", round(CPM, 2))  # show CPM

    print("Length of highest performing post:", len(highest_post))  # count letters

    campaign = {  # make campaign record
        "name": name,
        "campaign_impressions": campaign_impressions,
        "campaign_clicks": campaign_clicks,
        "campaign_budget": campaign_budget,
        "CTR": CTR,
        "CPC": CPC,
        "CPM": CPM,
        "highest_post": highest_post
    }

    campaigns.append(campaign)  # save campaign
    print(campaigns)  # show saved campaigns

    while True:  # ask to continue
        print('Add another campaign? (y/n)')  # ask
        another = input("...").strip().lower()  # get answer

        if another == "y":  # if yes
            break  # do another campaign
        elif another == "n":  # if no
            running = False  # stop program
            break
        else:
            print('Error. Add another campaign? (y/n)')  # wrong answer

print()  # blank line

print(f"{'Campaign Name':<20}{'CTR':>10}{'CPC (£)':>12}{'CPM (£)':>12}")  # table header
print("-" * 54)  # line under header

for campaign in campaigns:  # for each campaign
    print(
        f"{campaign['name']:<20}"  # show name
        f"{campaign['CTR']:>10.3f}"  # show CTR
        f"{campaign['CPC']:>12.2f}"  # show CPC
        f"{campaign['CPM']:>12.2f}"  # show CPM
    )