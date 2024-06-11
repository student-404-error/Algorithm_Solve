/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   12015.cpp                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: seong-ki <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/06/09 22:14:00 by seong-ki          #+#    #+#             */
/*   Updated: 2024/06/10 02:29:22 by seong-ki         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int	findLISLength(vector<int>& arr)
{
	if (arr.empty()) return (0);

	vector<int>	lis;
	for (int i = 0; i < arr.size(); ++i)
	{
		auto it = lower_bound(lis.begin(), lis.end(), arr[i]);
		if (it == lis.end())
			lis.push_back(arr[i]);
		else
			*it = arr[i];
	}
	return (lis.size());
}

int	main(void)
{
	int	n;
	cin >> n;
	vector<int>	arr(n);

	for (int i = 0; i < n; i++)
		cin >> arr[i];
	int	length = findLISLength(arr);
	cout << length << "\n";
	return (0);
}
