# Fuzzy_Controlled_Rover
Self-driving rover that follows a car (with specific license plate number) and maintains a constant distance between the later using fuzzy control

![alt text](https://github.com/daniazzam/Fuzzy_Controlled_Rover/blob/main/images/rover.jpg?raw=true)


Description
The designed mechatronic system consists of a car-following rover that aims to follow a nearby
moving obstacle and maintain a certain distance from it. To elaborate, a fuzzy controller
determines the rover’s motors’ speed depending on the relative distance and distance increase
with the obstacle to detect its speeding or deceleration, while accounting for any inclination the
traversed path is subject to. To simulate how a cop car would operate, we also added the feature
of detecting and registering the car’s license plate using a convolutional neural network.

[![Watch the video](https://media.istockphoto.com/vectors/video-button-red-play-icon-button-isolated-vector-illustration-arrow-vector-id1191661875?k=20&m=1191661875&s=612x612&w=0&h=M9GYAVTxsnG1d2WpsUjmMbIXYt0SskmMKGOvodNkmxc=)](https://github.com/daniazzam/Fuzzy_Controlled_Rover/blob/main/images/demo.mp4?raw=true)

Hardware Connections

![alt text](https://github.com/daniazzam/Fuzzy_Controlled_Rover/blob/main/images/ciruit.jpg?raw=true)

Features
The implemented features include:
- Detecting the presence of the nearby car using the distance sensors;
- Prompting the rover to follow it while maintaining a certain set reference distance from it;
- Adjusting the rover’s speed using fuzzy logic while accounting for any nonlinear path the
obstacle may take by varying the speed of its left and right pairs accordingly;
- Capturing the license plate of the speeding obstacle using the CNN
