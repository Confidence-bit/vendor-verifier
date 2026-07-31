from validator.loader import load_json
from validator.validators import validate_vendor_claims
from validator.checks import (
    check_tls_version,
    check_privileged_mfa,
    check_duplicate_events,
    check_hash_chain,
)
from validator.contradictions import build_contradiction_matrix
from validator.reporter import (
    write_verdicts,
    write_contradiction_matrix,
)


def main():
    # ---------------------------------
    # Load evidence files
    # ---------------------------------

    claims = load_json("input/vendor-claims.json")
    assurance = load_json("input/assurance-and-contract.json")
    telemetry = load_json("input/vendor-telemetry.json")

    # ---------------------------------
    # Validate vendor claims schema
    # ---------------------------------

    missing = validate_vendor_claims(claims)

    if missing:
        print("❌ Vendor claims schema is invalid.")

        for field in missing:
            print(f"Missing field: {field}")

        return

    print("✅ Vendor claims schema is valid.")

    print("Vendor claims loaded successfully!")
    print("Assurance and contract loaded successfully!")
    print("Vendor telemetry loaded successfully!")

    print()
    print(f"Vendor: {claims['vendor']}")
    print(f"Claims: {len(claims['claims'])}")
    print(f"Telemetry schema version: {telemetry['schema_version']}")

    # ---------------------------------
    # TLS Validation
    # ---------------------------------

    tls_failures = check_tls_version(telemetry)

    print("\nTLS Validation")
    print("----------------")

    if tls_failures:

        for failure in tls_failures:

            print(
                f"FAIL: {failure['endpoint']} "
                f"uses {failure['observed']} "
                f"(minimum {failure['required']})"
            )

    else:
        print("PASS")

    # ---------------------------------
    # Privileged MFA Validation
    # ---------------------------------

    mfa_failures = check_privileged_mfa(telemetry)

    print("\nPrivileged MFA Validation")
    print("-------------------------")

    if mfa_failures:

        for failure in mfa_failures:

            print(
                f"FAIL: {failure['actor']} "
                f"({failure['event_id']}) "
                f"did not use MFA"
            )

    else:
        print("PASS")

    # ---------------------------------
    # Duplicate Event Validation
    # ---------------------------------

    duplicate_failures = check_duplicate_events(telemetry)

    print("\nDuplicate Event Validation")
    print("--------------------------")

    if duplicate_failures:

        for failure in duplicate_failures:

            print(
                f"FAIL: Duplicate event ID "
                f"{failure['event_id']} "
                f"({failure['actor']})"
            )

    else:
        print("PASS")

    # ---------------------------------
    # Hash Chain Validation
    # ---------------------------------

    hash_failures = check_hash_chain(telemetry)

    print("\nHash Chain Validation")
    print("---------------------")

    if hash_failures:

        for failure in hash_failures:

            print(
                f"FAIL: Broken hash chain at "
                f"{failure['event_id']} "
                f"({failure['actor']})"
            )

    else:
        print("PASS")

    # ---------------------------------
    # Collect validation verdicts
    # ---------------------------------

    verdicts = []

    for failure in tls_failures:
        verdicts.append({
            "check": "TLS",
            "status": "FAIL",
            "code": failure["code"],
            "details": failure,
        })

    for failure in mfa_failures:
        verdicts.append({
            "check": "MFA",
            "status": "FAIL",
            "code": failure["code"],
            "details": failure,
        })

    for failure in duplicate_failures:
        verdicts.append({
            "check": "Duplicate Event",
            "status": "FAIL",
            "code": failure["code"],
            "details": failure,
        })

    for failure in hash_failures:
        verdicts.append({
            "check": "Hash Chain",
            "status": "FAIL",
            "code": failure["code"],
            "details": failure,
        })

    # ---------------------------------
    # Write evidence verdicts
    # ---------------------------------

    write_verdicts(verdicts)

    # ---------------------------------
    # Build contradiction matrix
    # ---------------------------------

    contradiction_rows = build_contradiction_matrix(
        claims,
        telemetry,
        assurance,
    )

    write_contradiction_matrix(contradiction_rows)


if __name__ == "__main__":
    main()
