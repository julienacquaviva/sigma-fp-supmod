# Changelog

Public releases only. Build numbers in between were test builds on the author's card.

## R166 (2026-10-07)

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
