cmake_minimum_required (VERSION 2.8.11)
project (YELLOW)

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}/")

include_directories(.)

find_package (Threads)

set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -O0 -ggdb")

add_executable (probe main.cpp probe.cpp)

target_include_directories (probe PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
target_link_libraries (probe ${LIBTINS_LIBRARIES})
target_link_libraries (probe ${CMAKE_THREAD_LIBS_INIT})
