# Hand Gesture Control Mouse

Control your computer's mouse, volume, and brightness entirely with hand gestures — no physical input device needed. Built with MediaPipe for real-time hand tracking and OpenCV for camera processing.

This project extends the original [Hand-Gesture-Recognition-for-Cursor-Controlling](https://github.com/ahmed-0egy/Hand-Gesture-Recognition-for-Cursor-Controlling) with additional features including on-screen gesture labels, FPS display, screenshot capture, system volume control, and screen brightness control.

---

## Features

- **Real-time hand tracking** using MediaPipe
- **Mouse control** — move, click, right-click, double-click, drag
- **Scroll and zoom** — scroll up/down, zoom in/out
- **Screenshot capture** — save a screenshot with a gesture
- **Volume control** — raise or lower system volume hands-free
- **Brightness control** — adjust screen brightness with your hand
- **On-screen FPS counter** — live performance display
- **On-screen gesture label** — shows the active gesture in real time

---

## Gesture Reference

| Gesture | Action |
|---|---|
| Move hand naturally | Move cursor |
| All fingers up, thumb down | Freeze cursor |
| Index finger into thumb | Left click |
| Middle finger into thumb | Right click |
| Ring finger into thumb | Double click |
| All fingers down | Drag |
| Little finger up only (thumb down) | Scroll up |
| Index finger up only | Scroll down |
| Index + middle up, spread apart | Zoom in |
| Index + middle up, pinched together | Zoom out |
| Little finger up, thumb down | Screenshot |
| Index + thumb up, hand raised | Volume up |
| Index + thumb up, hand lowered | Volume down |
| Index + middle up, thumb down | Brightness control (raise = brighter) |

---

## Requirements

- Python 3.10
- Webcam

---

## Installation

```bash
git clone https://github.com/ajmalsadhiq/handgesture-control-mouse.git
cd handgesture-control-mouse
pip install -r requirements.txt
```

---

## Usage

```bash
python app.py
```

- A window will open showing your webcam feed with hand landmarks drawn
- The current gesture and FPS are displayed in the top-left corner
- Press **ESC** to quit

Screenshots are saved to the project folder as `screenshot_<timestamp>.png`.

---

## Dependencies

| Package | Purpose |
|---|---|
| `mediapipe` | Hand landmark detection |
| `opencv-python` | Camera feed and display |
| `pyautogui` | Mouse and keyboard control |
| `screen-brightness-control` | Screen brightness adjustment |

---

## Project Structure

```
handgesture-control-mouse/
├── app.py              # Main loop — camera, MediaPipe, display
├── controller.py       # All gesture detection and system control logic
├── requirements.txt    # Python dependencies
└── README.md
```

---

## Notes

- Works on **Windows only** (volume control uses Windows media keys via PyAutoGUI)
- Brightness control may require running as administrator on some systems
- For best results, use in a well-lit environment with a plain background
- Keep your hand within the camera frame at all times

---

## Acknowledgements

Original project by [ahmed-0egy](https://github.com/ahmed-0egy/Hand-Gesture-Recognition-for-Cursor-Controlling). This fork adds gesture labelling, FPS counter, screenshot, volume, and brightness control features.