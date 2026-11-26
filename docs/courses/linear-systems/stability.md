# Chapter 4. Internal and Input–Output Stability

For a system at rest, two experiments ask different questions. Displace it slightly and release it to test the free motion. Start it at zero and apply a bounded command to test what can appear at the output.

## Reading the free motion

The origin is **Lyapunov stable** if, for every allowed excursion $\varepsilon>0$, there is a radius $\delta>0$ such that every zero-input trajectory starting within $\delta$ stays within $\varepsilon$ for all future time. Asymptotic stability also requires convergence to zero from a neighborhood. For finite-dimensional LTI dynamics, asymptotic stability is global and exponential.

| Free-motion test | Continuous time | Discrete time |
|---|---|---|
| Asymptotically stable | Every eigenvalue has strictly negative real part | Every eigenvalue has modulus strictly less than one |
| Stable, without decay of every mode | All real parts are nonpositive, at least one is zero, and every imaginary-axis Jordan block has size one | All moduli are at most one, at least one is one, and every unit-circle Jordan block has size one |
| Unstable | An eigenvalue lies in the open right half-plane or a boundary block has size greater than one | An eigenvalue lies outside the unit disk or a boundary block has size greater than one |

A Jordan block contributes a polynomial times an exponential. Strict decay absorbs any fixed polynomial, while a size-two block on the boundary produces a growing term. For the moving axis with $u=0$, $q(t)=q(0)+tv(0)$. However small the starting velocity, position eventually leaves any fixed neighborhood. Two zero eigenvalues alone do not reveal this distinction. The zero matrix has the same eigenvalues and keeps every initial state fixed.

**Reading a planar phase portrait.** With two real eigenvalues of opposite sign, trajectories decay along one eigenvector and grow along the other, producing a saddle. For a conjugate pair with negative real part and nonzero imaginary part, trajectories spiral inward. A pure imaginary pair gives closed ellipses. Evaluate $Ax$ at one point, such as $(1,0)^T$, to determine the direction of motion on the curves.

## A quadratic certificate

For $V(x)=x^TPx$ with $P=P^T\succ0$, the zero-input derivative is $\dot V=x^T(A^TP+PA)x$. If $A^TP+PA=-Q$ with $Q\succ0$, energy decreases strictly away from zero. For a Hurwitz matrix $A$ and any such $Q$, the unique solution is

$$
P=\int_0^\infty e^{A^Tt}Q e^{At}\,dt.
$$

For example, $A=\operatorname{diag}(-1,-2)$ and $Q=I$ give $P=\operatorname{diag}(1/2,1/4)$, so $\dot V=-x_1^2-x_2^2$. The discrete-time counterpart uses $A^TPA-P=-Q$, obtained by taking the one-step change in $V$.

## What a bounded input can excite

A zero-state system is bounded-input bounded-output (BIBO) stable if every bounded input produces a bounded output. For a continuous-time, finite-dimensional proper rational LTI system, all poles of every reduced transfer entry must lie in the open left half-plane. Equivalently, the strictly proper impulse response is absolutely integrable entry by entry. A finite direct gain $D$ sends bounded inputs directly to bounded outputs. For discrete time use absolute summability and the open unit disk.

**A stable measurement with a growing state.** Choose $A=\operatorname{diag}(-1,1)$, $B=(1,0)^T$, $C=(1,0)$, and $D=0$. The measured transfer is $1/(s+1)$, so an input bounded by one gives a zero-state output bounded by one. With $x_2(0)\ne0$, the second state grows as $e^t x_2(0)$ and never appears at the sensor. [Minimal realizations](realizations.md) explain when the transfer poles account for all state dynamics.

**Packet guide.** PDF pp. 340–341, 352–358 and 569 illustrate phase portraits. Pages 367–369 and 370–402 examine internal and BIBO stability. Pages 403–407 connect matrix integrals to Lyapunov equations.
