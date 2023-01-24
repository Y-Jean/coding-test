// Lv 1. 평균 구하기

fun solution(arr: IntArray): Double {
    var answer = 0
    for (num in arr) {
        answer += num
    }
    return answer / arr.size.toDouble()
}

fun main() {
    var a = intArrayOf(1,2,3,4)
    println(solution(a))
}