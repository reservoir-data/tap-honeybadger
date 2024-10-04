"""Stream type classes for tap-honeybadger."""

from __future__ import annotations

import typing as t

from singer_sdk import typing as th

from tap_honeybadger.client import HoneybadgerStream

if t.TYPE_CHECKING:
    from singer_sdk.helpers.types import Context, Record


class Accounts(HoneybadgerStream):
    """Accounts stream."""

    name = "accounts"
    path = "/v2/accounts"
    primary_keys = ("id",)
    replication_key = None

    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("email", th.StringType),
        th.Property("name", th.StringType),
        th.Property("active", th.BooleanType),
        th.Property("parked", th.BooleanType),
    ).to_dict()


class Projects(HoneybadgerStream):
    """Projects stream."""

    name = "projects"
    path = "/v2/projects"
    primary_keys = ("id",)
    replication_key = None

    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("active", th.BooleanType),
        th.Property("created_at", th.DateTimeType),
        th.Property("earliest_notice_at", th.DateTimeType),
        th.Property("environments", th.ArrayType(th.StringType)),
        th.Property("fault_count", th.IntegerType),
        th.Property("last_notice_at", th.DateTimeType),
        th.Property("name", th.StringType),
        th.Property(
            "owner",
            th.ObjectType(
                th.Property("email", th.StringType),
                th.Property("id", th.IntegerType),
                th.Property("name", th.StringType),
            ),
        ),
        th.Property(
            "sites",
            th.ArrayType(
                th.ObjectType(
                    th.Property("active", th.BooleanType),
                    th.Property("id", th.StringType),
                    th.Property("last_checked_at", th.DateTimeType),
                    th.Property("name", th.StringType),
                    th.Property("state", th.StringType),
                    th.Property("url", th.StringType),
                )
            ),
        ),
        th.Property(
            "teams",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("name", th.StringType),
                )
            ),
        ),
        th.Property("token", th.StringType),
        th.Property("unresolved_fault_count", th.IntegerType),
        th.Property(
            "users",
            th.ArrayType(
                th.ObjectType(
                    th.Property("email", th.StringType),
                    th.Property("id", th.IntegerType),
                    th.Property("name", th.StringType),
                )
            ),
        ),
    ).to_dict()

    def generate_child_contexts(
        self,
        record: Record,
        context: Context | None = None,  # noqa: ARG002
    ) -> t.Generator[Context, None, None]:
        """Generate child contexts for a record."""
        yield {"project_id": record["id"]}


class Faults(HoneybadgerStream):
    """Faults stream."""

    name = "faults"
    path = "/v2/projects/{project_id}/faults"
    primary_keys = ("id",)
    replication_key = None

    parent_stream_type = Projects

    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("action", th.StringType),
        th.Property(
            "assignee",
            th.ObjectType(
                th.Property("email", th.StringType),
                th.Property("id", th.IntegerType),
                th.Property("name", th.StringType),
            ),
        ),
        th.Property("comments_count", th.IntegerType),
        th.Property("component", th.StringType),
        th.Property("created_at", th.DateTimeType),
        th.Property("environment", th.StringType),
        th.Property("ignored", th.BooleanType),
        th.Property("klass", th.StringType),
        th.Property("last_notice_at", th.DateTimeType),
        th.Property("message", th.StringType),
        th.Property("notices_count", th.IntegerType),
        th.Property("project_id", th.IntegerType),
        th.Property("resolved", th.BooleanType),
        th.Property("tags", th.ArrayType(th.StringType)),
        th.Property("url", th.StringType),
    ).to_dict()


class Teams(HoneybadgerStream):
    """Teams stream."""

    name = "teams"
    path = "/v2/teams"
    primary_keys = ("id",)
    replication_key = None

    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("name", th.StringType),
        th.Property("created_at", th.DateTimeType),
        th.Property("owner", th.ObjectType(
            th.Property("id", th.IntegerType),
            th.Property("email", th.StringType),
            th.Property("name", th.StringType),
        )),
        th.Property("members", th.ArrayType(
            th.ObjectType(
                th.Property("id", th.IntegerType),
                th.Property("created_at", th.DateTimeType),
                th.Property("admin", th.BooleanType),
                th.Property("name", th.StringType),
                th.Property("email", th.StringType),
            )
        )),
        th.Property("projects", th.ArrayType(
            th.ObjectType(
                th.Property("id", th.IntegerType),
                th.Property("name", th.StringType),
                th.Property("created_at", th.DateTimeType),
            ),
        )),
        th.Property("invitations", th.ArrayType(
            th.ObjectType(
                th.Property("id", th.IntegerType),
            ),
        )),
        th.Property("project_id", th.IntegerType),
    ).to_dict()
