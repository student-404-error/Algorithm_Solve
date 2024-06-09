/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   11053.cpp                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: seong-ki <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/06/08 10:36:06 by seong-ki          #+#    #+#             */
/*   Updated: 2024/06/09 16:08:48 by seong-ki         ###   ########.fr       */
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
	int	i;

	i = 0;
	while (i < n)
	{
		cin >> arr[i];
		i++;
	}
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < i; j++)
		{
			if (arr[i] > arr[j])
			{
				if (dp[i] > dp[j] + 1)
					dp[i] = dp[i];
				else
					dp[i] = dp[j] + 1;
			}
		}
	}
	i = 0;
	int	max;
	max = dp[0];
	while (i < n)
	{
		if (dp[i] > max)
			max = dp[i];
		i++;
	}
	cout << max + 1 << "\n";
}
