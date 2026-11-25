# Chapter 6. Real Analysis

An iterative solver produces a sequence of estimates. Small updates can be encouraging even when the estimates drift without bound. What evidence proves that they approach a point, that the point is feasible, and that it solves the equation?

## 6.1 Open and Closed Sets in Normed Spaces

In a normed space the open ball $B_r(x)$ contains all $y$ with $\|y-x\|<r$. A point is interior to $S$ when some ball about it lies inside $S$. It is a boundary point if every ball meets both $S$ and its complement. A set is open when all its points are interior and closed when it contains its closure.

Distance to a nonempty set is $d(x,S)=\inf_{s\in S}\|x-s\|$. The condition $d(x,S)=0$ identifies the closure. For allowable travel $S=(0,1]$, the endpoint 0 has distance zero but is infeasible. The boundary is $\{0,1\}$, the interior is $(0,1)$, and the closure is $[0,1]$. Replacing a strict constraint by a closed one changes whether a limiting configuration is allowable.

## 6.2 Newton’s Method

To solve $F(x)=0$, approximate $F(x_k+s)$ by $F(x_k)+J_F(x_k)s$. Solve $J_F(x_k)s_k=-F(x_k)$ and set $x_{k+1}=x_k+s_k$. For a square system, invertibility of the Jacobian gives a unique linearized step. Local quadratic convergence holds near a simple root under suitable smoothness, for example a locally Lipschitz Jacobian and a sufficiently close initial estimate.

For $F(x)=x^2-2$, the update is $x_{k+1}=(x_k+2/x_k)/2$. Starting at 1 gives $1.5$ and then $17/12$. With $r=\sqrt2$, the exact error satisfies $x_{k+1}-r=(x_k-r)^2/(2x_k)$, which explains the rapid decrease near $r$. At zero the linearized step is undefined.

## 6.3 Sequences and Convergence

Convergence $x_k\to x$ means that for every $\varepsilon>0$ there is an index $N$ after which *all* terms satisfy $\|x_k-x\|<\varepsilon$. A limit is unique: if two proposed limits were distance $d>0$ apart, sufficiently late iterates would be within $d/3$ of both, contradicting the triangle inequality.

A point lies in the closure of $S$ exactly when some sequence from $S$ converges to it. To construct such a sequence at a closure point, choose $x_k$ in the intersection of $S$ and the ball of radius $1/k$. An isolated point of $S$ has a neighborhood containing no other member, so a sequence in $S$ converging to that point is eventually constant.

## 6.4 Cauchy Sequences and Completeness

A sequence is Cauchy when for every $\varepsilon>0$ there is an $N$ such that **every pair** of terms beyond $N$ is within $\varepsilon$. Convergence implies this by bounding each term’s distance from the limit by $\varepsilon/2$. The condition $\|x_{k+1}-x_k\|\to0$ alone is weaker: the partial sums of $1/k$ keep growing although their steps vanish.

A space is complete if every Cauchy sequence has a limit in that space. Rational decimal approximations to $\sqrt 2$ are Cauchy in the usual metric but have no rational limit. Euclidean space is complete, as is any closed subset with its inherited distance. Completeness can depend on the norm: continuous functions on a compact interval are complete in the uniform norm; under the integral one-norm, continuous ramps can approach a discontinuous step in integral error.

## 6.5 The Contraction Mapping Theorem

Suppose $T:S\to S$ on a nonempty complete set and $\|T(x)-T(y)\|\le c\|x-y\|$ for one constant $0\le c<1$ throughout $S$. For $x_{k+1}=T(x_k)$ the successive differences shrink geometrically. Summing their tail gives the usable error bound

$$
\|x_m-x_k\|\le\frac{c^k}{1-c}\|x_1-x_0\|,\qquad m>k .
$$

The sequence is Cauchy, so it converges in $S$. Continuity of $T$ makes the limit a fixed point. If two points were fixed, their distance would be at most $c$ times itself, forcing equality of the points.

For $T(x)=(x+2)/3$ on $[0,2]$, the interval maps into itself and $c=1/3$. Iterating from 0 gives $2/3,8/9,\ldots$, with fixed point 1. A stopping certificate follows from the same geometric sum: the remaining error at $x_k$ is at most $\|x_{k+1}-x_k\|/(1-c)$.

## 6.6 Continuous Functions

Continuity at $x$ means that every output tolerance $\varepsilon>0$ admits an input radius $\delta>0$ such that all domain points within that radius have outputs within $\varepsilon$ of $f(x)$. In normed spaces this is equivalent to preserving the limit of every sequence converging to $x$.

To disprove continuity it suffices to find one sequence. A threshold sensor reporting 1 for $x\ge0$ and 0 otherwise jumps at zero: inputs $-1/k$ approach zero but their outputs remain 0, whereas $f(0)=1$. For a positive result, the reverse triangle inequality $|\|x\|-\|y\||\le\|x-y\|$ proves continuity of the norm by taking $\delta=\varepsilon$.

## 6.7 Compact Sets and Extrema

In a metric space compactness is equivalent to every sequence having a subsequence that converges to a point in the set. In finite-dimensional normed spaces, closedness and boundedness together characterize compactness. All norms in a finite-dimensional space are equivalent, so they give the same convergent sequences.

**Why an optimum is attained.** Let $f$ be continuous on a nonempty compact feasible set. Its image is compact in $\mathbb R$, hence bounded. Take feasible points whose costs approach the infimum. Compactness gives a subsequence converging to a feasible point, and continuity makes the cost there equal to the infimum. Applying the same reasoning to $-f$ yields a maximum.

For $f(x)=x^2$ on $(0,1]$, points $1/k$ drive the cost to zero but the optimizer is missing. On $[0,1]$ the same cost attains its minimum at zero. [Convexity](ch7.md) addresses a different question: once a local minimizer exists, when must it be global?
