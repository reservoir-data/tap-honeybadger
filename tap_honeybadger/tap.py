"""Honeybadger tap class."""

from __future__ import annotations

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

    def discover_streams(self) -> list[Stream]:
        """Return a list of discovered streams.

        Returns:
            A list of Honeybadger streams.
        """
        return [
            streams.Accounts(tap=self),
            streams.Projects(tap=self),
            streams.Faults(tap=self),
            streams.Teams(tap=self),
        ]
