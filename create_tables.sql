CREATE TABLE mushrooms
(
  id                  INTEGER
    PRIMARY KEY,
  class               VARCHAR,
  bruises             VARCHAR,
  odor                VARCHAR,
  "spore-print-color" VARCHAR,
  population          VARCHAR,
  habitat             VARCHAR
);
CREATE TABLE cap
(
  "cap-shape"   VARCHAR,
  "cap-surface" VARCHAR,
  "cap-color"   VARCHAR,
  id            INTEGER
    PRIMARY KEY
    CONSTRAINT caps_id_mushroms_id_fk
    REFERENCES mushrooms
);
CREATE TABLE gill
(
  "gill-attachment" VARCHAR,
  "gill-spacing"    VARCHAR,
  "gill-size"       VARCHAR,
  "gill-color"      VARCHAR,
  id                INTEGER
    PRIMARY KEY
    CONSTRAINT gill_mushrooms_id_fk
    REFERENCES mushrooms
);
CREATE TABLE stalk
(
  "stalk-shape"              VARCHAR,
  "stalk-root"               VARCHAR,
  "stalk-surface-above-ring" VARCHAR,
  "stalk-surface-below-ring" VARCHAR,
  "stalk-color-above-ring"   VARCHAR,
  "stalk-color-below-ring"   VARCHAR,
  id                         INTEGER
    PRIMARY KEY
    CONSTRAINT stalk_mushrooms_id_fk
    REFERENCES mushrooms
);
CREATE TABLE "veil-ring"
(
  "veil-type"   VARCHAR,
  "veil-color"  VARCHAR,
  "ring-number" VARCHAR,
  "ring-type"   VARCHAR,
  id            INTEGER
    PRIMARY KEY
    CONSTRAINT "veil-ring_mushrooms_id_fk"
    REFERENCES mushrooms
);
