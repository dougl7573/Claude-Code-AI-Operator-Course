import csv

def read_vendor_list(csv_file_path):
    """Read vendor CSV and return list of active vendors (active=TRUE)."""
    active_vendors = []

    with open(csv_file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            # Active = TRUE; treat as "approved"
            if row["active"].upper() == "TRUE":
                vendor_info = {
                    "id": row["vendor_id"],
                    "name": row["vendor_name"],
                    "email": row["contact_email"],
                    "terms": row["payment_terms"],
                    "category": row["category"],
                }
                active_vendors.append(vendor_info)

    return active_vendors


import csv

def read_vendor_list(csv_file_path):
    """Read vendor CSV and return list of active vendors (active=TRUE)."""
    active_vendors = []

    with open(csv_file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            # Active = TRUE; treat as "approved"
            if row["active"].upper() == "TRUE":
                vendor_info = {
                    "id": row["vendor_id"],
                    "name": row["vendor_name"],
                    "email": row["contact_email"],
                    "terms": row["payment_terms"],
                    "category": row["category"],
                    "active": row["active"],
                }
                active_vendors.append(vendor_info)

    return active_vendors


def search_vendor(search_name, csv_file_path):
    """
    Search for a vendor by name among active vendors.
    - First try exact match (case-insensitive).
    - If no exact match, return active vendors whose name starts with
      the first letter of the search term.
    Returns: ('exact', vendor_dict) or ('starts_with', [vendor_dict, ...]) or (None, [])
    """
    search_name = search_name.strip()
    if not search_name:
        return None, []

    with open(csv_file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        active_rows = [
            row
            for row in reader
            if row["active"].upper() == "TRUE"
        ]

    # Exact match (case-insensitive)
    for row in active_rows:
        if row["vendor_name"].lower() == search_name.lower():
            return "exact", {
                "id": row["vendor_id"],
                "name": row["vendor_name"],
                "email": row["contact_email"],
                "terms": row["payment_terms"],
                "category": row["category"],
                "active": row["active"],
            }

    # Fallback: names starting with first letter of search
    first_letter = search_name[0].upper()
    starts_with = [
        {
            "id": row["vendor_id"],
            "name": row["vendor_name"],
            "email": row["contact_email"],
            "terms": row["payment_terms"],
            "category": row["category"],
            "active": row["active"],
        }
        for row in active_rows
        if row["vendor_name"].upper().startswith(first_letter)
    ]

    if starts_with:
        return "starts_with", starts_with
    return None, []


def main():
    # Demo search
    search_term = "Acme Corp"
    match_type, result = search_vendor(search_term, "vendor-list.csv")

    if match_type == "exact":
        print(f"Found vendor matching '{search_term}':\n")
        print(f"Name: {result['name']}")
        print(f"ID: {result['id']}")
        print(f"Email: {result['email']}")
        print(f"Payment Terms: {result['terms']}")
        print(f"Active: {result['active']}")
    elif match_type == "starts_with":
        print(f"No exact match for '{search_term}'. Active vendors whose name starts with '{search_term[0]}':\n")
        for v in result:
            print(f"  {v['id']}: {v['name']} ({v['category']})")
    else:
        print(f"No vendor found matching '{search_term}' (and no active vendors start with that letter).")

    # Optional: also list all active vendors
    print("\n" + "=" * 40)
    print("All active vendors:")
    vendors = read_vendor_list("vendor-list.csv")
    for v in vendors:
        print(f"  {v['id']}: {v['name']}")


if __name__ == "__main__":
    main()
