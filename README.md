# [Baekjoon](https://www.acmicpc.net) Algorithm

<p>
  <a href="https://solved.ac/dlsdudg15">
    <img align="center" src="http://mazassumnida.wtf/api/v2/generate_badge?boj=dlsdudg15" alt="PIYoung's baekjoon stat" />
  </a>
  &nbsp;
  <a href="https://solved.ac/dlsdudg15">
    <img align="center" src="http://mazandi.herokuapp.com/api?handle=dlsdudg15&theme=dark" alt="PIYoung's baekjoon stat" />
  </a>
</p>

<table>
  <thead>
    <tr>
      <th><span>언어</span></th>
      <th><span>맞았습니다</span></th>
      <th><span>출력 형식</span></th>
      <th><span>틀렸습니다</span></th>
      <th><span>시간 초과</span></th>
      <th><span>메모리 초과</span></th>
      <th><span>출력 초과</span></th>
      <th><span>런타임 에러</span></th>
      <th><span>컴파일 에러</span></th>
      <th><span>채점 불가</span></th>
      <th><span>맞은 문제</span></th>
      <th><span>제출</span></th>
      <th><span>정답 비율</span></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Python3</th>
      <td>218</td>
      <td>1</td>
      <td>58</td>
      <td>23</td>
      <td>2</td>
      <td>1</td>
      <td>20</td>
      <td>2</td>
      <td></td>
      <td>215</td>
      <td>325</td>
      <td>68.910%</td>
    </tr>
    <tr>
      <th>node.js</th>
      <td>106</td>
      <td>5</td>
      <td>57</td>
      <td>13</td>
      <td>4</td>
      <td></td>
      <td>23</td>
      <td></td>
      <td></td>
      <td>98</td>
      <td>208</td>
      <td>49.746%</td>
    </tr>
    <tr>
      <th>Java 8</th>
      <td>1</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>1</td>
      <td>1</td>
      <td>100.000%</td>
    </tr>
    <tr>
      <th>Java 11</th>
      <td>1</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>2</td>
      <td></td>
      <td>1</td>
      <td>3</td>
      <td>100.000%</td>
    </tr>
    <tr>
      <th>C++17</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>3</td>
      <td></td>
      <td>0</td>
      <td>3</td>
      <td>0.000%</td>
    </tr>
  </tbody>
</table>

## Python3

```python3
import sys

# 공백으로 구분된 2개 숫자 입력 받기
N, M = map(int, sys.stdin.readline().split())
  
# 여러 줄 입력 받기
n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(n)]
  
# 문자열 입력 받기
data = sys.stdin.readline().rstrip()
```

## NodeJS

```javascript
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString();

// 한 줄 입력 받기
input.split(' ');

// 여러 줄 입력 받기
input.split('\n');
```
