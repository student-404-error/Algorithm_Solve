/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   14002_opt.cpp                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: seong-ki <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/06/08 10:36:06 by seong-ki          #+#    #+#             */
/*   Updated: 2024/06/09 18:23:20 by seong-ki         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int	main(void)
{
	int	n;
	cin >> n;
	vector<int>	arr(n);
	vector<int>	dp(n, 1);

	for (int i = 0; i < n; i++)
		cin >> arr[i];

	for (int i = 0; i < n; i++)
		for (int j = 0; j < i; j++)
			if (arr[i] > arr[j])
				dp[i] = max(dp[i], dp[j] + 1);

	int	lis_length = *max_element(dp.begin(), dp.end());
	cout << lis_length << "\n";

	vector<int>	lis_arr(lis_length);
	for (int i = n - 1, len = lis_length; i >= 0; i--)
	{
		if (len == dp[i])
			lis_arr[--len] = arr[i];
	}

	for (int i = 0; i < lis_length; i++)
		cout << lis_arr[i] << " ";
}
