"""Constants for the Plum ecoMAX integration."""

from enum import StrEnum, unique
from typing import Final

DOMAIN = "plum_ecomax"

# Generic constants.
ALL: Final = "all"
MANUFACTURER: Final = "Plum Sp. z o.o."

# Generic attributes.
ATTR_BURNED_SINCE_LAST_UPDATE: Final = "burned_since_last_update"
ATTR_END: Final = "end"
ATTR_FIRMWARE: Final = "firmware"
ATTR_FROM: Final = "from"
ATTR_LOADED: Final = "loaded"
ATTR_MIXERS: Final = "mixers"
ATTR_MODULES: Final = "modules"
ATTR_NUMERIC_STATE: Final = "numeric_state"
ATTR_PASSWORD: Final = "password"
ATTR_PRESET: Final = "preset"
ATTR_PRODUCT: Final = "product"
ATTR_SCHEDULES: Final = "schedules"
ATTR_SENSORS: Final = "sensors"
ATTR_START: Final = "start"
ATTR_THERMOSTATS: Final = "thermostats"
ATTR_TO: Final = "to"
ATTR_TYPE: Final = "type"
ATTR_VALUE: Final = "value"
ATTR_WATER_HEATER: Final = "water_heater"
ATTR_WEEKDAYS: Final = "weekdays"


# Baudrates.
# (should be listed as strings due to the visual bug in hass selectors)
BAUDRATES: Final[tuple[str, ...]] = (
    "9600",
    "14400",
    "19200",
    "38400",
    "57600",
    "115200",
)

# Weekdays.
WEEKDAYS: Final[tuple[str, ...]] = (
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday",
)

# Configuration flow.
CONF_BAUDRATE: Final = "baudrate"
CONF_CAPABILITIES: Final = "capabilities"
CONF_CONNECTION_TYPE: Final = "connection_type"
CONF_DEVICE: Final = "device"
CONF_ENTITY_SOURCE: Final = "entity_source"
CONF_HOST: Final = "host"
CONF_KEY: Final = "key"
CONF_MODEL: Final = "model"
CONF_PORT: Final = "port"
CONF_PRODUCT_ID: Final = "product_id"
CONF_PRODUCT_TYPE: Final = "product_type"
CONF_SOFTWARE: Final = "software"
CONF_SUB_DEVICES: Final = "sub_devices"
CONF_TITLE: Final = "title"
CONF_UID: Final = "uid"
CONF_UPDATE_INTERVAL: Final = "update_interval"

# Connection types.
CONNECTION_TYPE_SERIAL: Final = "Serial"
CONNECTION_TYPE_TCP: Final = "TCP"
CONNECTION_TYPES: Final = (CONNECTION_TYPE_TCP, CONNECTION_TYPE_SERIAL)

# Defaults.
DEFAULT_BAUDRATE: Final = BAUDRATES[-1]
DEFAULT_CONNECTION_TYPE: Final = CONNECTION_TYPE_TCP
DEFAULT_DEVICE: Final = "/dev/ttyUSB0"
DEFAULT_PORT: Final = 8899

# Units of measurement.
CALORIFIC_KWH_KG: Final = "kWh/kg"
FLOW_KGH: Final = "kg/h"

# Events.
EVENT_PLUM_ECOMAX_ALERT: Final = "plum_ecomax_alert"

# Device classes.
DEVICE_CLASS_STATE: Final = "plum_ecomax__state"
DEVICE_CLASS_METER: Final = "plum_ecomax__meter"

# Data registry.
REGDATA = "regdata"


@unique
class Device(StrEnum):
    """Known devices, represented by PyPlumIO's Device class."""

    ECOMAX = "ecomax"
    MIXER = "mixer"
    THERMOSTAT = "thermostat"


@unique
class Module(StrEnum):
    """Known ecoMAX modules."""

    A = "module_a"
    B = "module_b"
    C = "module_c"
    ECOLAMBDA = "ecolambda"
    ECOSTER = "ecoster"
    PANEL = "panel"
