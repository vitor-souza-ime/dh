2DOF Robotic Arm Simulation

Overview
This Python script simulates a 2-degree-of-freedom (2DOF) robotic arm and visualizes its configuration in a 3D plot. The arm consists of two links with lengths a1 and a2, and two joint angles θ1 (base rotation) and θ2 (elbow angle). The script calculates the end-effector position using forward kinematics and plots the arm's configuration using Matplotlib's 3D plotting capabilities.
Requirements
To run the script, you need the following Python libraries:

numpy: For numerical computations, including trigonometric functions.
matplotlib: For creating the 3D visualization of the robotic arm.

You can install the required libraries using pip:
pip install numpy matplotlib

Usage

Run the script in a Python environment.
Enter the following inputs when prompted:
Length of the first link (a1) in arbitrary units.
Length of the second link (a2) in arbitrary units.
Angle of the first joint (θ1, base rotation) in degrees.
Angle of the second joint (θ2, elbow angle) in degrees.


The script will:
Convert the input angles from degrees to radians.
Compute the positions of the joints and the end-effector using forward kinematics.
Display the end-effector coordinates (xP, yP, zP) in the console.
Generate a 3D plot showing the robotic arm's configuration, with the end-effector highlighted.



Code Explanation

Input Parameters:
a1: Length of the first link.
a2: Length of the second link.
theta1_deg: Angle of the base joint in degrees (rotation about the Z-axis).
theta2_deg: Angle of the elbow joint in degrees (rotation relative to the first link).


Kinematics:
The base joint is at the origin (0, 0, 0).
The position after the first link is calculated as (x1, y1, z1) = (a1 * cos(θ1), a1 * sin(θ1), 0).
The end-effector position after the second link is calculated as:
x2 = x1 + a2 * cos(θ1) * cos(θ2)
y2 = y1 + a2 * sin(θ1) * cos(θ2)
z2 = a2 * sin(θ2)




Visualization:
A 3D plot is created using mpl_toolkits.mplot3d.Axes3D.
The arm is plotted as a line connecting the origin, the first joint, and the end-effector.
The end-effector is highlighted with a red dot.
The plot includes labeled axes, a title, a legend, and a grid, with equal aspect ratios for consistent visualization.
The plot limits are set dynamically based on the sum of the link lengths (a1 + a2 + 1) to ensure the entire arm is visible.



Example
For inputs:

a1 = 2.0
a2 = 3.0
θ1 = 45 degrees
θ2 = 30 degrees

The script will compute the end-effector position and display a 3D plot of the arm.
Notes

Ensure all inputs are valid numbers to avoid errors.
The plot uses equal aspect ratios to accurately represent the arm's geometry.
The script does not save the plot to a file; it displays it interactively using plt.show(). To save the plot, you can modify the script to use plt.savefig('filename.png') before plt.show().

License
This project is unlicensed and provided as-is for educational purposes.
