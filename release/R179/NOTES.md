**R179, test build** for the Sigma fp, firmware 5.02 (not the fp L). RAM only: nothing is flashed.

**Not tested on a camera yet.** R168 stays the recommended build until this one is confirmed.

R179 is R168 plus one fix:

- **Fixed: exposure step at the start of a clip in shutter angle mode.** With the shutter set as an angle, a clip could start at the wrong shutter time and jump to the right one after a second or two (seen at 25 fps, 180°: 1/60 for the first 42 frames, then 1/50). The angle is now applied from the first frame, as a shutter speed already was.

To test: shutter angle 180°, record a few seconds at 23.976, 24, 25 and 29.97, and check that the brightness does not change during the first two seconds. Shutter speed mode should behave as in R168.

**Install:** unzip, copy `FPOG.BIN`, `AutoRun.txt` and `BOOT.BIN` to the root of the SD card, boot in CINE and wait for the crop factor and ratio in the top bar.
**Uninstall:** delete the three files.

Unofficial, no warranty; see the fine print in the [README](https://github.com/julienacquaviva/sigma-fp-supmod).
