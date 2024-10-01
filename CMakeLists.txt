cmake_minimum_required(VERSION 3.26)

add_library(PromptIconFontHeader INTERFACE)
target_include_directories(PromptIconFontHeader INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}/include)
