#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import time

def square():

	rospy.init_node("turtlesim", anonymous = True)
	pub = rospy.Publisher("/turtle1/cmd_vel", Twist,queue_size = 10)

	move_cmd = Twist()

	move_cmd.linear.x = 0
	move_cmd.angular.z = 0
	time.sleep(1)
	rospy.loginfo("turle started")

	for i in range(4):

		move_cmd.linear.x = 3
		move_cmd.angular.z = 0
		pub.publish(move_cmd)
		time.sleep(1)
		rospy.loginfo("turle moving straight")

		
		move_cmd.linear.x = 0
		move_cmd.angular.z = 1.57
		pub.publish(move_cmd)
		time.sleep(1)
		rospy.loginfo("turle taking turn 90 degreee")

	move_cmd.linear.x = 0
	move_cmd.angular.z = 0
	time.sleep(1)
	rospy.loginfo("turle stopped")

if __name__ == "__main__":
	square()	


