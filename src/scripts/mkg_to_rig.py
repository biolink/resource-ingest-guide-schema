"""
This script loads details from a Biolink Model-compliant
Meta Knowledge Graph (TRAPI) json file, into a specified RIG YAML file.
"""
from pathlib import Path
import yaml
import json
import click

# TODO: weak link here: what exact value should
#       this actually be, from Translator Ingests?
TRANSLATOR_INGESTS = Path("src/translator_ingest/ingests")

@click.command()
@click.option(
    '--ingest',
    required=True,
    help='Target ingest folder name of the target data source folder (e.g., icees)'
)
@click.option(
    '--mkg',
    default='meta_knowledge_graph.json',
    help='Meta Knowledge Graph JSON file source of details to be loaded into the RIG ' +
         '(default: "meta_knowledge_graph.json",  assumed co-located with RIG in the ingest folder)'
)
@click.option(
    '--rig',
    default=None,
    help='Target RIG file (default: <ingest folder name>_rig.yaml)'
)
@click.option(
    '--knowledge_level',
    default='not_provided',
    help='Biolink Edge Knowledge Level (default: "not_provided")'
)
@click.option(
    '--agent_type',
    default='not_provided',
    help='Biolink Edge Agent Type (default: "not_provided")'
)
def main(ingest, mkg, rig, knowledge_level, agent_type):
    """
    Merge Meta Knowledge Graph node and edge information into RIG 'target_info'.

    :param ingest: Target ingest folder name of the target data source folder (e.g., icees)
    :param mkg: Meta Knowledge Graph JSON file source of details to be
                loaded into the RIG (assumed co-located with RIG in the ingest folder
    :param rig: Target RIG file (default: <ingest folder name>_rig.yaml)
    :param knowledge_level: Biolink edge knowledge level
    :param agent_type: Biolink edge agent type
    :return:

    Examples:

    \b
    mk_to_rig.py --ingest icees
    mk_to_rig.py --ingest icees --mkg my_meta_graph.json --rig my_rig.yaml
    """
    ingest_path = TRANSLATOR_INGESTS / ingest

    mkg_path = ingest_path / mkg

    # Validate infores format
    if rig is None:
        rig = f"{ingest}_rig.yaml"

    rig_path = ingest_path / rig

    # Check if mkg json file exists
    if not path.exists(mkg):
        click.echo(f"Error: Meta Knowledge Graph json file not found: {mkg}", err=True)
        sys.exit(1)

    # Check if mkg json file exists
    if not path.exists(rig):
        click.echo(f"Error: RIG yaml file not found: {rig}", err=True)
        sys.exit(1)

    try:
        rig_data: dict
        with open(rig, 'r') as r:
            rig_data = yaml.safe_load(r)
            # target_info:
            #   ...

            target_info = rig_data.setdefault('target_info', {}) # conservative, in case other info is present

            # TODO: what happens here if either 'node_type_info' and/or
            #      'edge_type_info' are already set? Should we rather
            #      consider overwriting their values?
            #
            #   node_type_info:
            node_type_info = target_info.setdefault('node_type_info', [])
            #   edge_type_info:
            edge_type_info = target_info.setdefault('edge_type_info', [])

            with open(mkg, 'r') as m:
                mkg_data = json.load(m)
                for category, details in mkg_data['nodes'].items():
                    # 'target_info.node_type_info' is a list of rig_node entries
                    rig_node = dict()

                    #   - node_category: "biolink:Disease"
                    rig_node['node_category'] = category

                    #     source_identifier_types:
                    #       - "OMIM" etc.
                    id_prefixes: list[str] = details['id_prefixes']
                    rig_node['source_identifier_types'] = id_prefixes.copy()

                    #     node_properties:
                    #     - "biolink:inheritance"
                    rig_node['node_properties'] = []
                    attributes = details['attributes']
                    for attribute in attributes:
                        attribute_type_id = attribute['attribute_type_id']
                        rig_node['node_properties'].append(attribute_type_id)

                        # TODO: unsure if or how to really record this at the moment,
                        #       let alone, other associated properties?
                        # original_attribute_names = attribute['original_attribute_names']

                for edge in mkg_data['edges']:
                    subject = edge['subject']
                    predicate = edge['predicate']
                    object = edge['object']
                    rig_edge = dict()
                    #       subject_categories:
                    #       - "biolink:Disease"

                    rig_edge['subject'] = [edge['subject']]
                    #       predicates:
                    #         - "biolink:has_phenotype"

                    rig_edge['predicates'] = [edge['predicates']]
                    #       object_categories:
                    #       - "biolink:PhenotypicFeature"

                    rig_edge['subject'] = [edge['subject']]
                    # TODO: rig_edge['qualifiers']

                    #       knowledge_level:
                    #       - knowledge_assertion
                    rig_edge['knowledge_level'] = knowledge_level

                    #       agent_type:
                    #       - manual_agent
                    rig_edge['agent_type'] = agent_type

                    rig_edge['edge_properties'] = []
                    attributes = details['attributes']
                    for attribute in attributes:
                        attribute_type_id = attribute['attribute_type_id']
                        rig_edge['edge_properties'].append(attribute_type_id)

                        # TODO: unsure if or how to really record this at the moment,
                        #       let alone, other associated properties?
                        # original_attribute_names = attribute['original_attribute_names']

        with open(rig, 'w') as r:
            yaml.safe_dump(rig_data, r)

    except Exception as e:
        click.echo(f"Error integrating Meta Knowledge Graph JSON data into RIG: {e}", err=True)
        sys.exit(1)


if __name__ == '__main__':
    main()
