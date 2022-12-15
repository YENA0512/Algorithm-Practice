// 프로그래머스 Lv 1 평균 구하기
function solution(arr) {
  var sum = 0;
  for (n of arr) {
    sum += n;
  }
  console.log(sum);
  var answer = sum / arr.length;
  return answer;
}

// Reduce
function solution(arr) {
  return arr.reduce((a, b) => a + b) / arr.length;
}
