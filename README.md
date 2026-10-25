English | [Türkçe](README.tr.md)

[![Site check](https://github.com/oguzhanbilir/radMap/actions/workflows/check.yml/badge.svg)](https://github.com/oguzhanbilir/radMap/actions/workflows/check.yml)

# RadMap: drone-based 3D radiation mapping

A Geiger-Müller counter mounted on a drone logs radiation readings with GPS coordinates. The readings are then turned into a 3D map of an area. This repo is the project website, built from the project report.

**Codeavour 7.0** · 3rd in Turkey, team SANKODE Intelligence (Feb 2026) · **Samsung Solve for Tomorrow 2026** · Turkey finalist, team GeigerTim (final on Nov 30, 2026) · **TÜBİTAK 2204-A** · Invited to the Adana regional exhibition

Live site: https://oguzhanbilir.github.io/radMap/

<p align="center">
  <img src="images/drone/dji%20mavic%203%20pro%20ile%20bitmi%C5%9F%20devrenin%20u%C3%A7u%C5%9F%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%201.JPG" width="420" alt="Drone in flight with the measurement circuit attached" />
  <img src="images/drone/dji%20mavic%203%20pro%20modeli%20ile%20devre%20haz%C4%B1r%20hali.JPG" width="420" alt="Measurement circuit mounted on the drone" />
</p>

## How it works

- Arduino Nano reads the Geiger-Müller tube (PCE-RAM10 used as a reference meter), with an OLED display, GPS module and microSD logging
- The board is mounted on a DJI drone and flown over a grid of measurement points
- Logged CPM and µSv/h values are processed in Python and visualised as a 3D map
- Readings were cross-checked indoors, outdoors and against a nuclear medicine reference measurement

## Site pages

| Page | Content |
|------|---------|
| `index.html` | Overview, finished drone, measurement summary, 3D map gallery |
| `malzemeler.html` | Hardware list |
| `proje.html` | Development process in 7 stages |
| `olcum-sonuclari.html` | Background, open area and indoor measurement tables, distance charts |
| `rehberler.html` | Step-by-step guides: Arduino circuit, PictoBlox, Python mapping, 3D mapping |
| `takim.html` | Team |

The site content is in Turkish.

## Running locally

Open `index.html` in a browser. No build step. Colours live in the `:root` variables in `style.css`.

## Credits

Student research project. Advisor and developer of the website: Oğuzhan Bilir.
