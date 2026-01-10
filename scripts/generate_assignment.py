#!/usr/bin/env python3
"""
Generate personalized ASSIGNMENT.md from template.
CSC3301 Programming Language Paradigms - Lab 3
"""
import json
from pathlib import Path


def main():
    repo_root = Path(__file__).parent.parent

    # Load variant config
    config_path = repo_root / ".variant_config.json"
    if not config_path.exists():
        print("No variant config found. Run variant_generator.py first.")
        return

    with open(config_path) as f:
        variant = json.load(f)

    # Load template
    template_path = repo_root / "ASSIGNMENT_TEMPLATE.md"
    if not template_path.exists():
        print("No assignment template found.")
        return

    template = template_path.read_text()

    # Extract test data
    map_test = variant["map_test"]
    filter_test = variant["filter_test"]
    reduce_test = variant["reduce_test"]
    zip_with_test = variant["zip_with_test"]
    chain = variant["transformation_chain"]

    # Replace placeholders
    assignment = template

    # Student info
    assignment = assignment.replace("{{STUDENT_ID}}", variant["student_id"])

    # Map test placeholders
    assignment = assignment.replace("{{MAP_INPUT_DATA}}", str(map_test["input_data"]))
    assignment = assignment.replace("{{MAP_TRANSFORM_DESC}}", map_test["transform_desc"])
    assignment = assignment.replace("{{MAP_EXPECTED}}", str(map_test["expected"]))

    # Filter test placeholders
    assignment = assignment.replace("{{FILTER_INPUT_DATA}}", str(filter_test["input_data"]))
    assignment = assignment.replace("{{FILTER_PREDICATE_DESC}}", filter_test["predicate_desc"])
    assignment = assignment.replace("{{FILTER_EXPECTED}}", str(filter_test["expected"]))

    # Reduce test placeholders
    assignment = assignment.replace("{{REDUCE_INPUT_DATA}}", str(reduce_test["input_data"]))
    assignment = assignment.replace("{{REDUCE_DESC}}", reduce_test["reduce_desc"])
    assignment = assignment.replace("{{REDUCE_INITIAL}}", str(reduce_test["initial_value"]))
    assignment = assignment.replace("{{REDUCE_EXPECTED}}", str(reduce_test["expected"]))

    # Zip-with test placeholders
    assignment = assignment.replace("{{ZIP_LIST1}}", str(zip_with_test["list1"]))
    assignment = assignment.replace("{{ZIP_LIST2}}", str(zip_with_test["list2"]))
    assignment = assignment.replace("{{ZIP_COMBINE_DESC}}", zip_with_test["combine_desc"])
    assignment = assignment.replace("{{ZIP_EXPECTED}}", str(zip_with_test["expected"]))

    # Chain placeholders
    assignment = assignment.replace("{{CHAIN_INITIAL_DATA}}", str(chain["initial_data"]))
    if len(chain["chain"]) >= 3:
        assignment = assignment.replace("{{CHAIN_FILTER_DESC}}", chain["chain"][0]["description"])
        assignment = assignment.replace("{{CHAIN_MAP_DESC}}", chain["chain"][1]["description"])
        assignment = assignment.replace("{{CHAIN_REDUCE_DESC}}", chain["chain"][2]["description"])
    assignment = assignment.replace("{{CHAIN_FINAL_RESULT}}", str(chain["final_result"]))

    # Write personalized assignment
    output_path = repo_root / "ASSIGNMENT.md"
    output_path.write_text(assignment)
    print(f"Generated personalized assignment: {output_path}")


if __name__ == "__main__":
    main()
