# Chapter 7. Introduction to Optimization

Three calibration readings for a single offset are 0, 0, and 6. Which offset fits them best? Squared error, total absolute error, and worst-case error give three different answers. Each criterion expresses a different engineering requirement, and each can be written as a convex optimization problem.

## 7.1 Convex Sets and Convex Functions

A feasible set $D$ is convex if $(1-t)x+ty$ remains in $D$ for all $x,y\in D$ and $0\le t\le1$. A convex combination uses nonnegative weights summing to one. All finite convex combinations of a set form its **convex hull**, the smallest convex set containing it. Affine equality constraints and linear inequalities define convex sets, and their intersection remains convex.

A function on a convex domain is convex if
$$
f((1-t)x+ty)\le(1-t)f(x)+tf(y).
$$

**Why local optimality suffices.** Suppose $x$ is locally minimizing but a feasible $y$ has lower cost. For every $0<t\le1$ the segment point is feasible and has cost strictly below $f(x)$. Choosing $t$ arbitrarily small places these better points inside any neighborhood of $x$, a contradiction. Strict convexity further gives at most one minimizer. Existence still needs its own argument: $f(x)=x$ on $(0,1)$ is convex and has no minimizer.

## 7.2 Optimization Notation

For a nonempty feasible set $D$, $\inf_{x\in D} f(x)$ denotes the greatest lower bound of achievable costs. When attained, it equals the minimum. The notation $\arg\min_{x\in D}f(x)$ denotes the set of feasible points attaining that value. Writing $x^*\in\arg\min f$ allows for several optimal decisions.

For example, minimize $(u_1+u_2-3)^2$ subject to $u_1,u_2\ge0$. The minimum cost is zero. The minimizers form the segment from $(3,0)$ to $(0,3)$, representing all nonnegative allocations giving the same total command. A solver can return one point from the segment while the model leaves the split undetermined.

## 7.3 Quadratic Programs

A quadratic program minimizes $\tfrac12 x^THx+g^Tx$ subject to affine equalities, componentwise inequalities, and possibly bounds on each variable. A symmetric $H\succeq0$ makes the objective convex. If $H\succ0$, any attained minimum on a convex feasible set is unique.

**From a residual to a QP.** Expanding $\tfrac12\|Ax-b\|_2^2$ gives $H=A^TA$ and $g=-A^Tb$. The omitted constant $\tfrac12 b^Tb$ affects the reported cost but leaves the optimizing decision unchanged. For a weight matrix $W\succ0$, replace these coefficients by $A^TWA$ and $-A^TWb$.

For the three readings, the unscaled squared error is $2x^2+(x-6)^2=3(x-2)^2+24$. The optimal offset is 2 and the minimum squared error is 24. If calibration limits require $0\le x\le1$, the closest feasible point to 2 is 1, with cost 27. This scalar example also shows why solving the unconstrained normal equations alone can produce an infeasible decision.

## 7.4 Linear Programs and Norm Minimization

A linear program has a linear objective and affine constraints. Absolute values become linear inequalities by adding variables that bound the residuals. With $r=Ax-b$, the two useful formulations are

| Objective | Equivalent linear program |
|---|---|
| Total absolute error $\|r\|_1$ | Minimize $\sum_i s_i$ subject to $-s_i\le r_i\le s_i$ for each $i$. |
| Worst-case error $\|r\|_\infty$ | Minimize $t$ subject to $-t\le r_i\le t$ for each $i$. |

For fixed $x$, the smallest feasible $s_i$ equals $|r_i|$, and the smallest shared $t$ equals $\max_i |r_i|$. This proves equivalence and explains why the first formulation needs one auxiliary variable per residual while the second needs only one in total. Additional affine constraints on $x$ can be carried into either formulation.

**Compare the three fits.** For the unconstrained offset data $0,0,6$, total absolute error is $2|x|+|x-6|$. On $[0,6]$ it equals $6+x$ and outside this interval it exceeds 6. The unique minimizer is 0, the median. For worst-case error, $|x|$ and $|6-x|$ cannot both be below 3 because their sum is at least 6. At $x=3$ both equal 3, attaining this lower bound.

| Fit criterion | Offset | Engineering interpretation |
|---|---:|---|
| Sum of squared errors | 2 | The large residual pulls the estimate toward the distant reading. |
| Sum of absolute errors | 0 | The two agreeing readings determine the median. |
| Maximum absolute error | 3 | The offset balances the errors at the two extremes. |

The observations and model are identical in all three fits. The requirement on residuals determines which estimate is optimal.
