# Chapter 3. Modes and State Response

A state trajectory has two contributions. The initial condition evolves even when the actuator is off. Each subsequent input changes the state, and that change evolves for the remaining time. The state-transition matrix propagates both contributions.

## Eigenvectors and Jordan chains

For an eigenvector $v$ of a constant matrix $A$ with eigenvalue $\lambda$, $x(t)=e^{\lambda t}v$ solves $\dot x=Ax$. If $A=V\Lambda V^{-1}$ has a full eigenbasis, $e^{At}=V e^{\Lambda t}V^{-1}$. For a real matrix, a conjugate pair $\alpha\pm i\beta$ gives real oscillatory solutions with envelope $e^{\alpha t}$.

The algebraic multiplicity of $\lambda$ counts its appearances in the characteristic polynomial. The geometric multiplicity $\dim\ker(A-\lambda I)$ counts independent eigenvectors. When the latter is smaller, a generalized eigenvector $w$ with $(A-\lambda I)w=v$ provides the solution $e^{At}w=e^{\lambda t}(w+tv)$. More generally, for a Jordan block $J=\lambda I+N$ of size $d$, $N^d=0$ and

$$
e^{Jt}=e^{\lambda t}\sum_{j=0}^{d-1}\frac{t^j}{j!}N^j.
$$

The longest block at each eigenvalue determines its exponent in the minimal polynomial. By Cayley–Hamilton, the characteristic polynomial annihilates $A$, so analytic functions of $A$ can also be computed with a polynomial of degree below $n$. For the moving axis, $A^2=0$ immediately gives $e^{At}=I+tA$. Acting on initial velocity produces the position term $t v(0)$.

## Transition matrices and forcing

For continuous $A(t)$, the transition matrix satisfies $\partial_t\Phi(t,s)=A(t)\Phi(t,s)$ and $\Phi(s,s)=I$. A matrix $X(t)$ of independent homogeneous solutions gives $\Phi(t,s)=X(t)X(s)^{-1}$. Propagating in two stages yields $\Phi(t,r)\Phi(r,s)=\Phi(t,s)$ and hence $\Phi(s,t)=\Phi(t,s)^{-1}$. Variation of constants gives

$$
x(t)=\underbrace{\Phi(t,t_0)x_0}_{\text{zero-input state}}
+\underbrace{\int_{t_0}^{t}\Phi(t,\tau)B(\tau)u(\tau)\,d\tau}_{\text{zero-state contribution}}.
$$

Differentiating reproduces the state equation because the integral's upper endpoint contributes $B(t)u(t)$. For LTI dynamics $\Phi(t,s)=e^{A(t-s)}$, also obtainable by inverse Laplace transform of $(sI-A)^{-1}$. For LTV dynamics, writing $\Phi(t,s)=\exp(\int_s^t A(\tau)d\tau)$ requires extra conditions, for example pairwise commuting coefficient matrices.

**Time-varying rotation.** Let $A(t)=\omega(t)J$ with $J=\left[\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right]$. The matrices commute here. Since $J^2=-I$, the transition is $I\cos\theta+J\sin\theta$ where $\theta=\int_s^t\omega(\tau)d\tau$. Starting at $(1,0)^T$ gives $(\cos\theta,\sin\theta)^T$ with constant length even when the angular speed changes.

## Sampled evolution

For $x_{k+1}=A_k x_k+B_k u_k$, define $\Phi(k,j)=A_{k-1}\cdots A_j$ for $k>j$, and $\Phi(j,j)=I$. Then

$$
x_k=\Phi(k,0)x_0+\sum_{j=0}^{k-1}\Phi(k,j+1)B_j u_j.
$$

The most recent command enters with the identity because it has experienced no subsequent state update. For LTI dynamics the factors become $A^k$ and $A^{k-1-j}$. With singular $A_k$, the forward update remains defined, but different initial states may merge after a sample.

**Packet guide.** PDF pp. 246–258 and 268–281 develop repeated eigenvalues, matrix functions, and Jordan form. Pages 295–308 compare five ways to compute the exponential. Pages 337–341 and 359–366 connect these methods to state response.
