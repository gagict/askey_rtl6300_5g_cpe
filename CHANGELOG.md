# Changelog

## 1.2.1 (fork)

Fork of [cretudorin/askey_rtl6300_5g_cpe](https://github.com/cretudorin/askey_rtl6300_5g_cpe) (v1.2.0).
All credit for the original integration goes to its author.

### Fixed

- **`sensors/traffic.py`** — the modem reports monthly traffic as strings with a unit
  (`"8.26MB"`, `"694.38KB"`), which made the sensors raise
  `could not convert string to float` every poll. Added `_to_gb()` which converts
  TB / GB / MB / KB / B (and plain numbers) to gigabytes.
- **`sensors/pcc_cell_info.py`** — `AskeyPccBandSensor` and `AskeyPccBandwSensor`
  computed the value but never returned it, so `PCC Band` / `PCC Bandwidth` always
  showed `unknown`.

### Notes

- The upstream `manifest.json` in the `v1.2.0` tag still said `1.1.0`; this fork
  bumps it to `1.2.1` so HACS sees the fix as an update.
