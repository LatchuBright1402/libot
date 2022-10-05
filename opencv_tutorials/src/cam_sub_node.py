#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def callback(data):

	br = CvBridge()

	rospy.loginfo("Receiving camera feed")
	current_frame = br.imgmsg_to_cv2(data)
	cv2.imshow("camera", current_frame)
	cv2.waitKey(1)

def cam_sub_msg():

	rospy.init_node("cam_sub_py", anonymous = True)
	rospy.Subscriber("cam_frames", Image, callback)

	rospy.spin()

	cv2.destroyAllWindows()

if __name__ == '__main__':

	cam_sub_msg()
