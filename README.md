# Smart Traffic Management System  

## 📌 Overview  
This project demonstrates an **AI-powered Smart Traffic Management System** designed to improve late-night road safety and reduce traffic collisions. Using **YOLOv8 object detection** and **real-time simulation with Pygame**, the system detects vehicles in traffic footage and dynamically controls traffic signals based on vehicle density.  

The project was presented as part of *Late-Night Safety in Odisha using Machine Learning*.  

## 🚦 Features  
- **AI Vehicle Detection**: Uses YOLOv8 to detect vehicles (cars, trucks, buses, motorcycles) from video footage.  
- **Dynamic Signal Control**: Traffic lights adapt based on real-time vehicle counts in each direction.  
- **Simulation Dashboard**: Pygame visualization of traffic lights and vehicle counts per direction.  
- **Safety-Oriented**: Helps reduce accidents and waiting times, especially during low-traffic hours.  

## 🛠️ Tech Stack  
- **Python**  
- **YOLOv8 (Ultralytics)**  
- **OpenCV** (for video processing)  
- **Pygame** (for traffic light simulation)  
- **Regex + Subprocess** (for AI ↔ simulation communication)  

## 📂 Key Files  
- `main.py` → Runs YOLOv8 object detection on traffic video and outputs vehicle counts per direction.  
- `simulation.py` → Pygame-based traffic simulation that dynamically switches signals based on AI output.  
- `night_traffic.mp4` → Sample traffic video used for detection.  
- `yolov8n.pt` → Pre-trained YOLOv8 model weights.  
- `Smart_Traffic_Final.pptx` → Project presentation.  

## ▶️ How to Run  
1. Install dependencies:  
   ```bash
   pip install ultralytics opencv-python pygame
2. Run the simulation:
   ```bash
   python simulation.py
3. Press q in the OpenCV window to stop detection.

## 📊 Working

1. main.py detects vehicles in night_traffic.mp4 and outputs counts (NORTH, SOUTH, EAST, WEST).

2. simulation.py reads AI outputs, adjusts green signal time, and updates visualization.

3. The system ensures the busiest direction gets priority, reducing waiting time and risks.
## 👨‍💻 Contributors  

<a href="https://github.com/swastiswagat">
  <img src="https://github.com/swastiswagat.png" width="80" style="border-radius:50%">
</a>
<a href="https://github.com/AyushAshutosh">
  <img src="https://github.com/AyushAshutosh.png" width="80" style="border-radius:50%">
</a>
<a href="https://github.com/Satya-suvam07">
  <img src="https://github.com/Satya-suvam07.png" width="80" style="border-radius:50%">
</a>
<a href="https://github.com/smruti264">
  <img src="https://github.com/smruti264.png" width="80" style="border-radius:50%">
</a>

