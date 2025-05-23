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

from gns3client.openapi_client import schemas  # noqa: F401


class ProjectCreate(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Properties for project creation.
    """


    class MetaOapg:
        required = {
            "name",
        }
        
        class properties:
            name = schemas.AnyTypeSchema
            project_id = schemas.AnyTypeSchema
            path = schemas.AnyTypeSchema
            auto_close = schemas.AnyTypeSchema
            auto_open = schemas.AnyTypeSchema
            auto_start = schemas.AnyTypeSchema
            scene_height = schemas.AnyTypeSchema
            scene_width = schemas.AnyTypeSchema
            zoom = schemas.AnyTypeSchema
            show_layers = schemas.AnyTypeSchema
            snap_to_grid = schemas.AnyTypeSchema
            show_grid = schemas.AnyTypeSchema
            grid_size = schemas.AnyTypeSchema
            drawing_grid_size = schemas.AnyTypeSchema
            show_interface_labels = schemas.AnyTypeSchema
            supplier = schemas.AnyTypeSchema
            variables = schemas.AnyTypeSchema
            __annotations__ = {
                "name": name,
                "project_id": project_id,
                "path": path,
                "auto_close": auto_close,
                "auto_open": auto_open,
                "auto_start": auto_start,
                "scene_height": scene_height,
                "scene_width": scene_width,
                "zoom": zoom,
                "show_layers": show_layers,
                "snap_to_grid": snap_to_grid,
                "show_grid": show_grid,
                "grid_size": grid_size,
                "drawing_grid_size": drawing_grid_size,
                "show_interface_labels": show_interface_labels,
                "supplier": supplier,
                "variables": variables,
            }

    
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["project_id"]) -> MetaOapg.properties.project_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["path"]) -> MetaOapg.properties.path: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["auto_close"]) -> MetaOapg.properties.auto_close: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["auto_open"]) -> MetaOapg.properties.auto_open: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["auto_start"]) -> MetaOapg.properties.auto_start: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scene_height"]) -> MetaOapg.properties.scene_height: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scene_width"]) -> MetaOapg.properties.scene_width: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["zoom"]) -> MetaOapg.properties.zoom: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["show_layers"]) -> MetaOapg.properties.show_layers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["snap_to_grid"]) -> MetaOapg.properties.snap_to_grid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["show_grid"]) -> MetaOapg.properties.show_grid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["grid_size"]) -> MetaOapg.properties.grid_size: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["drawing_grid_size"]) -> MetaOapg.properties.drawing_grid_size: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["show_interface_labels"]) -> MetaOapg.properties.show_interface_labels: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["supplier"]) -> MetaOapg.properties.supplier: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["variables"]) -> MetaOapg.properties.variables: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "project_id", "path", "auto_close", "auto_open", "auto_start", "scene_height", "scene_width", "zoom", "show_layers", "snap_to_grid", "show_grid", "grid_size", "drawing_grid_size", "show_interface_labels", "supplier", "variables", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["project_id"]) -> typing.Union[MetaOapg.properties.project_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["path"]) -> typing.Union[MetaOapg.properties.path, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["auto_close"]) -> typing.Union[MetaOapg.properties.auto_close, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["auto_open"]) -> typing.Union[MetaOapg.properties.auto_open, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["auto_start"]) -> typing.Union[MetaOapg.properties.auto_start, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scene_height"]) -> typing.Union[MetaOapg.properties.scene_height, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scene_width"]) -> typing.Union[MetaOapg.properties.scene_width, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["zoom"]) -> typing.Union[MetaOapg.properties.zoom, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["show_layers"]) -> typing.Union[MetaOapg.properties.show_layers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["snap_to_grid"]) -> typing.Union[MetaOapg.properties.snap_to_grid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["show_grid"]) -> typing.Union[MetaOapg.properties.show_grid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["grid_size"]) -> typing.Union[MetaOapg.properties.grid_size, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["drawing_grid_size"]) -> typing.Union[MetaOapg.properties.drawing_grid_size, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["show_interface_labels"]) -> typing.Union[MetaOapg.properties.show_interface_labels, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["supplier"]) -> typing.Union[MetaOapg.properties.supplier, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["variables"]) -> typing.Union[MetaOapg.properties.variables, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "project_id", "path", "auto_close", "auto_open", "auto_start", "scene_height", "scene_width", "zoom", "show_layers", "snap_to_grid", "show_grid", "grid_size", "drawing_grid_size", "show_interface_labels", "supplier", "variables", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        name: typing.Union[MetaOapg.properties.name, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        project_id: typing.Union[MetaOapg.properties.project_id, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        path: typing.Union[MetaOapg.properties.path, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        auto_close: typing.Union[MetaOapg.properties.auto_close, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        auto_open: typing.Union[MetaOapg.properties.auto_open, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        auto_start: typing.Union[MetaOapg.properties.auto_start, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        scene_height: typing.Union[MetaOapg.properties.scene_height, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        scene_width: typing.Union[MetaOapg.properties.scene_width, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        zoom: typing.Union[MetaOapg.properties.zoom, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        show_layers: typing.Union[MetaOapg.properties.show_layers, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        snap_to_grid: typing.Union[MetaOapg.properties.snap_to_grid, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        show_grid: typing.Union[MetaOapg.properties.show_grid, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        grid_size: typing.Union[MetaOapg.properties.grid_size, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        drawing_grid_size: typing.Union[MetaOapg.properties.drawing_grid_size, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        show_interface_labels: typing.Union[MetaOapg.properties.show_interface_labels, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        supplier: typing.Union[MetaOapg.properties.supplier, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        variables: typing.Union[MetaOapg.properties.variables, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProjectCreate':
        return super().__new__(
            cls,
            *_args,
            name=name,
            project_id=project_id,
            path=path,
            auto_close=auto_close,
            auto_open=auto_open,
            auto_start=auto_start,
            scene_height=scene_height,
            scene_width=scene_width,
            zoom=zoom,
            show_layers=show_layers,
            snap_to_grid=snap_to_grid,
            show_grid=show_grid,
            grid_size=grid_size,
            drawing_grid_size=drawing_grid_size,
            show_interface_labels=show_interface_labels,
            supplier=supplier,
            variables=variables,
            _configuration=_configuration,
            **kwargs,
        )
