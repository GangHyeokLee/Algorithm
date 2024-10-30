const input = require('fs').readFileSync(process.platform === 'linux'
  ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n")
  .map((x) => x.split(" ").map(Number));

const n = input[0][0]

const friend = Array.from({ length: n + 1 }, () => Array())

for (let i = 1; i < input.length - 1; i++) {
  [a, b] = input[i];
  friend[a].push(b);
  friend[b].push(a);
}

const score = Array(n + 1).fill(100);

for (let i = 1; i <= n; i++) {
  const que = [[i, 0]]
  let idx = 0;
  const visited = Array(n + 1).fill(true);
  visited[i] = false;

  while (idx < que.length) {
    const [now, count] = que[idx++];
    friend[now].forEach((val, idx) => {
      if (visited[val]) {
        visited[val] = false;
        que.push([val, count + 1]);
      }
    })
  }
  score[i] = Math.max(...que.map((x) => x[1]));
}

const ans = Math.min(...score);
let count = 0;
const candi = [];

for (let i = 1; i <= n; i++) {
  if (score[i] === ans) {
    count++;
    candi.push(i);
  }
}

console.log(ans, count);
console.log(candi.join(" "));