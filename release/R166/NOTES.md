**R166** for the Sigma fp, firmware 5.02 (not the fp L). RAM only: nothing is flashed.

CINE becomes a raw configurator: **ratio** (3:2, 16:9, 2:1) × **crop** (1.0x to 2.8x) × **frame rate** (23.976 to 119.88) × **media** (SSD, v90, v60, v30), always lossless-compressed 12-bit CinemaDNG, with gyro data in every frame. Every mode is listed in the [README](https://github.com/julienacquaviva/sigma-fp-supmod#-every-mode); what changed since R120 is in the [changelog](https://github.com/julienacquaviva/sigma-fp-supmod/blob/main/docs/CHANGELOG.md).

**Install:** unzip, copy `FPOG.BIN`, `AutoRun.txt` and `BOOT.BIN` to the root of the SD card, boot in CINE and wait for the crop factor and ratio in the top bar.
**Uninstall:** delete the three files.

Unofficial, no warranty; see the fine print in the README.
