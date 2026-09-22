student_data = {
    "id1": {"Name": "Sarah", "Class": "V", "subject_integration": "English, Math , science"},
    "id2": {"Name": "John", "Class": "V", "subject_integration": "English, Math , science"},
    "id3": {"Name": "Sarah", "Class": "V", "subject_integration": "English, Math , science"},
    "id4": {"Name": "ben", "Class": "V", "subject_integration": "English, Math , science"}
}

result = {}
seen_keys = []

for student_id, details in student_data.items():
    name = details["Name"]
    Unique_key = (name, details["Class"], details["subject_integration"])
    if Unique_key not in seen_keys:
        seen_keys[Unique_key] = student_id
        result[student_id] = details

for k, v in result.items():
    print(k, ":", v)