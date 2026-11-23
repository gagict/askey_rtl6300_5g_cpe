from .base_sensor import AskeyBaseSensorDiagnostic

"""
SCC2 is not always present and the router has changes the json respose structure in that case.
not worth using safe_get_property
"""


class AskeyScc1PciSensor(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the Physical Cell Identity (PCI) of SCC2.
    PCI is used to identify the specific cell within a network.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator, "SCC2 PCI", "askey_scc2_pci", "mdi:network", "pci"
        )

    @property
    def native_value(self):
        try:
            return self.coordinator.data["cellular_info_ex"]["data"][2]["pci"]
        except (KeyError, IndexError, TypeError):
            return None

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Physical Cell Identity (PCI) of SCC2 used to identify cells within the network.",
            "Unit": "None",
        }


class AskeyScc1RssiSensor(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the Received Signal Strength Indicator (RSSI) of SCC2.
    RSSI measures the power level of the received signal, indicating signal strength.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "SCC2 RSSI",
            "askey_scc2_rssi",
            "mdi:signal",
            "rssi",
            "dBm",
        )

    @property
    def native_value(self):
        try:
            return float(self.coordinator.data["cellular_info_ex"]["data"][2]["rssi"])
        except (KeyError, IndexError, TypeError, ValueError):
            return None

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Received Signal Strength Indicator (RSSI) of SCC2. A measure of the power level being received by the device.",
            "Unit": "dBm",
        }


class AskeyScc1RsrpSensor(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the Reference Signal Received Power (RSRP) of SCC2.
    RSRP indicates the strength of the reference signal, which is important for connection stability.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "SCC2 RSRP",
            "askey_scc2_rsrp",
            "mdi:signal",
            "rsrp",
            "dBm",
        )

    @property
    def native_value(self):
        try:
            return float(self.coordinator.data["cellular_info_ex"]["data"][2]["rsrp"])
        except (KeyError, IndexError, TypeError, ValueError):
            return None

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Reference Signal Received Power (RSRP) of SCC2. Indicates the strength of the reference signal.",
            "Unit": "dBm",
        }


class AskeyScc1RsrqSensor(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the Reference Signal Received Quality (RSRQ) of SCC2.
    RSRQ is a measure of signal quality, combining signal strength and interference.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "SCC2 RSRQ",
            "askey_scc2_rsrq",
            "mdi:signal",
            "rsrq",
            "dB",
        )

    @property
    def native_value(self):
        try:
            return float(self.coordinator.data["cellular_info_ex"]["data"][2]["rsrq"])
        except (KeyError, IndexError, TypeError, ValueError):
            return None

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Reference Signal Received Quality (RSRQ) of SCC2. A measure of signal quality combining signal strength and interference.",
            "Unit": "dB",
        }


class AskeyScc1SinrSensor(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the Signal to Interference plus Noise Ratio (SINR) of SCC2.
    SINR measures the quality of the received signal relative to interference and noise.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "SCC2 SINR",
            "askey_scc2_sinr",
            "mdi:signal",
            "sinr",
            "dB",
        )

    @property
    def native_value(self):
        try:
            return float(self.coordinator.data["cellular_info_ex"]["data"][2]["sinr"])
        except (KeyError, IndexError, TypeError, ValueError):
            return None

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Signal to Interference plus Noise Ratio (SINR) of SCC2. Measures the quality of the signal relative to interference and noise.",
            "Unit": "dB",
        }


class AskeyScc1BandSensor(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the cellular frequency band of SCC2.
    The band determines the frequency range for communication.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator, "SCC2 Band", "askey_scc2_band", "mdi:network", "band"
        )

    @property
    def native_value(self):
        try:
            return self.coordinator.data["cellular_info_ex"]["data"][2]["band"]
        except (KeyError, IndexError, TypeError):
            return None

    @property
    def extra_state_attributes(self):
        return {"Description": "Cellular frequency band of SCC2.", "Unit": "None"}


class AskeyScc1BandwSensor(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the bandwidth (in MHz) of SCC2.
    The bandwidth indicates the width of the frequency band used for communication.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "SCC2 Bandwidth",
            "askey_scc2_bandw",
            "mdi:network",
            "bandw",
            "MHz",
        )

    @property
    def native_value(self):
        try:
            return float(self.coordinator.data["cellular_info_ex"]["data"][2]["bandw"])
        except (KeyError, IndexError, TypeError, ValueError):
            return None

    @property
    def extra_state_attributes(self):
        return {"Description": "Bandwidth of SCC2 in megahertz (MHz).", "Unit": "MHz"}


class AskeyScc1RxchSensor(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the receive channel (RX) of SCC2.
    This channel is used for receiving data in the network.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "SCC2 RX Channel",
            "askey_scc2_rxch",
            "mdi:radio-tower",
            "rxch",
        )

    @property
    def native_value(self):
        try:
            return self.coordinator.data["cellular_info_ex"]["data"][2]["rxch"]
        except (KeyError, IndexError, TypeError):
            return None

    @property
    def extra_state_attributes(self):
        return {"Description": "Receive Channel for SCC2.", "Unit": "None"}


class AskeyScc1TxchSensor(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the transmit channel (TX) of SCC2.
    This channel is used for sending data to the network.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "SCC2 TX Channel",
            "askey_scc2_txch",
            "mdi:radio-tower",
            "txch",
        )

    @property
    def native_value(self):
        try:
            return self.coordinator.data["cellular_info_ex"]["data"][2]["txch"]
        except (KeyError, IndexError, TypeError):
            return None

    @property
    def extra_state_attributes(self):
        return {"Description": "Transmit Channel for SCC2.", "Unit": "None"}


class AskeyScc1RxfreqSensor(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the receive frequency (RX) of SCC2 in megahertz (MHz).
    This frequency is used for receiving signals from the network.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "SCC2 RX Freq",
            "askey_scc2_rxfreq",
            "mdi:radio-tower",
            "rxfreq",
            "MHz",
        )

    @property
    def native_value(self):
        try:
            return float(self.coordinator.data["cellular_info_ex"]["data"][2]["rxfreq"])
        except (KeyError, IndexError, TypeError, ValueError):
            return None

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Receive Frequency for SCC2 in megahertz (MHz).",
            "Unit": "MHz",
        }


class AskeyScc1TxfreqSensor(AskeyBaseSensorDiagnostic):
    """
    Sensor for monitoring the transmit frequency (TX) of SCC2 in megahertz (MHz).
    This frequency is used for transmitting signals to the network.
    """

    def __init__(self, coordinator):
        super().__init__(
            coordinator,
            "SCC2 TX Freq",
            "askey_scc2_txfreq",
            "mdi:radio-tower",
            "txfreq",
            "MHz",
        )

    @property
    def native_value(self):
        try:
            return float(self.coordinator.data["cellular_info_ex"]["data"][2]["txfreq"])
        except (KeyError, IndexError, TypeError, ValueError):
            return None

    @property
    def extra_state_attributes(self):
        return {
            "Description": "Transmit Frequency for SCC2 in megahertz (MHz).",
            "Unit": "MHz",
        }
