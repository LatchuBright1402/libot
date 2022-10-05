#!/usr/bin/env python3

import rospy
import time
from geometry_msgs.msg import Twist
import sys

def circle(radius):
	rospy.init_node("turtlesim", anonymous = True)
	pub_msg = rospy.Publisher("/turtle1/cmd_vel",  Twist, queue_size = 10 )
	
	rate = rospy.Rate(10)
	msg_cmd = Twist()
	while not rospy.is_shutdown: 
	
		msg_cmd.linear.x = 1.0
		msg_cmd.angular.z = 1.4


		rospy.loginfo("Radius = %f ", radius)
		pub_msg.publish(msg_cmd)
		rospy.sleep()

if __name__ == "__main__":
	try:
		circle(float(sys.argv[1]))
	except rospy.ROSInterruptException:
		pass

