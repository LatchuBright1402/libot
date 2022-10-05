#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

def turtle_pose_callback(pose:Pose):
	message = Twist()
	
	
	#print(pose.x)

	if pose.x > 8.0 or pose.y > 8.0 or pose.x < 2.0 or pose.y < 2.0:
		message.linear.x = 1.0
		message.angular.z = 1.4
		
		message.angular.z = message.angular.z + 0.2

	else:
		message.linear.x = 1.0
		message.angular.z = 0.0



	pub.publish(message)



if __name__ == "__main__":

	rospy.init_node("turtle_pub", anonymous = True)

	pub = rospy.Publisher("/turtle1/cmd_vel",Twist, queue_size = 10)
	sub = rospy.Subscriber("/turtle1/pose", Pose, callback = turtle_pose_callback)
	rospy.loginfo("The Node started")


	rospy.spin()



