cmake_minimum_required(VERSION 3.28)
project(z2 C)

set(CMAKE_C_STANDARD 11)
add_compile_options(-Wall -Wextra -Wuninitialized -pedantic -g)

add_executable(z2 src/functions.c src/data.c src/z2.c)
target_include_directories(z2 PRIVATE include)
target_link_libraries(z2 -lm)



