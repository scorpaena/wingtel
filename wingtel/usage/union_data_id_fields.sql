CREATE VIEW union_data_id_fields AS 
    SELECT 
        DATE(usage_date) AS date, 
        subscription_id
    FROM 
        usage_datausagerecord
    GROUP BY
        DATE(usage_date), 
        subscription_id
    UNION
    SELECT 
        DATE(usage_date) AS date,
        subscription_id
    FROM
        usage_voiceusagerecord
    GROUP BY
        DATE(usage_date), 
        subscription_id
    ORDER BY
        date;