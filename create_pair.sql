BEGIN;
CREATE TABLE "pair_programmer" (
    "id" serial NOT NULL PRIMARY KEY,
    "name" varchar(200) NOT NULL
)
;
CREATE TABLE "pair_pair_programmers" (
    "id" serial NOT NULL PRIMARY KEY,
    "pair_id" integer NOT NULL,
    "programmer_id" integer NOT NULL REFERENCES "pair_programmer" ("id") DEFERRABLE INITIALLY DEFERRED,
    UNIQUE ("pair_id", "programmer_id")
)
;
CREATE TABLE "pair_pair" (
    "id" serial NOT NULL PRIMARY KEY
)
;
ALTER TABLE "pair_pair_programmers" ADD CONSTRAINT "pair_id_refs_id_19fb447d" FOREIGN KEY ("pair_id") REFERENCES "pair_pair" ("id") DEFERRABLE INITIALLY DEFERRED;
COMMIT;