# Chapter 3. Inner Product Spaces and Least Squares

Two measurements of the same distance read 2 and 4. A model that predicts $(x,x)$ cannot match both. Choosing how to measure the residual turns this inconsistent system into a well-defined approximation problem.

## 3.1 Norms and Normed Spaces

A norm is nonnegative, vanishes only at zero, satisfies $\|\alpha x\|=|\alpha|\|x\|$, and obeys the triangle inequality. For a residual $r$, the one-norm sums absolute errors, the two-norm measures Euclidean distance, and the maximum norm reports the largest absolute error.

With readings 2 and 4, minimizing $|x-2|+|x-4|$ gives every $x$ in $[2,4]$: the sum is exactly 2 throughout. Minimizing the sum of squares gives a unique estimate, 3. The choice of norm can change both the estimate and its uniqueness.

## 3.2 Inner Products

A real inner product is symmetric, bilinear, and positive definite. Over complex scalars, conjugate symmetry and conjugation in one argument replace real symmetry and bilinearity. The induced norm is $\|u\|=\sqrt{\langle u,u\rangle}$. Cauchy–Schwarz gives $|\langle u,v\rangle|\le\|u\|\|v\|$. When $\langle u,v\rangle=0$, expanding the square gives $\|u+v\|^2=\|u\|^2+\|v\|^2$.

For continuous real trajectories on $[0,1]$, use $\langle f,g\rangle=\int_0^1 f(t)g(t)\,dt$. The functions $1$ and $t-1/2$ are orthogonal because the positive and negative signed areas of $t-1/2$ cancel.

## 3.3 Gram–Schmidt Orthogonalization

Given linearly independent real vectors $a_1,\dots,a_n$, construct the next direction by removing its components along the orthonormal directions already found:

$$
u_j=a_j-\sum_{i<j}\langle q_i,a_j\rangle q_i,\qquad q_j=u_j/\|u_j\|.
$$

For $a_1=1$ and $a_2=t$ with the integral inner product, $q_1=1$, $\langle 1,t\rangle=1/2$, and $\|t-1/2\|^2=1/12$. The second unit direction is $\sqrt{12}(t-1/2)$. Both bases span the same affine functions of time.

An exactly zero remainder signals dependence. In floating-point arithmetic near-dependent inputs can lose orthogonality. Modified Gram–Schmidt projects the progressively updated remainder onto each successive direction.

## 3.4 The Projection Theorem and Normal Equations

For a finite-dimensional subspace $M$, a vector $p\in M$ is the closest point to $b$ exactly when $b-p$ is orthogonal to $M$. To see sufficiency, take any $m\in M$. Orthogonality gives $\|b-m\|^2=\|b-p\|^2+\|p-m\|^2$. For necessity, move a candidate minimizer in any direction $v\in M$ and differentiate $\|b-p-tv\|^2$ at $t=0$.

For $M=\operatorname{col}A$, this condition becomes $A^T A\hat x=A^Tb$. In the distance example the model column is $(1,1)^T$ and $b=(2,4)^T$. The normal equation is $2\hat x=6$. The residual $(-1,1)^T$ is orthogonal to the model column, directly verifying optimality. Dependent columns still give a unique projected vector $A\hat x$, even when several parameter vectors produce it.

## 3.5 Symmetric and Orthogonal Matrices

The spectral theorem gives $H=U\Lambda U^T$ for real symmetric $H$, where $U^TU=I$ and $\Lambda$ contains real eigenvalues. Eigenvectors for distinct eigenvalues are orthogonal: if $Hv=\lambda v$ and $Hw=\mu w$, symmetry equates $v^THw$ with $(Hv)^Tw$, giving $(\mu-\lambda)v^Tw=0$. Inside a repeated eigenspace one can choose an orthonormal basis.

An orthogonal coordinate change preserves lengths because $\|Uz\|^2=z^TU^TU z$. In these coordinates a quadratic cost $x^THx$ separates into $\sum_i\lambda_i z_i^2$, where $z=U^Tx$.

## 3.6 Quadratic Forms, Positive Definiteness, and Schur Complements

A symmetric matrix is positive definite if $x^THx>0$ for every nonzero $x$, equivalently if all its eigenvalues are positive. Positive semidefiniteness allows zero eigenvalues. For a symmetric block matrix with top-left block $A\succ0$, completing the square gives

$$
x^TAx+2x^TBy+y^TCy
=(x+A^{-1}By)^TA(x+A^{-1}By)+y^T(C-B^TA^{-1}B)y.
$$

The full matrix is positive definite precisely when its **Schur complement** $C-B^TA^{-1}B$ is positive definite. For $\left[\begin{smallmatrix}4&2\\2&c\end{smallmatrix}\right]$, the threshold is $c>1$. At $c=1$ the cost equals $(2x+y)^2$, which vanishes along an entire line.

## 3.7 Least Squares Problems

**Weighted observations.** Minimize $(b-Ax)^TW(b-Ax)$ with $W\succ0$. Orthogonality in this weighted inner product gives $A^TWA\hat x=A^TWb$. For the two distance readings, weights 1 and $1/4$ give $\hat x=(2+4/4)/(1+1/4)=2.4$. The first reading now carries four times the weight of the second.

**An exact constraint with many solutions.** For full-row-rank $A$, minimize $x^TWx$ subject to $Ax=b$. Stationarity gives $Wx=A^T\lambda$ after scaling the multiplier. Substitution gives $x=W^{-1}A^T(AW^{-1}A^T)^{-1}b$. With $W=I$ and $x_1+x_2=6$, the minimum-norm allocation is $(3,3)$.

**Recursive least squares.** Once the accumulated normal matrix $H$ is invertible, keep $P=H^{-1}$ and the current estimate. For one new scalar reading $y$ with model row $a^T$ and weight $w>0$, the new normal matrix is $H+waa^T$. Applying the rank-one inverse identity gives

$$
K=\frac{Pa}{w^{-1}+a^TPa},\qquad
\hat x_{\rm new}=\hat x+K(y-a^T\hat x),\qquad
P_{\rm new}=P-Ka^TP .
$$

The scalar in parentheses is the discrepancy of the new measurement. Starting from the single reading 2 with unit weight gives $P=1$. Adding 4 with weight $1/4$ gives $K=1/5$ and the same estimate 2.4 as the batch calculation.
