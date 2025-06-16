🖱️🖐️ VIRTUAL MOUSE USING HAND GESTURE CONTROL

Control your computer mouse with just your hand movements captured via your webcam.  
Built with Python, this project uses MediaPipe, OpenCV, and PyAutoGUI to enable gesture-based interactions like cursor movement, clicking, and dragging — without touching the mouse.

🎬 DEMO

Coming Soon: Add a short GIF or video here to visualize the virtual mouse in action.

🚀 FEATURES

🟢 Real-time hand tracking using MediaPipe  
🟢 Cursor control based on index finger position  
🟢 Pinch-to-click gesture using thumb and index finger  
🟢 Drag-and-drop with sustained pinch gesture  
🟢 Works with any standard webcam

🧠 TECH STACK

🐍 Python  
🎥 OpenCV  
✋ MediaPipe  
🖱️ PyAutoGUI  
📊 NumPy

🛠️ INSTALLATION AND USAGE

1. Clone the Repository  
   git clone https://github.com/your-username/virtual-mouse.git  
   cd virtual-mouse

2. (Optional) Create a Virtual Environment  
   python -m venv venv  
   source venv/bin/activate   (On Windows: venv\Scripts\activate)

3. Install the Required Dependencies  
   pip install -r requirements.txt

4. Run the Application  
   python virtual_mouse.py

✅ Now you're ready to control your mouse virtually.

📁 PROJECT STRUCTURE

virtual-mouse/  
├── handTrackingModule.py      ← Custom hand tracking class using MediaPipe  
├── virtual_mouse.py           ← Main gesture control script  
├── requirements.txt           ← Python dependencies  
└── README.md                  ← This file

⚙️ HOW IT WORKS

🎥 Webcam captures your hand in real-time  
🧠 MediaPipe detects 21 hand landmarks  
👉 Cursor moves when index finger is raised  
🤏 Mouse click is triggered when thumb and index finger pinch  
📦 Drag-and-drop is handled with continuous pinch motion

📌 REQUIREMENTS

✅ Python 3.6 or higher  
✅ A working webcam  
✅ Good lighting for better detection

🤝 CONTRIBUTIONS

Want to contribute?  
You can fork this repo, create a new feature, fix a bug, or suggest improvements. All contributions are welcome.

📄 LICENSE

This project is open-source and available under the MIT License.

💖 Made with passion, Python, and a pinch of creativity.
