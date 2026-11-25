# Chapter 2. Abstract Linear Algebra

A robot's reference trajectory can be a vector in a space of functions. Choosing a basis turns that trajectory into a list of coefficients. Which properties belong to the trajectory, and which depend on the list? We will use a short polynomial trajectory to track the distinction.

## 2.1 Fields and Vector Spaces

A **field** supplies scalars with addition, subtraction, multiplication, and division by any nonzero element. The real and complex numbers are fields. The integers fail the division test: the equation $2a=1$ has no integer solution.

A **vector space** over a field is closed under addition and scalar multiplication, with a zero vector, additive inverses, and the usual associative and distributive laws. For example, let $\mathcal P_2$ contain the real polynomials of degree at most two, including zero. Adding two such trajectories or scaling one keeps the result in $\mathcal P_2$. Polynomials of *exactly* degree two fail this test because their leading terms can cancel.

## 2.2 Subspaces

A nonempty subset $W$ of a vector space is a subspace precisely when $\alpha u+\beta v\in W$ for all $u,v\in W$ and all scalars $\alpha,\beta$. The remaining vector-space laws are inherited from the ambient space.

**Test a trajectory constraint.** The constraint $p(0)=0$ defines a subspace of $\mathcal P_2$: evaluating a linear combination at zero gives $\alpha p(0)+\beta q(0)=0$. The constraint $p(0)=1$ defines a translate of that subspace. It excludes the zero trajectory. In matrix language, this is the distinction between the kernel $Ax=0$ and the feasible set $Ax=b$ with $b\ne0$.

## 2.3 Linear Combinations and Independence

The **span** of a set contains every finite linear combination of its elements. Vectors are independent when $\sum_i a_iv_i=0$ forces each $a_i=0$. A dependence relation with $a_j\ne0$ expresses $v_j$ as a combination of the remaining vectors, so removing it preserves the span.

For polynomials, $a+bt+ct^2=0$ as a function means the equality holds at every $t$. Evaluating at $0,1,-1$ gives $a=0$, $b+c=0$, and $-b+c=0$, forcing all three coefficients to vanish. The choice of field matters too: $1,i$ are independent over the reals, while complex scalars permit $i\cdot1-1\cdot i=0$.

## 2.4 Bases and Dimension

An ordered **basis** spans the space and is linearly independent. Spanning gives existence of coordinates. Independence gives uniqueness: subtract two representations and the resulting zero combination forces the coefficient lists to agree.

The ordered basis $(1,t,t^2)$ makes $\dim\mathcal P_2=3$. In a space of dimension $n$, any $n$ independent vectors form a basis. To extend a shorter independent list, add a vector outside its span and repeat. All polynomials of unrestricted degree form an infinite-dimensional space because the list of independent monomials can grow without bound.

## 2.5 Coordinates and Change of Basis

Let $E=(1,t,t^2)$ and $B=(1,t,1+t^2)$. Write the columns of $S$ as the coordinates of the $B$ basis vectors in $E$. For $p(t)=2-t+3t^2$ this gives

$$
S=\begin{bmatrix}1&0&1\\0&1&0\\0&0&1\end{bmatrix},
\qquad [p]_E=S[p]_B,\qquad
[p]_E=(2,-1,3)^T,\quad [p]_B=(-1,-1,3)^T .
$$

Check the direction by reconstructing $p=-1-t+3(1+t^2)$. To convert from $E$ to $B$, solve $Sc=[p]_E$. Reversing the direction of the basis change is a common source of coordinate errors.

## 2.6 Linear Operators and Matrix Representations

A map $L$ is linear if $L(\alpha u+\beta v)=\alpha L(u)+\beta L(v)$. Its action on a basis determines its action everywhere. For differentiation on $\mathcal P_2$, the images of $1,t,t^2$ are $0,1,2t$. Placing their coordinates in columns gives

$$
D_E=\begin{bmatrix}0&1&0\\0&0&2\\0&0&0\end{bmatrix}.
$$

Multiplying by $(2,-1,3)^T$ returns $(-1,6,0)^T$, the coefficients of the velocity $-1+6t$. In the other basis the same operator has matrix $D_B=S^{-1}D_ES$: convert input coordinates to $E$, differentiate, then convert the output back.

## 2.7 Eigenvalues, Eigenvectors, and Diagonalization

An eigenpair satisfies $Av=\lambda v$ with $v\ne0$. The characteristic equation $\det(\lambda I-A)=0$ supplies candidate eigenvalues. For each one, solve $(A-\lambda I)v=0$ to find its eigenspace. If $V$ contains a basis of eigenvectors, $AV=V\Lambda$ and $A^k=V\Lambda^kV^{-1}$. Powers then reduce to scalar powers along the eigenvectors.

Distinct eigenvalues give independent eigenvectors. A repeated eigenvalue requires checking the eigenspace dimension. The differentiation matrix above is triangular with three zero eigenvalues, but only constant polynomials have zero derivative. Its eigenspace has dimension one, so no eigenvector basis exists.

## 2.8 Rank and Null Spaces

The rank is the dimension of the image. For $A$ with $n$ columns, $\operatorname{rank}A+\dim\ker A=n$. An observation $b$ can be explained exactly when $b$ belongs to the image. Given one solution $x_0$, every solution has the form $x_0+z$ with $Az=0$. For differentiation, rank two and nullity one explain why a velocity determines a quadratic trajectory only up to an additive constant.

For real $A$, $x^TA^TAx=\|Ax\|_2^2$, so $A^TA$ and $A$ have the same kernel. Thus $A^TA$ is invertible exactly when the columns of $A$ are independent. This is the rank test behind the [least squares normal equations](ch3.md).

**A reusable matrix identity.** With invertible $M$ and $1+v^TM^{-1}u\ne0$, a rank-one change has inverse
$$
(M+uv^T)^{-1}=M^{-1}-\frac{M^{-1}uv^TM^{-1}}{1+v^TM^{-1}u}.
$$
Multiplying by $M+uv^T$ cancels the correction terms. When one sensor observation adds a single outer product to a normal matrix, this identity updates the inverse using the old one.
