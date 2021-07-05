#pragma once

#include <vector>
#include <algorithm>

enum Order
{
    ASC,
    DESC
};

std::vector<int> generate_random_vector(std::size_t size, int min, int max);

std::vector<int> generate_ordered_vector(std::size_t size, int min, int max, Order order);