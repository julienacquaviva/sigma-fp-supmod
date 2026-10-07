# Changelog

Public releases only. Build numbers in between were test builds on the author's card.

## R168 (2026-10-08)

- **Fixed: a bright line at 23.976 fps.** With a shutter faster than about 1/40, one row of every 23.976 frame was exposed for a whole frame instead of the shutter time and showed as a bright horizontal line on bright areas. The 23.976 and 59.94 timings now use the same frame layout as Sigma's own firmware. Frame rate and rolling shutter are unchanged. 24, 25, 29.97 and the other rates were not affected.
- **MEDIA is now DATA.** The Quick Set tile shows the estimated data rate in the colour of the target, with FAST (SSD), REGULAR (v90), MEDIUM (v60) or SLOW (v30) underneath. Record Settings shows the same, for example `369MB/s (FAST)`. The Custom QS editor follows.

## R166 (2026-10-07)

**Known fault, fixed in R168:** a bright line across the frame at 23.976 fps with shutters faster than about 1/40.


A new way to choose what you record. The six named modes of R120 are replaced by four settings that work together.

- **Ratio**: 3:2, 16:9, 2:1.
- **Crop**: 1.0x to 2.8x in steps of 0.1, per ratio.
- **Frame rate**: 23.976 to 100, and 119.88 in 2:1. A dedicated 48 fps sensor mode; the widest possible sensor areas at 48, 50 and 59.94.
- **Media**: SSD, v90, v60, v30. A data-rate budget; the mod records the largest frame that fits.
- One rule set: the frame rate wins, the crop follows; lists stop at their ends.
- Quick Set redesigned: SENSOR, RATIO, FPS, CROP, OUTPUT, MEDIA, RS, IRIS, over one even 50 % shade.
- MENU › Record Settings is one page with the same six values, edited in place with either dial.
- Top bar shows the crop factor and the ratio.
- Custom QS editor lists the new tiles.
- Lossless compression is always on. 12-bit only: the 14-bit option and the uncompressed switch are gone.

## R120 (2026-10-02)

First public release.

- Six modes: UHD, XQ, HQ, MQ, LQ, S16.
- 12 / 14-bit choice (14-bit in UHD with DC Crop and in S16).
- Lossless compression as a switch (DATA- / DATA+).
- Gyro data in every DNG frame.
- STILL mode native in features.
