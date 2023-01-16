<?php

// Lesson 2. Arrays - CyclicRotation

function solution($A, $K)
{
    $answer = [];

    if (!empty($A)) {
        $K %= count($A);

        if ($K === 0) {
            $answer = $A;
        } else {
            $right = array_slice($A, -$K);
            $left = array_slice($A, 0, -$K);
            $answer = array_merge($right, $left);
        }
    }

    return $answer;
}
