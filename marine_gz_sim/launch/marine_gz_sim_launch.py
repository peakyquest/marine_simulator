import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    package_name = 'marine_gz_sim'
    world_file = os.path.join(get_package_share_directory(package_name), 'worlds', 'ocean_world.sdf')
    
    # Define the models directory path
    models_path = os.path.join(get_package_share_directory(package_name), 'models')
    
    # Set the environment variable so that Gazebo can locate the models
    set_gazebo_resource_path = SetEnvironmentVariable(
        name='GZ_SIM_RESOURCE_PATH',
        value=models_path
    )

    # Path to the ign_gazebo launch file in ros_ign_gazebo package
    ign_gazebo_launch = os.path.join(
        get_package_share_directory('ros_gz_sim'),
        'launch',
        'gz_sim.launch.py'
    )
    
    # Include the ign_gazebo launch file and pass the world file argument
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(ign_gazebo_launch),
        launch_arguments=[('gz_args', ' -r -v 1 ' + world_file)]
    )

    return LaunchDescription([
        set_gazebo_resource_path,
        gazebo_launch
    ])