#include <iostream>
#include <cstdlib>
#include <ctime>
#include <omp.h>

using namespace std;

// Parallel Bubble Sort function
void parallelBubbleSort(int *array, int n)
{
    int i, j;

#pragma omp parallel for private(i, j) shared(array)
    for (i = 0; i < n - 1; i++)
    {
        for (j = 0; j < n - i - 1; j++)
        {
            if (array[j] > array[j + 1])
            {
                // Swap elements
                int temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp;
            }
        }
    }
}
int main()
{
    int n;
    cout << "Enter the size of the array: ";
    cin >> n;

    int *array = new int[n];
    srand(time(0));
    for (int i = 0; i < n; i++)
    {
        array[i] = rand() % 100;
    }

    cout << "Original Array: ";
    for (int i = 0; i < n; i++)
    {
        cout << array[i] << " ";
    }
    cout << endl;

    parallelBubbleSort(array, n);


    cout << "Sorted Array: ";
    for (int i = 0; i < n; i++)
    {
        cout << array[i] << " ";
    }
    cout << endl;

    delete[] array;

    return 0;
}
