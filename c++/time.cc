#include<iostream>
#include <chrono>
 
int main()
{
    const auto p1 = std::chrono::system_clock::now();
 
    std::cout << "seconds since epoch: "
              << std::chrono::duration_cast<std::chrono::seconds>(
                   p1.time_since_epoch()).count() << '\n';
}