"""Honeybadger tap class."""

from __future__ import annotations

from typing import override

from singer_sdk import Stream, Tap
from singer_sdk import typing as th

from tap_honeybadger import streams


class TapHoneybadger(Tap):
    """Singer tap for Honeybadger."""

    name = "tap-honeybadger"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "auth_token",
            th.StringType,
            required=True,
            secret=True,
            description="Honeybadger personal authentication token",
        ),
    ).to_dict()

    @override
    def discover_streams(self) -> list[Stream]:
        return [
            streams.Accounts(tap=self),
            streams.Projects(tap=self),
            streams.Faults(tap=self),
            streams.Teams(tap=self),
        ]
