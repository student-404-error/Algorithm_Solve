#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int	main(void)
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int	n, oper;
	priority_queue<int> max_heap;
	cin >> n;
	while (n--)
	{
		cin >> oper;
		if (oper == 0)
		{
			if (max_heap.empty())
				cout << "0\n";
			else
			{
				cout << max_heap.top() << '\n';
				max_heap.pop();
			}
		}
		else
			max_heap.push(oper);
	}
}
