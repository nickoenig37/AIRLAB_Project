from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, TextSubstitution
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # Argument for enabling/disabling depth alignment for RealSense
    align_depth_arg = DeclareLaunchArgument(
        'align_depth',
        default_value='true',
        description='Whether to enable depth image alignment for RealSense camera.'
    )

    # --- Define paths to external launch files ---
    realsense_pkg_dir = get_package_share_directory('realsense2_camera')
    realsense_launch_file = os.path.join(realsense_pkg_dir, 'launch', 'rs_launch.py')

    return LaunchDescription([
        # --- Add declared arguments to the launch description ---
        align_depth_arg,

        # --- 1. Launch RealSense Camera with depth alignment ---
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(realsense_launch_file),
            launch_arguments={
                'align_depth.enable': LaunchConfiguration('align_depth')
            }.items()
        ),

        # --- 2. Launch hand_visualization node ---
        Node(
            package='hand_visualization',
            executable='hand_visualization',
            name='hand_visualization_node',
            output='screen',
            emulate_tty=True, # Recommended for seeing node output
        ),

        # --- 3. Launch mediapipe_hand_publisher node ---
        Node(
            package='mediapipe_hand_publisher',
            executable='hand_publisher',
            name='mediapipe_hand_publisher_node',
            output='screen',
            emulate_tty=True,
        ),

        # --- 4. Launch body_pose_detector node ---
        Node(
            package='body_pose_detector',
            executable='body_pose_detector',
            name='body_pose_detector_node',
            output='screen',
            emulate_tty=True,
        ),

        # --- 5. Launch skeleton_visualization node ---
        Node(
            package='skeleton_visualization',
            executable='skeleton_visualization',
            name='skeleton_visualization_node',
            output='screen',
            emulate_tty=True,
        ),
    ])