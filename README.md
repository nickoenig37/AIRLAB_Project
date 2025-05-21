# Information about using project


## Starting the realsense
```bash
ros2 launch realsense2_camera rs_launch.py
```

```bash
ros2 launch realsense2_camera rs_launch.py depth_module.depth_profile:=1280x720x30 pointcloud.enable:=true
```

### Starting the realsense with aligned depth-- needed for hand tracking
```bash
ros2 launch realsense2_camera rs_launch.py align_depth.enable:=true
```

## Starting hand tracking node
```bash
ros2 run mediapipe_hand_publisher hand_publisher
```

- Source for the mediapipe usage which could help for images:
https://link.springer.com/chapter/10.1007/978-3-031-09062-2_1

This was the OG link tho:
https://medium.com/@smart-design-techology/hand-detection-in-3d-space-888433a1c1f3


## Using AprilTags (setup guide)

- Step one, clone into your ros2 workspace
```bash
cd ~/ros2_ws/src
git clone https://github.com/christianrauch/apriltag_ros.git
```
- Then install the dependencies and build
```bash
cd ~/ros2_ws
rosdep install --from-paths src --ignore-src -r -y
colcon build --packages-select apriltag_ros
source install/setup.bash
```

- April tag images can be found in this github repository
https://github.com/AprilRobotics/apriltag-imgs


- Launching 
```bash
ros2 run apriltag_ros apriltag_node --ros-args \
-r image_rect:=/camera/camera/color/image_raw \
-r camera_info:=/camera/camera/color/camera_info \
--params-file `ros2 pkg prefix apriltag_ros`/share/apriltag_ros/cfg/tags_36h11.yaml

OR

ros2 run apriltag_ros apriltag_node --ros-args -r image_rect:=/camera/camera/color/image_raw -r camera_info:=/camera/camera/color/camera_info --params-file ~/Documents/AIRLab/ros2_ws/src/apriltag_ros/cfg/my_tags_36h11.yaml
```


- Trying to get better AprilTag detection using imageproc:
```bash 
sudo apt install ros-humble-image-proc
ros2 run image_proc image_proc --ros-args   -r image:=/camera/camera/color/image_raw   -r camera_info:=/camera/camera/color/camera_info

```


## Using Aruco Markers Now

- Step one, clone into your ros2 workspace
```bash
git clone https://github.com/Tekkrez/ros2_aruco.git
```
- Then install the dependencies and build
```bash
cd ~/ros2_ws
rosdep install --from-paths src --ignore-src -r -y
```
```bash
pip3 install opencv-contrib-python transforms3d
sudo apt install ros-humble-tf-transformations

```



