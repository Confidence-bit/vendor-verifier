from validator.loader import load_json


def main():
    claims = load_json("input/vendor-claims.json")
    assurance = load_json("input/assurance-and-contract.json")
    telemetry = load_json("input/vendor-telemetry.json")

    print("Vendor claims loaded successfully!")
    print("Assurance and contract loaded successfully!")
    print("Vendor telemetry loaded successfully!")

    print()
    print(f"Vendor: {claims['vendor']}")
    print(f"Claims: {len(claims['claims'])}")
    print(f"Telemetry schema version: {telemetry['schema_version']}")


if __name__ == "__main__":
    main()
