// 프로그래머스 Lv 2 JadenCase 문자열 만들기

function solution(s) {
  var answer = "";
  s = s.toLowerCase();
  var arr = s.split(" ");
  var answer = arr
    .map((e) => {
      var arr3 = e.split("");
      if (arr3[0] != null) {
        arr3[0] = arr3[0].toUpperCase();
      }
      return arr3.join("");
    })
    .join(" ");
  return answer;
}

//다른 풀이
function solution(s) {
  return s
    .split(" ")
    .map((v) => v.charAt(0).toUpperCase() + v.substring(1).toLowerCase())
    .join(" ");
}
