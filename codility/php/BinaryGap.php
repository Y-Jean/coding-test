<?
// Lesson 1. Iterations - BinaryGap

function solution ($N)
{
    $answer = 0;
    $binary_num = str_split(decbin($N));

    $count = 0;
    foreach ($binary_num as $num) {
        if ($num == 1) {
            if ($answer < $count) {
                $answer = $count;
            }
            $count = 0;
        } else {
            $count++;
        }
    }

    return $answer;
}
