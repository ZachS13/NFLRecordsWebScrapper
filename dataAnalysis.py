import json
from collections import defaultdict

# Load arrest data
with open('arrest_records.json') as f:
    data = json.load(f)

# Violent terms to look for
violent_terms = [
    "assault", "battery", "violence", "resisting arrest", "aggravated",
    "murder", "gun", "rape", "child abuse", "animal cruelty", "robbery",
    "burglary", "menacing", "stalking", "abuse", "weapon", "attempted murder",
    "bomb threat", "kidnapping", "strangle", "choking", "injury", "homicide", "dogfighting"
]

# Normalize terms for matching
violent_terms = [term.lower() for term in violent_terms]

# Dictionary to store matched records by term
violent_term_index = defaultdict(list)
total_violent_records = 0

for record in data:
    category = record.get("category", "").lower()

    for term in violent_terms:
        if term in category:
            violent_term_index[term].append(record)
            total_violent_records += 1
            break  # Only assign each record once

# Print results
for term in sorted(violent_term_index.keys()):
    print(f"{term}: {len(violent_term_index[term])} records")

print()
print(f"Total records: {len(data)}")
print(f"Total violent records: {total_violent_records}")
print(f"Percentage violent: {total_violent_records / len(data) * 100:.2f}%")
