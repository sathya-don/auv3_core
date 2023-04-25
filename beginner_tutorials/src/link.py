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
talker_publisher = rospy.Publisher('/alpha/Laserscan', LaserScan, queue_size = 10)
#scan_subscriber  = rospy.Subscriber(

#Subscriber
talker_sub = roslibpy.Topic(ros,'/scan','sensor_msgs/LaserScan')

#def Laserscan():
    

def sub_callback(msg):
    scan_msg = LaserScan()
    range_arr = Float32MultiArray()
    scan_msg.header.stamp = rospy.Time.now()
    scan_msg.header.frame_id = msg["header"]["frame_id"]
    #print(scan_msg.header.frame_id)
    scan_msg.angle_min = msg['angle_min']
    scan_msg.angle_max = msg['angle_max']
    scan_msg.angle_increment = msg['angle_increment']
    scan_msg.time_increment = msg['time_increment']
    scan_msg.scan_time = msg['scan_time']
    scan_msg.range_min = msg['range_min']
    scan_msg.range_max = msg['range_max']
        
    #print(msg["ranges"][120])
    # print(len(msg["ranges"]))
    #for i in range(0,150):
    
        #scan_msg.ranges.append(msg["ranges"][151])
    
    #for i in range(0,150):
    
        #scan_msg.intensities.append(msg["intensities"][151])
    #scan_msg.intensities = msg["intensities"]
    #print((scan_msg.ranges)
    #scan_msg.ranges = msg['ranges']
    #scan_msgprint(msg['ranges'])
    #scan_msg.intensities = msg['intensities']
    talker_publisher.publish(scan_msg)
    #talker_publisher.publish("55")
 
def main():
    
    rospy.init_node("ros_bridge_task",anonymous=True)
    rate = rospy.Rate(15) 
    ros.run()
    print('Is ROS connected?', ros.is_connected)
    if(ros.is_connected):
        talker_sub.subscribe(sub_callback)
        rospy.spin()
    else:
        print("Please connect to bridge!!")
                                                        
if __name__ == "__main__":
    main()
