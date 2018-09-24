/* Selection Query #1 */
SELECT * FROM (SELECT * FROM mushrooms WHERE id = 0 GROUP BY id) q1
JOIN (SELECT * FROM cap WHERE id = 0 GROUP BY id) q2
ON q1.id = q2.id
JOIN (SELECT * FROM gill WHERE id = 0 GROUP BY id) q3
ON q2.id = q3.id
JOIN (SELECT * FROM stalk WHERE id = 0 GROUP BY id) q4
ON q3.id = q4.id
JOIN (SELECT * FROM "veil-ring" WHERE id = 0 GROUP BY id) q5
ON q4.id = q5.id;

/* Selection Query #2*/
SELECT ((Q1*1.0)/((Q1+Q2)*1.0)*100)
FROM (SELECT count(*) AS Q1 FROM mushrooms WHERE class = "p" AND bruises = "t" AND odor = "p" AND "spore-print-color" = "k" AND population = "s" AND habitat = "u"),
(SELECT count(*) AS Q2 FROM mushrooms WHERE class = "e" AND bruises = "t" AND odor = "p" AND "spore-print-color" = "k" AND population = "s" AND habitat = "u");
