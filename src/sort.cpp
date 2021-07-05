#include <chrono>
#include <string>
#include <iostream>

#include "sorting.hpp"
#include "vector_generation.hpp"

int main(int argc, char *argv[])
{
    if (argc < 4)
    {
        return 0;
    }

    std::string sort_case(argv[1]);
    std::string method(argv[2]);
    int entries = std::atoi(argv[3]);

    // auto vec = generate_random_vector(entries, 0, 1000);
    std::vector<int> vec;

    std::chrono::_V2::system_clock::time_point start;

    if (method == "bubble")
    {
        if (sort_case == "random")
        {
            vec = generate_random_vector(entries, 0, 1000);
        }
        else if (sort_case == "best")
        {
            vec = generate_ordered_vector(entries, 0, 1000, Order::ASC);
        }
        else if (sort_case == "worst")
        {
            vec = generate_ordered_vector(entries, 0, 1000, Order::DESC);
        }
        start = std::chrono::high_resolution_clock::now();
        bubble_sort(vec);
    }
    else if (method == "merge")
    {
        vec = generate_random_vector(entries, 0, 1000);
        start = std::chrono::high_resolution_clock::now();
        merge_sort(vec);
    }
    else if (method == "heap")
    {
        vec = generate_random_vector(entries, 0, 1000);
        start = std::chrono::high_resolution_clock::now();
        heap_sort(vec);
    }
    auto finish = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(finish - start);

    std::cout << sort_case << "_case"
              << " | " << method << "_sort"
              << " | " << entries << " | " << duration.count() << std::endl;
}

// int main()
// {
//     for (auto entries : generate_random_vector(5, 1000, 10000))
//     {
//         for (auto order : {Order::ASC, Order::DESC})
//         {
//             auto vec = generate_ordered_vector(entries, 0, 1000, order);

//             std::cout << ((order == Order::ASC) ? "Ascendent" : "Descendent") << "(" << entries << "): ";
//             for (auto x : vec)
//             {
//                 std::cout << x << " ";
//             }
//             std::cout << std::endl
//                       << std::endl;
//         }
//     }
// }
