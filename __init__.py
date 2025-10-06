from __future__ import annotations
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN
from .api import ZSEApiClient


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up ZSE Slovakia integration from a config entry."""
    hass.data.setdefault(DOMAIN, {})

    client = ZSEApiClient()
    hass.data[DOMAIN]["client"] = client

    # Forward setup to the sensor platform
    await hass.config_entries.async_forward_entry_setups(entry, ["sensor"])
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, ["sensor"])
    if unload_ok:
        hass.data.pop(DOMAIN)
    return unload_ok
