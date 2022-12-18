// 프로그래머스 Lv 2 최솟값 만들기

function solution(A, B) {
  var answer = 0;
  A.sort((a, b) => a - b);
  B.sort((a, b) => b - a);
  A.map((e, idx) => {
    answer += e * B[idx];
  });
  // return A.reduce((acc,cur,idx) => acc + cur*B[idx],0)
  return answer;
}
