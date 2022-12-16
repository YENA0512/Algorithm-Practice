// 프로그래머스 Lv 2 최댓값과 최솟값
function solution(s) {
  var answer = "";

  var arr = s.split(" ");
  var arr2 = [];
  arr.forEach((e) => {
    e = parseInt(e);
    arr2.push(e);
  });
  arr2.sort();
  var max = Math.max.apply(null, arr2);
  var min = Math.min.apply(null, arr2);
  answer = min + "" + (" " + max + "");
  return answer;
}

// 다른 풀이
const arr = s.split(" ");
return Math.min(...arr) + " " + Math.max(...arr);
