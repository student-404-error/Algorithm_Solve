/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   14003.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: seong-ki <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/06/09 22:14:00 by seong-ki          #+#    #+#             */
/*   Updated: 2024/06/10 04:24:14 by seong-ki         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>

int	binary_search(int *arr, int value, int left, int right)
{
	int	mid;

	while (left < right)
	{
		mid = (left + right) / 2;
		if (value <= arr[mid])
			right = mid;
		else
			left = mid + 1;
	}
	return (right);
}

int	main(void)
{
	int	n;

	scanf("%d", &n);
	int	arr[n];
	int	result[n];
	int	dp[n];
	for (int i = 0; i < n; i++)
		scanf("%d", &arr[i]);
	for (int i = 0; i < n; i++)
		dp[i] = 1;
	result[0] = arr[0];
	int	length;
	length = 1;
	for (int i = 1; i < n; i++)
	{
		if (arr[i] <= result[0])
		{
			result[0] = arr[i];
			dp[i] = 1;
		}
		else if (arr[i] > result[length - 1])
		{
			result[length++] = arr[i];
			dp[i] = length;
		}
		else
		{
			int idx = binary_search(result, arr[i], 0, length);
			result[idx] = arr[i];
			if (dp[i] < idx + 1)
				dp[i] = idx + 1;
		}
	}
	printf("%d\n", length);
	for (int i = n - 1, len = length; i >= 0; i--)
	{
		if (len == dp[i])
			result[--len] = arr[i];
	}
	for (int i = 0; i < length; i++)
		printf("%d ", result[i]);
	//printf("%d\n", length);
}
