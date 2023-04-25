#!usr/bin/env python3

import rospy
import roslibpy
#from std_msgs.msg import *
#from std_msgs.msg import String
from std_msgs.msg import Header
from std_msgs.msg import Float32
from std_msgs.msg import Float32MultiArray
from sensor_msgs.msg import LaserScan

ros = roslibpy.Ros(host='192.168.43.152', port=9090)


#Publishers
talker_publisher = rospy.Publisher('/alpha/LaserScan', LaserScan, queue_size = 10)
#scan_subscriber  = rospy.Subscriber(

#Subscriber
talker_sub = roslibpy.Topic(ros,'/scan','sensor_msgs/LaserScan')

#def Laserscan():
    

class ros_bridge_task1():
    {
    def sub_callback(self, msg):
        self.scan_data = msg
        scan_msg = LaserScan()
        scan_msg.header = self.scan_data.header
        #scan_msg.header.frame_id = laser
        scan_msg.angle_min = self.scan_data.angle_min
        scan_msg.angle_max = self.scan_data.angle_max
        scan_msg.angle_increment = self.scan_data.angle_increment
        scan_msg.time_increment = self.scan_data.time_increment
        scan_msg.scan_time = self.scan_data.scan_time
        scan_msg.range_min = self.scan_data.range_min
        scan_msg.range_max = self.scan_data.range_max
        scan_msg.ranges = self.scan_data.ranges
        #scan_msgprint(msg['ranges'])
        scan_msg.intensities = self.scan_data.intensities

        
        talker_publisher.publish(scan_msg)
        #talker_publisher.publish("55")
 
def main():
    
    rospy.init_node("ros_bridge_task",anonymous=True)
    now = rospy.get_rostime()
    rate = rospy.Rate(15) 
    ros.run()
    print('Is ROS connected?', ros.is_connected)
    if(ros.is_connected):
        talker_sub.subscribe(sub_callback)
        rospy.spin()
    else:
        print("Please connect to bridge!!")
                                                        
if __name__ == "__main__":
    try:
        rospy.init_node("ros_bridge_task",anonymous=True)
        main()
    except rospy.ROSInterruptException:
        pass
