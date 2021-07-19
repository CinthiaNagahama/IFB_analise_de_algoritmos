#include "sorting.hpp"
#include <iostream>

void merge(std::vector<int> &vec, std::vector<int> &v1, std::vector<int> &v2)
{
    auto it_vec = vec.begin();
    auto it_v1 = v1.begin();
    auto it_v2 = v2.begin();

    while (it_v1 != v1.end() && it_v2 != v2.end())
    {
        if (*it_v1 < *it_v2)
        {
            *(it_vec++) = *(it_v1++);
        }
        else
        {
            *(it_vec++) = *(it_v2++);
        }
    }

    while (it_v1 != v1.end())
    {
        *(it_vec++) = *(it_v1++);
    }

    while (it_v2 != v2.end())
    {
        *(it_vec++) = *(it_v2++);
    }
}

void merge_sort(std::vector<int> &vec)
{
    if (vec.size() <= 1)
    {
        return;
    }

    int vec_size = vec.size();
    std::vector<int> v1(vec.begin(), std::prev(vec.end(), vec_size / 2));
    std::vector<int> v2(std::next(vec.begin(), vec_size % 2 == 0 ? vec_size / 2 : vec_size / 2 + 1), vec.end());

    merge_sort(v1);
    merge_sort(v2);

    merge(vec, v1, v2);
}