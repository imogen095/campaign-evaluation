# This programme helps B2B campaign leads evaluate LinkedIn campaigns
# using simple performance metrics

# Ask user for total campaign impressions
campaign_impressions = int(input("Share campaign impressions:\n"))
if campaign_impressions <= 0:
    print("Error, too few impressions to analyse meaningful results.")
    exit()

# Ask user for website clicks during campaign
campaign_clicks = int(input("Share campaign clicks:\n"))
if campaign_clicks <= 0:
    print("Error, campaign website clicks required to deliver meaningful results.")
    exit()

# Ask user for campaign budget
campaign_budget = int(input("What was the campaign budget:\n"))
if campaign_budget < 0:
    print("Error, budget required to analyse results.")
    exit()

# Ask user for highest performing social copy
highest_post = input("What post performed best:\n")

# -----------------------
# CTR
# -----------------------
CTR = campaign_clicks / campaign_impressions
print("CTR:", round(CTR, 3))

if CTR >= 0.02:
    print("CTR of 2% or higher is excellent by industry standards\n.")
elif CTR >= 0.01:
    print("CTR between 1% and 2% is good by industry standards\n.")
else:
    print("CTR below 1% is below benchmark\n.")

# -----------------------
# CPC
# -----------------------
CPC = campaign_budget / campaign_clicks
print("CPC: £", round(CPC, 2))

if CPC <= 1:
    print("Very good CPC\n.")
elif CPC <= 3:
    print("Average CPC\n.")
elif CPC <= 5:
    print("High CPC\n.")
else:
    print("Very high CPC — may need optimisation\n.")

# -----------------------
# CPM (LinkedIn)
# -----------------------
# CPM = (cost / impressions) * 1000
CPM = (campaign_budget / campaign_impressions) * 1000
print("CPM: £", round(CPM, 2))

if CPM <= 15:
    print("Very good CPM for LinkedIn B2B\n.")
elif CPM <= 25:
    print("Normal CPM for LinkedIn B2B\n.")
elif CPM <= 40:
    print("High CPM, but common on LinkedIn\n.")
else:
    print("Very high CPM — audience likely very competitive\n.")

# -----------------------
# Character count
# -----------------------
print("Length of highest performing post:", len(highest_post))