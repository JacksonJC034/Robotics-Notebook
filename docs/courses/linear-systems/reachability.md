# Chapter 5. Reachability and Observability

To move the carriage from rest to a specified position *and* finish at rest, one actuator must meet two endpoint conditions. To infer its initial velocity from a position encoder, several measurements must jointly distinguish two initial states. Both questions reduce to the rank of a linear map.

## Reachable states and minimum-energy control

Over $[0,T]$ the endpoint displacement relative to free motion is $d=x_f-\Phi(T,0)x_0$. Set $H(t)=\Phi(T,t)B(t)$. A command reaches the target exactly when $d=\int_0^T H(t)u(t)\,dt$ has a solution. The reachability Gramian is

$$
W_c=\int_0^T H(t)H(t)^T\,dt.
$$

Its range is the reachable subspace. Indeed, $v^TW_c v=\int_0^T\|H(t)^Tv\|^2dt$, so its null directions are precisely those orthogonal to all input-induced displacements. If $W_c$ is invertible, the minimum-energy input is $u(t)=H(t)^TW_c^{-1}d$ and its energy is $d^TW_c^{-1}d$. Substitution verifies the endpoint. Any other successful input differs by a command with zero endpoint contribution, orthogonal to this input in the integral inner product. For a singular Gramian, check $d\in\operatorname{range}W_c$ first and use $W_c^\dagger$ for a reachable target.

**Move one unit in one second.** For the axis in [Chapter 1](models.md), $T=1$ gives $H(t)=(1-t,1)^T$ and

$$
W_c=\begin{bmatrix}1/3&1/2\\1/2&1\end{bmatrix},\qquad
W_c^{-1}\begin{bmatrix}1\\0\end{bmatrix}=\begin{bmatrix}12\\-6\end{bmatrix}.
$$

Hence $u(t)=6-12t$. Integration gives $v(t)=6t-6t^2$ and $q(t)=3t^2-2t^3$. At $t=1$ the carriage has reached $q=1$ with $v=0$. The squared-input integral is 12.

## Rank tests and the discrete-time horizon

For an $n$-state LTI pair, the reachable subspace is the range of $\mathcal C=[B\;AB\;\cdots\; A^{n-1}B]$. Cayley–Hamilton places every higher power times $B$ in this same span. Complete reachability requires rank $n$. The Popov–Belevitch–Hautus (PBH) test asks whether $[\lambda I-A\quad B]$ has rank $n$ at each eigenvalue. A left eigenvector $w^*A=\lambda w^*$ with $w^*B=0$ certifies failure because $w^*A^jB=0$ for all $j$.

In discrete time, stack $N$ commands in chronological order. Their endpoint map is $[A^{N-1}B\;\cdots\;AB\;B]$, and the desired displacement is $x_f-A^Nx_0$. The shortest horizon for a particular target is the first $N$ for which that displacement belongs to the range. Reachability from zero and controllability *to* zero can differ for a singular update. For $A=0$ and $B=0$, every initial state goes to zero in one step and the only state reachable from zero is zero.

## Initial states visible at the sensor

Subtract the output due to any known input. The remaining signal is $r(t)=C(t)\Phi(t,0)x_0=M(t)x_0$. Its energy defines the observability Gramian $W_o=\int_0^T M(t)^TM(t)\,dt$. A nonzero state in $\ker W_o$ yields the same output history as zero. When $W_o$ is invertible the initial state follows from $x_0=W_o^{-1}\int_0^T M(t)^Tr(t)\,dt$.

For an LTI model, stack $C,CA,\ldots,CA^{n-1}$ vertically to form $\mathcal O$. Full column rank is equivalent to observability. Equivalently, the vertical stack of $\lambda I-A$ and $C$ must have rank $n$ at every eigenvalue. These are the reachability tests for the dual pair $(A^T,C^T)$, transposed. For the axis encoder $C=(1,0)$, the two rows $C,CA$ are the identity. With zero input, $q(h)-q(0)=hv(0)$ recovers the missing velocity. A velocity-only sensor $C=(0,1)$ leaves every constant position offset invisible.

**Adjoint interpretation.** For the endpoint operator $L:u\mapsto d$, its adjoint sends an endpoint vector $v$ to the signal $H(t)^Tv$. This follows by moving $v$ inside $v^T\int H u\,dt$. Compute it by integrating $\dot p=-A(t)^Tp$ backward from $p(T)=v$ and reading $B(t)^Tp(t)$. Thus $W_c=LL^*$. For the observation operator $M:x_0\mapsto r(\cdot)$, $W_o=M^*M$. If $A$ is constant and Hurwitz, the infinite-horizon Gramians solve $AW_c+W_cA^T=-BB^T$ and $A^TW_o+W_o A=-C^TC$, respectively.

**Packet guide.** PDF pp. 259–267 and 430–439 test individual modes. Pages 403–411 and 484–485 work through state transfers and Gramians. Pages 511–519 connect input and observation operators to their adjoints.
