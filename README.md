//C++ Program to Implement Max Heap
 
#include <iostream.h>

#include <conio.h>

using namespace std;

void max_heapify(int *b, int k, int n)
{
    int i, temp;
    temp = b[k];
    i = 2 * k;
    while (i <= n)
    {
        if (i < n && b[i+1] > b[i])
            i = i + 1;
        if (temp > b[i])
            break;
        else if (temp <= b[i])
        {
            b[i / 2] = b[i];
            i = 2 * i;
        }
    }
    b[i/2] = temp;
    return;
}
void build_maxheap(int *b,int n)
{
    int k;
    for(k = n/2; k >= 1; k--)
    {
        max_heapify(b,k,n);
    }
}
int main()
{
    int n, k, x;
    cout<<"enter no of elements of array\n";
    cin>>n;
    int b[20];
    for (k = 1; k <= n; k++)
    {
        cout<<"enter element"<<(k)<<endl;
        cin>>b[k];
    }
    build_maxheap(b,n);
    cout<<"Max Heap\n";
    for (k = 1; k <= n; k++)
    {
        cout<<b[k]<<endl;
    }
    getch();
}





