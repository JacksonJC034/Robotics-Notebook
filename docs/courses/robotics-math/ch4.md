# Chapter 4. Matrix Factorizations

A matrix factorization rewrites one difficult operation as several simpler ones. QR uses orthonormal coordinates to solve a fit. SVD exposes poorly measured directions. LU and Cholesky turn repeated square solves into triangular substitutions.

## 4.1 QR Factorization

For a real $m\times n$ matrix with independent columns and $m\ge n$, reduced QR gives $A=QR$, with $Q^TQ=I_n$ and $R$ upper triangular. In Gram–Schmidt, the entries of column $j$ of $R$ are the coefficients of $a_j$ along $q_1,\ldots,q_j$; the diagonal entry is the norm of the remainder before normalization.

The squared residual splits into perpendicular pieces:

$$
\|Ax-b\|_2^2=\|Rx-Q^Tb\|_2^2+\|(I-QQ^T)b\|_2^2 .
$$

Only the first term depends on $x$. Solve $Rx=Q^Tb$ by back substitution. For $A=(1,1)^T$, $Q=(1,1)^T/\sqrt2$ and $R=\sqrt2$. With $b=(2,4)^T$, the triangular system gives $x=3$. The second term is 2, the squared residual that no choice of $x$ can remove. QR obtains the fit without forming $A^TA$, whose two-norm condition number is the square of that of a full-column-rank $A$.

## 4.2 Singular Value Decomposition

For a real $m\times n$ matrix, $A=U\Sigma V^T$ with orthogonal $U,V$ and singular values $\sigma_1\ge\cdots\ge0$ on the rectangular diagonal. Each right singular vector satisfies $Av_i=\sigma_i u_i$ for the corresponding paired direction. Squaring the relation gives $A^TAv_i=\sigma_i^2v_i$. Exactly $r$ positive singular values means rank $r$.

**A weakly observed parameter.** Let $A=\operatorname{diag}(1,0.001)$. An observation error $(0,0.002)^T$ changes the exact solution by $(0,2)^T$. Both columns are independent, yet the second parameter is a thousand times as sensitive as the first to noise of the same size. Numerical rank therefore depends on a tolerance and the units of the problem.

The minimum-norm least squares solution is $\sum_{i=1}^{r}(u_i^Tb/\sigma_i)v_i$. Components of $b$ outside the image become residual. Components of $x$ in the kernel cannot affect the fit, so the minimum-norm solution sets them to zero. Truncating a small positive singular value deliberately discards sensitivity in that direction at the cost of possible bias.

## 4.3 LU Factorization

Gaussian elimination replaces a row by itself minus a multiple of a pivot row. The multipliers form a unit lower triangular matrix $L$ and the final rows form $U$. When rows are exchanged, record their permutation in $P$, giving $PA=LU$. To solve $Ax=b$, apply the same permutation to $b$, then solve $Ly=Pb$ and $Ux=y$.

**Example with a row exchange.** Take $A=\left[\begin{smallmatrix}0&2\\1&3\end{smallmatrix}\right]$ and $b=(4,7)^T$. Swapping the rows gives $U=\left[\begin{smallmatrix}1&3\\0&2\end{smallmatrix}\right]$, $L=I$, and $Pb=(7,4)^T$. The last equation gives $x_2=2$ and the first then gives $x_1=1$. The original leading entry is zero even though the system has a unique solution. A row exchange supplies a usable pivot. With a new load vector and the same matrix, the stored factors remain usable.

## 4.4 Cholesky Factorization

For symmetric positive definite $H$, elimination gives $H=LDL^T$ with unit lower triangular $L$ and positive diagonal $D$. Absorb $\sqrt D$ into the lower factor to get the Cholesky form $H=CC^T$. Positive pivots allow this factorization without row exchanges.

For $H=\left[\begin{smallmatrix}4&2\\2&5\end{smallmatrix}\right]$, the first pivot is 4 and the multiplier is $1/2$. The second pivot is the Schur complement $5-2^2/4=4$. Thus

$$
L=\begin{bmatrix}1&0\\1/2&1\end{bmatrix},\quad
D=\begin{bmatrix}4&0\\0&4\end{bmatrix},\quad
C=\begin{bmatrix}2&0\\1&2\end{bmatrix}.
$$

For $Hx=(6,7)^T$, forward substitution in $Cy=(6,7)^T$ gives $y=(3,2)^T$. Back substitution in $C^Tx=y$ gives $(1,1)^T$. If $H$ is only positive semidefinite, a symmetrically permuted $LDL^T$ can contain zero pivots. For $H=A^TA$, the count of positive diagonal entries of $D$ gives the exact rank of $A$; a singular factor cannot support a unique triangular solve.
