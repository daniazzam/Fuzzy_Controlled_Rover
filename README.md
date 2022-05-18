# Fuzzy_Controlled_Rover
Self-driving rover that follows a car (with specific license plate number) and maintains a constant distance between the later using fuzzy control

Head-Controlled Rover
Rover

Description
The designed mechatronic system consists of a car-following rover that aims to follow a nearby
moving obstacle and maintain a certain distance from it. To elaborate, a fuzzy controller
determines the rover’s motors’ speed depending on the relative distance and distance increase
with the obstacle to detect its speeding or deceleration, while accounting for any inclination the
traversed path is subject to. To simulate how a cop car would operate, we also added the feature
of detecting and registering the car’s license plate using a convolutional neural network.


Hardware Connections
Hardware Circuit

Features
The implemented features include:
- Detecting the presence of the nearby car using the distance sensors;
- Prompting the rover to follow it while maintaining a certain set reference distance from it;
- Adjusting the rover’s speed using fuzzy logic while accounting for any nonlinear path the
obstacle may take by varying the speed of its left and right pairs accordingly;
- Capturing the license plate of the speeding obstacle using the CNN
