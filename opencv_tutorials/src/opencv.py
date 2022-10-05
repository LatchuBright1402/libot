#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images
import cv2 # OpenCV library

def getData(msg):
	br = CvBridge()
	rospy.loginfo("receiving frames")

	current_frame = br.imgmsg_to_cv2(msg)

	cv2.imshow("camera", current_frame)

	cv2.waitKey(1)

def CamSub():
	rospy.init_node("cam_view")
	rospy.Subscriber("/camera1/image_raw", Image, getData)
	rospy.spin()
	cv2.destroyAllWindows()
if __name__ == '__main__':
	CamSub()
