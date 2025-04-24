#!/usr/bin/env python3
# coding=utf-8
import rospy
from sensor_msgs.msg import LaserScan

def lidar_callback(msg):
    # 打印激光雷达数据的基本信息
    rospy.loginfo("----- 接收到激光雷达数据 -----")
    rospy.loginfo("测距范围: [%.2f m, %.2f m]", msg.range_min, msg.range_max)
    rospy.loginfo("角度范围: [%.2f rad, %.2f rad]", msg.angle_min, msg.angle_max)
    rospy.loginfo("角度增量: %.2f rad", msg.angle_increment)
    rospy.loginfo("扫描点数: %d", len(msg.ranges))
    rospy.loginfo("正前方距离: %.2f m", msg.ranges[180])
    rospy.loginfo("左前方距离: %.2f m", msg.ranges[180+30])
    rospy.loginfo("右前方距离: %.2f m", msg.ranges[180-30])

def main():
    rospy.init_node('lidar_subscriber', anonymous=True)
    rospy.Subscriber('/scan', LaserScan, lidar_callback, queue_size=10)
    rospy.loginfo("激光雷达订阅节点已启动，等待数据...")
    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass