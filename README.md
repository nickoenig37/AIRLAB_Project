# Information about using project


## Setup Guide For The Project
- Follow these steps starting from within your ros2_ws 
```bash
cd ~/ros2_ws/src
```
- Clone the repository for ROS2 Mediapipe Packages
```bash
git clone https://github.com/nickoenig37/ROS2_MediaPipe_D435.git
```
- Clone the repository for the Realsense D435 in ROS2
```bash
git clone https://github.com/IntelRealSense/realsense-ros.git
```
- Move into this repositories directory for the following steps
```bash
cd AIRLAB_Project
```
- Clone the repository for the Aruco Marker Detection
```bash
git clone https://github.com/nickoenig37/ros2_aruco.git
```
- Install Needed Dependencies for Aruco Marker Detection
```bash
pip3 install opencv-contrib-python transforms3d
sudo apt install ros-humble-tf-transformations
```

- Then install the dependencies and build
```bash
cd ~/ros2_ws
rosdep install --from-paths src --ignore-src -r -y
```




