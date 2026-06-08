/*--TOP GDP PER CAPITA CANTON BY REGION
WITH ranked_cantones AS (
	SELECT
		region,
		canton,
		gdp_pc,
		RANK() OVER (
			PARTITION BY region ORDER BY gdp_pc DESC)
		AS gdp_pc_rank
	FROM
		socioeconomic_analysis)

SELECT
	region,
	canton,
	gdp_pc
FROM
	ranked_cantones
WHERE
	gdp_pc_rank = 1
ORDER BY
	region*/

/*--GDP RANKING WITHIN REGION
SELECT
	region,
	canton,
	gdp,
	RANK() OVER (PARTITION BY region ORDER BY gdp DESC) AS gdp_rank
FROM
	socioeconomic_analysis*/

/*--GDP PER CAPITA GROWTH RANKING
SELECT
	region,
	canton,
	gdp_pc_cagr,
	DENSE_RANK() OVER (ORDER BY gdp_pc_cagr DESC) AS gdp_pc_cagr_rank
FROM
	socioeconomic_analysis*/

/*--GROWTH TYPE RANKING
SELECT
	growth_type,
	canton,
	gdp_cagr,
	RANK() OVER (PARTITION BY growth_type ORDER BY gdp_cagr DESC) AS rank_growth_type
FROM
	socioeconomic_analysis*/