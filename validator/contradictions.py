def build_contradiction_matrix(claims, telemetry, assurance):
    """
    Compare vendor claims against the available technical evidence.

    Returns a list of dictionaries that will later be written
    to contradiction-matrix.csv.
    """

    rows = []

    # ---------------------------------------
    # Gather evidence we'll use
    # ---------------------------------------

    tls_fail = any(
        obs["protocol"] == "TLSv1.0"
        for obs in telemetry["tls"]["observations"]
    )

    non_us_region = any(
        event["region"] != "us-east-1"
        for event in telemetry["privileged_access"]
    )

    backup_missing = any(
        job["backup_purge_at"] is None
        for job in telemetry["deletion_jobs"]
    )

    soc_alert_exception = any(
        ex["id"] == "EX-CC7.2"
        for ex in assurance["assurance_report"]["exceptions"]
    )

    # ---------------------------------------
    # Evaluate each vendor claim
    # ---------------------------------------

    for claim in claims["claims"]:

        verdict = "SUPPORTED"
        evidence = "Available"
        reason = "Evidence supports the claim."

        # ENC-03
        if claim["claim_id"] == "ENC-03":

            if tls_fail:
                verdict = "CONTRADICTED"
                evidence = "TLSv1.0 observed"
                reason = "Transport encryption below claimed minimum."

        # LOC-02
        elif claim["claim_id"] == "LOC-02":

            if non_us_region:
                verdict = "CONTRADICTED"
                evidence = "Privileged access observed outside us-east-1"
                reason = "Activity occurred in another region."

        # DEL-05
        elif claim["claim_id"] == "DEL-05":

            if backup_missing:
                verdict = "CONTRADICTED"
                evidence = "Backup purge missing"
                reason = "Deletion evidence is incomplete."

        # LOG-07
        elif claim["claim_id"] == "LOG-07":

            if soc_alert_exception:
                verdict = "CONTRADICTED"
                evidence = "SOC 2 exception EX-CC7.2"
                reason = "Alert review evidence was absent."

        # Claims without evidence supplied
        elif not claim["evidence_supplied"]:

            verdict = "INSUFFICIENT"
            evidence = "No technical evidence supplied"
            reason = "Unable to verify vendor claim."

        rows.append({
            "claim_id": claim["claim_id"],
            "control": claim["control"],
            "vendor_claim": str(claim["value"]),
            "evidence": evidence,
            "verdict": verdict,
            "reason": reason,
        })

    return rows
