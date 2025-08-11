#!/usr/bin/env python3
"""
Script to create a new Reference Ingest Guide (RIG) from the template.
"""

import os
import sys
from pathlib import Path
import yaml
from datetime import datetime
import click


def load_template(template_path):
    """Load the RIG template from YAML file."""
    with open(template_path, 'r') as f:
        return yaml.safe_load(f)


def create_rig(infores_id, rig_name, output_file, template_path):
    """Create a new RIG from template with user-specified values."""
    
    # Load template
    template = load_template(template_path)
    
    # Update template with user values
    template['ReferenceIngestGuide']['name'] = rig_name
    template['ReferenceIngestGuide']['source_info']['infores_id'] = infores_id
    
    # Set target infores_id based on source (optional but commonly done)
    if 'target_info' not in template['ReferenceIngestGuide']:
        template['ReferenceIngestGuide']['target_info'] = {}
    template['ReferenceIngestGuide']['target_info']['infores_id'] = infores_id
    
    # Add creation timestamp in additional_notes if not present
    if 'additional_notes' not in template['ReferenceIngestGuide']['source_info']:
        template['ReferenceIngestGuide']['source_info']['additional_notes'] = f"RIG created on {datetime.now().strftime('%Y-%m-%d')}"
    
    # Write the new RIG file
    with open(output_file, 'w') as f:
        yaml.dump(template, f, default_flow_style=False, sort_keys=False, indent=2)
    
    click.echo(f"Created new RIG: {output_file}")
    click.echo(f"  Name: {rig_name}")
    click.echo(f"  InfoRes ID: {infores_id}")
    click.echo(f"\nNext steps:")
    click.echo(f"1. Edit {output_file} to fill in the template sections")
    click.echo(f"2. See src/docs/files/example-rigs.md for detailed guidance")


@click.command()
@click.option(
    '--infores', 
    required=True,
    help='InfoRes identifier for the data source (e.g., infores:ctd)'
)
@click.option(
    '--name',
    required=True, 
    help='Human-readable name for the RIG (e.g., "CTD Chemical-Disease Associations")'
)
@click.option(
    '--output',
    help='Output filename for the new RIG (default: based on infores ID)'
)
@click.option(
    '--template',
    default='src/docs/files/rig_template.yaml',
    help='Path to the RIG template file (default: src/docs/files/rig_template.yaml)'
)
def main(infores, name, output, template):
    """Create a new Reference Ingest Guide from template.
    
    Examples:
    
    \b
    create_rig.py --infores infores:ctd --name "CTD Chemical-Disease Associations"
    create_rig.py --infores infores:pharmgkb --name "PharmGKB Drug-Gene Interactions" --output pharmgkb_rig.yaml
    """
    
    # Validate infores format
    if not infores.startswith('infores:'):
        click.echo("Error: InfoRes ID must start with 'infores:'", err=True)
        sys.exit(1)
    
    # Generate output filename if not provided
    if not output:
        # Extract source name from infores ID and create filename
        source_name = infores.replace('infores:', '').replace(':', '_')
        output = f"src/docs/rigs/{source_name}_rig.yaml"
    
    # Ensure the rigs directory exists
    os.makedirs(os.path.dirname(output), exist_ok=True)
    
    # Check if template exists
    if not os.path.exists(template):
        click.echo(f"Error: Template file not found: {template}", err=True)
        sys.exit(1)
    
    # Check if output file already exists
    if os.path.exists(output):
        if not click.confirm(f"File {output} already exists. Overwrite?"):
            click.echo("Aborted.")
            sys.exit(0)
    
    try:
        create_rig(infores, name, output, template)
    except Exception as e:
        click.echo(f"Error creating RIG: {e}", err=True)
        sys.exit(1)


if __name__ == '__main__':
    main()