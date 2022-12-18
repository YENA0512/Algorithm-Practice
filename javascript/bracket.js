// 프로그래머스 Lv 2 올바른 괄호

function solution(s) {
  var answer = true;
  var arr = [];
  for (const e of s) {
    if (e == "(") {
      arr.push(e);
    } else {
      if (arr.length === 0) {
        answer = false;
      }
      arr.pop();
    }
  }
  if (arr.length != 0) {
    answer = false;
  }
  return answer;
}

// 다른 풀이
let cum = 0;
for (const e of s) {
  cum += e === "(" ? 1 : -1;
  if (cum < 0) {
    return false;
  }
}
return cum === 0 ? true : false;
