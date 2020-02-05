# Generated by protox. DO NOT EDIT!
# source: service/ping.proto
from enum import IntEnum

import protox


class PingRequest(protox.Message):
    message: str

    def __init__(
        self,
        *,
        message: str = None,
    ):
        super().__init__(
            message=message,
        )


class PingResponse(protox.Message):
    class Status(IntEnum):
        OK = 1
        ERROR = 2

    status: 'PingResponse.Status'
    message: str

    def __init__(
        self,
        *,
        status: 'PingResponse.Status' = None,
        message: str = None,
    ):
        super().__init__(
            status=status,
            message=message,
        )


protox.define_fields(
    PingRequest,
    message=protox.String(
        number=1, required=True
    ),
)

protox.define_fields(
    PingResponse,
    status=protox.EnumField(
        number=1, py_enum=PingResponse.Status, required=True
    ),
    message=protox.String(
        number=2, required=True
    ),
)