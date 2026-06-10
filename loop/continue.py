pipeline_stages = ["extract", "transform", "validate", "load"]
failed_stage = "validate"

for stage in pipeline_stages:
    print(f"Running stage: {stage}")
    if stage == failed_stage:
        print(f"FAILURE at stage '{stage}'. Stopping pipeline.")
        break

# CONTINUE: Skip null/missing records
records = [
    {"id": 1, "value": 500},
    None, # Corrupt/missing records
    {"id": 3, "value": 750},
    None,
    {"id": 5, "value": 300}
]

