# sigma-fp-supmod 🎬

**A RAM-only CinemaDNG mod for the Sigma fp.** Three files on the SD card, loaded at boot, gone when you take the card out.

[![release](https://img.shields.io/github/v/release/julienacquaviva/sigma-fp-supmod)](https://github.com/julienacquaviva/sigma-fp-supmod/releases/latest)
[![downloads](https://img.shields.io/github/downloads/julienacquaviva/sigma-fp-supmod/total)](https://github.com/julienacquaviva/sigma-fp-supmod/releases)
[![camera](https://img.shields.io/badge/Sigma%20fp-firmware%205.02-blue)](#-install)

Nothing is flashed. Nothing is written to the camera. Pull the card and your fp is exactly the camera Sigma shipped. Put it back and CINE becomes a small raw configurator: pick a **ratio**, a **frame rate**, a **crop** and the **media** you record to, and the camera works out the largest lossless-compressed CinemaDNG frame that fits.

| | |
|---|---|
| **Release** | **R166** · [download the zip](../../releases/latest) |
| **Camera** | Sigma fp, firmware **5.02**. Not the fp L. |
| **Status** | Personal project. Built for and tested on one fp body, by its owner. It works on that one. |
| **For whom** | People who shoot CinemaDNG on an fp, read changelogs for fun and own a spare battery. |

> ⚠️ Unofficial. Not affiliated with, endorsed by or supported by SIGMA. No warranty of any kind. You use it at your own risk; see [the fine print](#the-fine-print).

**Contents:** [Install](#-install) · [What you get](#-what-you-get) · [On screen](#️-on-screen) · [Every mode](#-every-mode) · [Known limits](#-known-limits-the-honest-list) · [How it was made](#-how-it-was-made) · [Older releases](#-older-releases)

---

## 🙏 Standing on shoulders

This mod exists because other people did the hard part first.

- **Bei (ijigen)** and the **[fpSup](https://github.com/ijigen/fpSup)** project: the open-gate research, the sensor-mode metadata, the gyro logger, the menu discoveries, the tools. Much of what this mod knows about the fp, it learned from there.
- **Vitaly** and his **FP3K** mod, which showed that a 3K open-gate fp was a real thing and not a daydream.
- The **fpSup Discord community** (reachable through the fpSup project): testers, test reports, sample clips, patient answers.

Thank you. This project is a separate implementation and none of the people above have reviewed or endorsed it; if it misbehaves, that is on this repo, not on them.

---

## 📦 Install

1. Download **`sigma-fp-supmod-R166.zip`** from the [latest release](../../releases/latest) and unzip it. (The same three files are in [`release/R166`](release/R166); check them against `SHA256SUMS.txt` if you like your bits verified.)
2. Copy `FPOG.BIN`, `AutoRun.txt` and `BOOT.BIN` to the **root of the SD card**.
3. Put the card in, switch the camera on, switch to CINE.
4. Wait a few seconds until the **crop factor and the ratio** (for example `1.0x  3:2`) appear in the top bar, next to the clip name. That is the mod saying hello.

**Uninstall:** delete the three files, or use another card.
**If anything looks wrong:** switch off, pull the battery for ten seconds, boot without the card. The camera is stock again.

---

## ✨ What you get

| Feature | What it means |
|---|---|
| **Three ratios** | **3:2** (open gate), **16:9** and **2:1**, each read from the full sensor width. |
| **19 crops per ratio** | From **1.0x** to **2.8x** in steps of 0.1. The crop picks how much of the sensor is read; tighter crops unlock higher frame rates. |
| **Nine frame rates** | 23.976, 24, 25, 29.97, 48, 50, 59.94, 100 and, in 2:1, 119.88. |
| **Four media targets** | **SSD**, **v90**, **v60**, **v30**. Each is a data-rate budget (370 / 195 / 125 / 85 MB/s); the mod records the largest frame that stays under it. Same sensor area, same field of view, smaller file. |
| **Oversampled or 1:1** | Wide crops are scaled down from more sensor pixels than they record; tight crops are recorded pixel for pixel. The screen tells you which. |
| **Lossless compression, always** | The camera's own hardware lossless-JPEG encoder on 12-bit frames. No switch: every mode uses it. |
| **Gyro in every frame** | Each DNG carries its own slice of gyro samples (block "FPG2", about 2.5 kHz, three axes) in the unused tail of the MakerNote, with the readout and exposure time of the frame. No sidecar file, no length limit. |
| **Rolling shutter on screen** | The readout time of the current mode, in milliseconds, on its own tile. |
| **No more sideways clips** | Movie DNGs no longer copy the orientation tag. |
| **Fast boot** | The mod is up about 6 seconds after power-on. |
| **STILL stays native** | In STILL the mod steps aside: stock menus, stock Quick Set, stock battery icon. |

That is **1,552 recording states** (389 on SSD, and nearly as many for each card class), all listed in [Every mode](#-every-mode).

### How the choices work together

The frame rate wins. Whatever you change, the mod keeps the rate you asked for and moves the rest:

- **Change the frame rate:** the crop goes to the widest one that can run it.
- **Change the ratio:** same thing, the widest crop that runs the current rate. (119.88 exists only in 2:1; leaving 2:1 drops it to 100.)
- **Change the crop:** only crops that run the current rate are offered.
- **Change the media:** ratio and rate stay; the crop stays too unless that card class cannot run it.

Nothing wraps around: at the end of a list the dial simply stops.

---

## 🖥️ On screen

### Quick Set

Eight tiles, two rows:

| SENSOR | RATIO | FPS | CROP |
|---|---|---|---|
| **OUTPUT** | **MEDIA** | **RS** | **IRIS** |

- **SENSOR** shows the sensor area being read, in blue. **OUTPUT** shows the recorded frame size in the colour of the media (green SSD, purple v90, orange v60, red v30), or in grey when it is recorded 1:1.
- **RATIO**, **FPS**, **CROP** and **MEDIA** are the four things you set, with either dial.
- **MEDIA** also shows the estimated data rate in MB/s. **RS** shows the rolling shutter in ms.
- The picture stays visible behind the tiles under one even 50 % shade.

### MENU › Record Settings

The same six values on one page: **Sensor** and **Output** to read, **Media**, **Ratio**, **FPS** and **Crop** to set. Up / Down move the cursor; both dials and Left / Right change the value in place; MENU goes back. The page and Quick Set always show the same state.

### Live view

- The top bar shows the **crop factor and the ratio** next to the clip name, and the battery as a percentage.
- The live view is framed in the ratio you record.

### Custom QS editor

The tiles are listed under their new names (SENSOR, RATIO, FPS, CROP, OUTPUT, MEDIA, RS), so you can lay Quick Set out the way you like.

---

## 📋 Every mode

Read a table like this: pick the row of your **crop**, the column of your **frame rate**; the cell is the frame that gets recorded. An empty cell means that crop cannot run that rate. **Bold** = recorded 1:1 (no scaling). The sensor area is what is read before scaling.

The data rates behind these tables are planned for a detailed scene at high ISO, where a frame compresses to about 40 to 47 % of its raw size. Easier scenes come out well below the budget.

{{TABLES}}

¹ At this frame rate a slightly smaller sensor area is read: 4584x3056 for 3:2 1.3x at 50 fps, 6036x4024 for 3:2 1.0x at 29.97 fps on v30.

The tables are generated from [`tools/modes_v45.json`](tools/modes_v45.json) by [`tools/make_readme.py`](tools/make_readme.py).

---

## 🧱 Known limits (the honest list)

- **The media setting is a plan, not a guarantee.** It sizes the frame for a data rate; your card or drive still has to hold that rate. A card class is a minimum write speed (v60 = 60 MB/s), so a busy scene on a slow card can still fill the buffer and stop the take. If it does, pick the next media step down.
- **If the camera itself aborts a take** (write buffer full), the last frames that were still in the encoder can be lost. A normal stop with the REC button is fine.
- **12-bit only.** Earlier releases had a 14-bit option; it is gone in favour of compression everywhere.
- **MOV is not available in CINE** while the mod is loaded. That is a design choice, and also a limit.
- **Wait for the crop factor and ratio in the top bar** after power-on before you record. Until then the camera is still stock.
- **STILL is native in features, not in every byte.** The mod stays in memory, and the black-level clamp settings of a few sensor modes that stills share with the mod are the mod's values. No visible effect was reported; it is listed because you would want to know.
- **Gyro axis signs:** pan and tilt are confirmed, the roll sign is not.
- Tested on one camera, one firmware (5.02), a handful of lenses, one SSD and a couple of SD cards. Yours may find something new. 🙂

---

## 🔧 How it was made

- **Reverse engineering** of the stock firmware, one function at a time, mostly to find the place where the camera already does what you want and politely ask it to do it for another mode.
- **A simulator first.** Every mode in the tables above was worked out in a simulator of the camera's limits (sensor rows, scaler steps, encoder speed, data rate) before it was built, and corrected whenever the camera disagreed.
- **Emulation-based verification.** Every build runs a chain of checks that execute the patched code, and the camera's own menu engine, in an emulator: the dials, the tiles, the menu page, the recorder. Independent checkers have to pass before a build goes on the card.
- **Small steps.** 166 builds, each changing one thing, each with a written change note and a camera test list. Several were built, tested and thrown away. That is what the numbers are for.
- Development from build 46 onwards was done with an AI coding assistant (Claude) doing the analysis, code and verification under the owner's direction, and the owner doing what no emulator can: pointing a camera at things.

### Milestones

| Build | What happened |
|---|---|
| R46 | Open-gate profiles on a common core; the black-level clamp fix for the open-gate sensor modes |
| R52 | In-camera lossless compression with the hardware encoder |
| R87 | Fast boot: about 6 seconds to a ready mod |
| R112 | Gyro data inside every DNG frame |
| R120 | STILL mode native in features. First public release. |
| R131 | Compression fast enough for 2:1 at 50 fps on an SSD |
| R139 | Ratios instead of named modes; the CROP tile |
| R159 | A dedicated 48 fps sensor mode; the widest sensor areas for 48, 50 and 59.94 |
| R162 | The rate wins: ratio, rate and crop follow one rule set |
| R163 | Media targets: SSD, v90, v60, v30 |
| R164 | Record Settings as one page of six values |
| R165 | Custom QS editor shows the new tiles |
| **R166** | Top bar tidied. **This release.** |

---

## 🗂 Older releases

| Release | What it was | Files |
|---|---|---|
| **R120** | Six named modes (UHD, XQ, HQ, MQ, LQ, S16), a 12 / 14-bit choice, compression as a switch | [`release/R120`](release/R120) · [zip](../../releases/tag/R120) |

What changed between builds: [`docs/CHANGELOG.md`](docs/CHANGELOG.md).

---

## 🎨 Companion plugin

**[sigma-fp-raw](https://github.com/julienacquaviva/sigma-fp-raw)**: a DaVinci Resolve OFX plugin that develops these DNGs and stabilises them from the in-frame gyro data.

---

## The fine print

This is an unofficial modification made by a hobbyist. It is **not affiliated with, authorised by or supported by SIGMA Corporation**; "SIGMA" and "fp" are their trademarks. It does not include Sigma's firmware: the files are a set of patches that are applied in the camera's memory at boot. It is provided **as is, without warranty of any kind**. Using it may void your warranty, lose your footage or ruin your day. Test before you shoot anything that matters, and keep a card without the mod in your pocket.
