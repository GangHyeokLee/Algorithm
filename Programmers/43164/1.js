function solution(tickets) {
  let answer = [];
  let hash = {}

  tickets.forEach(x => {
    if (hash[x[0]]) {
      hash[x[0]].push(x[1])
    } else {
      hash[x[0]] = [x[1]]
    }
  })

  dfs(hash, 'ICN', answer, ['ICN']);



  return answer.filter(x => x.length == tickets.length + 1).sort()[0]
}

function dfs(hash, start, answer, course) {

  if (hash[start] === undefined) {
    answer.push([...course])
    return;
  }
  // let tmp;
  for (let i = 0; i < hash[start].length; i++) {
    course.push(hash[start][i])
    // tmp = hash[start].filter((_, idx)=>idx!=i)
    // tmp = tmp.length==0?null:tmp
    dfs({ ...hash, [start]: hash[start].filter((_, idx) => idx != i) }, hash[start][i], answer, course)
    course.pop();
  }
}