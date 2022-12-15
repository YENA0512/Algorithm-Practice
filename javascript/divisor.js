// 프로그래머스 Lv1.약수의 합

function solution(n) {
  var answer = [];
  var m = n;
  var sum = 0;
  while (m > 0) {
    if (n % m == 0) {
      answer.push(m);
    }
    m -= 1;
  }
  for (n of answer) {
    sum += n;
  }
  return sum;
}
