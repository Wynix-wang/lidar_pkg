## 使用Gmapping进行建模

1. 进入catkin_ws并使用catkin_make进行编译
2. 使用 ‘roslaunch lidar_pkg gmapping.launch’ 运行
3. 在弹出窗口中使用wsad移动，空格暂停来控制机器人在Gazebo中移动进行绘图
4. 使用 ‘rosrun map_server map_saver -f 文件名’ 对地图进行保存
5. 使用 ‘rosrun map_server map_sever 文件名’ 对地图进行加载，会加载到map话题

