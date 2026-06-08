--TOP 3 GDP PER CAPITA GROWTH BY REGION
WITH ranked_cantones AS (
	SELECT
		region,
		canton,
		gdp_pc_cagr,
		RANK() OVER (
			PARTITION BY region ORDER BY gdp_pc_cagr DESC)
		AS gdp_pc_cagr_rank
	FROM
		socioeconomic_analysis)

SELECT
	region,
	canton,
	gdp_pc_cagr,
	gdp_pc_cagr_rank
FROM
	ranked_cantones
WHERE
	gdp_pc_cagr_rank <= 3
ORDER BY
	region