from validator.utils import compare_tls_versions


def check_tls_version(telemetry):
    """
    Check that all observed TLS versions meet the claimed minimum.

    Returns:
        list: A list of TLS validation failures.
    """

    failures = []

    # Get the minimum TLS version claimed by the vendor
    minimum = telemetry["tls"]["minimum_version_claimed"]

    # Check every observed endpoint
    for observation in telemetry["tls"]["observations"]:

        protocol = observation["protocol"]

        # Compare the observed version with the required minimum
        if not compare_tls_versions(protocol, minimum):

            failures.append({
                "endpoint": observation["endpoint"],
                "observed": protocol,
                "required": minimum,
                "code": "TLS_BELOW_MINIMUM"
            })

    return failures
