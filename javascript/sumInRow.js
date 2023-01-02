//프로그래머스 LV2. 숫자의 표현

function solution(n) {
  var answer = 0;
  var clone = n;
  while (clone != 0) {
    if (n % clone == 0 && clone % 2 != 0) {
      answer += 1;
    }
    clone -= 1;
  }
  return answer;
}

//연속된 자연수의 합 갯수 구하기 = 홀수 약수의 갯수
