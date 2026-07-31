from validator.loader import load_json
from validator.validators import validate_vendor_claims


def main():
    # Load the three evidence files
    claims = load_json("input/vendor-claims.json")
    assurance = load_json("input/assurance-and-contract.json")
    telemetry = load_json("input/vendor-telemetry.json")

    # Validate the vendor claims schema
    missing = validate_vendor_claims(claims)

    if missing:
        print("❌ Vendor claims schema is invalid.")
        for field in missing:
            print(f"Missing field: {field}")
        return
    else:
        print("✅ Vendor claims schema is valid.")

    # Display information about the loaded files
    print("Vendor claims loaded successfully!")
    print("Assurance and contract loaded successfully!")
    print("Vendor telemetry loaded successfully!")

    print()
    print(f"Vendor: {claims['vendor']}")
    print(f"Claims: {len(claims['claims'])}")
    print(f"Telemetry schema version: {telemetry['schema_version']}")


if __name__ == "__main__":
    main()
