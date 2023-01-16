<?php

// Lesson 3. Time Complexity - FrogJmp

function solution($X, $Y, $D)
{
    $answer = 0;

    if ($X === $Y) {
        $answer = 0;
    } else {
        $answer = (int)(($Y - $X) / $D);
        if (($Y - $X) % $D !== 0) {
            $answer++;
        }
    }

    return $answer;
}
