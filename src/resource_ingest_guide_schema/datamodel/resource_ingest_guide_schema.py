# Auto generated from resource_ingest_guide_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-07-08T15:57:25
# Schema: reference_ingest_guide
#
# id: https://w3id.org/biolink/resource-ingest-guide-schema
# description: A schema for describing the scope, rationale, and modeling approach for ingesting content from an external resource to a data repository compliant with the Biolink Model.
# license: MIT

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.7.0"
version = None

# Namespaces
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
DEFAULT_ = BIOLINK


# Types

# Class references



@dataclass(repr=False)
class ReferenceIngestGuide(YAMLRoot):
    """
    A container that holds attributes for the discrete sections of information comprising a Resource Ingest Guide.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["ReferenceIngestGuide"]
    class_class_curie: ClassVar[str] = "biolink:ReferenceIngestGuide"
    class_name: ClassVar[str] = "ReferenceIngestGuide"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ReferenceIngestGuide

    source_info: Union[dict, "SourceInformation"] = None
    ingest_info: Union[dict, "IngestInformation"] = None
    target_info: Union[dict, "TargetInformation"] = None
    name: Optional[str] = None
    supporting_data_source_info: Optional[Union[Union[dict, "SupportingDataSourceInformation"], list[Union[dict, "SupportingDataSourceInformation"]]]] = empty_list()
    provenance_info: Optional[Union[dict, "ProvenanceInformation"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.source_info):
            self.MissingRequiredField("source_info")
        if not isinstance(self.source_info, SourceInformation):
            self.source_info = SourceInformation(**as_dict(self.source_info))

        if self._is_empty(self.ingest_info):
            self.MissingRequiredField("ingest_info")
        if not isinstance(self.ingest_info, IngestInformation):
            self.ingest_info = IngestInformation(**as_dict(self.ingest_info))

        if self._is_empty(self.target_info):
            self.MissingRequiredField("target_info")
        if not isinstance(self.target_info, TargetInformation):
            self.target_info = TargetInformation(**as_dict(self.target_info))

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        self._normalize_inlined_as_dict(slot_name="supporting_data_source_info", slot_type=SupportingDataSourceInformation, key_name="infores_id", keyed=False)

        if self.provenance_info is not None and not isinstance(self.provenance_info, ProvenanceInformation):
            self.provenance_info = ProvenanceInformation(**as_dict(self.provenance_info))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SupportingDataSourceInformation(YAMLRoot):
    """
    A container for information about upstream sources of data that are used by an ingested source, to derive the
    knowledge that we ingest. This info is not relevant for typical ingest of an external knowledge source, and
    applies mainly for describing "ingest" of data-derived KPs like ICEES, COHD, various Multiomics KPs, etc.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["SupportingDataSourceInformation"]
    class_class_curie: ClassVar[str] = "biolink:SupportingDataSourceInformation"
    class_name: ClassVar[str] = "SupportingDataSourceInformation"
    class_model_uri: ClassVar[URIRef] = BIOLINK.SupportingDataSourceInformation

    infores_id: Union[str, URIorCURIE] = None
    terms_of_use_info: Union[dict, "TermsOfUseInformation"] = None
    relevant_files: Union[Union[dict, "RelevantFiles"], list[Union[dict, "RelevantFiles"]]] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.infores_id):
            self.MissingRequiredField("infores_id")
        if not isinstance(self.infores_id, URIorCURIE):
            self.infores_id = URIorCURIE(self.infores_id)

        if self._is_empty(self.terms_of_use_info):
            self.MissingRequiredField("terms_of_use_info")
        if not isinstance(self.terms_of_use_info, TermsOfUseInformation):
            self.terms_of_use_info = TermsOfUseInformation(**as_dict(self.terms_of_use_info))

        if self._is_empty(self.relevant_files):
            self.MissingRequiredField("relevant_files")
        self._normalize_inlined_as_dict(slot_name="relevant_files", slot_type=RelevantFiles, key_name="file_name", keyed=False)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SourceInformation(YAMLRoot):
    """
    A container for capturing information about the source of the ingest.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["SourceInformation"]
    class_class_curie: ClassVar[str] = "biolink:SourceInformation"
    class_name: ClassVar[str] = "SourceInformation"
    class_model_uri: ClassVar[URIRef] = BIOLINK.SourceInformation

    infores_id: Union[str, URIorCURIE] = None
    terms_of_use_info: Union[dict, "TermsOfUseInformation"] = None
    data_access_locations: Union[str, list[str]] = None
    source_status: Union[str, "SourceStatusEnum"] = None
    name: Optional[str] = None
    description: Optional[str] = None
    citations: Optional[Union[str, list[str]]] = empty_list()
    data_provision_mechanisms: Optional[Union[Union[str, "ProvisionMechanismEnum"], list[Union[str, "ProvisionMechanismEnum"]]]] = empty_list()
    data_formats: Optional[Union[Union[str, "DataFormatEnum"], list[Union[str, "DataFormatEnum"]]]] = empty_list()
    data_versioning_and_releases: Optional[str] = None
    additional_notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.infores_id):
            self.MissingRequiredField("infores_id")
        if not isinstance(self.infores_id, URIorCURIE):
            self.infores_id = URIorCURIE(self.infores_id)

        if self._is_empty(self.terms_of_use_info):
            self.MissingRequiredField("terms_of_use_info")
        if not isinstance(self.terms_of_use_info, TermsOfUseInformation):
            self.terms_of_use_info = TermsOfUseInformation(**as_dict(self.terms_of_use_info))

        if self._is_empty(self.data_access_locations):
            self.MissingRequiredField("data_access_locations")
        if not isinstance(self.data_access_locations, list):
            self.data_access_locations = [self.data_access_locations] if self.data_access_locations is not None else []
        self.data_access_locations = [v if isinstance(v, str) else str(v) for v in self.data_access_locations]

        if self._is_empty(self.source_status):
            self.MissingRequiredField("source_status")
        if not isinstance(self.source_status, SourceStatusEnum):
            self.source_status = SourceStatusEnum(self.source_status)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.citations, list):
            self.citations = [self.citations] if self.citations is not None else []
        self.citations = [v if isinstance(v, str) else str(v) for v in self.citations]

        if not isinstance(self.data_provision_mechanisms, list):
            self.data_provision_mechanisms = [self.data_provision_mechanisms] if self.data_provision_mechanisms is not None else []
        self.data_provision_mechanisms = [v if isinstance(v, ProvisionMechanismEnum) else ProvisionMechanismEnum(v) for v in self.data_provision_mechanisms]

        if not isinstance(self.data_formats, list):
            self.data_formats = [self.data_formats] if self.data_formats is not None else []
        self.data_formats = [v if isinstance(v, DataFormatEnum) else DataFormatEnum(v) for v in self.data_formats]

        if self.data_versioning_and_releases is not None and not isinstance(self.data_versioning_and_releases, str):
            self.data_versioning_and_releases = str(self.data_versioning_and_releases)

        if self.additional_notes is not None and not isinstance(self.additional_notes, str):
            self.additional_notes = str(self.additional_notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TermsOfUseInformation(YAMLRoot):
    """
    A structured representation describing terms for re-use of data from an information resource.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["TermsOfUseInformation"]
    class_class_curie: ClassVar[str] = "biolink:TermsOfUseInformation"
    class_name: ClassVar[str] = "TermsOfUseInformation"
    class_model_uri: ClassVar[URIRef] = BIOLINK.TermsOfUseInformation

    terms_of_use_url: Optional[Union[str, URIorCURIE]] = None
    terms_of_use_description: Optional[str] = None
    license_name: Optional[str] = None
    license_url: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.terms_of_use_url is not None and not isinstance(self.terms_of_use_url, URIorCURIE):
            self.terms_of_use_url = URIorCURIE(self.terms_of_use_url)

        if self.terms_of_use_description is not None and not isinstance(self.terms_of_use_description, str):
            self.terms_of_use_description = str(self.terms_of_use_description)

        if self.license_name is not None and not isinstance(self.license_name, str):
            self.license_name = str(self.license_name)

        if self.license_url is not None and not isinstance(self.license_url, URIorCURIE):
            self.license_url = URIorCURIE(self.license_url)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IngestInformation(YAMLRoot):
    """
    A container for capturing information about the rationale and scope of an ingest, including what source content
    was included and excluded from the ingest, and what additional content might be considered in future iterations.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["IngestInformation"]
    class_class_curie: ClassVar[str] = "biolink:IngestInformation"
    class_name: ClassVar[str] = "IngestInformation"
    class_model_uri: ClassVar[URIRef] = BIOLINK.IngestInformation

    utility: str = None
    relevant_files: Union[Union[dict, "RelevantFiles"], list[Union[dict, "RelevantFiles"]]] = None
    ingest_categories: Optional[Union[Union[str, "IngestCategoryEnum"], list[Union[str, "IngestCategoryEnum"]]]] = empty_list()
    scope: Optional[str] = None
    included_content: Optional[Union[Union[dict, "IncludedContent"], list[Union[dict, "IncludedContent"]]]] = empty_list()
    filtered_content: Optional[Union[Union[dict, "FilteredContent"], list[Union[dict, "FilteredContent"]]]] = empty_list()
    future_considerations: Optional[Union[Union[dict, "FutureContentConsiderations"], list[Union[dict, "FutureContentConsiderations"]]]] = empty_list()
    additional_notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.utility):
            self.MissingRequiredField("utility")
        if not isinstance(self.utility, str):
            self.utility = str(self.utility)

        if self._is_empty(self.relevant_files):
            self.MissingRequiredField("relevant_files")
        self._normalize_inlined_as_dict(slot_name="relevant_files", slot_type=RelevantFiles, key_name="file_name", keyed=False)

        if not isinstance(self.ingest_categories, list):
            self.ingest_categories = [self.ingest_categories] if self.ingest_categories is not None else []
        self.ingest_categories = [v if isinstance(v, IngestCategoryEnum) else IngestCategoryEnum(v) for v in self.ingest_categories]

        if self.scope is not None and not isinstance(self.scope, str):
            self.scope = str(self.scope)

        self._normalize_inlined_as_dict(slot_name="included_content", slot_type=IncludedContent, key_name="file_name", keyed=False)

        self._normalize_inlined_as_dict(slot_name="filtered_content", slot_type=FilteredContent, key_name="file_name", keyed=False)

        self._normalize_inlined_as_dict(slot_name="future_considerations", slot_type=FutureContentConsiderations, key_name="category", keyed=False)

        if self.additional_notes is not None and not isinstance(self.additional_notes, str):
            self.additional_notes = str(self.additional_notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RelevantFiles(YAMLRoot):
    """
    A structure for describing each source file (or API endpoint, database, or table) that contains content in scope
    for the ingest. Source files containing which content is not retrieved in this ingest need not be listed or
    described.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["RelevantFiles"]
    class_class_curie: ClassVar[str] = "biolink:RelevantFiles"
    class_name: ClassVar[str] = "RelevantFiles"
    class_model_uri: ClassVar[URIRef] = BIOLINK.RelevantFiles

    file_name: str = None
    location: Union[str, URIorCURIE] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.file_name):
            self.MissingRequiredField("file_name")
        if not isinstance(self.file_name, str):
            self.file_name = str(self.file_name)

        if self._is_empty(self.location):
            self.MissingRequiredField("location")
        if not isinstance(self.location, URIorCURIE):
            self.location = URIorCURIE(self.location)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IncludedContent(YAMLRoot):
    """
    A structure for describing the types of records from relevant files/endpoints/tables are included in this ingest,
    and optionally a list of fields from these records that are part of the ingest or used to inform it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["IncludedContent"]
    class_class_curie: ClassVar[str] = "biolink:IncludedContent"
    class_name: ClassVar[str] = "IncludedContent"
    class_model_uri: ClassVar[URIRef] = BIOLINK.IncludedContent

    file_name: str = None
    included_records: str = None
    fields_used: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.file_name):
            self.MissingRequiredField("file_name")
        if not isinstance(self.file_name, str):
            self.file_name = str(self.file_name)

        if self._is_empty(self.included_records):
            self.MissingRequiredField("included_records")
        if not isinstance(self.included_records, str):
            self.included_records = str(self.included_records)

        if self.fields_used is not None and not isinstance(self.fields_used, str):
            self.fields_used = str(self.fields_used)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FilteredContent(YAMLRoot):
    """
    A structure for describing the types of records from each relevant file/endpoint/table not included in the ingest,
    and the rationale for any filtering rules or exclusion criteria. Only list a file if some but not all records it
    contains are included in the ingest - to document what subset was excluded, and why.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["FilteredContent"]
    class_class_curie: ClassVar[str] = "biolink:FilteredContent"
    class_name: ClassVar[str] = "FilteredContent"
    class_model_uri: ClassVar[URIRef] = BIOLINK.FilteredContent

    file_name: str = None
    filtered_records: str = None
    rationale: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.file_name):
            self.MissingRequiredField("file_name")
        if not isinstance(self.file_name, str):
            self.file_name = str(self.file_name)

        if self._is_empty(self.filtered_records):
            self.MissingRequiredField("filtered_records")
        if not isinstance(self.filtered_records, str):
            self.filtered_records = str(self.filtered_records)

        if self._is_empty(self.rationale):
            self.MissingRequiredField("rationale")
        if not isinstance(self.rationale, str):
            self.rationale = str(self.rationale)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FutureContentConsiderations(YAMLRoot):
    """
    A structure for collecting notes about content additions or changes to consider in future iterations of this
    ingest. Create separate objects for each distinct consideration, and indicate if it relates to content that will
    be captured as Edges, Node Properties, or Edge Properties in the target knowledge graph.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["FutureContentConsiderations"]
    class_class_curie: ClassVar[str] = "biolink:FutureContentConsiderations"
    class_name: ClassVar[str] = "FutureContentConsiderations"
    class_model_uri: ClassVar[URIRef] = BIOLINK.FutureContentConsiderations

    category: Union[str, "ContentCategoryEnum"] = None
    consideration: str = None
    relevant_files: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, ContentCategoryEnum):
            self.category = ContentCategoryEnum(self.category)

        if self._is_empty(self.consideration):
            self.MissingRequiredField("consideration")
        if not isinstance(self.consideration, str):
            self.consideration = str(self.consideration)

        if self.relevant_files is not None and not isinstance(self.relevant_files, str):
            self.relevant_files = str(self.relevant_files)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TargetInformation(YAMLRoot):
    """
    A structure for capturing information about the target dataset / knowledge graph output by the ingest, including
    what types of edges and nodes were produced, modeling rationale, and what modeling changes might be considered in
    future iterations.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["TargetInformation"]
    class_class_curie: ClassVar[str] = "biolink:TargetInformation"
    class_name: ClassVar[str] = "TargetInformation"
    class_model_uri: ClassVar[URIRef] = BIOLINK.TargetInformation

    edge_type_info: Union[Union[dict, "EdgeType"], list[Union[dict, "EdgeType"]]] = None
    node_type_info: Union[Union[dict, "NodeType"], list[Union[dict, "NodeType"]]] = None
    infores_id: Optional[Union[str, URIorCURIE]] = None
    future_considerations: Optional[Union[Union[dict, "FutureModelingConsiderations"], list[Union[dict, "FutureModelingConsiderations"]]]] = empty_list()
    additional_notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.edge_type_info):
            self.MissingRequiredField("edge_type_info")
        self._normalize_inlined_as_dict(slot_name="edge_type_info", slot_type=EdgeType, key_name="subject_categories", keyed=False)

        if self._is_empty(self.node_type_info):
            self.MissingRequiredField("node_type_info")
        self._normalize_inlined_as_dict(slot_name="node_type_info", slot_type=NodeType, key_name="node_category", keyed=False)

        if self.infores_id is not None and not isinstance(self.infores_id, URIorCURIE):
            self.infores_id = URIorCURIE(self.infores_id)

        self._normalize_inlined_as_dict(slot_name="future_considerations", slot_type=FutureModelingConsiderations, key_name="consideration", keyed=False)

        if self.additional_notes is not None and not isinstance(self.additional_notes, str):
            self.additional_notes = str(self.additional_notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EdgeType(YAMLRoot):
    """
    A structure for describing each type of edge (metaedge) created in the target knowledge graph by this ingest,
    including what types of edge properties it holds, and a brief explanation of why this modeling pattern was deemed
    appropriate to represent the source data (for display to end users in a UI system). Note that an edge type with
    multiple subject_category and object_category values does not mean that the full cross-product must be
    instantiated in the data. e.g. A KG with the edge type sub_cat: [Gene, Protein, Small Molecule], predicate:
    affects, obj_cat: [disease, phenotype, symptom] might include Protein-affects-Disease and Gene-affects-Symptom
    edges, but not include any Protein-affects-Symptom edges.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["EdgeType"]
    class_class_curie: ClassVar[str] = "biolink:EdgeType"
    class_name: ClassVar[str] = "EdgeType"
    class_model_uri: ClassVar[URIRef] = BIOLINK.EdgeType

    subject_categories: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    predicates: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    object_categories: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    knowledge_level: Union[Union[str, "KnowledgeLevelEnum"], list[Union[str, "KnowledgeLevelEnum"]]] = None
    agent_type: Union[Union[str, "AgentTypeEnum"], list[Union[str, "AgentTypeEnum"]]] = None
    primary_knowledge_sources: Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]] = None
    ui_explanation: str = None
    qualifiers: Optional[Union[Union[dict, "Qualifier"], list[Union[dict, "Qualifier"]]]] = empty_list()
    supporting_data_sources: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    aggregator_knowledge_sources: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    edge_properties: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    source_files: Optional[Union[str, list[str]]] = empty_list()
    additional_notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.subject_categories):
            self.MissingRequiredField("subject_categories")
        if not isinstance(self.subject_categories, list):
            self.subject_categories = [self.subject_categories] if self.subject_categories is not None else []
        self.subject_categories = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.subject_categories]

        if self._is_empty(self.predicates):
            self.MissingRequiredField("predicates")
        if not isinstance(self.predicates, list):
            self.predicates = [self.predicates] if self.predicates is not None else []
        self.predicates = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.predicates]

        if self._is_empty(self.object_categories):
            self.MissingRequiredField("object_categories")
        if not isinstance(self.object_categories, list):
            self.object_categories = [self.object_categories] if self.object_categories is not None else []
        self.object_categories = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.object_categories]

        if self._is_empty(self.knowledge_level):
            self.MissingRequiredField("knowledge_level")
        if not isinstance(self.knowledge_level, list):
            self.knowledge_level = [self.knowledge_level] if self.knowledge_level is not None else []
        self.knowledge_level = [v if isinstance(v, KnowledgeLevelEnum) else KnowledgeLevelEnum(v) for v in self.knowledge_level]

        if self._is_empty(self.agent_type):
            self.MissingRequiredField("agent_type")
        if not isinstance(self.agent_type, list):
            self.agent_type = [self.agent_type] if self.agent_type is not None else []
        self.agent_type = [v if isinstance(v, AgentTypeEnum) else AgentTypeEnum(v) for v in self.agent_type]

        if self._is_empty(self.primary_knowledge_sources):
            self.MissingRequiredField("primary_knowledge_sources")
        if not isinstance(self.primary_knowledge_sources, list):
            self.primary_knowledge_sources = [self.primary_knowledge_sources] if self.primary_knowledge_sources is not None else []
        self.primary_knowledge_sources = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.primary_knowledge_sources]

        if self._is_empty(self.ui_explanation):
            self.MissingRequiredField("ui_explanation")
        if not isinstance(self.ui_explanation, str):
            self.ui_explanation = str(self.ui_explanation)

        self._normalize_inlined_as_dict(slot_name="qualifiers", slot_type=Qualifier, key_name="property", keyed=False)

        if not isinstance(self.supporting_data_sources, list):
            self.supporting_data_sources = [self.supporting_data_sources] if self.supporting_data_sources is not None else []
        self.supporting_data_sources = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.supporting_data_sources]

        if not isinstance(self.aggregator_knowledge_sources, list):
            self.aggregator_knowledge_sources = [self.aggregator_knowledge_sources] if self.aggregator_knowledge_sources is not None else []
        self.aggregator_knowledge_sources = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.aggregator_knowledge_sources]

        if not isinstance(self.edge_properties, list):
            self.edge_properties = [self.edge_properties] if self.edge_properties is not None else []
        self.edge_properties = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.edge_properties]

        if not isinstance(self.source_files, list):
            self.source_files = [self.source_files] if self.source_files is not None else []
        self.source_files = [v if isinstance(v, str) else str(v) for v in self.source_files]

        if self.additional_notes is not None and not isinstance(self.additional_notes, str):
            self.additional_notes = str(self.additional_notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Qualifier(YAMLRoot):
    """
    A qualifier property + value tuple that specifies a type of qualifier and value that may be applied to a
    Statement. Qualified predicates are considered qualifiers and captured here as well. Values can be specified to
    come from a proper range (e.g. Biolink class, data type, or enum), come from an enumerated list, use a specific id
    prefix, and/or conform informally to a free-text description.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["Qualifier"]
    class_class_curie: ClassVar[str] = "biolink:Qualifier"
    class_name: ClassVar[str] = "Qualifier"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Qualifier

    property: Union[str, URIorCURIE] = None
    value_range: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    value_enumeration: Optional[Union[str, list[str]]] = empty_list()
    value_id_prefixes: Optional[Union[str, list[str]]] = empty_list()
    value_description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.property):
            self.MissingRequiredField("property")
        if not isinstance(self.property, URIorCURIE):
            self.property = URIorCURIE(self.property)

        if not isinstance(self.value_range, list):
            self.value_range = [self.value_range] if self.value_range is not None else []
        self.value_range = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.value_range]

        if not isinstance(self.value_enumeration, list):
            self.value_enumeration = [self.value_enumeration] if self.value_enumeration is not None else []
        self.value_enumeration = [v if isinstance(v, str) else str(v) for v in self.value_enumeration]

        if not isinstance(self.value_id_prefixes, list):
            self.value_id_prefixes = [self.value_id_prefixes] if self.value_id_prefixes is not None else []
        self.value_id_prefixes = [v if isinstance(v, str) else str(v) for v in self.value_id_prefixes]

        if self.value_description is not None and not isinstance(self.value_description, str):
            self.value_description = str(self.value_description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NodeType(YAMLRoot):
    """
    A structured object describing each type of node created in the target knowledge graph by this ingest.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["NodeType"]
    class_class_curie: ClassVar[str] = "biolink:NodeType"
    class_name: ClassVar[str] = "NodeType"
    class_model_uri: ClassVar[URIRef] = BIOLINK.NodeType

    node_category: Union[str, URIorCURIE] = None
    source_identifier_types: Union[str, list[str]] = None
    node_properties: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    additional_notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.node_category):
            self.MissingRequiredField("node_category")
        if not isinstance(self.node_category, URIorCURIE):
            self.node_category = URIorCURIE(self.node_category)

        if self._is_empty(self.source_identifier_types):
            self.MissingRequiredField("source_identifier_types")
        if not isinstance(self.source_identifier_types, list):
            self.source_identifier_types = [self.source_identifier_types] if self.source_identifier_types is not None else []
        self.source_identifier_types = [v if isinstance(v, str) else str(v) for v in self.source_identifier_types]

        if not isinstance(self.node_properties, list):
            self.node_properties = [self.node_properties] if self.node_properties is not None else []
        self.node_properties = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.node_properties]

        if self.additional_notes is not None and not isinstance(self.additional_notes, str):
            self.additional_notes = str(self.additional_notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FutureModelingConsiderations(YAMLRoot):
    """
    A structure for collecting discrete considerations about modeling changes to consider in future iterations of this
    ingest. Create and categorize separate objects for each distinct consideration.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["FutureModelingConsiderations"]
    class_class_curie: ClassVar[str] = "biolink:FutureModelingConsiderations"
    class_name: ClassVar[str] = "FutureModelingConsiderations"
    class_model_uri: ClassVar[URIRef] = BIOLINK.FutureModelingConsiderations

    consideration: str = None
    category: Optional[Union[str, "ModelingCategoryEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.consideration):
            self.MissingRequiredField("consideration")
        if not isinstance(self.consideration, str):
            self.consideration = str(self.consideration)

        if self.category is not None and not isinstance(self.category, ModelingCategoryEnum):
            self.category = ModelingCategoryEnum(self.category)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProvenanceInformation(YAMLRoot):
    """
    A container holding information about the provenance of the ingest, including who contributed and how, and links
    to external provenance artifacts.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["ProvenanceInformation"]
    class_class_curie: ClassVar[str] = "biolink:ProvenanceInformation"
    class_name: ClassVar[str] = "ProvenanceInformation"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ProvenanceInformation

    contributions: Optional[Union[str, list[str]]] = empty_list()
    artifacts: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.contributions, list):
            self.contributions = [self.contributions] if self.contributions is not None else []
        self.contributions = [v if isinstance(v, str) else str(v) for v in self.contributions]

        if not isinstance(self.artifacts, list):
            self.artifacts = [self.artifacts] if self.artifacts is not None else []
        self.artifacts = [v if isinstance(v, str) else str(v) for v in self.artifacts]

        super().__post_init__(**kwargs)


# Enumerations
class ProvisionMechanismEnum(EnumDefinitionImpl):
    """
    Ways in which data can be made accessible for retrieval.
    """
    file_download = PermissibleValue(text="file_download")
    api_endpoint = PermissibleValue(text="api_endpoint")
    database_dump = PermissibleValue(text="database_dump")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="ProvisionMechanismEnum",
        description="Ways in which data can be made accessible for retrieval.",
    )

class DataFormatEnum(EnumDefinitionImpl):
    """
    Formats in which data is serialized.
    """
    tsv = PermissibleValue(text="tsv")
    xml = PermissibleValue(text="xml")
    csv = PermissibleValue(text="csv")
    json = PermissibleValue(text="json")
    yaml = PermissibleValue(text="yaml")
    obo = PermissibleValue(text="obo")
    protobuff = PermissibleValue(text="protobuff")
    kgx = PermissibleValue(text="kgx")
    mysql = PermissibleValue(text="mysql")
    postgresql = PermissibleValue(text="postgresql")
    sqlite = PermissibleValue(text="sqlite")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="DataFormatEnum",
        description="Formats in which data is serialized.",
    )

class ContentCategoryEnum(EnumDefinitionImpl):
    """
    Categories of content for future considerations
    """
    edge_content = PermissibleValue(text="edge_content")
    node_property_content = PermissibleValue(text="node_property_content")
    edge_property_content = PermissibleValue(text="edge_property_content")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="ContentCategoryEnum",
        description="Categories of content for future considerations",
    )

class KnowledgeLevelEnum(EnumDefinitionImpl):
    """
    Knowledge levels relevant to edges of a particular type.
    """
    knowledge_assertion = PermissibleValue(text="knowledge_assertion")
    logical_entailment = PermissibleValue(text="logical_entailment")
    prediction = PermissibleValue(text="prediction")
    statistical_association = PermissibleValue(text="statistical_association")
    observation = PermissibleValue(text="observation")
    not_provided = PermissibleValue(text="not_provided")
    varies = PermissibleValue(text="varies")

    _defn = EnumDefinition(
        name="KnowledgeLevelEnum",
        description="Knowledge levels relevant to edges of a particular type.",
    )

class AgentTypeEnum(EnumDefinitionImpl):
    """
    Agent types relevant to edges of a particular type.
    """
    manual_agent = PermissibleValue(text="manual_agent")
    automated_agent = PermissibleValue(text="automated_agent")
    computational_model = PermissibleValue(text="computational_model")
    data_analysis_pipeline = PermissibleValue(text="data_analysis_pipeline")
    text_mining_agent = PermissibleValue(text="text_mining_agent")
    image_processing_agent = PermissibleValue(text="image_processing_agent")
    manual_validation_of_automated_agent = PermissibleValue(text="manual_validation_of_automated_agent")
    experimental_agent = PermissibleValue(text="experimental_agent")
    not_provided = PermissibleValue(text="not_provided")
    varies = PermissibleValue(text="varies")

    _defn = EnumDefinition(
        name="AgentTypeEnum",
        description="Agent types relevant to edges of a particular type.",
    )

class SourceStatusEnum(EnumDefinitionImpl):
    """
    The maintenance status of a source, indicating whether it is actively maintained and how regularly it is updated.
    """
    maintained_regular_updates = PermissibleValue(
        text="maintained_regular_updates",
        description="The source is actively maintained and updated on a regular, predictable release cadence.")
    maintained_as_needed_updates = PermissibleValue(
        text="maintained_as_needed_updates",
        description="""The source is actively maintained but updated on an as-needed basis rather than a regular cadence.""")
    not_maintained = PermissibleValue(
        text="not_maintained",
        description="The source is no longer actively maintained or updated.")
    unknown = PermissibleValue(
        text="unknown",
        description="The maintenance status of the source is not known.")

    _defn = EnumDefinition(
        name="SourceStatusEnum",
        description="""The maintenance status of a source, indicating whether it is actively maintained and how regularly it is updated.""",
    )

class ModelingCategoryEnum(EnumDefinitionImpl):
    """
    Categories of future modeling considerations (what type of modeling the consideration is about).
    """
    spoq_pattern = PermissibleValue(text="spoq_pattern")
    predicates = PermissibleValue(text="predicates")
    qualifiers = PermissibleValue(text="qualifiers")
    edge_properties = PermissibleValue(text="edge_properties")
    node_properties = PermissibleValue(text="node_properties")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="ModelingCategoryEnum",
        description="Categories of future modeling considerations (what type of modeling the consideration is about).",
    )

class IngestCategoryEnum(EnumDefinitionImpl):
    """
    The type of source being ingested, from the perspective of the ingesting system.
    """
    primary_knowledge_provider = PermissibleValue(
        text="primary_knowledge_provider",
        description="""Provides knowledge that is curated/created/mined by the source (e.g. via  literature curation/interpretation, analysis of datasets, inference over evidence)""")
    aggregation_provider = PermissibleValue(
        text="aggregation_provider",
        description="""Aggregates knowledge from external sources and provides as is - with  minimal alteration/interpretation of what the primary source reported.  (e.g. Monarch, Diseases, Pharos)""")
    aggregation_interpreter = PermissibleValue(
        text="aggregation_interpreter",
        description="""Aggregates knowledge and assesses/interprets it as evidence to draw and report its  own conclusion (e.g. DGIdb, DisGenNet)""")
    supporting_data_provider = PermissibleValue(
        text="supporting_data_provider",
        description="""Provides information (data or prior facts) that is subsequently analyzed/ interpreted  by a Translator tool to derive new knowledge (e.g. TCGA, GTex, Carolina Data Warehouse)""")
    translator_knowledge_creator = PermissibleValue(
        text="translator_knowledge_creator",
        description="""A Translator tool that generates de novo knowledge from statistical  analysis, interpretation, or reasoning with more foundational data/ or facts  (e.g. ICEES, COHD, Multiomics Wellness, BigGIM)""")
    ontology_provider = PermissibleValue(
        text="ontology_provider",
        description="""An ontology or terminology artifact providing concept identifiers,  definitions, mappings, hierarchical relationships that are ingested into Translator KGs""")
    node_property_only_provider = PermissibleValue(
        text="node_property_only_provider",
        description="""Provides only information that is used to annotate nodes of a particular kind in  Translator graphs.""")
    other = PermissibleValue(
        text="other",
        description="""Used when the information provided by a source is not known, or does not fit into  the defined categories above""")

    _defn = EnumDefinition(
        name="IngestCategoryEnum",
        description="The type of source being ingested, from the perspective of the ingesting system.",
    )

# Slots
class slots:
    pass

slots.referenceIngestGuide__name = Slot(uri=BIOLINK.name, name="referenceIngestGuide__name", curie=BIOLINK.curie('name'),
                   model_uri=BIOLINK.referenceIngestGuide__name, domain=None, range=Optional[str])

slots.referenceIngestGuide__supporting_data_source_info = Slot(uri=BIOLINK.supporting_data_source_info, name="referenceIngestGuide__supporting_data_source_info", curie=BIOLINK.curie('supporting_data_source_info'),
                   model_uri=BIOLINK.referenceIngestGuide__supporting_data_source_info, domain=None, range=Optional[Union[Union[dict, SupportingDataSourceInformation], list[Union[dict, SupportingDataSourceInformation]]]])

slots.referenceIngestGuide__source_info = Slot(uri=BIOLINK.source_info, name="referenceIngestGuide__source_info", curie=BIOLINK.curie('source_info'),
                   model_uri=BIOLINK.referenceIngestGuide__source_info, domain=None, range=Union[dict, SourceInformation])

slots.referenceIngestGuide__ingest_info = Slot(uri=BIOLINK.ingest_info, name="referenceIngestGuide__ingest_info", curie=BIOLINK.curie('ingest_info'),
                   model_uri=BIOLINK.referenceIngestGuide__ingest_info, domain=None, range=Union[dict, IngestInformation])

slots.referenceIngestGuide__target_info = Slot(uri=BIOLINK.target_info, name="referenceIngestGuide__target_info", curie=BIOLINK.curie('target_info'),
                   model_uri=BIOLINK.referenceIngestGuide__target_info, domain=None, range=Union[dict, TargetInformation])

slots.referenceIngestGuide__provenance_info = Slot(uri=BIOLINK.provenance_info, name="referenceIngestGuide__provenance_info", curie=BIOLINK.curie('provenance_info'),
                   model_uri=BIOLINK.referenceIngestGuide__provenance_info, domain=None, range=Optional[Union[dict, ProvenanceInformation]])

slots.supportingDataSourceInformation__infores_id = Slot(uri=BIOLINK.infores_id, name="supportingDataSourceInformation__infores_id", curie=BIOLINK.curie('infores_id'),
                   model_uri=BIOLINK.supportingDataSourceInformation__infores_id, domain=None, range=Union[str, URIorCURIE])

slots.supportingDataSourceInformation__name = Slot(uri=BIOLINK.name, name="supportingDataSourceInformation__name", curie=BIOLINK.curie('name'),
                   model_uri=BIOLINK.supportingDataSourceInformation__name, domain=None, range=Optional[str])

slots.supportingDataSourceInformation__description = Slot(uri=BIOLINK.description, name="supportingDataSourceInformation__description", curie=BIOLINK.curie('description'),
                   model_uri=BIOLINK.supportingDataSourceInformation__description, domain=None, range=Optional[str])

slots.supportingDataSourceInformation__terms_of_use_info = Slot(uri=BIOLINK.terms_of_use_info, name="supportingDataSourceInformation__terms_of_use_info", curie=BIOLINK.curie('terms_of_use_info'),
                   model_uri=BIOLINK.supportingDataSourceInformation__terms_of_use_info, domain=None, range=Union[dict, TermsOfUseInformation])

slots.supportingDataSourceInformation__relevant_files = Slot(uri=BIOLINK.relevant_files, name="supportingDataSourceInformation__relevant_files", curie=BIOLINK.curie('relevant_files'),
                   model_uri=BIOLINK.supportingDataSourceInformation__relevant_files, domain=None, range=Union[Union[dict, RelevantFiles], list[Union[dict, RelevantFiles]]])

slots.sourceInformation__infores_id = Slot(uri=BIOLINK.infores_id, name="sourceInformation__infores_id", curie=BIOLINK.curie('infores_id'),
                   model_uri=BIOLINK.sourceInformation__infores_id, domain=None, range=Union[str, URIorCURIE])

slots.sourceInformation__name = Slot(uri=BIOLINK.name, name="sourceInformation__name", curie=BIOLINK.curie('name'),
                   model_uri=BIOLINK.sourceInformation__name, domain=None, range=Optional[str])

slots.sourceInformation__description = Slot(uri=BIOLINK.description, name="sourceInformation__description", curie=BIOLINK.curie('description'),
                   model_uri=BIOLINK.sourceInformation__description, domain=None, range=Optional[str])

slots.sourceInformation__citations = Slot(uri=BIOLINK.citations, name="sourceInformation__citations", curie=BIOLINK.curie('citations'),
                   model_uri=BIOLINK.sourceInformation__citations, domain=None, range=Optional[Union[str, list[str]]])

slots.sourceInformation__terms_of_use_info = Slot(uri=BIOLINK.terms_of_use_info, name="sourceInformation__terms_of_use_info", curie=BIOLINK.curie('terms_of_use_info'),
                   model_uri=BIOLINK.sourceInformation__terms_of_use_info, domain=None, range=Union[dict, TermsOfUseInformation])

slots.sourceInformation__data_access_locations = Slot(uri=BIOLINK.data_access_locations, name="sourceInformation__data_access_locations", curie=BIOLINK.curie('data_access_locations'),
                   model_uri=BIOLINK.sourceInformation__data_access_locations, domain=None, range=Union[str, list[str]])

slots.sourceInformation__data_provision_mechanisms = Slot(uri=BIOLINK.data_provision_mechanisms, name="sourceInformation__data_provision_mechanisms", curie=BIOLINK.curie('data_provision_mechanisms'),
                   model_uri=BIOLINK.sourceInformation__data_provision_mechanisms, domain=None, range=Optional[Union[Union[str, "ProvisionMechanismEnum"], list[Union[str, "ProvisionMechanismEnum"]]]])

slots.sourceInformation__data_formats = Slot(uri=BIOLINK.data_formats, name="sourceInformation__data_formats", curie=BIOLINK.curie('data_formats'),
                   model_uri=BIOLINK.sourceInformation__data_formats, domain=None, range=Optional[Union[Union[str, "DataFormatEnum"], list[Union[str, "DataFormatEnum"]]]])

slots.sourceInformation__data_versioning_and_releases = Slot(uri=BIOLINK.data_versioning_and_releases, name="sourceInformation__data_versioning_and_releases", curie=BIOLINK.curie('data_versioning_and_releases'),
                   model_uri=BIOLINK.sourceInformation__data_versioning_and_releases, domain=None, range=Optional[str])

slots.sourceInformation__source_status = Slot(uri=BIOLINK.source_status, name="sourceInformation__source_status", curie=BIOLINK.curie('source_status'),
                   model_uri=BIOLINK.sourceInformation__source_status, domain=None, range=Union[str, "SourceStatusEnum"])

slots.sourceInformation__additional_notes = Slot(uri=BIOLINK.additional_notes, name="sourceInformation__additional_notes", curie=BIOLINK.curie('additional_notes'),
                   model_uri=BIOLINK.sourceInformation__additional_notes, domain=None, range=Optional[str])

slots.termsOfUseInformation__terms_of_use_url = Slot(uri=BIOLINK.terms_of_use_url, name="termsOfUseInformation__terms_of_use_url", curie=BIOLINK.curie('terms_of_use_url'),
                   model_uri=BIOLINK.termsOfUseInformation__terms_of_use_url, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.termsOfUseInformation__terms_of_use_description = Slot(uri=BIOLINK.terms_of_use_description, name="termsOfUseInformation__terms_of_use_description", curie=BIOLINK.curie('terms_of_use_description'),
                   model_uri=BIOLINK.termsOfUseInformation__terms_of_use_description, domain=None, range=Optional[str])

slots.termsOfUseInformation__license_name = Slot(uri=BIOLINK.license_name, name="termsOfUseInformation__license_name", curie=BIOLINK.curie('license_name'),
                   model_uri=BIOLINK.termsOfUseInformation__license_name, domain=None, range=Optional[str])

slots.termsOfUseInformation__license_url = Slot(uri=BIOLINK.license_url, name="termsOfUseInformation__license_url", curie=BIOLINK.curie('license_url'),
                   model_uri=BIOLINK.termsOfUseInformation__license_url, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.ingestInformation__ingest_categories = Slot(uri=BIOLINK.ingest_categories, name="ingestInformation__ingest_categories", curie=BIOLINK.curie('ingest_categories'),
                   model_uri=BIOLINK.ingestInformation__ingest_categories, domain=None, range=Optional[Union[Union[str, "IngestCategoryEnum"], list[Union[str, "IngestCategoryEnum"]]]])

slots.ingestInformation__utility = Slot(uri=BIOLINK.utility, name="ingestInformation__utility", curie=BIOLINK.curie('utility'),
                   model_uri=BIOLINK.ingestInformation__utility, domain=None, range=str)

slots.ingestInformation__scope = Slot(uri=BIOLINK.scope, name="ingestInformation__scope", curie=BIOLINK.curie('scope'),
                   model_uri=BIOLINK.ingestInformation__scope, domain=None, range=Optional[str])

slots.ingestInformation__relevant_files = Slot(uri=BIOLINK.relevant_files, name="ingestInformation__relevant_files", curie=BIOLINK.curie('relevant_files'),
                   model_uri=BIOLINK.ingestInformation__relevant_files, domain=None, range=Union[Union[dict, RelevantFiles], list[Union[dict, RelevantFiles]]])

slots.ingestInformation__included_content = Slot(uri=BIOLINK.included_content, name="ingestInformation__included_content", curie=BIOLINK.curie('included_content'),
                   model_uri=BIOLINK.ingestInformation__included_content, domain=None, range=Optional[Union[Union[dict, IncludedContent], list[Union[dict, IncludedContent]]]])

slots.ingestInformation__filtered_content = Slot(uri=BIOLINK.filtered_content, name="ingestInformation__filtered_content", curie=BIOLINK.curie('filtered_content'),
                   model_uri=BIOLINK.ingestInformation__filtered_content, domain=None, range=Optional[Union[Union[dict, FilteredContent], list[Union[dict, FilteredContent]]]])

slots.ingestInformation__future_considerations = Slot(uri=BIOLINK.future_considerations, name="ingestInformation__future_considerations", curie=BIOLINK.curie('future_considerations'),
                   model_uri=BIOLINK.ingestInformation__future_considerations, domain=None, range=Optional[Union[Union[dict, FutureContentConsiderations], list[Union[dict, FutureContentConsiderations]]]])

slots.ingestInformation__additional_notes = Slot(uri=BIOLINK.additional_notes, name="ingestInformation__additional_notes", curie=BIOLINK.curie('additional_notes'),
                   model_uri=BIOLINK.ingestInformation__additional_notes, domain=None, range=Optional[str])

slots.relevantFiles__file_name = Slot(uri=BIOLINK.file_name, name="relevantFiles__file_name", curie=BIOLINK.curie('file_name'),
                   model_uri=BIOLINK.relevantFiles__file_name, domain=None, range=str)

slots.relevantFiles__location = Slot(uri=BIOLINK.location, name="relevantFiles__location", curie=BIOLINK.curie('location'),
                   model_uri=BIOLINK.relevantFiles__location, domain=None, range=Union[str, URIorCURIE])

slots.relevantFiles__description = Slot(uri=BIOLINK.description, name="relevantFiles__description", curie=BIOLINK.curie('description'),
                   model_uri=BIOLINK.relevantFiles__description, domain=None, range=Optional[str])

slots.includedContent__file_name = Slot(uri=BIOLINK.file_name, name="includedContent__file_name", curie=BIOLINK.curie('file_name'),
                   model_uri=BIOLINK.includedContent__file_name, domain=None, range=str)

slots.includedContent__included_records = Slot(uri=BIOLINK.included_records, name="includedContent__included_records", curie=BIOLINK.curie('included_records'),
                   model_uri=BIOLINK.includedContent__included_records, domain=None, range=str)

slots.includedContent__fields_used = Slot(uri=BIOLINK.fields_used, name="includedContent__fields_used", curie=BIOLINK.curie('fields_used'),
                   model_uri=BIOLINK.includedContent__fields_used, domain=None, range=Optional[str])

slots.filteredContent__file_name = Slot(uri=BIOLINK.file_name, name="filteredContent__file_name", curie=BIOLINK.curie('file_name'),
                   model_uri=BIOLINK.filteredContent__file_name, domain=None, range=str)

slots.filteredContent__filtered_records = Slot(uri=BIOLINK.filtered_records, name="filteredContent__filtered_records", curie=BIOLINK.curie('filtered_records'),
                   model_uri=BIOLINK.filteredContent__filtered_records, domain=None, range=str)

slots.filteredContent__rationale = Slot(uri=BIOLINK.rationale, name="filteredContent__rationale", curie=BIOLINK.curie('rationale'),
                   model_uri=BIOLINK.filteredContent__rationale, domain=None, range=str)

slots.futureContentConsiderations__category = Slot(uri=BIOLINK.category, name="futureContentConsiderations__category", curie=BIOLINK.curie('category'),
                   model_uri=BIOLINK.futureContentConsiderations__category, domain=None, range=Union[str, "ContentCategoryEnum"])

slots.futureContentConsiderations__consideration = Slot(uri=BIOLINK.consideration, name="futureContentConsiderations__consideration", curie=BIOLINK.curie('consideration'),
                   model_uri=BIOLINK.futureContentConsiderations__consideration, domain=None, range=str)

slots.futureContentConsiderations__relevant_files = Slot(uri=BIOLINK.relevant_files, name="futureContentConsiderations__relevant_files", curie=BIOLINK.curie('relevant_files'),
                   model_uri=BIOLINK.futureContentConsiderations__relevant_files, domain=None, range=Optional[str])

slots.targetInformation__infores_id = Slot(uri=BIOLINK.infores_id, name="targetInformation__infores_id", curie=BIOLINK.curie('infores_id'),
                   model_uri=BIOLINK.targetInformation__infores_id, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.targetInformation__edge_type_info = Slot(uri=BIOLINK.edge_type_info, name="targetInformation__edge_type_info", curie=BIOLINK.curie('edge_type_info'),
                   model_uri=BIOLINK.targetInformation__edge_type_info, domain=None, range=Union[Union[dict, EdgeType], list[Union[dict, EdgeType]]])

slots.targetInformation__node_type_info = Slot(uri=BIOLINK.node_type_info, name="targetInformation__node_type_info", curie=BIOLINK.curie('node_type_info'),
                   model_uri=BIOLINK.targetInformation__node_type_info, domain=None, range=Union[Union[dict, NodeType], list[Union[dict, NodeType]]])

slots.targetInformation__future_considerations = Slot(uri=BIOLINK.future_considerations, name="targetInformation__future_considerations", curie=BIOLINK.curie('future_considerations'),
                   model_uri=BIOLINK.targetInformation__future_considerations, domain=None, range=Optional[Union[Union[dict, FutureModelingConsiderations], list[Union[dict, FutureModelingConsiderations]]]])

slots.targetInformation__additional_notes = Slot(uri=BIOLINK.additional_notes, name="targetInformation__additional_notes", curie=BIOLINK.curie('additional_notes'),
                   model_uri=BIOLINK.targetInformation__additional_notes, domain=None, range=Optional[str])

slots.edgeType__subject_categories = Slot(uri=BIOLINK.subject_categories, name="edgeType__subject_categories", curie=BIOLINK.curie('subject_categories'),
                   model_uri=BIOLINK.edgeType__subject_categories, domain=None, range=Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]])

slots.edgeType__predicates = Slot(uri=BIOLINK.predicates, name="edgeType__predicates", curie=BIOLINK.curie('predicates'),
                   model_uri=BIOLINK.edgeType__predicates, domain=None, range=Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]])

slots.edgeType__object_categories = Slot(uri=BIOLINK.object_categories, name="edgeType__object_categories", curie=BIOLINK.curie('object_categories'),
                   model_uri=BIOLINK.edgeType__object_categories, domain=None, range=Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]])

slots.edgeType__qualifiers = Slot(uri=BIOLINK.qualifiers, name="edgeType__qualifiers", curie=BIOLINK.curie('qualifiers'),
                   model_uri=BIOLINK.edgeType__qualifiers, domain=None, range=Optional[Union[Union[dict, Qualifier], list[Union[dict, Qualifier]]]])

slots.edgeType__knowledge_level = Slot(uri=BIOLINK.knowledge_level, name="edgeType__knowledge_level", curie=BIOLINK.curie('knowledge_level'),
                   model_uri=BIOLINK.edgeType__knowledge_level, domain=None, range=Union[Union[str, "KnowledgeLevelEnum"], list[Union[str, "KnowledgeLevelEnum"]]])

slots.edgeType__agent_type = Slot(uri=BIOLINK.agent_type, name="edgeType__agent_type", curie=BIOLINK.curie('agent_type'),
                   model_uri=BIOLINK.edgeType__agent_type, domain=None, range=Union[Union[str, "AgentTypeEnum"], list[Union[str, "AgentTypeEnum"]]])

slots.edgeType__primary_knowledge_sources = Slot(uri=BIOLINK.primary_knowledge_sources, name="edgeType__primary_knowledge_sources", curie=BIOLINK.curie('primary_knowledge_sources'),
                   model_uri=BIOLINK.edgeType__primary_knowledge_sources, domain=None, range=Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]])

slots.edgeType__supporting_data_sources = Slot(uri=BIOLINK.supporting_data_sources, name="edgeType__supporting_data_sources", curie=BIOLINK.curie('supporting_data_sources'),
                   model_uri=BIOLINK.edgeType__supporting_data_sources, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.edgeType__aggregator_knowledge_sources = Slot(uri=BIOLINK.aggregator_knowledge_sources, name="edgeType__aggregator_knowledge_sources", curie=BIOLINK.curie('aggregator_knowledge_sources'),
                   model_uri=BIOLINK.edgeType__aggregator_knowledge_sources, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.edgeType__edge_properties = Slot(uri=BIOLINK.edge_properties, name="edgeType__edge_properties", curie=BIOLINK.curie('edge_properties'),
                   model_uri=BIOLINK.edgeType__edge_properties, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.edgeType__ui_explanation = Slot(uri=BIOLINK.ui_explanation, name="edgeType__ui_explanation", curie=BIOLINK.curie('ui_explanation'),
                   model_uri=BIOLINK.edgeType__ui_explanation, domain=None, range=str)

slots.edgeType__source_files = Slot(uri=BIOLINK.source_files, name="edgeType__source_files", curie=BIOLINK.curie('source_files'),
                   model_uri=BIOLINK.edgeType__source_files, domain=None, range=Optional[Union[str, list[str]]])

slots.edgeType__additional_notes = Slot(uri=BIOLINK.additional_notes, name="edgeType__additional_notes", curie=BIOLINK.curie('additional_notes'),
                   model_uri=BIOLINK.edgeType__additional_notes, domain=None, range=Optional[str])

slots.qualifier__property = Slot(uri=BIOLINK.property, name="qualifier__property", curie=BIOLINK.curie('property'),
                   model_uri=BIOLINK.qualifier__property, domain=None, range=Union[str, URIorCURIE])

slots.qualifier__value_range = Slot(uri=BIOLINK.value_range, name="qualifier__value_range", curie=BIOLINK.curie('value_range'),
                   model_uri=BIOLINK.qualifier__value_range, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.qualifier__value_enumeration = Slot(uri=BIOLINK.value_enumeration, name="qualifier__value_enumeration", curie=BIOLINK.curie('value_enumeration'),
                   model_uri=BIOLINK.qualifier__value_enumeration, domain=None, range=Optional[Union[str, list[str]]])

slots.qualifier__value_id_prefixes = Slot(uri=BIOLINK.value_id_prefixes, name="qualifier__value_id_prefixes", curie=BIOLINK.curie('value_id_prefixes'),
                   model_uri=BIOLINK.qualifier__value_id_prefixes, domain=None, range=Optional[Union[str, list[str]]])

slots.qualifier__value_description = Slot(uri=BIOLINK.value_description, name="qualifier__value_description", curie=BIOLINK.curie('value_description'),
                   model_uri=BIOLINK.qualifier__value_description, domain=None, range=Optional[str])

slots.nodeType__node_category = Slot(uri=BIOLINK.node_category, name="nodeType__node_category", curie=BIOLINK.curie('node_category'),
                   model_uri=BIOLINK.nodeType__node_category, domain=None, range=Union[str, URIorCURIE])

slots.nodeType__source_identifier_types = Slot(uri=BIOLINK.source_identifier_types, name="nodeType__source_identifier_types", curie=BIOLINK.curie('source_identifier_types'),
                   model_uri=BIOLINK.nodeType__source_identifier_types, domain=None, range=Union[str, list[str]])

slots.nodeType__node_properties = Slot(uri=BIOLINK.node_properties, name="nodeType__node_properties", curie=BIOLINK.curie('node_properties'),
                   model_uri=BIOLINK.nodeType__node_properties, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.nodeType__additional_notes = Slot(uri=BIOLINK.additional_notes, name="nodeType__additional_notes", curie=BIOLINK.curie('additional_notes'),
                   model_uri=BIOLINK.nodeType__additional_notes, domain=None, range=Optional[str])

slots.futureModelingConsiderations__category = Slot(uri=BIOLINK.category, name="futureModelingConsiderations__category", curie=BIOLINK.curie('category'),
                   model_uri=BIOLINK.futureModelingConsiderations__category, domain=None, range=Optional[Union[str, "ModelingCategoryEnum"]])

slots.futureModelingConsiderations__consideration = Slot(uri=BIOLINK.consideration, name="futureModelingConsiderations__consideration", curie=BIOLINK.curie('consideration'),
                   model_uri=BIOLINK.futureModelingConsiderations__consideration, domain=None, range=str)

slots.provenanceInformation__contributions = Slot(uri=BIOLINK.contributions, name="provenanceInformation__contributions", curie=BIOLINK.curie('contributions'),
                   model_uri=BIOLINK.provenanceInformation__contributions, domain=None, range=Optional[Union[str, list[str]]])

slots.provenanceInformation__artifacts = Slot(uri=BIOLINK.artifacts, name="provenanceInformation__artifacts", curie=BIOLINK.curie('artifacts'),
                   model_uri=BIOLINK.provenanceInformation__artifacts, domain=None, range=Optional[Union[str, list[str]]])
