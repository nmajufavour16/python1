# pipeline_stages = ["extract", "transform", "validate", "load"]
# failed_stage = "validate"

# for stage in pipeline_stages:
#     print(f"Running stage: {stage}")
#     if stage == failed_stage:
#         print(f"FAILURE at stage '{stage}'. Stopping pipeline.")
#         break

# # CONTINUE: Skip null/missing records
# records = [
#     {"id": 1, "value": 500},
#     None, # Corrupt/missing records
#     {"id": 3, "value": 750},
#     None,
#     {"id": 5, "value": 300}
# ]
    
# total = 0
# for record in records:
#     if records is None:
#         print("Skipping null records...")
#         continue    #Skip this iteration; go to the next record
#     total += record["value"] 

# print(f"Total value of valid records: {total}")     #1550

# CLASSWORK
"""
Build a mini data pipeline simulator;
    Create a list of 8 records, make 2 of them None (simuulating corrupt data)
    use a for loop with continue to skip None records and print a skip message.
    For  each valid record (a dictionary), print its values.
"""

pipeline_stages = ["extract", "transform", "validate", "load", "display"]
failed_stage = "display"

for stage in pipeline_stages:
    print(f"Running stage: {stage}")
    if stage == failed_stage:
        print(f"FAILURE at stage '{stage}'. Stopping pipeline.")
        break
    
Assessment = [
    {"name": "Denzel", "score": 54},
    {"name": "Liquid", "score": 77},
    {"name": "Angelica", "score": 29},
    {"name": "Esther", "score": 99},
    None,
    {"name": "Uche", "score": 93},
    None,
    {"name": "Wike", "score": 47}
]

# this <for> block of code checks for individual items in the list and ensure the satisfy the condition
for student in Assessment:
    if student is None:
        print("Skipping null records...")
        continue
    
    # This checks for the key and value pairs in the dictionary within the list and prints it out
    # for name, score in student.items():
    #     print(score)
        
    # This prints the value only
    print(Assessment[student])

# total = 0
# for student in Assessment:
#     if student is None:
#         print("Skipping null records...")
#         continue
#     total += student["score"]

# print(f"The scores are: {total}")