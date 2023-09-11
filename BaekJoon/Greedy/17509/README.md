## 문제
Let us remind you about how the total penalties are calculated for this contest:

When you solve a problem at 
$T$ minutes, 
$T+20V$ is added to your penalty, where 
$V$ is the number of incorrect verdicts (except compile errors) received on that problem.
If you do not solve a problem before the contest ends, the incorrect verdicts on that problem are not counted as penalties.
Here is a bad news for all of you: we, the problem setters, are planning to join the competition and solve our own problems!

We know our problems really well, so we can solve all the problems before the contest ends. Furthermore, we can precisely predict how long it takes to solve each problem, and how many incorrect verdicts (except compile errors) we get in each problem. Depending on the order of the problems we solve, our total penalty might differ. What is the minimum penalty if we solve all problems?

## 입력

11 lines are given as the input. The 
$i$-th line contains two space-separated integers, 
$D_i$ and 
$V_i$, where 
$D_i$ is the amount of minutes required to solve the 
$i$-th problem, and 
$V_i$ is the number of incorrect verdicts on the 
$i$-th problem.

For each 
$i$, 
$1 \leq D_i$ and 
$0 \leq V_i \leq 1\ 000$. Also, 
$\sum_{i=1}^{11} D_i \leq 300$.


## 출력
Output the minimum penalty if we solve all problems.

## 예제 입력 

### 입력
```
20 1
20 0
20 3
10 0
10 0
10 0
30 0
30 0
30 0
20 0
20 10
```
### 출력
```
1360
```