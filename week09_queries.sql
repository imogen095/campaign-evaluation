-- 1. View all campaigns
SELECT * FROM campaigns;

-- 2. Top 3 campaigns by impressions
SELECT * FROM campaigns
ORDER BY impressions DESC
LIMIT 3;

-- 3. Campaigns with high CTR (> 0.04)
SELECT * FROM campaigns
WHERE CTR > 0.04;

-- 4. Campaigns with low CPC (< 2)
SELECT * FROM campaigns
WHERE CPC < 2;

-- 5. Count number of campaigns
SELECT COUNT(*) FROM campaigns;

-- 6. Average CTR across campaigns
SELECT AVG(CTR) FROM campaigns;

-- 7. Campaign with highest budget
SELECT * FROM campaigns
ORDER BY budget DESC
LIMIT 1;

-- 8. Campaign with lowest CPM
SELECT * FROM campaigns
ORDER BY CPM ASC
LIMIT 1;

-- 9. Campaigns with clicks over 500
SELECT * FROM campaigns
WHERE clicks > 500;

-- 10. Order campaigns by CTR (descending)
SELECT name, CTR
FROM campaigns
ORDER BY CTR DESC;