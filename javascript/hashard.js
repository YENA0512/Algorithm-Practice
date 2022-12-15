// 프로그래머스 Lv 1 하샤드 수

function solution(x) {
  return (
    x % (x + "").split("").reduce((acc, cur) => acc + parseInt(cur), 0) === 0
  );
}
