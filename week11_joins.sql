CREATE TABLE campaign_targets (
  name TEXT,
  target_ctr REAL
);

INSERT INTO campaign_targets VALUES
('send Spring Launch', 0.035),
('Summer Promo', 0.032),
('Autumn Webinar', 0.040),
('Winter Sale', 0.028);

SELECT
  c.name,
  c.CTR,
  t.target_ctr,
  c.CTR - t.target_ctr AS ctr_delta
FROM campaigns c
LEFT JOIN campaign_targets t
ON c.name = t.name;