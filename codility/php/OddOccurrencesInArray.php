<?
// Lesson 2. Arrays - OddOccurrencesInArray

function solution ($A)
{
    $answer = 0;

    sort($A);

    while (1) {
        if (count($A) == 1) {
            $answer = $A[0];
            break;
        } else {
            if ($A[0] !== $A[1]) {
                $answer = $A[0];
                break;
            }

            $A = array_slice($A, 2);
        }
    }

    return $answer;
}
/*
function solution($A) {
    $answer = 0;

    $A = array_count_values($A);
    foreach($A as $number => $count) {
        if ($count % 2) {
            $answer = $number;
            break;
        }
    }
    
    return $answer;
}
*/