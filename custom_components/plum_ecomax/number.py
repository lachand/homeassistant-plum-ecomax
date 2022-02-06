"""Platform for number integration."""
from __future__ import annotations

import logging

from homeassistant.components.number import NumberEntity
from homeassistant.const import PERCENTAGE, TEMP_CELSIUS
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType
from pyplumio.devices import EcoMAX

from .const import DOMAIN
from .entity import EcomaxEntity

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigType,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the number platform."""

    sensors = [
        EcomaxNumberTemperature("heating_set_temp", "Boiler Temperature"),
        EcomaxNumberTemperature("heating_temp_grate", "Grate Mode Temperature"),
        EcomaxNumberPercent("min_fuzzylogic_power", "FuzzyLogic Minimum Power"),
        EcomaxNumberPercent("max_fuzzylogic_power", "FuzzyLogic Maximum Power"),
    ]

    connection = hass.data[DOMAIN][config_entry.entry_id]
    await connection.add_entities(sensors, async_add_entities)


class EcomaxNumber(EcomaxEntity, NumberEntity):
    """ecoMAX number entity representation."""

    async def update_entity(self, ecomax: EcoMAX):
        """Update sensor state. Called by connection instance."""
        await super().update_entity(ecomax)
        self.async_write_ha_state()

    async def async_set_value(self, value: float):
        """Update the current value."""
        self.set_attribute(self._id, int(value))
        self.async_write_ha_state()

    @property
    def value(self):
        attr = self.get_attribute(self._id)
        if attr is not None:
            return attr.value

        return 0

    @property
    def min_value(self):
        attr = self.get_attribute(self._id)
        if attr is not None:
            return attr.min_

        return 0

    @property
    def max_value(self):
        attr = self.get_attribute(self._id)
        if attr is not None:
            return attr.max_

        return 0


class EcomaxNumberTemperature(EcomaxNumber):
    """Setup temperature number."""

    @property
    def unit_of_measurement(self):
        return TEMP_CELSIUS


class EcomaxNumberPercent(EcomaxNumber):
    """Setup percent number."""

    @property
    def unit_of_measurement(self):
        return PERCENTAGE
