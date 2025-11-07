-- Quantas mensagens cada pessoa enviou
-- SELECT from_user, COUNT(*) AS total_envios
-- FROM interactions
-- GROUP BY from_user;

--Confiurações do terminal sqlite:
-- .mode column
-- .header on

-- Comparação do ranking por window function
SELECT 
    from_user,
    total_sent,
    ROW_NUMBER() OVER (ORDER BY total_sent DESC) AS row_number_rank,
    RANK()       OVER (ORDER BY total_sent DESC) AS rank_rank,
    DENSE_RANK() OVER (ORDER BY total_sent DESC) AS dense_rank_rank
FROM (
    SELECT from_user, COUNT(*) AS total_sent
    FROM interactions
    GROUP BY from_user
) AS counts;