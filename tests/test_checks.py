from validator.checks import (
    check_tls_version,
    check_privileged_mfa,
)


def test_tls_check():
    telemetry = {
        "tls": {
            "minimum_version_claimed": "1.2",
            "observations": [
                {
                    "endpoint": "example.com",
                    "protocol": "TLSv1.0"
                }
            ]
        }
    }

    failures = check_tls_version(telemetry)

    assert len(failures) == 1
    assert failures[0]["code"] == "TLS_BELOW_MINIMUM"


def test_mfa_check():
    telemetry = {
        "privileged_access": [
            {
                "event_id": "A1",
                "actor": "admin",
                "region": "us-east-1",
                "mfa": False
            }
        ]
    }

    failures = check_privileged_mfa(telemetry)

    assert len(failures) == 1
    assert failures[0]["code"] == "PRIVILEGED_MFA_MISSING"
