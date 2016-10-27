#!/usr/bin/env python

"""
Implementation of the gdc api. Relies on gdc-backend, a mock data faker.
https://gdc-docs.nci.nih.gov/API/Users_Guide/Getting_Started/#api-endpoints
Leverages the gdc data dictionary
https://github.com/NCI-GDC/gdcdictionary
"""

import os

from flask import Flask, request, jsonify, Response, json
from gdcdictionary import gdcdictionary
import requests
# import python_jsonschema_objects as pjs
# builder = pjs.ObjectBuilder(gdcdictionary.schema)
# ns = builder.build_classes()

app = Flask(__name__)


# @app.errorhandler(ValidationError)
# def on_validation_error(e):
#     return "error"


@app.route('/v0/status')
def status():
    """Status Get the API status and version information"""
    return jsonify({
      "commit": "snapshot",
      "status": "OK",
      "tag": "1.4.0",
      "version": 1
    })


@app.route('/v0/projects')
def projects():
    """Search & Retrieval Search all data generated by a project"""
    return _makeFakeResponse('project')


@app.route('/v0/cases')
def cases():
    """Search & Retrieval Find all files related to a specific case,
     or sample donor."""
    return _makeFakeResponse('case')


@app.route('/v0/files')
def files():
    """Search & Retrieval Find all files with specific characteristics such
    as file_name, md5sum, data_format and others."""
    return _makeFakeResponse('file')


@app.route('/v0/annotations')
def annotations():
    """Search & Retrieval Search annotations added to data after curation"""
    return _makeFakeResponse('annotation')


@app.route('/v0/data')
def data():
    """Download Used to download GDC data"""
    pass


@app.route('/v0/manifest')
def manifest():
    """Download Generates manifests for use with GDC Data Transfer Tool"""
    pass


@app.route('/v0/slicing')
def slicing():
    """BAM Slicing Allows remote slicing of BAM format objects"""
    pass


@app.route('/v0/submission')
def submission():
    """Submission Returns the available resources at the top level above
    programs i.e., registered programs"""
    pass


def _makeFakeResponse(schema_key):
    """ create a response object with random data based on jsonschema
    currently the schema_key values are:
    ['submitted_unaligned_reads',
     'somatic_mutation_calling_workflow',
     'pathology_report',
     'run_metadata',
     'read_group',
     'family_history',
     'publication',
     'aligned_reads_metric',
     'demographic',
     'platform',
     'data_subtype',
     'treatment',
     'biospecimen_supplement',
     'clinical',
     'alignment_cocleaning_workflow',
     'submitted_tangent_copy_number',
     'aliquot',
     'methylation_beta_value',
     'analysis_metadata',
     'masked_somatic_mutation',
     'annotated_somatic_mutation',
     'case',
     'submitted_aligned_reads',
     'simple_somatic_mutation',
     'filtered_copy_number_segment',
     'rna_expression_workflow',
     'aggregated_somatic_mutation',
     'project',
     'slide',
     'tissue_source_site',
     'germline_mutation_calling_workflow',
     'experiment_metadata',
     'program',
     'sample_level_maf',
     'sample',
     'tag',
     'analyte',
     'file',
     'simple_germline_variation',
     'somatic_aggregation_workflow',
     'slide_image',
     'archive',
     'read_group_qc',
     'mirna_expression',
     'submitted_methylation_beta_value',
     'somatic_annotation_workflow',
     'experimental_strategy',
     'data_type',
     'copy_number_segment',
     'aligned_reads',
     'copy_number_liftover_workflow',
     'aligned_reads_index',
     'methylation_liftover_workflow',
     'annotation',
     'exon_expression',
     'exposure',
     'gene_expression',
     'center',
     'alignment_workflow',
     'clinical_supplement',
     'data_format',
     'portion',
     'diagnosis',
     'mirna_expression_workflow']
    """
    headers = {'content-type': 'application/json'}
    r = requests.post(os.environ['CGD_BACKEND_URL'],
                      data=json.dumps(gdcdictionary.schema[schema_key]),
                      headers=headers)
    return Response(r.text, mimetype='application/json')
