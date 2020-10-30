#include <thrust/host_vector.h>
#include <thrust/device_vector.h>
#include <iostream>
#include <chrono>
#include <stdio.h>
#include <string>
#include <string.h>
#include <math.h>
#include <iostream>
#include <time.h>
#include <ctime>
#include <ratio>
#include <chrono>
#include <iomanip>
#include <locale.h>

using namespace std;

int main()
{
    const std::string intention = "I am love. REGULATE AND INTEGRATE. OM.";

    int num_chars = intention.length();

    thrust::host_vector<int> host_intention_vector;

    for (int i = 0; i < num_chars; ++i)
    {
        host_intention_vector.push_back(int(intention.at(i)));
    }

    long long num_iterations = 0;

    thrust::device_vector<int> device_intention_vector;

    // copy all of H back to the beginning of D
    thrust::copy(host_intention_vector.begin(), host_intention_vector.end(), device_intention_vector.begin());

    auto start = std::chrono::system_clock::now();
    auto end = std::chrono::system_clock::now();

    for (int i = 0; i < 10000; ++i) {
        for (int j = 0; j < num_chars; ++j) {
            device_intention_vector[j] = 3; //The Intention Repeater Call
        }
        end = std::chrono::system_clock::now();
        ++num_iterations;
    }
    cout << "Number times repeated: " << std::to_string(num_iterations) << endl;
    return 0;
}