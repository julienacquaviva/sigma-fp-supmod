**R181, test build** for the Sigma fp, firmware 5.02 (not the fp L). RAM only: nothing is flashed.

**Not confirmed on a camera yet.** R168 stays the recommended build until this one is. R181 replaces the test build R179, whose fix did not take effect.

R181 is R168 plus two things:

- **Shutter angle fixed.** With the shutter set as an angle, 23.976, 24, 25 and 48 fps used the wrong shutter time (180° gave 1/60 at 24 and 25 fps, 1/100 at 48), and a half-press of the shutter button during a take made the exposure jump to the right one. The angle is now converted with the real frame rate, in live view and in clips: 180° gives 1/48, 1/48, 1/50 and 1/96, and a half-press changes nothing. Expect the picture to be about 20 to 25 % brighter than before at 24 and 25 fps in angle mode: that is the correct exposure. Shutter speed mode and the other frame rates are unchanged.
- **In-camera playback of the mod's clips.** Clips now show as a picture in their own shape instead of noise, with pause and frame step. Frames that are stored compressed are skipped (the last good frame is held), so clips recorded to an SSD play at about half their frame rate and clips recorded to a card show their first frame only. While a clip plays the overlay is hidden; it returns on pause. The single view shows the clip's real resolution.

To test the angle fix: shutter angle 180°, record a few seconds at 25, 24 or 23.976 and at 48 fps, and half-press the shutter button a few times during the take. The brightness should not change.

**Install:** unzip, copy `FPOG.BIN`, `AutoRun.txt` and `BOOT.BIN` to the root of the SD card, boot in CINE and wait for the crop factor and ratio in the top bar.
**Uninstall:** delete the three files.

Unofficial, no warranty; see the fine print in the [README](https://github.com/julienacquaviva/sigma-fp-supmod).
