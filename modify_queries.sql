/* Modify Queries */
BEGIN TRANSACTION;
INSERT INTO mushrooms(id, class, bruises, odor, "spore-print-color", population, habitat) VALUES (8124,"e","t","a","k","k","g");
INSERT INTO cap ("cap-shape", "cap-surface", "cap-color", id) VALUES ("b","f","n",8124);
INSERT INTO gill ("gill-attachment", "gill-spacing", "gill-size", "gill-color", id) VALUES ("a","c","b","k",8124);
INSERT INTO stalk ("stalk-shape", "stalk-root", "stalk-surface-above-ring", "stalk-surface-below-ring", "stalk-color-above-ring", "stalk-color-below-ring", id) VALUES ("e","b","f","f","n","n",8124);
INSERT INTO "veil-ring" ("veil-type", "veil-color", "ring-number", "ring-type", id) VALUES ("p","n","n","c",8124);
COMMIT;

BEGIN;
CREATE TEMP TABLE _var(Name varchar, value INT);
INSERT INTO _var(Name,value) VALUES ('Max', ((SELECT max(id) as maximum FROM mushrooms) + 1));
INSERT INTO mushrooms (id, class, bruises, odor, "spore-print-color", population, habitat) VALUES ((SELECT value FROM _var WHERE Name = 'Max'), (SELECT class FROM mushrooms WHERE id = 0),(SELECT bruises FROM mushrooms WHERE id = 0),(SELECT odor FROM mushrooms WHERE id = 0),(SELECT "spore-print-color" FROM mushrooms WHERE id = 0),(SELECT population FROM mushrooms WHERE id = 0),(SELECT habitat FROM mushrooms WHERE id = 0));
UPDATE cap SET id = (SELECT max(id) as maximum FROM mushrooms) WHERE id = 0;
UPDATE gill SET id = (SELECT max(id) as maximum FROM mushrooms)  WHERE id = 0;
UPDATE stalk SET id = (SELECT max(id) as maximum FROM mushrooms) WHERE id = 0;
UPDATE "veil-ring" SET id = (SELECT max(id) as maximum FROM mushrooms) WHERE id = 0;
DELETE FROM mushrooms WHERE id = 0;
DROP TABLE _var;
END;
