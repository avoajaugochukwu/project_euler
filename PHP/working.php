<?php

	$number = 11322;
	$new_list = [];
	for($i = 1; $i <= $number; $i++)
	{
		if ($number % $i == 0)
		{
			$new_list[] += $i;
		}
	}

	foreach ($new_list as $i)
	{
		$count = 0;
		for ($j=1; $j <= $i ; $j++) { 
			if ($i % $j == 0)
			{
				$count += 1;
			}
		}
		if ($count == 2)
		{
			echo $i;
		}
	}