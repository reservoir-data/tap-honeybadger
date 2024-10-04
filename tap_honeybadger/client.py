"""REST client handling, including HoneybadgerStream base class."""

from __future__ import annotations

import typing as t

from requests.auth import HTTPBasicAuth
from singer_sdk import RESTStream

if t.TYPE_CHECKING:
    from singer_sdk.helpers.types import Context


class HoneybadgerStream(RESTStream[t.Any]):
    """Honeybadger stream class."""

    url_base = "https://app.honeybadger.io"
    records_jsonpath = "$.results[*]"
    # next_page_token_jsonpath = "$.next_page"  # noqa: S105

    @property
    def authenticator(self) -> HTTPBasicAuth:
        """Get an authenticator object.

        Returns:
            The authenticator instance for this REST stream.
        """
        return HTTPBasicAuth(self.config["auth_token"], password="")

    @property
    def http_headers(self) -> dict[str, str]:
        """Return the http headers needed.

        Returns:
            A dictionary of HTTP headers.
        """
        return {"User-Agent": f"{self.tap_name}/{self._tap.plugin_version}"}

    def get_url_params(
        self,
        context: Context | None,  # noqa: ARG002
        next_page_token: t.Any | None,  # noqa: ARG002, ANN401
    ) -> dict[str, t.Any]:
        """Get URL query parameters.

        Args:
            context: Stream sync context.
            next_page_token: Next offset.

        Returns:
            Mapping of URL query parameters.
        """
        params: dict[str, t.Any] = {}
        return params
