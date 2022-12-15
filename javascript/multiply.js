// 프로그래머스 Lv 1 x만큼 간격이 있는 n개의 숫자

function solution(x, n) {
  var answer = [];
  var cnt = 0;
  for (let i = x; ; i += x) {
    if (cnt == n) {
      break;
    }
    console.log(i);
    answer.push(i);
    cnt++;
  }
  return answer;
}

//다른 풀이
return Array(n)
  .fill(x)
  .map((v, i) => (i + 1) * v);
