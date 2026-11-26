# Chapter 2. Linear Operators, Projection, and Singular Values

The reachable states of a linear plant form the range of a map from inputs to states. Initial states that produce no measured output form the kernel of another map. The same geometry answers two practical questions in calibration and control allocation.

## Spaces, bases, and coordinate changes

A vector space is closed under addition and scalar multiplication over its chosen field. For instance, real polynomials of degree at most two have basis $(1,s,s^2)$. Differentiation is linear on this space, has range $\operatorname{span}(1,s)$ and kernel $\operatorname{span}(1)$. The dimensions add to three, illustrating rank–nullity. A map is injective exactly when its kernel is trivial and surjective when its range is the full codomain.

A basis matrix $T$ carries new coordinates $z$ to old coordinates $x=Tz$. For constant invertible $T$, substitution into the state equations gives

$$
A_z=T^{-1}AT,\qquad B_z=T^{-1}B,\qquad C_z=CT,\qquad D_z=D.
$$

Thus the physical output is identical in either coordinate system. For a map between *different* spaces, use the basis of each space separately. If $S$ contains the output basis vectors in old coordinates, the map in the new coordinates is $S^{-1}AT$.

## Inner products, adjoints, and projection

The adjoint satisfies $\langle Ax,y\rangle=\langle x,A^*y\rangle$. In Euclidean orthonormal coordinates $A^*$ is the conjugate transpose. Hence $y\in\ker A^*$ exactly when $y$ is orthogonal to every $Ax$. Likewise $\ker A=(\operatorname{range} A^*)^\perp$. These identities separate attainable outputs from residuals and identifiable parameters from invisible ones.

For a basis of a measurement subspace, Gram–Schmidt subtracts the projections of each new basis vector onto all previous orthonormal vectors, then normalizes the remainder. If $Q$ contains the resulting orthonormal columns, $QQ^*b$ is the closest point in the subspace to $b$. Least squares therefore asks for $A^*(b-A\hat x)=0$. With readings $b=(2,4)^T$ of one constant offset and $A=(1,1)^T$, the fit is $\hat x=3$. The residual $(-1,1)^T$ is orthogonal to $A$.

## Minimum effort and the SVD

For an actuator array $Au=b$ with full row rank, many commands can achieve the requested effort. Minimizing $u^*R u$ with $R$ positive definite gives

$$
u_{\min}=R^{-1}A^*(AR^{-1}A^*)^{-1}b.
$$

Stationarity puts $Ru$ in the range of $A^*$, and enforcing $Au=b$ fixes the multiplier. For two actuators with $u_1+u_2=1$ and cost $u_1^2+4u_2^2$, this gives $(4/5,1/5)$. Any other allocation adds $(d,-d)$ and increases the cost by $5d^2$.

For rank $r$, write the compact singular value decomposition as $A=U_r\Sigma_r V_r^*$. Each input direction $v_i$ maps to $\sigma_i u_i$. The pseudoinverse $A^\dagger=V_r\Sigma_r^{-1}U_r^*$ gives the minimum Euclidean norm among all least-squares solutions, including when $A$ loses rank. The induced two-norm is $\sigma_1$, the largest gain on a unit input. The induced one- and infinity-norms are the largest absolute column sum and row sum, respectively.

**A weak measurement direction.** For $A=\operatorname{diag}(1,0.01)$, a measurement error of $0.01$ along the second axis changes the inferred state by one unit. Keeping only the leading singular direction gives a rank-one approximation with worst-case unit-input error $0.01$, but discards all sensitivity to that second state. This is the tradeoff in SVD truncation.

**Packet guide.** PDF pp. 37–46 and 71–80 cover bases and operators, pp. 107–124 and 154–171 cover orthogonality and inverses, and pp. 309–311 and 337–351 cover the SVD. Further worked projections appear in [Inner Product Spaces and Least Squares](../robotics-math/ch3.md).
