# This programme helps campaign leads evaluate campaigns
# using simple performance metrics

# Ask user for total campaign impressions
campaign_impressions = int(input("Share campaign impressions:\n"))
# input() stores data as a string by default, so int() converts it to a number

# Ask user for website traffic before campaign
precampaign_traffic = int(input("Share website traffic before campaign:\n"))
# Stores traffic before campaign started

# Ask user for website traffic during campaign
livecampaign_traffic = int(input("Share website traffic during campaign:\n"))
# Stores traffic while campaign was live

# Ask user for campaign budget
campaign_budget = int(input("What was the campaign budget:\n"))
# Budget converted from string to integer

# Ask user for highest performing social copy
highest_post = input("What post performed best:\n")
# Stored as string (no conversion needed)

# Calculate click-through rate (CTR)
# CTR = clicks divided by impressions
CTR = livecampaign_traffic / campaign_impressions
print("CTR:", round(CTR, 3))

# Calculate cost per click (CPC)
# Uses uplift in traffic (after - before)
CPC = campaign_budget / (livecampaign_traffic - precampaign_traffic)
print("CPC:", round(CPC, 2))

# Calculate cost per mille (CPM)
# Cost per impression
CPM = campaign_budget / campaign_impressions
print("CPM:", round(CPM, 2))

# Identify character count of highest performing post
# len() counts how many characters are in the string
print("Length of highest performing post:", len(highest_post))