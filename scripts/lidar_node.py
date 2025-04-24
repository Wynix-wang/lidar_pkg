#!/usr/bin/env python3
# coding=utf-8
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
count = 0
routate_count = 0

def LidarCallback(msg):
    global vel_pub
    global count
    global routate_count
    
    front_dist = msg.ranges[180]
    for i in range(180-45, 180+45):
        front_dist = min(front_dist, msg.ranges[i])
    right_dist = msg.ranges[90]
    for i in range(90-45, 90+45):
        right_dist = min(right_dist, msg.ranges[i])

    rospy.loginfo('%d,%.3f, %.3f', routate_count, front_dist, right_dist)
    if count > 0:
           count = count - 1
           return
    vel_cmd = Twist()
    if front_dist < 1.0 and front_dist >= 0.5:
        vel_cmd.angular.z = 0.3
        routate_count = routate_count + 1
    elif front_dist < 0.5:
        vel_cmd.linear.x = 0.00
    else:
        vel_cmd.linear.x = 0.2
        if routate_count > 0 and right_dist > 0.5:
            vel_cmd.angular.z = -0.3
            routate_count = routate_count - 1
    vel_pub.publish(vel_cmd)

def min(a, b):
    if a <= b:
        return a
    else:
        return b

if __name__ == '__main__':
    rospy.init_node('lidar_node')
    lidar_sub = rospy.Subscriber('/scan', LaserScan, LidarCallback, queue_size = 10)
    vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size = 10)
    rospy.spin()