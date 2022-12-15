// 프로그래머스 Lv 1 문자열 내 p와 y의 개수

function solution(s) {
  var answer = true;
  var a = (b = 0);
  s.split("").forEach((e) => {
    if (e === "p" || e === "P") a += 1;
    if (e === "y" || e === "Y") b += 1;
  });
  console.log(a, b);
  if (a !== b) answer = false;
  return answer;
}

//다른 풀이
return s.toUpperCase().split("P").length === s.toUpperCase().split("Y").length;
