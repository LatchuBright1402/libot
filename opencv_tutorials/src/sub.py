#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose

def turtle_pose_callback(msg:Pose):
	rospy.loginfo("(" + str(msg.x) + ", " + str(msg.y) + ")")

	rospy.init_node("tutle_sub")
	sub = rospy.Subscriber("/tuurtle/pose", Pose, callback = turtle_pose_callback)

	rospy.loginfo(" Subscriber node started")

	rospy.spin()

if __name__ = "__main__":

	turtle_pose_callback()