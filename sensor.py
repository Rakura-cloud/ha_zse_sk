from __future__ import annotations
from datetime import timedelta
import logging

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

SCAN_INTERVAL = timedelta(minutes=5)


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """Set up the ZSE sensor."""
    client = hass.data[DOMAIN]["client"]
    async_add_entities([ZSEPowerSensor(client)], True)


class ZSEPowerSensor(SensorEntity):
    """Representation of the current power usage from ZSE."""

    _attr_name = "ZSE Current Power"
    _attr_native_unit_of_measurement = "kW"

    def __init__(self, client):
        self._client = client
        self._attr_unique_id = "zse_current_power"
        self._attr_native_value = None

    async def async_update(self):
        """Fetch new state data for the sensor."""
        try:
            data = await self._client.async_get_data()
            self._attr_native_value = data["current_power_kw"]
        except Exception as e:
            _LOGGER.error("Error updating ZSE data: %s", e)
