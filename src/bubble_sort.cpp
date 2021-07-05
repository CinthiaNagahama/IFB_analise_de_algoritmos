#include "sorting.hpp"

void bubble_sort(std::vector<int> &v)
{
    int n = v.size();
    bool swap = true;
    for (int i = 0; i < (n - 1) && swap; i++)
    {
        swap = false;
        for (int j = 0; j < (n - i - 1); j++)
        {
            if (v[j] > v[j + 1])
            {
                std::swap(v[j], v[j + 1]);
                swap = true;
            }
        }
    }
}