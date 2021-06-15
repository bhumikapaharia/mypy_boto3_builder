from typing import Any

from botocore.exceptions import EventStreamError as EventStreamError

class ParserError(Exception): ...

class DuplicateHeader(ParserError):
    def __init__(self, header: Any) -> None: ...

class InvalidHeadersLength(ParserError):
    def __init__(self, length: Any) -> None: ...

class InvalidPayloadLength(ParserError):
    def __init__(self, length: Any) -> None: ...

class ChecksumMismatch(ParserError):
    def __init__(self, expected: Any, calculated: Any) -> None: ...

class NoInitialResponseError(ParserError):
    def __init__(self) -> None: ...

class DecodeUtils:
    UINT8_BYTE_FORMAT: str = ...
    UINT16_BYTE_FORMAT: str = ...
    UINT32_BYTE_FORMAT: str = ...
    INT8_BYTE_FORMAT: str = ...
    INT16_BYTE_FORMAT: str = ...
    INT32_BYTE_FORMAT: str = ...
    INT64_BYTE_FORMAT: str = ...
    PRELUDE_BYTE_FORMAT: str = ...
    UINT_BYTE_FORMAT: Any = ...
    @staticmethod
    def unpack_true(data: Any) -> Any: ...
    @staticmethod
    def unpack_false(data: Any) -> Any: ...
    @staticmethod
    def unpack_uint8(data: Any) -> Any: ...
    @staticmethod
    def unpack_uint32(data: Any) -> Any: ...
    @staticmethod
    def unpack_int8(data: Any) -> Any: ...
    @staticmethod
    def unpack_int16(data: Any) -> Any: ...
    @staticmethod
    def unpack_int32(data: Any) -> Any: ...
    @staticmethod
    def unpack_int64(data: Any) -> Any: ...
    @staticmethod
    def unpack_byte_array(data: Any, length_byte_size: int = ...) -> Any: ...
    @staticmethod
    def unpack_utf8_string(data: Any, length_byte_size: int = ...) -> Any: ...
    @staticmethod
    def unpack_uuid(data: Any) -> Any: ...
    @staticmethod
    def unpack_prelude(data: Any) -> Any: ...

class MessagePrelude:
    total_length: Any = ...
    headers_length: Any = ...
    crc: Any = ...
    def __init__(self, total_length: Any, headers_length: Any, crc: Any) -> None: ...
    @property
    def payload_length(self) -> Any: ...
    @property
    def payload_end(self) -> Any: ...
    @property
    def headers_end(self) -> Any: ...

class EventStreamMessage:
    prelude: Any = ...
    headers: Any = ...
    payload: Any = ...
    crc: Any = ...
    def __init__(self, prelude: Any, headers: Any, payload: Any, crc: Any) -> None: ...
    def to_response_dict(self, status_code: int = ...) -> Any: ...

class EventStreamHeaderParser:
    def __init__(self) -> None: ...
    def parse(self, data: Any) -> Any: ...

class EventStreamBuffer:
    def __init__(self) -> None: ...
    def add_data(self, data: Any) -> None: ...
    def next(self) -> Any: ...
    def __next__(self) -> Any: ...
    def __iter__(self) -> Any: ...

class EventStream:
    def __init__(
        self, raw_stream: Any, output_shape: Any, parser: Any, operation_name: Any
    ) -> None: ...
    def __iter__(self) -> Any: ...
    def get_initial_response(self) -> Any: ...
    def close(self) -> None: ...