# sigma-fp-supmod 🎬

**A RAM-only CinemaDNG mod for the Sigma fp.** Three files on the SD card, loaded at boot, gone when you take the card out.

Nothing is flashed. Nothing is written to the camera. Pull the card and your fp is exactly the camera Sigma shipped. Put it back and the fp wakes up with open-gate modes, 14-bit raw, lossless compression, gyro data in every frame and a tidier Quick Set screen.

| | |
|---|---|
| **Release** | R120 (build number 120; yes, there were 119 before it) |
| **Camera** | Sigma fp, firmware **5.02**. Not the fp L. |
| **Status** | Personal project. Built for and tested on one fp body, by its owner. It works on that one. |
| **For whom** | People who shoot CinemaDNG on an fp, read changelogs for fun and own a spare battery. |

> ⚠️ Unofficial. Not affiliated with, endorsed by or supported by SIGMA. No warranty of any kind. You use it at your own risk; see [the fine print](#the-fine-print).

---

## 🙏 Standing on shoulders

This mod exists because other people did the hard part first.

- **Bei (ijigen)** and the **[fpSup](https://github.com/ijigen/fpSup)** project: the open-gate research, the sensor-mode metadata, the gyro logger, the tools. Much of what this mod knows about the fp, it learned from there.
- **Vitaly** and his **FP3K** mod, which showed that a 3K open-gate fp was a real thing and not a daydream.
- The **fpSup Discord community** (reachable through the fpSup project): testers, test reports, sample clips, patient answers.

Thank you. This project is a separate implementation and none of the people above have reviewed or endorsed it; if it misbehaves, that is on this repo, not on them.

---

## 📦 Install

1. Download the three files from [`release/R120`](release/R120): `FPOG.BIN`, `AutoRun.txt`, `BOOT.BIN`. Check them against `SHA256SUMS.txt` if you like your bits verified.
2. Copy them to the **root of the SD card**.
3. Put the card in, switch the camera on, switch to CINE.
4. Wait a few seconds until the **purple mode name** (UHD, XQ, HQ, MQ, LQ or S16) appears in the top bar. That is the mod saying hello.

**Uninstall:** delete the three files, or use another card.
**If anything looks wrong:** switch off, pull the battery, boot without the card. The camera is stock again.

---

## 🎞️ Recording modes

CINE records **CinemaDNG only** while the mod runs. Six modes, picked on the RES tile or in Record Settings.

| Mode | 12bit | $\color{#a371f7}{\textsf{14bit}}$ | DC crop | Resolution | Ratio | Scaling | Max FPS | Crop vs full readout | Rolling shutter | Lossless compression (DATA-) at 23.976 | Uncompressed (DATA+) at 23.976 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **UHD** | ✓ | $\color{#a371f7}{\checkmark}$ $\color{#a371f7}{\textsf{(DC}}$ $\color{#a371f7}{\textsf{only)}}$ | ✓ | 3840x2160 | 16:9 | ISP | 29.97, $\color{#a371f7}{\textsf{14bit}}$ $\color{#a371f7}{\textsf{23.976}}$ | 1.0, DC 1.5 | 21.0 ms, DC 13.4 ms, $\color{#a371f7}{\textsf{DC}}$ $\color{#a371f7}{\textsf{14bit}}$ $\color{#a371f7}{\textsf{27.5}}$ $\color{#a371f7}{\textsf{ms}}$ | 220 MB/s | 303 MB/s, $\color{#a371f7}{\textsf{14bit}}$ $\color{#a371f7}{\textsf{353}}$ $\color{#a371f7}{\textsf{MB/s}}$ |
| **XQ** | ✓ | | ✓ | 3840x2560 | 3:2 | ISP | 29.97 | 1.0, DC 1.5 | 24.8 ms, DC 15.9 ms | 274 MB/s | 358 MB/s |
| **HQ** | ✓ | | ✓ | 3240x2160 | 3:2 | ISP | 29.97 | 1.0, DC 1.5 | 24.8 ms, DC 15.9 ms | 172 MB/s | 257 MB/s |
| **MQ** | ✓ | | | 3000x2000 | 3:2 | 2x2 | 50 | 1.0 | 12.4 ms | 134 MB/s | 221 MB/s |
| **LQ** | ✓ | | | 2000x1334 | 3:2 | 3x3 | 119.88 | 1.0 | 8.3 ms | 52 MB/s | 99 MB/s |
| **S16** | ✓ | $\color{#a371f7}{\checkmark}$ | | 2160x1440 | 3:2 | Full readout | 29.97, $\color{#a371f7}{\textsf{14bit}}$ $\color{#a371f7}{\textsf{23.976}}$ | 2.8 | 9.0 ms, $\color{#a371f7}{\textsf{14bit}}$ $\color{#a371f7}{\textsf{18.3}}$ $\color{#a371f7}{\textsf{ms}}$ | 61 MB/s | 115 MB/s, $\color{#a371f7}{\textsf{14bit}}$ $\color{#a371f7}{\textsf{134}}$ $\color{#a371f7}{\textsf{MB/s}}$ |

Purple = 14-bit.

A few footnotes for the curious:

- Frame rates below the maximum: 23.976, 24, 25 and 29.97 everywhere; MQ adds 48 and 50; LQ adds 48, 50, 59.94, 100 and 119.88.
- The rolling shutter is a hair longer at 25p in UHD and S16 (21.2 / 13.6 / 9.1 ms) and shorter at the top of LQ (7.4 ms at 100p, 6.2 ms at 119.88p).
- The MB/s figures are what the DATA tile shows: an estimate from the frame size, the frame rate and how many frames the encoder can compress. Your scene decides the real number.

---

## ✨ What the mod adds

| Feature | What you get |
|---|---|
| **Open-gate and crop modes** | XQ, HQ, MQ and LQ use the full 3:2 sensor; S16 is a 1:1 pixel window from the centre; UHD is still UHD. |
| **14-bit raw** | A 12bit / 14bit choice. Available in **UHD with DC Crop** and in **S16**. It locks the frame rate to **23.976** and records uncompressed. |
| **Lossless compression** | The camera's own hardware lossless-JPEG encoder, applied to 12-bit frames. **DATA-** = compression on, **DATA+** = off. A compressed frame is roughly half the size. |
| **Gyro in every frame** | Each DNG carries its own slice of gyro samples (block "FPG2", about 2.5 kHz, three axes) in the unused tail of the MakerNote. No sidecar file, no length limit. The block also stores the readout time and the exposure time of the frame, so a reader can line samples up with the picture. |
| **Per-mode frame-rate memory** | Each mode remembers its own frame rate. Go to LQ for 100p, come back to XQ, and XQ is still at 24. |
| **No more sideways clips** | Movie DNGs no longer copy the orientation tag, so a tilted camera does not give you a clip that opens rotated. |
| **Fast boot** | A tiny first-stage loader brings the mod up in about 6 seconds after power-on. |
| **STILL mode stays native** | In STILL the mod steps aside: stock battery icon, stock menus, no mod polling. Switch back to CINE and everything is there again. |

### How the compression behaves

The encoder is real hardware with a real speed limit, so compression is **per frame**: the camera compresses as many frames as the encoder can take and writes the rest uncompressed. Both kinds are ordinary DNG frames in the same clip.

| Mode | Frames per second the DATA tile assumes the encoder keeps up with |
|---|---|
| XQ | 12 |
| UHD | 14 |
| HQ | 17 |
| MQ | 20 |
| S16 | 35 |
| LQ | 41 |

So S16 and LQ at 24p are fully compressed, while XQ at 24p is about half and half.

---

## 🖥️ What changed on screen

### Quick Set (QS) menu

- **RES tile:** now picks the mode (UHD / XQ / HQ / MQ / LQ / S16), with the resolution shown underneath.
- **FPS tile:** frame rate is remembered per mode; unavailable rates are greyed (14-bit locks it to 23.976).
- **Format tile:** shows `cDNG`, `12bit` or `14bit`, and the rolling shutter in ms for the current mode.
- **DATA tile:** replaces Headphone Volume. It shows the estimated MB/s and switches between DATA- (lossless compression) and DATA+ (uncompressed); in 14-bit it is DATA+ only.
- **DC Crop tile:** greyed and locked Off in MQ, LQ and S16.
- **Director's Viewfinder:** greyed in CINE (it would force MOV; it works as usual in STILL).

### Record Settings menu

- Resolution list shows the new mode names.
- CinemaDNG only in CINE, in every mode including UHD (MOV is locked).
- New Bit Depth row (12 / 14) and a Lossless Compression row.
- Time left and clip limit account for compression.

### Live view

- Top bar shows the mode name in purple (it also signals the mod is loaded), and battery as a percentage. CINE only: STILL keeps the stock battery icon.
- STBY / REC text is hidden.
- 3:2 modes get a 3:2 live view and a fitted HDMI display.
- S16 shows the true 1:1 crop in standby, including during AF.

### Custom Buttons Functions menu

- DC Crop is now an assignable function in CINE mode. It replaces HDR in the list and is labelled "DC Crop", so any custom button (MODE, for example) can toggle it. In STILL the entry is HDR as always.

### Custom QS editor

- Adds a "DT / Data Rate" entry so the DATA tile can be placed in your own layout.
- The editor's preview shows nothing under RES. and DT (the live values only exist on the real QS screen), and the function strip uses the stock icons for everything else.

---

## 🧱 Known limits (the honest list)

- **If the camera itself aborts a take** (write buffer full, card too slow) with compression on, the last frames that were still in the encoder can be lost, leaving gaps in the frame numbers near the end. A normal stop with the REC button is fine.
- **MQ at 50p sits at the edge** of what an SSD takes. On the author's drive it ran about 43 seconds at roughly 339 MB/s before the camera stopped. Lower frame rates are comfortable.
- **14-bit is 23.976 only**, uncompressed, and only in UHD with DC Crop and in S16.
- **Wait for the purple name** after power-on before you start recording. Until then the camera is still stock.
- **STILL is native in features, not in every byte.** The mod stays in memory, and the black-level clamp settings of a few sensor modes that stills share with the mod (12-bit stills at LOW size or with DC Crop, the fast AF live view) are the mod's values. No visible effect was reported; it is listed because you would want to know.
- **Gyro axis signs:** pan and tilt are confirmed, the roll sign is not.
- **MOV is not available in CINE** while the mod is loaded. That is a design choice, and also a limit.
- Tested on one camera, one firmware (5.02), a handful of lenses and one SSD. Yours may find something new. 🙂

---

## 🔧 How it was made

- **Reverse engineering** of the stock firmware, one function at a time, mostly to find the place where the camera already does what you want and politely ask it to do it for another mode.
- **Emulation-based verification.** Every build runs a chain of verifiers that execute the patched code in an emulator against fixtures of the camera's state: thousands of cases for the menus, the Quick Set logic, the recorder, the gyro block, the battery icon. A build goes on the card only when the whole chain passes.
- **Small steps.** 120 builds, each changing one thing, each with a written change note and a camera test list. Several were built, tested and thrown away. That is what the numbers are for.
- Development from build 46 onwards was done with an AI coding assistant (Claude) doing the analysis, code and verification under the owner's direction, and the owner doing what no emulator can: pointing a camera at things.

### Milestones

| Build | What happened |
|---|---|
| R46 | Open-gate profiles on a common core; the black-level clamp fix for the open-gate sensor modes |
| R52 | In-camera lossless compression with the hardware encoder |
| R55 | Frame-rate ceilings per mode (MQ to 50, LQ to 119.88) |
| R64 | "cDNG Lossless Compression" as a setting |
| R71 | DATA tile with live MB/s |
| R87 | Fast boot: about 6 seconds to a ready mod |
| R88 | Mode names UHD / XQ / HQ / MQ / LQ and per-mode frame-rate memory |
| R89 | Purple mode name in the live-view top bar |
| R90 | DC Crop locked off in MQ and LQ |
| R97 | 14-bit CinemaDNG with the right black level |
| R99 | S16 mode, 14-bit as a user choice, CinemaDNG only |
| R100 | Quick Set made consistent; readout time on the cDNG tile |
| R104 | S16 as a 2160 x 1440 window; orientation tag dropped for movie DNGs |
| R112 | Gyro data inside every DNG frame |
| R113 | No frame lost when recording stops during compression |
| R116 | Gyro sync from the exposure time of each frame |
| R117 | Custom QS editor shows the right icons again |
| R119 | Director's Viewfinder greyed in CINE |
| **R120** | STILL mode native in features. **This release.** |

---

## 🎨 Companion plugin

A DaVinci Resolve OFX plugin that develops these DNGs and stabilises them from the in-frame gyro data exists and is in use. It is **not published yet**.

---

## The fine print

This is an unofficial modification made by a hobbyist. It is **not affiliated with, authorised by or supported by SIGMA Corporation**; "SIGMA" and "fp" are their trademarks. It does not include Sigma's firmware: the files are a set of patches that are applied in the camera's memory at boot. It is provided **as is, without warranty of any kind**. Using it may void your warranty, lose your footage or ruin your day. Test before you shoot anything that matters, and keep a card without the mod in your pocket.
