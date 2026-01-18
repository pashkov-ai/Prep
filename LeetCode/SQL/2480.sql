SELECT A.symbol as metal, B.Symbol as nonmetal
FROM Elements A, Elements B
WHERE A.type = "Metal" AND B.type = 'Nonmetal'