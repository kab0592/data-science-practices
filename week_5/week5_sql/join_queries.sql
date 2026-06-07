/*--Creating a temporary table (view) that can be used for reference.
CREATE VIEW week5_population AS
SELECT
    canton,
    2019 AS year,
    population_2019 AS population
FROM
	week5_pop2019

UNION ALL

SELECT
    canton,
    2022 AS year,
    population_2022 AS population
FROM
	week5_pop2022;*/

/*--Creating a province-level GDP summary
SELECT
    week5_economic.year,
    week5_economic.province,
    ROUND(AVG(CAST(week5_economic.gdp AS numeric)), 2) AS avg_gdp,
    ROUND(AVG(CAST((week5_economic.gdp / week5_population.population) AS numeric)), 2) AS avg_gdp_percapita
FROM
	week5_economic
INNER JOIN
	week5_population
    ON week5_economic.canton = week5_population.canton
	AND week5_economic.year = week5_population.year
GROUP BY
    week5_economic.year,
    week5_economic.province;*/

/*--Create region GDP per capita ranking
SELECT
	e.year,
	e.region,
	ROUND(AVG(CAST((e.gdp / p.population) AS numeric)), 2) AS avg_gdp_percapita
FROM
	week5_economic AS e
INNER JOIN
	week5_population AS p
	ON e.canton = p.canton
	AND e.year = p.year
GROUP BY
	e.year,
	e.region;*/

/*--Growth type summary
SELECT
	growth_type,
	COUNT(canton),
	ROUND(AVG(CAST(gdp_cagr AS numeric)), 2) AS avg_gdp_cagr
FROM
	socioeconomic_analysis
GROUP BY
	growth_type*/