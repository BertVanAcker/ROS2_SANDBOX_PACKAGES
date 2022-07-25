======================================
  ROS2 Getting Started Packages
======================================
Containing ROS2 packages to try out the basics

Build all packages within the ROS2_SANDBOX_PACKAGES. Execute the following commands within the terminal in the ROS2 workspace (e.g. ~/ros2_ws)

.. code-block::

   user:~/ros2_ws$ colcon build --symlink-install
   user:~/ros2_ws$ source install/setup.bash # source the workspace

After building, the different nodes can be run individually:

ROS2_talker_py:

.. code-block::

   user:~/ros2_ws$ ros2 run ros2_talker_py talker

ROS2_listner_py:

.. code-block::

   user:~/ros2_ws$ ros2 run ros2_listner_py listner