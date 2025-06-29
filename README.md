# 全局路径规划与局部避障

## 一、使用Gmapping进行建模

1. 进入catkin_ws并使用catkin_make进行编译

2. 运行launch文件

   ```
   roslaunch lidar_pkg gmapping.launch
   ```

   - 场景使用wpb_stage_robocup

3. 在弹出窗口中使用wsad移动，空格暂停来控制机器人在Gazebo中移动进行绘图

4. 保存地图和加载地图的指令如下，这会把地图加载到/map话题

   ```
   rosrun map_server map_saver -f 文件名
   rosrun map_server map_server 文件名.yaml
   ```



---

## 二、使用move_base进行导航

1. 添加导航所需依赖

   ```
   cd ~/catkin_ws/src/
   git clone https://github.com/6-robot/wpb_home.git
   cd ~/catkin_ws/src/wpb_home_bringup/scripts/
   ./install_for_noetic.sh 
   ```

   > 如果有问题使用鱼香ROS更新一下源
   >
   > ```
   > wget http://fishros.com/install -O fishros && . fishros
   > ```

2. 重新编译一次

   ```
   cd ~/catkin_ws
   catkin_make
   ```

3. 运行launch文件

   ```
   roslaunch lidar_pkg nav.launch
   ```

   此时可以在rviz中手动放置2D Nav Goal来设置导航目标。

   - 全局规划器使用GlobalPlanner。默认Dijkstra算法，可以通过添加以下参数来切换为A*（不推荐）。

   ```
   <param name="GlobalPlanner/use_dijkstra" value="false" /> 
   <param name="GlobalPlanner/use_grid_path" value="false" /> 
   ```

   - 局部规划器使用WpbhLocalPlanner
   - 恢复策略为：保守重置(2.0m)->旋转恢复->激进重置(0m)->旋转恢复

   > 部分参数在 /lidar_pkg/nav_lidar 文件夹下
   >
   > 更多参数设置在ROS Index中搜索查看，大部分是通过降低路径质量来进行优化。

     - 实时调整参数

   ```
   rosrun rqt_reconfigure rqt_reconfigure
   ```

4. 通过程序设置导航目标点

   ```
   rosrun lidar_pkg nav_client.py <param>
   ```

   参数输入预设的导航目标点，可选值：a、b、c、d、0

