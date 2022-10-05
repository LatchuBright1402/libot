#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import time

def draw_d():

	rospy.init_node("turtlesim", anonymous = True)
	pub = rospy.Publisher("/turtle1/cmd_vel", Twist,queue_size = 10)

	move_cmd = Twist()

	move_cmd.linear.x = 0
	move_cmd.angular.z = 0
	pub.publish(move_cmd)
	time.sleep(1)
	rospy.loginfo("turle started")


	move_cmd.linear.y = 2.5
	move_cmd.angular.z = 0
	pub.publish(move_cmd)
	time.sleep(1)
	rospy.loginfo("turtle started drawing staright line in y axis")


	move_cmd.linear.x = 5
	move_cmd.angular.z = -4.05
	pub.publish(move_cmd)
	time.sleep(1)
	rospy.loginfo("turtle started drawing the arc")



if __name__ == "__main__":
	draw_d()	

