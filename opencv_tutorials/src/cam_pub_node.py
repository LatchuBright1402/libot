#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def cam_pub_msg():

	pub = rospy.Publisher("cam_frames", Image, queue_size = 10)

	rospy.init_node('cam_pub_py', anonymous = True)
	rate = rospy.Rate(10)

	cap = cv2.VideoCapture(0)

	br = CvBridge()

	while not rospy.is_shutdown():
		ret,frame = cap.read()

		if ret == True:

			rospy.loginfo("Camera started")

			pub.publish(br.cv2_to_imgmsg(frame))

		rate.sleep()

if __name__ == '__main__':
	try:
		cam_pub_msg()
	except rospy.ROSInterruptException:
		pass
