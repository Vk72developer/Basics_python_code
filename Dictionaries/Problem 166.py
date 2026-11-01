# Nested Dictionary Access 

company = {
    "emp1": {"name": "Riya", "salary": 50000},
    "emp2": {"name": "Karan", "salary": 60000},
}

print(company["emp1"]["name"])
print(company["emp2"]["salary"])

print(company.get("emp3", {}).get("name", "Unknown"))
