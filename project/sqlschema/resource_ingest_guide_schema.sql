-- # Class: ReferenceIngestGuide Description: A container that holds attributes for the discrete sections of information comprising a Resource Ingest Guide.
--     * Slot: id
--     * Slot: name Description: A human readable name for the RIG.
--     * Slot: source_info_id Description: Information about the source from which content is ingested.
--     * Slot: ingest_info_id Description: Information about the rationale and scope of an ingest, including what source content was included and excluded from the ingest, and what additional content might be considered in future iterations.
--     * Slot: target_info_id Description: Information about the dataset / knowledge graph output by the ingest,  including what types of edges and nodes were produced, modeling rationale,  and what modeling changes might be considered in future iterations.
--     * Slot: provenance_info_id Description: Information about the provenance of the ingest, including who contributed and how, and links to external provenance-related artifacts (e.g. Github tickets, ingest surveys, etc.)
-- # Class: SupportingDataSourceInformation Description: A container for information about upstream sources of data that are used by an ingested source, to derive the knowledge that we ingest. This info is not relevant for typical ingest of an external knowledge source, and applies mainly for describing "ingest" of data-derived KPs like ICEES, COHD, various Multiomics KPs, etc.
--     * Slot: id
--     * Slot: infores_id Description: The infores identifier of the source from which content is being ingested, e.g. "infores:ctd".
--     * Slot: name Description: A human-readable name for the source of supporting data, e.g. "Aggregate Analysis of ClinicalTrial.gov (AACT)"
--     * Slot: description Description: A brief description of the source, including its purpose, scope, and any relevant background information.
--     * Slot: terms_of_use_info_id Description: Information about conditions for use of the ingested source. May include the name of a community license (e.g. `CC-BY 4.0`), a link to a "terms of use" or license information web page (e.g. `https://ctdbase.org/about/legal.jsp`), and/or a free-text summary of key terms of use.
-- # Class: SourceInformation Description: A container for capturing information about the source of the ingest.
--     * Slot: id
--     * Slot: infores_id Description: The infores identifier of the source from which content is being ingested, e.g. "infores:ctd".
--     * Slot: name Description: A human readable name for the RIG
--     * Slot: description Description: A brief description of the source, including its purpose, scope, and any relevant background information.
--     * Slot: data_versioning_and_releases Description: A description of how releases are versioned and managed by the source (e.g. general approach, frequency, other important considerations). May also include links to web pages describing such information.
--     * Slot: source_status Description: The maintenance status of the source, indicating whether it is actively maintained and how regularly it is updated.
--     * Slot: additional_notes Description: Additional notes, considerations, or resources relevant to the source, that were not otherwise captured in dedicated attributes.
--     * Slot: terms_of_use_info_id Description: Information about conditions for use of the ingested source. May include the name of a community license (e.g. `CC-BY 4.0`), a link to a "terms of use" or license information web page (e.g. `https://ctdbase.org/about/legal.jsp`), and/or a free-text summary of key terms of use.
-- # Class: TermsOfUseInformation Description: A structured representation describing terms for re-use of data from an information resource.
--     * Slot: id
--     * Slot: terms_of_use_url Description: The url of a document or web page where a source describes its terms of use, and/or references a community license that it adopts. (e.g. "https://ctdbase.org/about/legal.jsp")
--     * Slot: terms_of_use_description Description: A free text description of the terms of use for a source.  (e.g. "Source only indicates 'all rights reserved' in their documentation")
--     * Slot: license_name Description: The name of an established license used by the source (e.g. "CC BY 4.0")
--     * Slot: license_url Description: The url of an established license (e.g. "https://creativecommons.org/licenses/by/4.0/")
-- # Class: IngestInformation Description: A container for capturing information about the rationale and scope of an ingest, including what source content was included and excluded from the ingest, and what additional content might be considered in future iterations.
--     * Slot: id
--     * Slot: utility Description: Brief description of why the source was ingested, and the utility of the data it provides for target system use cases.
--     * Slot: scope Description: A short, high-level narrative describing of the types of knowledge form the source that are included and excluded in this ingest.
--     * Slot: additional_notes Description: Additional notes, considerations or resources relevant to source content ingest, that were not otherwise captured in dedicated attributes.
-- # Class: RelevantFiles Description: A structure for describing each source file (or API endpoint, database, or table) that contains content in scope for the ingest. Source files containing which content is not retrieved  in this ingest need not be listed or described.
--     * Slot: id
--     * Slot: file_name Description: The name of the relevant file (or endpoint, or table).
--     * Slot: location Description: The URL of a web page or ftp site where the indicated file (or endpoint or table) was accessed.
--     * Slot: description Description: An optional brief description of the content and/or utility of the file (or endpoint or table)
-- # Class: IncludedContent Description: A structure for describing the types of records from relevant files/endpoints/tables are included in this ingest, and optionally a list of fields from these records that are part of the ingest or used to inform it.
--     * Slot: id
--     * Slot: file_name Description: The name of the relevant file (or endpoint, or table) from which content is included.
--     * Slot: included_records Description: A description of the types of records that are included in the ingest.
--     * Slot: fields_used Description: Optional list of the specific source fields that are part of or inform the ingest.
-- # Class: FilteredContent Description: A structure for describing the types of records from each relevant file/endpoint/table not included in the ingest, and the rationale for any filtering rules or exclusion criteria. Only list a file if some but not all records it contains are included in the ingest - to document what subset was excluded, and why.
--     * Slot: id
--     * Slot: file_name Description: The name of the relevant file (or endpoint, or table) form which content was filtered.
--     * Slot: filtered_records Description: A description of what types of records were excluded from the ingest, in terms of filtering rules or exclusion criteria.
--     * Slot: rationale Description: The rationale for excluding the indicated content (why this subset of records was filtered out).
-- # Class: FutureContentConsiderations Description: A structure for collecting notes about content additions or changes to consider in future iterations of this ingest. Create separate objects for each distinct consideration, and indicate if it relates to  content that will be captured as Edges, Node Properties, or Edge Properties in the target knowledge graph.
--     * Slot: id
--     * Slot: category Description: The category of content described by a given consideration, based on how the content will be represented in the target graph (e.g. "Edges", 'Node Properties",  "Edge Properties").
--     * Slot: consideration Description: A description of what additional content should be considered and why.
--     * Slot: relevant_files Description: A list of the relevant source file or files that provide the considered content.
-- # Class: TargetInformation Description: A structure for capturing information about the target dataset / knowledge graph output by the ingest, including what types of edges and nodes were produced, modeling rationale, and what modeling changes might be considered in future iterations.
--     * Slot: id
--     * Slot: infores_id Description: An infores identifier assigned to the target resource that will be created from the ingested content. e.g. "infores:translator-ctd".
--     * Slot: additional_notes Description: Additional notes, considerations or resources relevant to mapping or modeling source data to the target model, that were not otherwise captured in dedicated attributes.
-- # Class: EdgeType Description: A structure for describing each type of edge (metaedge) created in the target knowledge graph by this ingest, including what types of edge properties it holds, and a brief explanation of why this modeling pattern was deemed appropriate to represent the source data (for display to end users in a UI system). Note that an edge type with multiple subject_category and object_category values does not mean that the full cross-product must be instantiated in the data. e.g. A KG with the edge type sub_cat: [Gene, Protein, Small Molecule], predicate: affects, obj_cat: [disease, phenotype, symptom] might include  Protein-affects-Disease and Gene-affects-Symptom edges, but not include any  Protein-affects-Symptom edges.
--     * Slot: id
--     * Slot: ui_explanation Description: An explanation of how the source data for an edge of a particular type was generated (as rationale for why the knowledge level, agent type, and knowledge source choices for this edge type were made), along with an explanation for how/why the source data record for a particular edge was transformed into a its current Biolink edge-based representation. Note that this text will be displayed in the UI to explain the provenance of a specific edge, and should be framed accordingly.
--     * Slot: additional_notes Description: Additional notes, considerations, or explanations of modeling patterns used for this edge type, that were not otherwise captured in dedicated fields.
-- # Class: Qualifier Description: A qualifier property + value tuple that specifies a type of qualifier and value that may be applied to a Statement. Qualified predicates are considered qualifiers and captured here as well. Values can be specified to come from a proper range (e.g. Biolink class, data type, or enum), come from an enumerated list, use a specific id prefix, and/or conform informally to a free-text description.
--     * Slot: id
--     * Slot: property Description: The Biolink qualifier slot that defines the kind of Qualifier specified, e.g. "biolink:subject_aspect_qualifier", "qualified_predicate".
--     * Slot: value_description Description: A free text description of the types of value allowed for the qualifier.
-- # Class: NodeType Description: A structured object describing each type of node created in the target knowledge graph by this ingest.
--     * Slot: id
--     * Slot: node_category Description: The high-level Biolink category of nodes as assumed or assigned by ingestors. e.g. "biolink:Gene". Note that downstream normalization of node identifiers may result in new/different categories ultimately being assigned in the final graph.
--     * Slot: additional_notes Description: Additional notes, considerations, or explanations concerning this node type, that were not otherwise captured in dedicated attributes.
-- # Class: FutureModelingConsiderations Description: A structure for collecting discrete considerations about modeling changes to consider in future iterations of this ingest. Create and categorize separate objects for each distinct consideration.
--     * Slot: id
--     * Slot: category Description: An optional general category for the modeling consideration (e.g. "spoq_pattern", "edge_properties")
--     * Slot: consideration Description: A description of the modeling changes to consider, and why.
-- # Class: ProvenanceInformation Description: A container holding information about the provenance of the ingest, including who contributed and how, and links to external provenance artifacts.
--     * Slot: id
-- # Class: ReferenceIngestGuide_supporting_data_source_info
--     * Slot: ReferenceIngestGuide_id Description: Autocreated FK slot
--     * Slot: supporting_data_source_info_id Description: Information about upstream sources of data that are used by an ingested source, to derive the knowledge that we ingest.
-- # Class: SupportingDataSourceInformation_relevant_files
--     * Slot: SupportingDataSourceInformation_id Description: Autocreated FK slot
--     * Slot: relevant_files_id Description: A description of each source file (or API endpoint, database, or table) that contains data used to create the ingested knowledge. Source files that contain data not used to created knowledge need not be listed or described.
-- # Class: SourceInformation_citations
--     * Slot: SourceInformation_id Description: Autocreated FK slot
--     * Slot: citations Description: One ore more citations to publications describing the source. May be a identifier (e.g a pmid or doi), a url to the published document, or a free-text citation.
-- # Class: SourceInformation_data_access_locations
--     * Slot: SourceInformation_id Description: Autocreated FK slot
--     * Slot: data_access_locations Description: Where the source data that is being ingested can be accessed. Provide one or more URLs,  along with optional descriptions of what each URL provides.
-- # Class: SourceInformation_data_provision_mechanisms
--     * Slot: SourceInformation_id Description: Autocreated FK slot
--     * Slot: data_provision_mechanisms Description: How the source distributes their data (file download, API endpoints, database dump).
-- # Class: SourceInformation_data_formats
--     * Slot: SourceInformation_id Description: Autocreated FK slot
--     * Slot: data_formats Description: The format(s) in which the data is serialized for retrieval and use.
-- # Class: IngestInformation_ingest_categories
--     * Slot: IngestInformation_id Description: Autocreated FK slot
--     * Slot: ingest_categories Description: A term or terms indicating the type of source being ingested, from the perspective of the ingesting system (e.g. primary knowledge provider, supporting data provider, ontology/terminology provider).
-- # Class: IngestInformation_relevant_files
--     * Slot: IngestInformation_id Description: Autocreated FK slot
--     * Slot: relevant_files_id Description: A description of each source file (or API endpoint, database, or table) that contains content in scope for the ingest. Source files containing content which is not retrieved  in this ingest need not be listed or described.
-- # Class: IngestInformation_included_content
--     * Slot: IngestInformation_id Description: Autocreated FK slot
--     * Slot: included_content_id Description: A description of what types of records from relevant files/endpoints/tables above are included in this ingest, and optionally a list of fields from these records that are part of the ingest or used to inform it.
-- # Class: IngestInformation_filtered_content
--     * Slot: IngestInformation_id Description: Autocreated FK slot
--     * Slot: filtered_content_id Description: A description of what types of records from each relevant file are not included in the ingest, and the rationale for any filtering rules or exclusion criteria. Only list a file if some but not all records it contains are included in the ingest - to document what subset was excluded, and why.
-- # Class: IngestInformation_future_considerations
--     * Slot: IngestInformation_id Description: Autocreated FK slot
--     * Slot: future_considerations_id Description: Notes about content additions or changes to consider in future iterations of this ingest. Separately consider content that will be represented as Edges vs Node Properties vs Edge Properties in the target knowledge graph.
-- # Class: TargetInformation_edge_type_info
--     * Slot: TargetInformation_id Description: Autocreated FK slot
--     * Slot: edge_type_info_id Description: A description of each type of edge (metaedge) created in the target knowledge graph by this ingest, including what types of edge properties it holds, and a brief explanation of why this modeling pattern was deemed appropriate to represent the source data (to be displayed for end users in a UI system).
-- # Class: TargetInformation_node_type_info
--     * Slot: TargetInformation_id Description: Autocreated FK slot
--     * Slot: node_type_info_id Description: A description of each type of node created in the target knowledge graph by this ingest, in terms of the high-level Biolink categories of nodes as assumed or assigned by ingestors.  Note however that downstream normalization of node identifiers may result in new/different categories ultimately being assigned in the final graph.
-- # Class: TargetInformation_future_considerations
--     * Slot: TargetInformation_id Description: Autocreated FK slot
--     * Slot: future_considerations_id Description: Notes about mapping/modeling changes to consider in future iterations of this ingest.
-- # Class: EdgeType_subject_categories
--     * Slot: EdgeType_id Description: Autocreated FK slot
--     * Slot: subject_categories Description: The Biolink category of the subject node of this edge type. e.g. "biolink:SmallMolecule". If two edge types differ only in their subject category, but use the same predicate, object_category,  edge properties, and general provenance, they can be described together in a single NodeType object that captures the alternative subject categories. e.g. if a source provides SmallMolecule-treats-Disease and  MolecularMixture-treats-Disease edge types, these can be described in a single EdgeType object with two subject categories (SmallMolecule and MolecularMixture).
-- # Class: EdgeType_predicates
--     * Slot: EdgeType_id Description: Autocreated FK slot
--     * Slot: predicates Description: Biolink predicate(s) that defines this type of edge. Multiple values allowed ONLY if they are a predicate and one or more of its descendent predicates (e.g. ["biolink:affects", "biolink:regulates", "biolink:disrupts"]. Otherwise,  separate EdgeType objects should be created for each predicate.
-- # Class: EdgeType_object_categories
--     * Slot: EdgeType_id Description: Autocreated FK slot
--     * Slot: object_categories Description: The Biolink category of the object node of this edge type. e.g. "biolink:Disease". If two edge types differ only in their object category, but use the same predicate, subject_category,  edge properties, and general provenance, they can be described together in a single NodeType object that captures the alternative object categories. e.g. if a source provides Gene-associated_with-Disease and  Gene-associated_with-PhenotypicFeature edge types, these can be described in a single EdgeType object with two subject categories (Disease and PhenotypicFeature)
-- # Class: EdgeType_qualifiers
--     * Slot: EdgeType_id Description: Autocreated FK slot
--     * Slot: qualifiers_id Description: If relevant, report any qualifiers applied to the edge type, as a Qualifier object that contains a  qualifier_property and qualifier_range pair. e.g. the property "biolink:subject_aspect_qualifier", and range  "biolink:GeneOrGeneProductOrChemicalEntityAspectEnum
-- # Class: EdgeType_knowledge_level
--     * Slot: EdgeType_id Description: Autocreated FK slot
--     * Slot: knowledge_level Description: The knowledge level (or levels) relevant to this type of edge. Multivalued only if instances of this type of edge can have different knowledge levels in the data.
-- # Class: EdgeType_agent_type
--     * Slot: EdgeType_id Description: Autocreated FK slot
--     * Slot: agent_type Description: The agent type (or types) relevant to this type of edge. Multivalued only if instances of this type of edge can have different agent types in the data.
-- # Class: EdgeType_primary_knowledge_sources
--     * Slot: EdgeType_id Description: Autocreated FK slot
--     * Slot: primary_knowledge_sources Description: The infores id(s) of the 'primary knowledge sources' for this type of edge. Note that only one primary knowledge source is allowed per edge, but there may be more than one possible value here across edges for a given type (e.g. see the infores:diseases RIG/data)
-- # Class: EdgeType_supporting_data_sources
--     * Slot: EdgeType_id Description: Autocreated FK slot
--     * Slot: supporting_data_sources Description: The infores id(s) of any 'supporting data sources' for this type of edge.
-- # Class: EdgeType_aggregator_knowledge_sources
--     * Slot: EdgeType_id Description: Autocreated FK slot
--     * Slot: aggregator_knowledge_sources Description: The infores id(s) of any 'aggregator_knowledge sources' for this type of edge.
-- # Class: EdgeType_edge_properties
--     * Slot: EdgeType_id Description: Autocreated FK slot
--     * Slot: edge_properties Description: A list of one or more Biolink edge properties used in instances of this edge type in the data.
-- # Class: EdgeType_source_files
--     * Slot: EdgeType_id Description: Autocreated FK slot
--     * Slot: source_files Description: The source file or files that provided data included in or informing edges of this type. Will usually be a single file. Multivalued because some edges are based on data that come form more than one file. If the data is ingested from a database instance or API endpoint, provide analogous information here (e.g. the name of an specific API endpoint, a database access url, or a set of tables in a database schema).
-- # Class: Qualifier_value_range
--     * Slot: Qualifier_id Description: Autocreated FK slot
--     * Slot: value_range Description: The Biolink class(es) or type(s) that specifies the kind of value the qualifier property takes, Reported as the name of a Biolink class, enumeration, or data type, as appropriate.  e.g. "biolink:Disease", "biolink:GeneOrGeneProductOrChemicalEntityAspectEnum", "biolink:string"
-- # Class: Qualifier_value_enumeration
--     * Slot: Qualifier_id Description: Autocreated FK slot
--     * Slot: value_enumeration Description: A set of one or more specific values for the qualifier in an Edge type (e.g. ["biolink:causes"] as the only value for the "biolink:qualified_predicate" qualifier property, ["activity_or_abundance", "activity", "abundance"]  as the values for the "biolink:object_aspect_qualifier" property).
-- # Class: Qualifier_value_id_prefixes
--     * Slot: Qualifier_id Description: Autocreated FK slot
--     * Slot: value_id_prefixes Description: One or more id prefixes from which the qualifier value must come. e.g. "HP" if the qualifier must be a Human Phenotype Ontology term.
-- # Class: NodeType_source_identifier_types
--     * Slot: NodeType_id Description: Autocreated FK slot
--     * Slot: source_identifier_types Description: The type of identifier(s) used for this category of entity by the source system. Report as a prefix for an identifier system where appropriate/possible (preferably a prefix as cataloged in the Biolink prefix map here: https://github.com/biolink/biolink-model/blob/master/project/prefixmap/biolink-model-prefix-map.json). e.g. "MESH", "CTD", "ECTO". If prefix for a public system/database is not in the prefix map, you may make a PR to add it.  If the identifiers used are bespoke, or no identifiers are used, the value can be a free text description. e.g. "The source uses entity names but does not assign identifiers".
-- # Class: NodeType_node_properties
--     * Slot: NodeType_id Description: Autocreated FK slot
--     * Slot: node_properties Description: A list of one or more Biolink node properties used in instances of this node type in the data.
-- # Class: ProvenanceInformation_contributions
--     * Slot: ProvenanceInformation_id Description: Autocreated FK slot
--     * Slot: contributions Description: The name of a person making a contribution, and the type of contribution made. e.g. "code author", "code support", "data modeling", "domain expertise".
-- # Class: ProvenanceInformation_artifacts
--     * Slot: ProvenanceInformation_id Description: Autocreated FK slot
--     * Slot: artifacts Description: Links to and descriptions of external artifacts related to the provenance of the ingest, such as Github issues, surveys of prior ingests of the source, etc.

CREATE TABLE "TermsOfUseInformation" (
	id INTEGER NOT NULL,
	terms_of_use_url TEXT,
	terms_of_use_description TEXT,
	license_name TEXT,
	license_url TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_TermsOfUseInformation_id" ON "TermsOfUseInformation" (id);
CREATE TABLE "IngestInformation" (
	id INTEGER NOT NULL,
	utility TEXT NOT NULL,
	scope TEXT,
	additional_notes TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_IngestInformation_id" ON "IngestInformation" (id);
CREATE TABLE "RelevantFiles" (
	id INTEGER NOT NULL,
	file_name TEXT NOT NULL,
	location TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_RelevantFiles_id" ON "RelevantFiles" (id);
CREATE TABLE "IncludedContent" (
	id INTEGER NOT NULL,
	file_name TEXT NOT NULL,
	included_records TEXT NOT NULL,
	fields_used TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_IncludedContent_id" ON "IncludedContent" (id);
CREATE TABLE "FilteredContent" (
	id INTEGER NOT NULL,
	file_name TEXT NOT NULL,
	filtered_records TEXT NOT NULL,
	rationale TEXT NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_FilteredContent_id" ON "FilteredContent" (id);
CREATE TABLE "FutureContentConsiderations" (
	id INTEGER NOT NULL,
	category VARCHAR(21) NOT NULL,
	consideration TEXT NOT NULL,
	relevant_files TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_FutureContentConsiderations_id" ON "FutureContentConsiderations" (id);
CREATE TABLE "TargetInformation" (
	id INTEGER NOT NULL,
	infores_id TEXT,
	additional_notes TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_TargetInformation_id" ON "TargetInformation" (id);
CREATE TABLE "EdgeType" (
	id INTEGER NOT NULL,
	ui_explanation TEXT NOT NULL,
	additional_notes TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_EdgeType_id" ON "EdgeType" (id);
CREATE TABLE "Qualifier" (
	id INTEGER NOT NULL,
	property TEXT NOT NULL,
	value_description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Qualifier_id" ON "Qualifier" (id);
CREATE TABLE "NodeType" (
	id INTEGER NOT NULL,
	node_category TEXT NOT NULL,
	additional_notes TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_NodeType_id" ON "NodeType" (id);
CREATE TABLE "FutureModelingConsiderations" (
	id INTEGER NOT NULL,
	category VARCHAR(15),
	consideration TEXT NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_FutureModelingConsiderations_id" ON "FutureModelingConsiderations" (id);
CREATE TABLE "ProvenanceInformation" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_ProvenanceInformation_id" ON "ProvenanceInformation" (id);
CREATE TABLE "SupportingDataSourceInformation" (
	id INTEGER NOT NULL,
	infores_id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	terms_of_use_info_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(terms_of_use_info_id) REFERENCES "TermsOfUseInformation" (id)
);CREATE INDEX "ix_SupportingDataSourceInformation_id" ON "SupportingDataSourceInformation" (id);
CREATE TABLE "SourceInformation" (
	id INTEGER NOT NULL,
	infores_id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	data_versioning_and_releases TEXT,
	source_status VARCHAR(28) NOT NULL,
	additional_notes TEXT,
	terms_of_use_info_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(terms_of_use_info_id) REFERENCES "TermsOfUseInformation" (id)
);CREATE INDEX "ix_SourceInformation_id" ON "SourceInformation" (id);
CREATE TABLE "IngestInformation_ingest_categories" (
	"IngestInformation_id" INTEGER,
	ingest_categories VARCHAR(28),
	PRIMARY KEY ("IngestInformation_id", ingest_categories),
	FOREIGN KEY("IngestInformation_id") REFERENCES "IngestInformation" (id)
);CREATE INDEX "ix_IngestInformation_ingest_categories_ingest_categories" ON "IngestInformation_ingest_categories" (ingest_categories);CREATE INDEX "ix_IngestInformation_ingest_categories_IngestInformation_id" ON "IngestInformation_ingest_categories" ("IngestInformation_id");
CREATE TABLE "IngestInformation_relevant_files" (
	"IngestInformation_id" INTEGER,
	relevant_files_id INTEGER NOT NULL,
	PRIMARY KEY ("IngestInformation_id", relevant_files_id),
	FOREIGN KEY("IngestInformation_id") REFERENCES "IngestInformation" (id),
	FOREIGN KEY(relevant_files_id) REFERENCES "RelevantFiles" (id)
);CREATE INDEX "ix_IngestInformation_relevant_files_IngestInformation_id" ON "IngestInformation_relevant_files" ("IngestInformation_id");CREATE INDEX "ix_IngestInformation_relevant_files_relevant_files_id" ON "IngestInformation_relevant_files" (relevant_files_id);
CREATE TABLE "IngestInformation_included_content" (
	"IngestInformation_id" INTEGER,
	included_content_id INTEGER,
	PRIMARY KEY ("IngestInformation_id", included_content_id),
	FOREIGN KEY("IngestInformation_id") REFERENCES "IngestInformation" (id),
	FOREIGN KEY(included_content_id) REFERENCES "IncludedContent" (id)
);CREATE INDEX "ix_IngestInformation_included_content_IngestInformation_id" ON "IngestInformation_included_content" ("IngestInformation_id");CREATE INDEX "ix_IngestInformation_included_content_included_content_id" ON "IngestInformation_included_content" (included_content_id);
CREATE TABLE "IngestInformation_filtered_content" (
	"IngestInformation_id" INTEGER,
	filtered_content_id INTEGER,
	PRIMARY KEY ("IngestInformation_id", filtered_content_id),
	FOREIGN KEY("IngestInformation_id") REFERENCES "IngestInformation" (id),
	FOREIGN KEY(filtered_content_id) REFERENCES "FilteredContent" (id)
);CREATE INDEX "ix_IngestInformation_filtered_content_IngestInformation_id" ON "IngestInformation_filtered_content" ("IngestInformation_id");CREATE INDEX "ix_IngestInformation_filtered_content_filtered_content_id" ON "IngestInformation_filtered_content" (filtered_content_id);
CREATE TABLE "IngestInformation_future_considerations" (
	"IngestInformation_id" INTEGER,
	future_considerations_id INTEGER,
	PRIMARY KEY ("IngestInformation_id", future_considerations_id),
	FOREIGN KEY("IngestInformation_id") REFERENCES "IngestInformation" (id),
	FOREIGN KEY(future_considerations_id) REFERENCES "FutureContentConsiderations" (id)
);CREATE INDEX "ix_IngestInformation_future_considerations_IngestInformation_id" ON "IngestInformation_future_considerations" ("IngestInformation_id");CREATE INDEX "ix_IngestInformation_future_considerations_future_considerations_id" ON "IngestInformation_future_considerations" (future_considerations_id);
CREATE TABLE "TargetInformation_edge_type_info" (
	"TargetInformation_id" INTEGER,
	edge_type_info_id INTEGER NOT NULL,
	PRIMARY KEY ("TargetInformation_id", edge_type_info_id),
	FOREIGN KEY("TargetInformation_id") REFERENCES "TargetInformation" (id),
	FOREIGN KEY(edge_type_info_id) REFERENCES "EdgeType" (id)
);CREATE INDEX "ix_TargetInformation_edge_type_info_TargetInformation_id" ON "TargetInformation_edge_type_info" ("TargetInformation_id");CREATE INDEX "ix_TargetInformation_edge_type_info_edge_type_info_id" ON "TargetInformation_edge_type_info" (edge_type_info_id);
CREATE TABLE "TargetInformation_node_type_info" (
	"TargetInformation_id" INTEGER,
	node_type_info_id INTEGER NOT NULL,
	PRIMARY KEY ("TargetInformation_id", node_type_info_id),
	FOREIGN KEY("TargetInformation_id") REFERENCES "TargetInformation" (id),
	FOREIGN KEY(node_type_info_id) REFERENCES "NodeType" (id)
);CREATE INDEX "ix_TargetInformation_node_type_info_TargetInformation_id" ON "TargetInformation_node_type_info" ("TargetInformation_id");CREATE INDEX "ix_TargetInformation_node_type_info_node_type_info_id" ON "TargetInformation_node_type_info" (node_type_info_id);
CREATE TABLE "TargetInformation_future_considerations" (
	"TargetInformation_id" INTEGER,
	future_considerations_id INTEGER,
	PRIMARY KEY ("TargetInformation_id", future_considerations_id),
	FOREIGN KEY("TargetInformation_id") REFERENCES "TargetInformation" (id),
	FOREIGN KEY(future_considerations_id) REFERENCES "FutureModelingConsiderations" (id)
);CREATE INDEX "ix_TargetInformation_future_considerations_TargetInformation_id" ON "TargetInformation_future_considerations" ("TargetInformation_id");CREATE INDEX "ix_TargetInformation_future_considerations_future_considerations_id" ON "TargetInformation_future_considerations" (future_considerations_id);
CREATE TABLE "EdgeType_subject_categories" (
	"EdgeType_id" INTEGER,
	subject_categories TEXT NOT NULL,
	PRIMARY KEY ("EdgeType_id", subject_categories),
	FOREIGN KEY("EdgeType_id") REFERENCES "EdgeType" (id)
);CREATE INDEX "ix_EdgeType_subject_categories_subject_categories" ON "EdgeType_subject_categories" (subject_categories);CREATE INDEX "ix_EdgeType_subject_categories_EdgeType_id" ON "EdgeType_subject_categories" ("EdgeType_id");
CREATE TABLE "EdgeType_predicates" (
	"EdgeType_id" INTEGER,
	predicates TEXT NOT NULL,
	PRIMARY KEY ("EdgeType_id", predicates),
	FOREIGN KEY("EdgeType_id") REFERENCES "EdgeType" (id)
);CREATE INDEX "ix_EdgeType_predicates_predicates" ON "EdgeType_predicates" (predicates);CREATE INDEX "ix_EdgeType_predicates_EdgeType_id" ON "EdgeType_predicates" ("EdgeType_id");
CREATE TABLE "EdgeType_object_categories" (
	"EdgeType_id" INTEGER,
	object_categories TEXT NOT NULL,
	PRIMARY KEY ("EdgeType_id", object_categories),
	FOREIGN KEY("EdgeType_id") REFERENCES "EdgeType" (id)
);CREATE INDEX "ix_EdgeType_object_categories_object_categories" ON "EdgeType_object_categories" (object_categories);CREATE INDEX "ix_EdgeType_object_categories_EdgeType_id" ON "EdgeType_object_categories" ("EdgeType_id");
CREATE TABLE "EdgeType_qualifiers" (
	"EdgeType_id" INTEGER,
	qualifiers_id INTEGER,
	PRIMARY KEY ("EdgeType_id", qualifiers_id),
	FOREIGN KEY("EdgeType_id") REFERENCES "EdgeType" (id),
	FOREIGN KEY(qualifiers_id) REFERENCES "Qualifier" (id)
);CREATE INDEX "ix_EdgeType_qualifiers_qualifiers_id" ON "EdgeType_qualifiers" (qualifiers_id);CREATE INDEX "ix_EdgeType_qualifiers_EdgeType_id" ON "EdgeType_qualifiers" ("EdgeType_id");
CREATE TABLE "EdgeType_knowledge_level" (
	"EdgeType_id" INTEGER,
	knowledge_level VARCHAR(23) NOT NULL,
	PRIMARY KEY ("EdgeType_id", knowledge_level),
	FOREIGN KEY("EdgeType_id") REFERENCES "EdgeType" (id)
);CREATE INDEX "ix_EdgeType_knowledge_level_EdgeType_id" ON "EdgeType_knowledge_level" ("EdgeType_id");CREATE INDEX "ix_EdgeType_knowledge_level_knowledge_level" ON "EdgeType_knowledge_level" (knowledge_level);
CREATE TABLE "EdgeType_agent_type" (
	"EdgeType_id" INTEGER,
	agent_type VARCHAR(36) NOT NULL,
	PRIMARY KEY ("EdgeType_id", agent_type),
	FOREIGN KEY("EdgeType_id") REFERENCES "EdgeType" (id)
);CREATE INDEX "ix_EdgeType_agent_type_agent_type" ON "EdgeType_agent_type" (agent_type);CREATE INDEX "ix_EdgeType_agent_type_EdgeType_id" ON "EdgeType_agent_type" ("EdgeType_id");
CREATE TABLE "EdgeType_primary_knowledge_sources" (
	"EdgeType_id" INTEGER,
	primary_knowledge_sources TEXT NOT NULL,
	PRIMARY KEY ("EdgeType_id", primary_knowledge_sources),
	FOREIGN KEY("EdgeType_id") REFERENCES "EdgeType" (id)
);CREATE INDEX "ix_EdgeType_primary_knowledge_sources_EdgeType_id" ON "EdgeType_primary_knowledge_sources" ("EdgeType_id");CREATE INDEX "ix_EdgeType_primary_knowledge_sources_primary_knowledge_sources" ON "EdgeType_primary_knowledge_sources" (primary_knowledge_sources);
CREATE TABLE "EdgeType_supporting_data_sources" (
	"EdgeType_id" INTEGER,
	supporting_data_sources TEXT,
	PRIMARY KEY ("EdgeType_id", supporting_data_sources),
	FOREIGN KEY("EdgeType_id") REFERENCES "EdgeType" (id)
);CREATE INDEX "ix_EdgeType_supporting_data_sources_EdgeType_id" ON "EdgeType_supporting_data_sources" ("EdgeType_id");CREATE INDEX "ix_EdgeType_supporting_data_sources_supporting_data_sources" ON "EdgeType_supporting_data_sources" (supporting_data_sources);
CREATE TABLE "EdgeType_aggregator_knowledge_sources" (
	"EdgeType_id" INTEGER,
	aggregator_knowledge_sources TEXT,
	PRIMARY KEY ("EdgeType_id", aggregator_knowledge_sources),
	FOREIGN KEY("EdgeType_id") REFERENCES "EdgeType" (id)
);CREATE INDEX "ix_EdgeType_aggregator_knowledge_sources_EdgeType_id" ON "EdgeType_aggregator_knowledge_sources" ("EdgeType_id");CREATE INDEX "ix_EdgeType_aggregator_knowledge_sources_aggregator_knowledge_sources" ON "EdgeType_aggregator_knowledge_sources" (aggregator_knowledge_sources);
CREATE TABLE "EdgeType_edge_properties" (
	"EdgeType_id" INTEGER,
	edge_properties TEXT,
	PRIMARY KEY ("EdgeType_id", edge_properties),
	FOREIGN KEY("EdgeType_id") REFERENCES "EdgeType" (id)
);CREATE INDEX "ix_EdgeType_edge_properties_edge_properties" ON "EdgeType_edge_properties" (edge_properties);CREATE INDEX "ix_EdgeType_edge_properties_EdgeType_id" ON "EdgeType_edge_properties" ("EdgeType_id");
CREATE TABLE "EdgeType_source_files" (
	"EdgeType_id" INTEGER,
	source_files TEXT,
	PRIMARY KEY ("EdgeType_id", source_files),
	FOREIGN KEY("EdgeType_id") REFERENCES "EdgeType" (id)
);CREATE INDEX "ix_EdgeType_source_files_source_files" ON "EdgeType_source_files" (source_files);CREATE INDEX "ix_EdgeType_source_files_EdgeType_id" ON "EdgeType_source_files" ("EdgeType_id");
CREATE TABLE "Qualifier_value_range" (
	"Qualifier_id" INTEGER,
	value_range TEXT,
	PRIMARY KEY ("Qualifier_id", value_range),
	FOREIGN KEY("Qualifier_id") REFERENCES "Qualifier" (id)
);CREATE INDEX "ix_Qualifier_value_range_value_range" ON "Qualifier_value_range" (value_range);CREATE INDEX "ix_Qualifier_value_range_Qualifier_id" ON "Qualifier_value_range" ("Qualifier_id");
CREATE TABLE "Qualifier_value_enumeration" (
	"Qualifier_id" INTEGER,
	value_enumeration TEXT,
	PRIMARY KEY ("Qualifier_id", value_enumeration),
	FOREIGN KEY("Qualifier_id") REFERENCES "Qualifier" (id)
);CREATE INDEX "ix_Qualifier_value_enumeration_value_enumeration" ON "Qualifier_value_enumeration" (value_enumeration);CREATE INDEX "ix_Qualifier_value_enumeration_Qualifier_id" ON "Qualifier_value_enumeration" ("Qualifier_id");
CREATE TABLE "Qualifier_value_id_prefixes" (
	"Qualifier_id" INTEGER,
	value_id_prefixes TEXT,
	PRIMARY KEY ("Qualifier_id", value_id_prefixes),
	FOREIGN KEY("Qualifier_id") REFERENCES "Qualifier" (id)
);CREATE INDEX "ix_Qualifier_value_id_prefixes_Qualifier_id" ON "Qualifier_value_id_prefixes" ("Qualifier_id");CREATE INDEX "ix_Qualifier_value_id_prefixes_value_id_prefixes" ON "Qualifier_value_id_prefixes" (value_id_prefixes);
CREATE TABLE "NodeType_source_identifier_types" (
	"NodeType_id" INTEGER,
	source_identifier_types TEXT NOT NULL,
	PRIMARY KEY ("NodeType_id", source_identifier_types),
	FOREIGN KEY("NodeType_id") REFERENCES "NodeType" (id)
);CREATE INDEX "ix_NodeType_source_identifier_types_source_identifier_types" ON "NodeType_source_identifier_types" (source_identifier_types);CREATE INDEX "ix_NodeType_source_identifier_types_NodeType_id" ON "NodeType_source_identifier_types" ("NodeType_id");
CREATE TABLE "NodeType_node_properties" (
	"NodeType_id" INTEGER,
	node_properties TEXT,
	PRIMARY KEY ("NodeType_id", node_properties),
	FOREIGN KEY("NodeType_id") REFERENCES "NodeType" (id)
);CREATE INDEX "ix_NodeType_node_properties_node_properties" ON "NodeType_node_properties" (node_properties);CREATE INDEX "ix_NodeType_node_properties_NodeType_id" ON "NodeType_node_properties" ("NodeType_id");
CREATE TABLE "ProvenanceInformation_contributions" (
	"ProvenanceInformation_id" INTEGER,
	contributions TEXT,
	PRIMARY KEY ("ProvenanceInformation_id", contributions),
	FOREIGN KEY("ProvenanceInformation_id") REFERENCES "ProvenanceInformation" (id)
);CREATE INDEX "ix_ProvenanceInformation_contributions_contributions" ON "ProvenanceInformation_contributions" (contributions);CREATE INDEX "ix_ProvenanceInformation_contributions_ProvenanceInformation_id" ON "ProvenanceInformation_contributions" ("ProvenanceInformation_id");
CREATE TABLE "ProvenanceInformation_artifacts" (
	"ProvenanceInformation_id" INTEGER,
	artifacts TEXT,
	PRIMARY KEY ("ProvenanceInformation_id", artifacts),
	FOREIGN KEY("ProvenanceInformation_id") REFERENCES "ProvenanceInformation" (id)
);CREATE INDEX "ix_ProvenanceInformation_artifacts_artifacts" ON "ProvenanceInformation_artifacts" (artifacts);CREATE INDEX "ix_ProvenanceInformation_artifacts_ProvenanceInformation_id" ON "ProvenanceInformation_artifacts" ("ProvenanceInformation_id");
CREATE TABLE "ReferenceIngestGuide" (
	id INTEGER NOT NULL,
	name TEXT,
	source_info_id INTEGER NOT NULL,
	ingest_info_id INTEGER NOT NULL,
	target_info_id INTEGER NOT NULL,
	provenance_info_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(source_info_id) REFERENCES "SourceInformation" (id),
	FOREIGN KEY(ingest_info_id) REFERENCES "IngestInformation" (id),
	FOREIGN KEY(target_info_id) REFERENCES "TargetInformation" (id),
	FOREIGN KEY(provenance_info_id) REFERENCES "ProvenanceInformation" (id)
);CREATE INDEX "ix_ReferenceIngestGuide_id" ON "ReferenceIngestGuide" (id);
CREATE TABLE "SupportingDataSourceInformation_relevant_files" (
	"SupportingDataSourceInformation_id" INTEGER,
	relevant_files_id INTEGER NOT NULL,
	PRIMARY KEY ("SupportingDataSourceInformation_id", relevant_files_id),
	FOREIGN KEY("SupportingDataSourceInformation_id") REFERENCES "SupportingDataSourceInformation" (id),
	FOREIGN KEY(relevant_files_id) REFERENCES "RelevantFiles" (id)
);CREATE INDEX "ix_SupportingDataSourceInformation_relevant_files_SupportingDataSourceInformation_id" ON "SupportingDataSourceInformation_relevant_files" ("SupportingDataSourceInformation_id");CREATE INDEX "ix_SupportingDataSourceInformation_relevant_files_relevant_files_id" ON "SupportingDataSourceInformation_relevant_files" (relevant_files_id);
CREATE TABLE "SourceInformation_citations" (
	"SourceInformation_id" INTEGER,
	citations TEXT,
	PRIMARY KEY ("SourceInformation_id", citations),
	FOREIGN KEY("SourceInformation_id") REFERENCES "SourceInformation" (id)
);CREATE INDEX "ix_SourceInformation_citations_SourceInformation_id" ON "SourceInformation_citations" ("SourceInformation_id");CREATE INDEX "ix_SourceInformation_citations_citations" ON "SourceInformation_citations" (citations);
CREATE TABLE "SourceInformation_data_access_locations" (
	"SourceInformation_id" INTEGER,
	data_access_locations TEXT NOT NULL,
	PRIMARY KEY ("SourceInformation_id", data_access_locations),
	FOREIGN KEY("SourceInformation_id") REFERENCES "SourceInformation" (id)
);CREATE INDEX "ix_SourceInformation_data_access_locations_SourceInformation_id" ON "SourceInformation_data_access_locations" ("SourceInformation_id");CREATE INDEX "ix_SourceInformation_data_access_locations_data_access_locations" ON "SourceInformation_data_access_locations" (data_access_locations);
CREATE TABLE "SourceInformation_data_provision_mechanisms" (
	"SourceInformation_id" INTEGER,
	data_provision_mechanisms VARCHAR(13),
	PRIMARY KEY ("SourceInformation_id", data_provision_mechanisms),
	FOREIGN KEY("SourceInformation_id") REFERENCES "SourceInformation" (id)
);CREATE INDEX "ix_SourceInformation_data_provision_mechanisms_SourceInformation_id" ON "SourceInformation_data_provision_mechanisms" ("SourceInformation_id");CREATE INDEX "ix_SourceInformation_data_provision_mechanisms_data_provision_mechanisms" ON "SourceInformation_data_provision_mechanisms" (data_provision_mechanisms);
CREATE TABLE "SourceInformation_data_formats" (
	"SourceInformation_id" INTEGER,
	data_formats VARCHAR(10),
	PRIMARY KEY ("SourceInformation_id", data_formats),
	FOREIGN KEY("SourceInformation_id") REFERENCES "SourceInformation" (id)
);CREATE INDEX "ix_SourceInformation_data_formats_SourceInformation_id" ON "SourceInformation_data_formats" ("SourceInformation_id");CREATE INDEX "ix_SourceInformation_data_formats_data_formats" ON "SourceInformation_data_formats" (data_formats);
CREATE TABLE "ReferenceIngestGuide_supporting_data_source_info" (
	"ReferenceIngestGuide_id" INTEGER,
	supporting_data_source_info_id INTEGER,
	PRIMARY KEY ("ReferenceIngestGuide_id", supporting_data_source_info_id),
	FOREIGN KEY("ReferenceIngestGuide_id") REFERENCES "ReferenceIngestGuide" (id),
	FOREIGN KEY(supporting_data_source_info_id) REFERENCES "SupportingDataSourceInformation" (id)
);CREATE INDEX "ix_ReferenceIngestGuide_supporting_data_source_info_ReferenceIngestGuide_id" ON "ReferenceIngestGuide_supporting_data_source_info" ("ReferenceIngestGuide_id");CREATE INDEX "ix_ReferenceIngestGuide_supporting_data_source_info_supporting_data_source_info_id" ON "ReferenceIngestGuide_supporting_data_source_info" (supporting_data_source_info_id);
