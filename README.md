# Line Following Robot - ROS2 Node

## Overview
This ROS2 node enables a robot to follow a line using a camera and image processing. The robot will continuously process the incoming camera images, identify the position of the line, and adjust its movement to stay on track. The movement commands are published via the `cmd_vel` topic, which controls the robot's linear and angular velocities.

## Dependencies
- ROS2 (Humble)
- OpenCV
- cv_bridge
- numpy

## Parameters
The following parameters can be configured at runtime:

- `boundary_left`: The threshold for detecting the left boundary of the line (default: 300)
- `boundary_right`: The threshold for detecting the right boundary of the line (default: 340)
- `speed_drive`: Linear speed of the robot (default: 0.1)
- `speed_turn`: Angular speed for turning (default: 0.3)

## Topics
- **Input**: `/image_raw/compressed` (`sensor_msgs/CompressedImage`) - Compressed image from the robot's camera.
- **Output**: `/cmd_vel` (`geometry_msgs/Twist`) - Velocity commands to control the robot's movement.

## How It Works
1. **Image Processing**: 
   - The camera image is converted to grayscale.
   - A bottom row of the image is analyzed to detect the position of the line based on the brightest pixel.
   - If the detected line is off-center, the robot adjusts its direction by turning left or right accordingly.
   
2. **Movement Control**:
   - Based on the position of the line in the image, the robot is commanded to either go straight or turn left/right to follow the line.
   
3. **Adjustable Parameters**:
   - Parameters like the left and right boundaries of the line, as well as the robot's speed and turning rate, can be dynamically configured.

## Launching the Node
To launch the node, you can use the following command in your ROS2 workspace:
```bash
ros2 launch follow_line follow_line_launch.py when configured like in setup.py
