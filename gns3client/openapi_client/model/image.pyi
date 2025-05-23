# coding: utf-8

"""
    GNS3 controller API

    This page describes the public controller API for GNS3  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_client import schemas  # noqa: F401


class Image(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "path",
            "filename",
            "image_size",
            "checksum_algorithm",
            "checksum",
            "image_type",
        }
        
        class properties:
            filename = schemas.AnyTypeSchema
            path = schemas.AnyTypeSchema
        
            @staticmethod
            def image_type() -> typing.Type['ImageType']:
                return ImageType
            image_size = schemas.AnyTypeSchema
            checksum = schemas.AnyTypeSchema
            checksum_algorithm = schemas.AnyTypeSchema
            created_at = schemas.AnyTypeSchema
            updated_at = schemas.AnyTypeSchema
            __annotations__ = {
                "filename": filename,
                "path": path,
                "image_type": image_type,
                "image_size": image_size,
                "checksum": checksum,
                "checksum_algorithm": checksum_algorithm,
                "created_at": created_at,
                "updated_at": updated_at,
            }

    
    path: MetaOapg.properties.path
    filename: MetaOapg.properties.filename
    image_size: MetaOapg.properties.image_size
    checksum_algorithm: MetaOapg.properties.checksum_algorithm
    checksum: MetaOapg.properties.checksum
    image_type: 'ImageType'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["filename"]) -> MetaOapg.properties.filename: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["path"]) -> MetaOapg.properties.path: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image_type"]) -> 'ImageType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image_size"]) -> MetaOapg.properties.image_size: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["checksum"]) -> MetaOapg.properties.checksum: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["checksum_algorithm"]) -> MetaOapg.properties.checksum_algorithm: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["filename", "path", "image_type", "image_size", "checksum", "checksum_algorithm", "created_at", "updated_at", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["filename"]) -> MetaOapg.properties.filename: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["path"]) -> MetaOapg.properties.path: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image_type"]) -> 'ImageType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image_size"]) -> MetaOapg.properties.image_size: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["checksum"]) -> MetaOapg.properties.checksum: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["checksum_algorithm"]) -> MetaOapg.properties.checksum_algorithm: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> typing.Union[MetaOapg.properties.updated_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["filename", "path", "image_type", "image_size", "checksum", "checksum_algorithm", "created_at", "updated_at", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        path: typing.Union[MetaOapg.properties.path, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        filename: typing.Union[MetaOapg.properties.filename, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        image_size: typing.Union[MetaOapg.properties.image_size, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        checksum_algorithm: typing.Union[MetaOapg.properties.checksum_algorithm, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        checksum: typing.Union[MetaOapg.properties.checksum, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        image_type: 'ImageType',
        created_at: typing.Union[MetaOapg.properties.created_at, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        updated_at: typing.Union[MetaOapg.properties.updated_at, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Image':
        return super().__new__(
            cls,
            *_args,
            path=path,
            filename=filename,
            image_size=image_size,
            checksum_algorithm=checksum_algorithm,
            checksum=checksum,
            image_type=image_type,
            created_at=created_at,
            updated_at=updated_at,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.image_type import ImageType
