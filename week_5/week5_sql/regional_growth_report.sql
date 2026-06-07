SELECT
	region,
	COUNT(CASE
			WHEN gdp_pc_cagr_cat = 'Strong' THEN 1
			END) AS strong_cantones,
	COUNT(canton) AS total_cantones,
	ROUND(100.0 * COUNT(CASE
							WHEN gdp_pc_cagr_cat = 'Strong' THEN 1
							END) / COUNT(canton), 2) AS strong_percentage
FROM
	socioeconomic_analysis
GROUP BY
	region;