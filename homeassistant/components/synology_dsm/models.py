"""The synology_dsm integration models."""
from __future__ import annotations

from dataclasses import dataclass

from .common import SynoApi
from .coordinator import (
    SynologyDSMCameraUpdateCoordinator,
    SynologyDSMCentralUpdateCoordinator,
    SynologyDSMDownloadStationUpdateCoordinator,
    SynologyDSMSwitchUpdateCoordinator,
)


@dataclass
class SynologyDSMData:
    """Data for the synology_dsm integration."""

    api: SynoApi
    coordinator_central: SynologyDSMCentralUpdateCoordinator
    coordinator_cameras: SynologyDSMCameraUpdateCoordinator | None
    coordinator_downloads: SynologyDSMDownloadStationUpdateCoordinator | None
    coordinator_switches: SynologyDSMSwitchUpdateCoordinator | None
