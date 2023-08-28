import cv2
import mediapipe as mp
from mouse import move_mouse, click_mouse

# Initialize Mediapipe Hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Set up camera capture
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# Set the cursor movement speed factor (adjust as needed)
cursor_speed = 2.0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    # Convert the image to RGB and process it using Mediapipe
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    click_detected = False

    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            # Get the coordinates of index, middle, and thumb fingers
            index_tip = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            middle_tip = landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
            thumb_tip = landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]

            # Calculate the distance between fingers
            index_thumb_distance = ((index_tip.x - thumb_tip.x)**2 + (index_tip.y - thumb_tip.y)**2)**0.5
            index_middle_distance = ((index_tip.x - middle_tip.x)**2 + (index_tip.y - middle_tip.y)**2)**0.5
            
            # If fingers touch, set click_detected to True
            if index_thumb_distance < 0.02 and index_middle_distance < 0.02:
                click_detected = True

            # If the distance is small (pinch gesture), move the mouse cursor
            if not click_detected:
                # Calculate the movement vector
                dx = thumb_tip.x - index_tip.x
                dy = thumb_tip.y - index_tip.y

                # Scale the movement vector for faster movement
                dx *= cursor_speed
                dy *= cursor_speed

                # Map normalized coordinates to screen dimensions
                move_mouse(thumb_tip.x + dx, thumb_tip.y + dy)
                
                # Clear any previous click detection text
                cv2.putText(frame, "", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # Display "Click Detected!" text on the screen if click is detected
        if click_detected:
            cv2.putText(frame, "Click Detected!", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            click_mouse()

    cv2.imshow("Pinch Gesture Mouse Control", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
