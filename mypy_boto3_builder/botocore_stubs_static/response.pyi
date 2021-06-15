import logging
from typing import IO, Any, Iterator, Optional, Tuple

import requests
from botocore.model import OperationModel

logger: logging.Logger

class StreamingBody:
    def __init__(self, raw_stream: IO[bytes], content_length: int) -> None: ...
    def set_socket_timeout(self, timeout: float) -> None: ...
    def read(self, amt: Optional[int] = ...) -> bytes: ...
    def __iter__(self) -> Iterator[bytes]: ...
    def iter_lines(self, chunk_size: int = ..., keepends: bool = ...) -> Iterator[bytes]: ...
    def iter_chunks(self, chunk_size: int = ...) -> Iterator[bytes]: ...
    def close(self) -> None: ...

def get_response(
    operation_model: OperationModel, http_response: requests.Response
) -> Tuple[requests.Response, Any]: ...