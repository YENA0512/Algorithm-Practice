// 프로그래머스 Lv 2 이진 변환 반복하기

function solution(s) {
  var a = 0; //delete zero
  var b = 0; //count
  while (s.length !== 1) {
    const originLen = s.length;
    s = s
      .split("")
      .filter((e) => e === "1")
      .join("");
    const newLen = s.length;
    a += originLen - newLen;
    s = newLen.toString(2);
    b++;
  }

  return [b, a];
}
