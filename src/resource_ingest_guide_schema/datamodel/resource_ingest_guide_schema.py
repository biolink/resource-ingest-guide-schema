# Auto generated from resource_ingest_guide_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-08-11T12:33:44
# Schema: resource-ingest-guide-schema
#
# id: https://w3id.org/biolink/resource-ingest-guide-schema
# description: This is the project description.
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

from linkml_runtime.linkml_model.types import Date, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE, XSDDate

metamodel_version = "1.7.0"
version = None

# Namespaces
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
RESOURCE_INGEST_GUIDE_SCHEMA = CurieNamespace('resource_ingest_guide_schema', 'https://w3id.org/biolink/resource-ingest-guide-schema/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = RESOURCE_INGEST_GUIDE_SCHEMA


# Types

# Class references
class NamedThingId(URIorCURIE):
    pass


class ReferenceIngestGuideId(NamedThingId):
    pass


@dataclass(repr=False)
class NamedThing(YAMLRoot):
    """
    A generic grouping for any identifiable entity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Thing"]
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = RESOURCE_INGEST_GUIDE_SCHEMA.NamedThing

    id: Union[str, NamedThingId] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ReferenceIngestGuide(NamedThing):
    """
    Represents a ReferenceIngestGuide
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RESOURCE_INGEST_GUIDE_SCHEMA["ReferenceIngestGuide"]
    class_class_curie: ClassVar[str] = "resource_ingest_guide_schema:ReferenceIngestGuide"
    class_name: ClassVar[str] = "ReferenceIngestGuide"
    class_model_uri: ClassVar[URIRef] = RESOURCE_INGEST_GUIDE_SCHEMA.ReferenceIngestGuide

    id: Union[str, ReferenceIngestGuideId] = None
    primary_email: Optional[str] = None
    birth_date: Optional[Union[str, XSDDate]] = None
    age_in_years: Optional[int] = None
    vital_status: Optional[Union[str, "PersonStatus"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReferenceIngestGuideId):
            self.id = ReferenceIngestGuideId(self.id)

        if self.primary_email is not None and not isinstance(self.primary_email, str):
            self.primary_email = str(self.primary_email)

        if self.birth_date is not None and not isinstance(self.birth_date, XSDDate):
            self.birth_date = XSDDate(self.birth_date)

        if self.age_in_years is not None and not isinstance(self.age_in_years, int):
            self.age_in_years = int(self.age_in_years)

        if self.vital_status is not None and not isinstance(self.vital_status, PersonStatus):
            self.vital_status = PersonStatus(self.vital_status)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ReferenceIngestGuideCollection(YAMLRoot):
    """
    A holder for ReferenceIngestGuide objects
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RESOURCE_INGEST_GUIDE_SCHEMA["ReferenceIngestGuideCollection"]
    class_class_curie: ClassVar[str] = "resource_ingest_guide_schema:ReferenceIngestGuideCollection"
    class_name: ClassVar[str] = "ReferenceIngestGuideCollection"
    class_model_uri: ClassVar[URIRef] = RESOURCE_INGEST_GUIDE_SCHEMA.ReferenceIngestGuideCollection

    entries: Optional[Union[dict[Union[str, ReferenceIngestGuideId], Union[dict, ReferenceIngestGuide]], list[Union[dict, ReferenceIngestGuide]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_dict(slot_name="entries", slot_type=ReferenceIngestGuide, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


# Enumerations
class PersonStatus(EnumDefinitionImpl):

    ALIVE = PermissibleValue(
        text="ALIVE",
        description="the person is living",
        meaning=PATO["0001421"])
    DEAD = PermissibleValue(
        text="DEAD",
        description="the person is deceased",
        meaning=PATO["0001422"])
    UNKNOWN = PermissibleValue(
        text="UNKNOWN",
        description="the vital status is not known")

    _defn = EnumDefinition(
        name="PersonStatus",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=RESOURCE_INGEST_GUIDE_SCHEMA.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=RESOURCE_INGEST_GUIDE_SCHEMA.name, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=RESOURCE_INGEST_GUIDE_SCHEMA.description, domain=None, range=Optional[str])

slots.primary_email = Slot(uri=SCHEMA.email, name="primary_email", curie=SCHEMA.curie('email'),
                   model_uri=RESOURCE_INGEST_GUIDE_SCHEMA.primary_email, domain=None, range=Optional[str])

slots.birth_date = Slot(uri=SCHEMA.birthDate, name="birth_date", curie=SCHEMA.curie('birthDate'),
                   model_uri=RESOURCE_INGEST_GUIDE_SCHEMA.birth_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.age_in_years = Slot(uri=RESOURCE_INGEST_GUIDE_SCHEMA.age_in_years, name="age_in_years", curie=RESOURCE_INGEST_GUIDE_SCHEMA.curie('age_in_years'),
                   model_uri=RESOURCE_INGEST_GUIDE_SCHEMA.age_in_years, domain=None, range=Optional[int])

slots.vital_status = Slot(uri=RESOURCE_INGEST_GUIDE_SCHEMA.vital_status, name="vital_status", curie=RESOURCE_INGEST_GUIDE_SCHEMA.curie('vital_status'),
                   model_uri=RESOURCE_INGEST_GUIDE_SCHEMA.vital_status, domain=None, range=Optional[Union[str, "PersonStatus"]])

slots.referenceIngestGuideCollection__entries = Slot(uri=RESOURCE_INGEST_GUIDE_SCHEMA.entries, name="referenceIngestGuideCollection__entries", curie=RESOURCE_INGEST_GUIDE_SCHEMA.curie('entries'),
                   model_uri=RESOURCE_INGEST_GUIDE_SCHEMA.referenceIngestGuideCollection__entries, domain=None, range=Optional[Union[dict[Union[str, ReferenceIngestGuideId], Union[dict, ReferenceIngestGuide]], list[Union[dict, ReferenceIngestGuide]]]])

slots.ReferenceIngestGuide_primary_email = Slot(uri=SCHEMA.email, name="ReferenceIngestGuide_primary_email", curie=SCHEMA.curie('email'),
                   model_uri=RESOURCE_INGEST_GUIDE_SCHEMA.ReferenceIngestGuide_primary_email, domain=ReferenceIngestGuide, range=Optional[str],
                   pattern=re.compile(r'^\S+@[\S+\.]+\S+'))
