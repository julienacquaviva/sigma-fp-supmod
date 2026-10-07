**R168** for the Sigma fp, firmware 5.02 (not the fp L). RAM only: nothing is flashed.

**Replaces R166.** What changed:

- **Fixed: a bright line at 23.976 fps.** In R166, with a shutter faster than about 1/40, every 23.976 frame had one bright horizontal line on bright areas. If you shot 23.976 with R166, check your footage. 24, 25, 29.97 and the other rates were not affected.
- **MEDIA is now DATA:** the tile shows the estimated data rate, with FAST (SSD), REGULAR (v90), MEDIUM (v60) or SLOW (v30) underneath.

CINE is a raw configurator: **ratio** (3:2, 16:9, 2:1) × **crop** (1.0x to 2.8x) × **frame rate** (23.976 to 119.88) × **data target**, always lossless-compressed 12-bit CinemaDNG, with gyro data in every frame. Every mode is listed in the [README](https://github.com/julienacquaviva/sigma-fp-supmod#-every-mode); the full list of changes is in the [changelog](https://github.com/julienacquaviva/sigma-fp-supmod/blob/main/docs/CHANGELOG.md).

**Install:** unzip, copy `FPOG.BIN`, `AutoRun.txt` and `BOOT.BIN` to the root of the SD card, boot in CINE and wait for the crop factor and ratio in the top bar.
**Uninstall:** delete the three files.

Unofficial, no warranty; see the fine print in the README.
