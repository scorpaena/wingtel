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


CREATE VIEW usage_metrics AS
    SELECT 
        row_number() OVER () as id,
        union_data.date,
        union_data.subscription_id,
        data.kilobytes_price,
        data.kilobytes_used,
        voice.seconds_price,
        voice.seconds_used
    FROM union_data_id_fields AS union_data
    LEFT JOIN
        (
        SELECT 
            DATE(usage_date) AS date,
            SUM(price) AS kilobytes_price, 
            SUM(kilobytes_used) AS kilobytes_used,
            subscription_id
        FROM
            usage_datausagerecord
        GROUP BY
            DATE(usage_date), 
            subscription_id
        ) AS data
    ON 
        union_data.date=data.date 
        AND 
        union_data.subscription_id=data.subscription_id

    LEFT JOIN
        (
        SELECT 
            DATE(usage_date) AS date,
            SUM(price) AS seconds_price, 
            SUM(seconds_used) AS seconds_used,
            subscription_id
        FROM
            usage_voiceusagerecord
        GROUP BY
            DATE(usage_date), 
            subscription_id
        ) AS voice
    ON 
        union_data.date=voice.date 
        AND 
        union_data.subscription_id=voice.subscription_id;