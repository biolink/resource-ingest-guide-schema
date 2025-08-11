-- # Class: NamedThing Description: A generic grouping for any identifiable entity
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
-- # Class: ReferenceIngestGuide Description: Represents a ReferenceIngestGuide
--     * Slot: primary_email Description: The main email address of a person
--     * Slot: birth_date Description: Date on which a person is born
--     * Slot: age_in_years Description: Number of years since birth
--     * Slot: vital_status Description: living or dead status
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: ReferenceIngestGuideCollection_id Description: Autocreated FK slot
-- # Class: ReferenceIngestGuideCollection Description: A holder for ReferenceIngestGuide objects
--     * Slot: id

CREATE TABLE "NamedThing" (
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_NamedThing_id" ON "NamedThing" (id);
CREATE TABLE "ReferenceIngestGuideCollection" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_ReferenceIngestGuideCollection_id" ON "ReferenceIngestGuideCollection" (id);
CREATE TABLE "ReferenceIngestGuide" (
	primary_email TEXT,
	birth_date DATE,
	age_in_years INTEGER,
	vital_status VARCHAR(7),
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	"ReferenceIngestGuideCollection_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ReferenceIngestGuideCollection_id") REFERENCES "ReferenceIngestGuideCollection" (id)
);CREATE INDEX "ix_ReferenceIngestGuide_id" ON "ReferenceIngestGuide" (id);
