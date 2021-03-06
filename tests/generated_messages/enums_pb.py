# Generated by protox. DO NOT EDIT!
# source: enums.proto
import typing
from enum import IntEnum

import protox


class Color(IntEnum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Hello(protox.Message):
    class Color(IntEnum):
        RED = 1
        GREEN = 2
        BLUE = 3

    a: 'Hello.Color'
    b: 'Hello.Color'
    default_enum: 'Hello.Color'
    repeated_enum: typing.List['Hello.Color']
    optional_enum: typing.Optional['Hello.Color']
    optional_default_enum: typing.Optional['Hello.Color']

    def __init__(
        self,
        *,
        a: 'Hello.Color' = None,
        b: 'Hello.Color' = None,
        default_enum: 'Hello.Color' = None,
        repeated_enum: typing.List['Hello.Color'] = None,
        optional_enum: typing.Optional['Hello.Color'] = None,
        optional_default_enum: typing.Optional['Hello.Color'] = None,
    ):
        super().__init__(
            a=a,
            b=b,
            default_enum=default_enum,
            repeated_enum=repeated_enum,
            optional_enum=optional_enum,
            optional_default_enum=optional_default_enum,
        )


FILE_DESCRIPTOR = protox.FileDescriptorProto.from_bytes(b'\n\x0benums.proto"\xc9\x02\n\x05Hello\x12\x1a\n\x01a\x18\x01 \x02(\x0e2\x0c.Hello.ColorR\x01a\x12\x1a\n\x01b\x18\x02 \x02(\x0e2\x0c.Hello.ColorR\x01b\x124\n\x0cdefault_enum\x18\x03 \x02(\x0e2\x0c.Hello.Color:\x03REDR\x0bdefaultEnum\x121\n\rrepeated_enum\x18\x04 \x03(\x0e2\x0c.Hello.ColorR\x0crepeatedEnum\x121\n\roptional_enum\x18\x05 \x01(\x0e2\x0c.Hello.ColorR\x0coptionalEnum\x12E\n\x15optional_default_enum\x18\x06 \x01(\x0e2\x0c.Hello.Color:\x03REDR\x13optionalDefaultEnum"%\n\x05Color\x12\x07\n\x03RED\x10\x01\x12\t\n\x05GREEN\x10\x02\x12\x08\n\x04BLUE\x10\x03*%\n\x05Color\x12\x07\n\x03RED\x10\x01\x12\t\n\x05GREEN\x10\x02\x12\x08\n\x04BLUE\x10\x03J\xbc\x06\n\x06\x12\x04\x00\x00\x17\x01\n\x08\n\x01\x0c\x12\x03\x00\x00\x12\n\n\n\x02\x05\x00\x12\x04\x02\x00\x06\x01\n\n\n\x03\x05\x00\x01\x12\x03\x02\x05\n\n\x0b\n\x04\x05\x00\x02\x00\x12\x03\x03\x04\x0c\n\x0c\n\x05\x05\x00\x02\x00\x01\x12\x03\x03\x04\x07\n\x0c\n\x05\x05\x00\x02\x00\x02\x12\x03\x03\n\x0b\n\x0b\n\x04\x05\x00\x02\x01\x12\x03\x04\x04\x0e\n\x0c\n\x05\x05\x00\x02\x01\x01\x12\x03\x04\x04\t\n\x0c\n\x05\x05\x00\x02\x01\x02\x12\x03\x04\x0c\r\n\x0b\n\x04\x05\x00\x02\x02\x12\x03\x05\x04\r\n\x0c\n\x05\x05\x00\x02\x02\x01\x12\x03\x05\x04\x08\n\x0c\n\x05\x05\x00\x02\x02\x02\x12\x03\x05\x0b\x0c\n\n\n\x02\x04\x00\x12\x04\x08\x00\x17\x01\n\n\n\x03\x04\x00\x01\x12\x03\x08\x08\r\n\x0c\n\x04\x04\x00\x04\x00\x12\x04\t\x04\r\x05\n\x0c\n\x05\x04\x00\x04\x00\x01\x12\x03\t\t\x0e\n\r\n\x06\x04\x00\x04\x00\x02\x00\x12\x03\n\x08\x10\n\x0e\n\x07\x04\x00\x04\x00\x02\x00\x01\x12\x03\n\x08\x0b\n\x0e\n\x07\x04\x00\x04\x00\x02\x00\x02\x12\x03\n\x0e\x0f\n\r\n\x06\x04\x00\x04\x00\x02\x01\x12\x03\x0b\x08\x12\n\x0e\n\x07\x04\x00\x04\x00\x02\x01\x01\x12\x03\x0b\x08\r\n\x0e\n\x07\x04\x00\x04\x00\x02\x01\x02\x12\x03\x0b\x10\x11\n\r\n\x06\x04\x00\x04\x00\x02\x02\x12\x03\x0c\x08\x11\n\x0e\n\x07\x04\x00\x04\x00\x02\x02\x01\x12\x03\x0c\x08\x0c\n\x0e\n\x07\x04\x00\x04\x00\x02\x02\x02\x12\x03\x0c\x0f\x10\n\x0b\n\x04\x04\x00\x02\x00\x12\x03\x0f\x04\x19\n\x0c\n\x05\x04\x00\x02\x00\x04\x12\x03\x0f\x04\x0c\n\x0c\n\x05\x04\x00\x02\x00\x06\x12\x03\x0f\r\x12\n\x0c\n\x05\x04\x00\x02\x00\x01\x12\x03\x0f\x13\x14\n\x0c\n\x05\x04\x00\x02\x00\x03\x12\x03\x0f\x17\x18\n\x0b\n\x04\x04\x00\x02\x01\x12\x03\x10\x04\x1f\n\x0c\n\x05\x04\x00\x02\x01\x04\x12\x03\x10\x04\x0c\n\x0c\n\x05\x04\x00\x02\x01\x06\x12\x03\x10\r\x18\n\x0c\n\x05\x04\x00\x02\x01\x01\x12\x03\x10\x19\x1a\n\x0c\n\x05\x04\x00\x02\x01\x03\x12\x03\x10\x1d\x1e\n\x0b\n\x04\x04\x00\x02\x02\x12\x03\x11\x04:\n\x0c\n\x05\x04\x00\x02\x02\x04\x12\x03\x11\x04\x0c\n\x0c\n\x05\x04\x00\x02\x02\x06\x12\x03\x11\r\x18\n\x0c\n\x05\x04\x00\x02\x02\x01\x12\x03\x11\x19%\n\x0c\n\x05\x04\x00\x02\x02\x03\x12\x03\x11()\n\x0c\n\x05\x04\x00\x02\x02\x08\x12\x03\x11*9\n\x0c\n\x05\x04\x00\x02\x02\x07\x12\x03\x1158\n\x0b\n\x04\x04\x00\x02\x03\x12\x03\x13\x04%\n\x0c\n\x05\x04\x00\x02\x03\x04\x12\x03\x13\x04\x0c\n\x0c\n\x05\x04\x00\x02\x03\x06\x12\x03\x13\r\x12\n\x0c\n\x05\x04\x00\x02\x03\x01\x12\x03\x13\x13 \n\x0c\n\x05\x04\x00\x02\x03\x03\x12\x03\x13#$\n\x0b\n\x04\x04\x00\x02\x04\x12\x03\x15\x04%\n\x0c\n\x05\x04\x00\x02\x04\x04\x12\x03\x15\x04\x0c\n\x0c\n\x05\x04\x00\x02\x04\x06\x12\x03\x15\r\x12\n\x0c\n\x05\x04\x00\x02\x04\x01\x12\x03\x15\x13 \n\x0c\n\x05\x04\x00\x02\x04\x03\x12\x03\x15#$\n\x0b\n\x04\x04\x00\x02\x05\x12\x03\x16\x04=\n\x0c\n\x05\x04\x00\x02\x05\x04\x12\x03\x16\x04\x0c\n\x0c\n\x05\x04\x00\x02\x05\x06\x12\x03\x16\r\x12\n\x0c\n\x05\x04\x00\x02\x05\x01\x12\x03\x16\x13(\n\x0c\n\x05\x04\x00\x02\x05\x03\x12\x03\x16+,\n\x0c\n\x05\x04\x00\x02\x05\x08\x12\x03\x16-<\n\x0c\n\x05\x04\x00\x02\x05\x07\x12\x03\x168;')

protox.define_fields(
    Hello,
    a=protox.EnumField(
        number=1, py_enum=Hello.Color, required=True
    ),
    b=protox.EnumField(
        number=2, py_enum=Hello.Color, required=True
    ),
    default_enum=protox.EnumField(
        number=3, py_enum=Hello.Color, default=Hello.Color.RED, required=True
    ),
    repeated_enum=protox.Repeated(
        number=4, of_type=Hello.Color
    ),
    optional_enum=protox.EnumField(
        number=5, py_enum=Hello.Color, required=False
    ),
    optional_default_enum=protox.EnumField(
        number=6, py_enum=Hello.Color, default=Hello.Color.RED, required=False
    ),
)
Hello.DESCRIPTOR = protox.DescriptorProto.from_bytes(b'\n\x05Hello\x12\x1a\n\x01a\x18\x01 \x02(\x0e2\x0c.Hello.ColorR\x01a\x12\x1a\n\x01b\x18\x02 \x02(\x0e2\x0c.Hello.ColorR\x01b\x124\n\x0cdefault_enum\x18\x03 \x02(\x0e2\x0c.Hello.Color:\x03REDR\x0bdefaultEnum\x121\n\rrepeated_enum\x18\x04 \x03(\x0e2\x0c.Hello.ColorR\x0crepeatedEnum\x121\n\roptional_enum\x18\x05 \x01(\x0e2\x0c.Hello.ColorR\x0coptionalEnum\x12E\n\x15optional_default_enum\x18\x06 \x01(\x0e2\x0c.Hello.Color:\x03REDR\x13optionalDefaultEnum"%\n\x05Color\x12\x07\n\x03RED\x10\x01\x12\t\n\x05GREEN\x10\x02\x12\x08\n\x04BLUE\x10\x03')
Hello.DESCRIPTOR.file_descriptor = FILE_DESCRIPTOR
Hello.DESCRIPTOR.full_name = 'Hello'
