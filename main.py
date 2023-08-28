import cv2
import mediapipe as mp
from mouse import move_mouse, click_mouse
import time

# Initialize Mediapipe Hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Set up camera capture
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# Set the cursor movement speed factor (adjust as needed)
cursor_speed = 2.0

# Click debounce settings
click_interval = 1.0  # Minimum time between clicks (in seconds)
last_click_time = time.time()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    # Convert the image to RGB and process it using Mediapipe
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            # Get the coordinates of thumb and index finger
            thumb_tip = landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            milddle_tip = landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
            
            # Calculate the distance between thumb and index finger tips
            thumb_index_distance = ((thumb_tip.x - index_tip.x)**2 + (thumb_tip.y - index_tip.y)**2)**0.5
            index_middle_distance = ((index_tip.x - milddle_tip.x)**2 + (index_tip.y - milddle_tip.y)**2)**0.5

            # If the distance is small (pinch gesture), move the mouse cursor
            if thumb_index_distance  < 0.05:
                # Calculate the movement vector
                dx = thumb_tip.x - index_tip.x
                dy = thumb_tip.y - index_tip.y

                # Scale the movement vector for faster movement
                dx *= cursor_speed
                dy *= cursor_speed

                # Map normalized coordinates to screen dimensions
                move_mouse(thumb_tip.x + dx, thumb_tip.y + dy)
            
                # Registering a click if middle finger touches the index finger
                if index_middle_distance < 0.05:
                    # Check if enough time has passed since the last click
                    current_time = time.time()
                    if current_time - last_click_time >= click_interval:
                        # Click the left button
                        # click_mouse()
                        print("Click")
                        last_click_time = current_time
                        

    cv2.imshow("Pinch Gesture Mouse Control", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
