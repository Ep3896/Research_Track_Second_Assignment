ROS SIMULATION
===================

### Professor. [Carmine Recchiuto](https://github.com/CarmineD8)

We will learn how to use ROS custom messages, services, and actions in this assignment. We'll also utilize Rviz and Gazebo's graphical user interfaces to observe the simulation of the robot. The assignment 2 2022 template was used as a starting point for the creation of the new package.

Second Assignment
===================
The task of this assignment was to implement three new nodes in the robot simulation:

* A node (a) that implements an action client, allowing the user to set a target (x, y) or to cancel it.
* A service node that prints the number of objectives attained and abandoned upon request;
* A node that uses a custom message to subscribe to the robot's position and velocity while also printing the robot's average speed and distance from the goal.

It is also required to create a launch file to start the simulation (assignment1.launch).

Installing and running:
-----------------------

The simulator requires specific ROS version and I recommend using the Docker image dedicated to this course to make installation and running easier. After cloning the repo to the ROS work space the following commands should be used in the workspace directory to install.

You must download the package second assignment in the src folder of your workspace after installing ROS and setting up your workspace. 

Run the following command from the shell:
```bash
$ git clone https://github.com/CarmineD8/assignment_2_2022.git
```
Run the following command from the shell:\
```bash
$ git clone https://github.com/Ep3896/Enrico_Piacenti_Second_Assignment_RT-.git
```
Just for be prudent , it is recommended to run the following commands if a buil in the catkin workspace was done beforehand:

```bash
$ sudo rm -rf devel/
$ sudo rm -rf build/
```

Then you must run:

```bash
$ catkin_make 
```

Finally, the final steps are the following:

```bash
$ sudo apt-get install konsole
$ sudo bash run_project.sh #inside the directory of the project.
```

Launching the script:
---------

The program will open five windows:

- *Gazebo*: A 3D visualization setup will be used to depict the arena and the robot.
- *Rviz*: a ROS visualization tool is employed for robot debugging and the development of new features.
- *sub_coord.py*: the display window where mesuarment about the robot will be printed .
- *action_client.py*: twindow through which a user can enter a goal or cancel it.



Action client Flowchart [node (a)]:
----------------------------
![Tux, the Linux mascot](/image/Flowchart_Second_Assignment.png)



