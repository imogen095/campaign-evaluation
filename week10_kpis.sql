-- Per-campaign KPI view
SELECT
  name,
  impressions,
  clicks,
  budget,
  CTR,
  CPC,
  CPM
FROM campaigns;

-- Top CTR campaign
SELECT
  name,
  CTR
FROM campaigns
ORDER BY CTR DESC
LIMIT 1;