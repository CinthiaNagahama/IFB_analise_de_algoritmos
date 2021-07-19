#include "vector_generation.hpp"

std::vector<int> generate_random_vector(std::size_t size, int min, int max)
{
    std::vector<int> vec(size);
    std::generate(vec.begin(), vec.end(), [&]() -> int
                  { return (rand() % (max - min) + min); });

    return vec;
}

std::vector<int> generate_ordered_vector(std::size_t size, int min, int max, Order order)
{
    int diference = std::abs(max - min);
    if (size < diference)
    {
        max = min + size;
        diference = std::abs(max - min);
    }

    std::vector<int> vec;

    if (order == Order::ASC)
    {
        int remaining = size % diference;
        vec.assign(size / diference + (remaining-- > 0 ? 1 : 0), min);
        for (int x = min + 1; x < max; x++)
        {
            vec.insert(vec.end(), size / diference + (remaining-- > 0 ? 1 : 0), x);
        }
    }
    else
    {
        int remaining = size % diference;
        vec.assign((size / diference + (remaining-- > 0 ? 1 : 0)), max - 1);
        for (int x = max - 2; x >= min; x--)
        {
            vec.insert(vec.end(), size / diference + (remaining-- > 0 ? 1 : 0), x);
        }
    }

    return vec;
}