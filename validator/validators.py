def validate_vendor_claims(data):
    """
    Validate the structure of vendor-claims.json.

    Returns:
        list[str]: Missing required top-level fields.
    """

    required_fields = [
        "schema_version",
        "vendor",
        "signed_at",
        "claims",
    ]

    missing = []

    for field in required_fields:
        if field not in data:
            missing.append(field)

    return missing
