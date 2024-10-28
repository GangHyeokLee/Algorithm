const input = require("fs").readFileSync(process.platform === "linux" ?
  "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n")
  .map((el) => el.split(" ").map(Number))

n = input[0][0]

const adj = input.slice(1)

const ans = Array.from({ length: n }, () => Array(n).fill(0));

for (let i = 0; i < n; i++) {
  let que = [i]
  let idx = 0
  let visited = Array.from({ length: n }, () => Array(n).fill(true))

  while (idx < que.length) {
    let now = que[idx++]

    for (let next = 0; next < n; next++) {
      if (adj[now][next] === 1 && visited[now][next]) {
        visited[now][next] = false
        que.push(next)
        ans[now][next] = 1
      }
    }
  }

  que.forEach((v, idx) => {
    if (idx > 0) ans[i][v] = 1
  })
}

ans.forEach(row => console.log(row.join(" ")));