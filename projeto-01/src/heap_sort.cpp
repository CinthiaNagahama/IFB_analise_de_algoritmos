#include "sorting.hpp"
#include <iostream>
#include <algorithm>

void heapify(std::vector<int> &vec, int parent, int end)
{
    int left_child = parent * 2 + 1;
    int right_child = parent * 2 + 2;

    int swap = parent;

    if (left_child <= end && vec[swap] < vec[left_child])
    {
        swap = left_child;
    }
    if (right_child <= end && vec[swap] < vec[right_child])
    {
        swap = right_child;
    }

    if (swap != parent)
    {
        std::swap(vec[parent], vec[swap]);
        heapify(vec, swap, end);
    }
}

void max_heap(std::vector<int> &vec)
{
    for (int parent = (vec.size() - 2) / 2; parent >= 0; parent--)
    {
        heapify(vec, parent, vec.size() - 1);
    }
}

void heap_sort(std::vector<int> &vec)
{
    max_heap(vec);

    for (int end = vec.size() - 1; end > 0;)
    {
        std::swap(vec[0], vec[end]);
        heapify(vec, 0, --end);
    }
}
