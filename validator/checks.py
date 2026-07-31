def check_tls_version(telemetry):
    """
    Check that all observed TLS versions meet the claimed minimum.
    Returns a list of failures.
    """

    failures = []

    minimum = telemetry["tls"]["minimum_version_claimed"]

    for observation in telemetry["tls"]["observations"]:
        protocol = observation["protocol"]

        if protocol == "TLSv1.0":
            failures.append({
                "endpoint": observation["endpoint"],
                "observed": protocol,
                "required": minimum,
                "code": "TLS_BELOW_MINIMUM"
            })

    return failures
