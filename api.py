import asyncio
import random


class ZSEApiClient:
    """Simple mock API client for ZSE Slovakia."""

    async def async_get_data(self) -> dict:
        """Simulate fetching data from API."""
        await asyncio.sleep(1)  # Simulate network delay
        return {
            "current_power_kw": round(random.uniform(2.0, 5.0), 2),
            "status": "OK",
        }
