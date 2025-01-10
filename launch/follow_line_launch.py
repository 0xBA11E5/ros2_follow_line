from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='follow_line',
            executable='line_following',

            # activate output
            output='screen',
            emulate_tty=True,
            arguments=[('__log_level:=debug')],

            parameters=[
                {'boundary_left': 300},
                {'boundary_right': 340},
                {'threshold_line': 102}
            ]
        ),
    ])
