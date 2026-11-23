from custom_components.askey_rtl6300_5g_cpe.utils import safe_get_property
from homeassistant.const import UnitOfInformation
from .base_sensor import AskeyBaseSensor


def _to_gb(raw):
    """Convert 'X.XXMB' / 'X.XXKB' / 'X.XXGB' / numbers to gigabytes."""
    if raw is None:
        return None
    if isinstance(raw, (int, float)):
        return round(float(raw), 3)
    s = str(raw).strip().replace(",", ".")
    for unit, factor in (
        ("TB", 1024.0),
        ("GB", 1.0),
        ("MB", 1.0 / 1024),
        ("KB", 1.0 / 1048576),
        ("B", 1.0 / 1073741824),
    ):
        if s.upper().endswith(unit):
            try:
                return round(float(s[: -len(unit)].strip()) * factor, 3)
            except ValueError:
                return None
    try:
        return round(float(s), 3)
    except ValueError:
        return None


class AskeyMonthlyRxSensor(AskeyBaseSensor):
    """
    Sensor for monitoring the monthly received traffic (RX).
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "Monthly Download",
            "askey_monthly_rx",
            "mdi:download",
            "rx",
            UnitOfInformation.GIGABYTES,
        )

    @property
    def native_value(self):
        return safe_get_property(
            self.coordinator.data,
            ["traffic_monthly", "rx"],
            _to_gb,
        )

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Monthly received traffic.",
            "Unit": UnitOfInformation.GIGABYTES,
        }


class AskeyMonthlyTxSensor(AskeyBaseSensor):
    """
    Sensor for monitoring the monthly transmitted traffic (TX).
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "Monthly Upload",
            "askey_monthly_tx",
            "mdi:upload",
            "tx",
            UnitOfInformation.GIGABYTES,
        )

    @property
    def native_value(self):
        return safe_get_property(
            self.coordinator.data,
            ["traffic_monthly", "tx"],
            _to_gb,
        )

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Monthly transmitted traffic.",
            "Unit": UnitOfInformation.GIGABYTES,
        }


class AskeyMonthlyTotalSensor(AskeyBaseSensor):
    """
    Sensor for monitoring the total monthly traffic.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "Monthly Total",
            "askey_monthly_total",
            "mdi:swap-horizontal",
            "total",
            UnitOfInformation.GIGABYTES,
        )

    @property
    def native_value(self):
        return safe_get_property(
            self.coordinator.data,
            ["traffic_monthly", "total"],
            _to_gb,
        )

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Total monthly traffic",
            "Unit": UnitOfInformation.GIGABYTES,
        }


class AskeyMonthlyUpdatedDatetimeSensor(AskeyBaseSensor):
    """
    Sensor for monitoring the last update datetime of monthly traffic data.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "Last Traffic Update",
            "askey_monthly_updated_datetime",
            "mdi:calendar-clock",
            "updated_datetime",
        )

    @property
    def native_value(self):
        return safe_get_property(
            self.coordinator.data, ["traffic_monthly", "updated_datetime"]
        )

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Last update datetime of monthly traffic data.",
            "Unit": "None",
        }
