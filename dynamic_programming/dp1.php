<?php

function fibonacci($n) {
    if($n <= 1) return $n;
    return fibonacci($n-1) + fibonacci($n-2);
}

function fibonacci_best(int $n): int {
    static $cache = [];
    if($n <= 1) return $n;
    if(isset($cache[$n])) return $cache[$n];
    return ($cache[$n]=fibonacci_best($n-1)+fibonacci_best($n-2));
}

$r = fibonacci_best(10);

print("\n\n _> value = $r \n\n");

$debug = 1;