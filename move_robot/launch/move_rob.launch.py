"""Launch file example"""

from launch import LaunchDescription
import launch_ros.actions


def generate_launch_description():
    return LaunchDescription([
        launch_ros.actions.Node(
            package='move_robot', executable='move_robot_pub', output='screen'),
    ])