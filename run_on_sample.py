"""
Runs the MetaSRA pipeline on a single sample
"""

import json
import sys

sys.path.extend(['bktree', 'map_sra_to_ontology'])

from all_pipelines import pipeline_v53

if __name__ == "__main__":
    from optparse import OptionParser

    (options, args) = OptionParser().parse_args()

    in_json = args[0]
    out_json = args[1]

    # Load input
    with open(in_json, 'r') as instream:
        in_dict = json.load(instream)

    # Encode as ascii characters
    in_dict = {
        key.encode('ascii', 'replace'): val.encode('ascii', 'replace') for key, val in in_dict.iteritems()
    }
    
    # Build pipeline
    pipeline = pipeline_v53.build_pipeline()

    # Run pipeline
    mapped_terms, real_props = pipeline.run(in_dict)

    # Write output
    with open(out_json, 'w') as outstream:
        json.dump([term.term_id for term in mapped_terms if not term.consequent], outstream)