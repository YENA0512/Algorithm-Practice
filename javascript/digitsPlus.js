// 프로그래머스 Lv 1 자릿수 더하기

function solution(n) {
  var answer = 0;
  // var arr = [];
  var arr = n.toString().split("");
  for (i of arr) {
    answer += parseInt(i);
  }
  return answer;
}

//reducer
function solution(n) {
  var answer = (n + "")
    .split("")
    .reduce((acc, curr) => (acc + parseInt(curr), 0));
  return answer;
}
