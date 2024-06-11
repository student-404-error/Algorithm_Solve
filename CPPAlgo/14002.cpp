/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   14002.cpp                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: seong-ki <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/06/08 10:36:06 by seong-ki          #+#    #+#             */
/*   Updated: 2024/06/09 17:51:43 by seong-ki         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>

using namespace std;
int	main(void)
{
	int	n;
	
	cin >> n;
	int	arr[n];
	int	dp[n] = {0, };
	int	max;

	dp[n] = -1;
	for (int i = 0; i < n; i++)
		cin >> arr[i];
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < i; j++)
		{
			if (arr[i] > arr[j])
			{
				if (dp[i] < dp[j] + 1)
					dp[i] = dp[j] + 1;
			}
		}
	}
	max = dp[0];
	for (int i = 0; i < n; i++)
	{
		if (dp[i] > max)
			max = dp[i];
	}
	int	lis_arr[max + 1] = {0, };
	int	idx;

	idx = max;
	cout << max + 1 << "\n";
	for (int i = n - 1; i >= 0; i--)
	{
		if (idx == dp[i])
		{
			lis_arr[idx] = arr[i];
			idx--;
		}
	}
	for (int i = 0; i < max; i++)
		cout << lis_arr[i] << " ";
	cout << lis_arr[max] << "\n";
}
