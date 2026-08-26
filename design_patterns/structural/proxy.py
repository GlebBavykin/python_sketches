import logging
from typing import Protocol, runtime_checkable

from requests import Response, Session

logger = logging.getLogger(__name__)


@runtime_checkable
class Requestable(Protocol):
    """
    Common interface for Session and Proxy
    """

    def get(self, url, params=None, **kwargs) -> Response: ...

    def options(self, url, **kwargs) -> Response: ...

    def head(self, url, **kwargs) -> Response: ...

    def post(self, url, data=None, json=None, **kwargs) -> Response: ...

    def put(self, url, data=None, **kwargs) -> Response: ...

    def patch(self, url, data=None, **kwargs) -> Response: ...

    def delete(self, url, **kwargs) -> Response: ...


class SessionWithLogging:
    """
    Proxy Session class with logging features
    """

    def __init__(self, session: Session) -> None:
        self.session = session

    def get(self, url, params=None, **kwargs) -> Response:
        logger.info(f"GET {url} with params: {params} and kwargs: {kwargs}")
        return self.session.get(url, params=params, **kwargs)

    def options(self, url, **kwargs) -> Response:
        logger.info(f"OPTIONS {url} with kwargs: {kwargs}")
        return self.session.options(url, **kwargs)

    def head(self, url, **kwargs) -> Response:
        logger.info(f"HEAD {url} with kwargs: {kwargs}")
        return self.session.head(url, **kwargs)

    def post(self, url, data=None, json=None, **kwargs) -> Response:
        logger.info(
            f"POST {url} with data: {data} data: {data}, json: {json} kwargs: {kwargs}"
        )
        return self.session.post(url, data=data, **kwargs)

    def put(self, url, data=None, **kwargs) -> Response:
        logger.info(f"PUT {url} with data: {data} and kwargs: {kwargs}")
        return self.session.put(url, data=data, **kwargs)

    def patch(self, url, data=None, **kwargs) -> Response:
        logger.info(f"PATCH {url} with data: {data} and kwargs: {kwargs}")
        return self.session.patch(url, data=data, **kwargs)

    def delete(self, url, **kwargs) -> Response:
        logger.info(f"DELETE {url} with kwargs: {kwargs}")
        return self.session.patch(url, **kwargs)
