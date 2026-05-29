SELECT
	province,
	AVG(gdp) AS avg_gdp,
	AVG(gdp_pc) AS avg_gdp_pc,
	COUNT(canton) AS num_cantones
FROM
	socioeconomic_analysis
GROUP BY
	prov_code,
	province
ORDER BY
	prov_code ASC