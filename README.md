# Information about using project


## Setup Guide For The Project
- Follow these steps starting from within your ros2_ws 
```bash
cd ~/ros2_ws/src
```
- Clone THIS repository into your Workspace
```bash
git clone https://github.com/nickoenig37/AIRLAB_Project.git
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
cd AIRLAB_Project/
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
cd ../.. # Or cd ~./ros2_ws
rosdep install --from-paths src --ignore-src -r -y
```
```bash
colcon build --symlink-install
```
```bash
source install/setup.bash
```

- Now you are ready to run the project!
## Using the Programs (Launch/Run each in a new terminal)
- First and foremost, make sure the camera is connected to the computer and powered on.

- This command launches the bringup launch file for Realsense and MediaPipe Packages
```bash
ros2 launch pkg_bringup bringup.launch.py
```
- To Visualize the camera data in RVIZ2, run the following command
```bash
rviz2
```
- This command launches the Aruco Marker Detection
```bash
ros2 launch ros2_aruco aruco_recognition.launch.py 
```


## Making Aruco Markers
To make Aruco markers, you can use the following link to generate them:
```bash
https://chev.me/arucogen/
```
In the aruco_parameters.yaml file, you can change the marker size to match the size of the markers you are using.
- I used ID 0 & 1 w/ size 0.11m Markers as part of the DICT_5X5_250



