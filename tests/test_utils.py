import pytest

from validator.utils import (
    compare_tls_versions,
    find_duplicate_event_ids,
    find_broken_hash_chain,
)


def test_compare_tls_versions_pass():
    assert compare_tls_versions("TLSv1.3", "1.2")


def test_compare_tls_versions_fail():
    assert not compare_tls_versions("TLSv1.0", "1.2")


def test_duplicate_event_detection():
    events = [
        {
            "event_id": "A1",
            "previous_hash": "ROOT",
            "hash": "111"
        },
        {
            "event_id": "A2",
            "previous_hash": "111",
            "hash": "222"
        },
        {
            "event_id": "A2",
            "previous_hash": "222",
            "hash": "333"
        }
    ]

    duplicates = find_duplicate_event_ids(events)

    assert len(duplicates) == 1
    assert duplicates[0]["event_id"] == "A2"


def test_hash_chain_detection():
    events = [
        {
            "event_id": "A1",
            "previous_hash": "ROOT",
            "hash": "111"
        },
        {
            "event_id": "A2",
            "previous_hash": "WRONG",
            "hash": "222"
        }
    ]

    broken = find_broken_hash_chain(events)

    assert len(broken) == 1
    assert broken[0]["event_id"] == "A2"
