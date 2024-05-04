SELECT 
    ID,
    CASE
        WHEN row_num <= total_count * 0.25 THEN 'CRITICAL'
        WHEN row_num <= total_count * 0.50 THEN 'HIGH'
        WHEN row_num <= total_count * 0.75 THEN 'MEDIUM'
        ELSE 'LOW'
    END AS COLONY_NAME
FROM (
    SELECT 
        ID,
        ROW_NUMBER() OVER (ORDER BY SIZE_OF_COLONY DESC) AS row_num,
        COUNT(*) OVER() AS total_count
    FROM ECOLI_DATA
) AS R
ORDER BY ID ASC;
