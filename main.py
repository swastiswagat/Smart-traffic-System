from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")
cap = cv2.VideoCapture('./night_traffic2.mp4')
vehicle_classes = [2, 3, 5, 7]

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    height, width, _ = frame.shape
    direction_counts = {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0}

    results = model(frame, stream=True, verbose=False)

    for r in results:
        boxes = r.boxes
        for box in boxes:
            cls_id = int(box.cls[0])
            if cls_id in vehicle_classes:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                center_x = (x1 + x2) // 2
                center_y = (y1 + y2) // 2

                if center_x < width/2 and center_y < height/2:
                    direction_counts["WEST"] += 1
                elif center_x < width/2 and center_y > height/2:
                    direction_counts["SOUTH"] += 1
                elif center_x > width/2 and center_y < height/2:
                    direction_counts["EAST"] += 1
                else:
                    direction_counts["NORTH"] += 1

    print(f"NORTH:{direction_counts['NORTH']}, SOUTH:{direction_counts['SOUTH']}, EAST:{direction_counts['EAST']}, WEST:{direction_counts['WEST']}")

    cv2.imshow('AI View', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()