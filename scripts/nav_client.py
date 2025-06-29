#!/usr/bin/env python3
# coding=utf-8

import rospy
import actionlib
import sys
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

if __name__ == "__main__":
    # 判断输入参数
    if len(sys.argv) != 2:
        print("Need a goal!")
        sys.exit(1)
    
    # 启动一个新节点nav_client
    rospy.init_node("nav_client")
    #等待move_base节点启动
    ac = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    ac.wait_for_server()
    # 设置导航目标
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id="map"
    goal.target_pose.pose.orientation.x = 0.0
    goal.target_pose.pose.orientation.y = 0.0
    goal.target_pose.pose.orientation.z = 0.0
    goal.target_pose.pose.orientation.w = 1.0
    position = sys.argv[1]
    if position == 'a':
        goal.target_pose.pose.position.x = 4.0
        goal.target_pose.pose.position.y = 3.0
        goal.target_pose.pose.position.z = 0.0
    elif position == 'b':
        goal.target_pose.pose.position.x = -3.0
        goal.target_pose.pose.position.y = 2.0
        goal.target_pose.pose.position.z = 0.0
    elif position == 'c':
        goal.target_pose.pose.position.x = -4.0
        goal.target_pose.pose.position.y = -3.0
        goal.target_pose.pose.position.z = 0.0
    elif position == 'd':
        goal.target_pose.pose.position.x = 2.0
        goal.target_pose.pose.position.y = -3.0
        goal.target_pose.pose.position.z = 0.0
    else:
        position = '0'
        goal.target_pose.pose.position.x = 0.0
        goal.target_pose.pose.position.y = 0.0
        goal.target_pose.pose.position.z = 0.0
    # 持续更新全局导航路径
    ac.send_goal(goal)
    print("Start navigation, goal: " + position)
    while ac.get_state() != actionlib.GoalStatus.SUCCEEDED:
        ac.send_goal(goal)
        rospy.sleep(1)
        ac.get_result()
    print("Mission complete!")