

# Hand Gesture Mouse Control

This Python script uses the Mediapipe library to control the mouse cursor using hand gestures. The script detects pinch gesture between the thumb and index finger and moves the mouse cursor accordingly. Additionally, the script can register clicks by touching the middle finger to the index finger. A debouncing mechanism is implemented to prevent multiple clicks in a short period of time.

## Prerequisites

- Python 3.7+
- OpenCV (`pip install opencv-python`)
- Mediapipe (`pip install mediapipe`)
- `mouse` module (provided)

## Usage

1. Clone the repository:

```

   git clone https://github.com/your-username/hand-gesture-mouse-control.git

```

2. Navigate to the project directory:

```

   cd hand-gesture-mouse-control

```

3. Run the script:

```

   python main.py

```

4. Place your hand in front of the camera and make pinch gestures between your thumb and index finger to control the mouse cursor. Touching your middle finger to the index finger will register a left mouse click. The cursor movement speed and click interval can be adjusted in the script.

5. Press 'q' to quit the script.

## Customization

- You can adjust the `cursor_speed` variable in the script to control the speed of mouse cursor movement.
- You can change the `click_interval` variable to set the minimum time between clicks to prevent rapid multiple clicks.

## Acknowledgments

This project is inspired by the potential applications of hand gesture recognition using computer vision. It uses the Mediapipe library, developed by Google, for hand tracking.

## License

This project is licensed under the [MIT License](LICENSE).
