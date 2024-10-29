const input = require("fs").readFileSync(process.platform === "linux" ?
  "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n")
  .map((el) => el.split(" ").map(Number));

const [n, m] = input[0];

const bacon = Array.from({ length: (n + 1) }, () => Array(n + 1).fill(0));
const adj = Array.from({ length: (n + 1) }, () => Array(0));

for (let i = 1; i <= m; i++) {
  const [a, b] = input[i];
  adj[a].push(b);
  adj[b].push(a);
}

const ans = [0, 3000 * n * m];

for (let i = 1; i < n + 1; i++) {
  const que = [[i, 0]]
  let idx = 0;

  const visited = Array(n + 1).fill(true);
  visited[i] = false;
  let tmp = 0;

  while (idx < que.length) {
    [now, count] = que[idx++];
    adj[now].forEach((next) => {
      if (visited[next]) {
        visited[next] = false;
        que.push([next, count + 1])
        tmp += count + 1;
      }
    });
  }

  if (ans[1] > tmp) {
    ans[0] = i;
    ans[1] = tmp;
  }
}


console.log(ans[0])