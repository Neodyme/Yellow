cmake_minimum_required (VERSION 2.8.11)
project (YELLOW)

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}/")

find_package(LibTINS REQUIRED)
include_directories(${LibTINS_INCLUDE_DIRS})
set(LIBS ${LIBS} ${LibTINS_LIBRARIES})

find_package (Threads)

include_directories(${LIBTINS_INCLUDE_DIRS})
include_directories(.)
add_executable (probe main.cpp probe.cpp)
target_include_directories (probe PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
target_link_libraries (probe ${LIBTINS_LIBRARIES})
target_link_libraries (probe ${CMAKE_THREAD_LIBS_INIT})
