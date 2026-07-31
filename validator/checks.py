from validator.utils import (
    compare_tls_versions,
    find_duplicate_event_ids,
    find_broken_hash_chain,
)


def check_tls_version(telemetry):
    """
    Check that all observed TLS versions meet the claimed minimum.
    """

    failures = []

    minimum = telemetry["tls"]["minimum_version_claimed"]

    for observation in telemetry["tls"]["observations"]:

        protocol = observation["protocol"]

        if not compare_tls_versions(protocol, minimum):

            failures.append({
                "endpoint": observation["endpoint"],
                "observed": protocol,
                "required": minimum,
                "code": "TLS_BELOW_MINIMUM"
            })

    return failures


def check_privileged_mfa(telemetry):
    """
    Check that every privileged access event uses MFA.
    """

    failures = []

    for event in telemetry["privileged_access"]:

        if not event["mfa"]:

            failures.append({
                "event_id": event["event_id"],
                "actor": event["actor"],
                "region": event["region"],
                "code": "PRIVILEGED_MFA_MISSING"
            })

    return failures


def check_duplicate_events(telemetry):
    """
    Detect duplicate privileged access event IDs.
    """

    failures = []

    duplicates = find_duplicate_event_ids(
        telemetry["privileged_access"]
    )

    for event in duplicates:

        failures.append({
            "event_id": event["event_id"],
            "actor": event["actor"],
            "code": "DUPLICATE_EVENT_ID"
        })

    return failures


def check_hash_chain(telemetry):
    """
    Detect broken privileged access hash chains.
    """

    failures = []

    broken = find_broken_hash_chain(
        telemetry["privileged_access"]
    )

    for event in broken:

        failures.append({
            "event_id": event["event_id"],
            "actor": event["actor"],
            "code": "HASH_CHAIN_BROKEN"
        })

    return failures
