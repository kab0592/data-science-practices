/*--Query 1: GDP by province
SELECT
	province,
	SUM(gdp)
FROM
	socioeconomic_analysis
GROUP BY
	province*/

/*--Query 2: Average CAGR GDP by region
SELECT
	region,
	AVG(gdp_cagr)
FROM
	socioeconomic_analysis
GROUP BY
	region*/

/*--Query 3: Top ten cantones by GDP per capita
SELECT
	canton,
	gdp_pc
FROM
	socioeconomic_analysis
ORDER BY
	gdp_pc DESC
LIMIT
	10*/

/*--Query 4: Number of cantones by growth type
SELECT
	COUNT(canton),
	growth_type
FROM
	socioeconomic_analysis
GROUP BY
	growth_type*/

/*--Query 5: Strong-growth cantones only
SELECT
	canton
FROM
	socioeconomic_analysis
WHERE
	gdp_pc_cagr_cat = 'Strong'*/