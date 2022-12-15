// 프로그래머스 Lv 1 자연수 뒤집어 배열로 만들기

function solution(n) {
  var answer = [];
  var a = (n + "").split("");
  for (let i = a.length - 1; i >= 0; i--) {
    answer.push(parseInt(a[i]));
  }
  return answer;
}

// 다른 풀이
return (n + "")
  .split("")
  .reverse()
  .map((e) => parseInt(e));
