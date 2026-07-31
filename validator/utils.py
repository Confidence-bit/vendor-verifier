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
    Return a list of duplicate event IDs.
    """

    seen = set()
    duplicates = []

    for event in events:

        event_id = event["event_id"]

        if event_id in seen:
            duplicates.append(event)

        else:
            seen.add(event_id)

    return duplicates
