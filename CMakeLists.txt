cmake_minimum_required(VERSION 2.8)
project( DisplayImage )
find_package( OpenCV REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS} )
add_executable( flood_fill fill.cpp )
target_link_libraries( flood_fill ${OpenCV_LIBS} )
