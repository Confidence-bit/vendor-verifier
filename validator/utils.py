def compare_tls_versions(observed, minimum):
    """
    Return True if the observed TLS version
    is greater than or equal to the minimum version.
    """

    versions = {
        "TLSv1.0": 1.0,
        "TLSv1.1": 1.1,
        "TLSv1.2": 1.2,
        "TLSv1.3": 1.3,
    }

    observed_value = versions.get(observed, 0)
    minimum_value = float(minimum)

    return observed_value >= minimum_value


def find_duplicate_event_ids(events):
    """
    Return duplicate privileged access events.
    """

    seen = set()
    duplicates = []

    for event in events:

        if event["event_id"] in seen:
            duplicates.append(event)
        else:
            seen.add(event["event_id"])

    return duplicates


def find_broken_hash_chain(events):
    """
    Return events whose previous_hash does not match
    the previous event's hash.

    Duplicate event IDs are ignored because they are
    handled separately by the duplicate event validator.
    """

    failures = []

    previous_hash = "ROOT"
    seen_event_ids = set()

    for event in events:

        # Ignore duplicate event IDs
        if event["event_id"] in seen_event_ids:
            continue

        seen_event_ids.add(event["event_id"])

        if event["previous_hash"] != previous_hash:
            failures.append(event)

        previous_hash = event["hash"]

    return failures
