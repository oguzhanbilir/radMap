# RadMap — Drone-based 3D Radiation Mapping

Real-time radiation mapping using DJI Avata 2 + Arduino-controlled Geiger-Müller sensor.

🏆 **Winner:** Codeavour 7.0 Track 1 · 3rd in Turkey, 2024

[🔗 Live Site](https://oguzhanbilir.github.io/radMap/) | [📖 Turkish README](README.md)

---

## Overview

RadMap is an autonomous system that maps radiation levels in real-time using a drone-mounted sensor. Data is collected via GPS, visualized in 3D on Google Earth, and validated against lab instruments.

**Use case:** Environmental monitoring, nuclear safety assessment, educational demonstration.

---

## Hardware

| Component | Part | Purpose |
|-----------|------|---------|
| **Drone** | DJI Avata 2 | Autonomous flight + data transmission |
| **Microcontroller** | Arduino Nano | Sensor + GPS + SD card coordination |
| **Detector** | PCE-RAM10 Geiger-Müller | Radiation measurement (cpm, µSv/h) |
| **GPS** | Neo-6M | Geographic coordinates |
| **Display** | 128x64 OLED | Real-time readings |
| **Storage** | SD Card Module | Data logging |

---

## Process

1. **Design** — CAD modeling, 3D printed enclosure
2. **Integration** — Arduino wiring (Geiger, GPS, OLED, SD card)
3. **Flight** — Drone captures radiation + GPS every 2 seconds
4. **Post-Processing** — Python script converts to KML → Google Earth
5. **Validation** — Cross-check with Nuclear Medicine lab measurements

---

## Results

| Environment | Dose Rate |
|-------------|-----------|
| Open field (background) | 0.2 µSv/h |
| Closed area (test) | 1.5 µSv/h |
| Lab validation | ±5% accuracy |

---

## Tech Stack

- **Firmware:** Arduino C
- **Visualization:** JavaScript (Three.js, Cesium.js)
- **Processing:** Python (matplotlib, KML generation)
- **Frontend:** HTML/CSS
- **Data format:** CSV → KML

## Project Structure

```
.
├── firmware/                # Arduino code (Geiger, GPS, OLED, SD)
├── backend/                 # Python data processing + KML generation
├── frontend/                # JavaScript 3D visualization (Three.js)
├── images/                  # Photos: components, drone, measurements
├── docs/                    # Technical report, calibration data
└── README.md (Turkish)
```

## Installation

```bash
git clone https://github.com/oguzhanbilir/radMap.git
cd radMap

# Firmware: upload firmware/ to Arduino Nano via Arduino IDE
# Frontend: open index.html in browser
# Backend: python process_data.py (converts CSV to KML)
```

## Team

- **Neda** — Sensor calibration
- **Günseli** — Arduino integration
- **Ekin** — 3D visualization
- **Mentor:** Oğuzhan Bilir — AP Cybersecurity Educator, Turkey

## Impact

- Real-world environmental monitoring system
- 180+ high school students trained
- Codeavour national competition 3rd place
- Published open source for STEM education

## License

MIT

---

**Live Demo:** [Google Earth Visualization](https://oguzhanbilir.github.io/radMap/)
