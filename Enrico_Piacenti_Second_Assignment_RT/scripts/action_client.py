#! /usr/bin/env python

"""

Node: action_client and User Interface

Description: Python code that implements the user interface to select the desired action on the robot and the action_client , allowing the user to set a target (x,y).

author: Enrico Piacenti  enricopiacenti96@gmail.com

"""

import rospy
from geometry_msgs.msg import PoseStamped
import actionlib
import actionlib.msg
import assignment_2_2022.msg
from std_srvs.srv import *
import os



def Controller():

    """
    This function asks the user about his/her choice and therefore runs the corresponding function.
    If the user inputs a wrong choice it is printed out for the user and the while loop starts over again.
    The two choices are:
        *1) autonomously reach a x,y coordinate provided by the user*
        *2) Stop the moving robot and cancel its given prompt*
    """

    os.system('clear')  
    print("                 Controller                    \n")
    print("1:Choose the destination\n")
    print("2:Stop the Robot\n")   
    instruction_selected = input("Please enter your choice:")  
    if   (instruction_selected == "1"):
        selected_target()
    elif (instruction_selected == "2"):
        remove_instruction() 
    else:
        wrong_input()


def wrong_input():

    """
    This function occurs when the user select a wrong input at the start of the command
    """

    print("Input not allowed")
    rospy.sleep(3)
    Controller()


def remove_instruction():

    """
    This function request the server to remove the instuction given by the user about reaching a spcific target
    """
    
    action_client.cancel_goal()
    print("\nReaching target canceled by the user")
    rospy.sleep(3)
    Controller()

def selected_target():

    """
    This function does the following:
    1) Read the request provided by the user .
    2) Create a goal using the user data.
    3) Waits the server.
    4) Create the goal.
    5) Set the goal.
    &) Start the user interface back again.
    """

    # Reading input from user
    goal_target_pos_x = input("\n enter the X pos: ")
    goal_target_pos_y = input(" enter the Y pos: ")
    goal_target_pos_x = int(goal_target_pos_x)
    goal_target_pos_y = int(goal_target_pos_y)
    print(f'\n Target is: (X,Y): ({goal_target_pos_x},{goal_target_pos_y}) ')
    
    # Waits the server
    print("\n Waiting the Server")
    action_client.wait_for_server()
    
    #create the goal
    destination_target = PoseStamped()
    destination_target.pose.position.x = goal_target_pos_x
    destination_target.pose.position.y = goal_target_pos_y

    # Creates a custom messagr according to structure of PlanningGoal()
    destination_target = assignment_2_2022.msg.PlanningGoal(destination_target)

    # send the goal
    action_client.send_goal(destination_target)
    
    rospy.sleep(3)
    Controller()
      


if __name__ == '__main__':

    """
    The main function enables the SimpleActionClient to publish and subscribe via ROS by initializing a rospy node. 
    """
    try:
        rospy.init_node('action_client')
        action_client = actionlib.SimpleActionClient('/reaching_goal',assignment_2_2022.msg.PlanningAction )
        Controller()
        rospy.spin()

    except rospy.ROSInterruptException:
        print("program interrupted before completion", file=sys.stderr)

