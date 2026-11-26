# Chapter 6. Transfer Functions and Realizations

A measured input–output response can be consistent with several internal state models. To see which states an experiment can reveal, follow an input through the dynamics to the sensor.

## From the state to the transfer function

With zero initial state, the Laplace transform gives $(sI-A)X=BU$ and hence

$$
G(s)=C(sI-A)^{-1}B+D.
$$

The discrete-time expression is $G(z)=C(zI-A)^{-1}B+D$. A constant invertible state coordinate change leaves both expressions invariant because the transformation factors cancel. For a nonzero continuous-time initial state, add $C(sI-A)^{-1}x_0$ to $G(s)U(s)$ to recover the full output.

## Three realizations of one response

Consider the packet's $G(s)=(s+3)/((s+1)(s+2))$. Expanding the denominator gives $s^2+3s+2$. A controllable canonical realization is

$$
A_c=\begin{bmatrix}0&1\\-2&-3\end{bmatrix},\quad
B_c=\begin{bmatrix}0\\1\end{bmatrix},\quad C_c=\begin{bmatrix}3&1\end{bmatrix},\quad D=0.
$$

The first coordinate satisfies $\ddot x_1+3\dot x_1+2x_1=u$, while $y=3x_1+\dot x_1$, which verifies the numerator. The observable canonical realization follows by transposing the single-input single-output model, $(A_o,B_o,C_o)=(A_c^T,C_c^T,B_c^T)$. The scalar transfer equals its transpose.

Partial fractions give $G(s)=2/(s+1)-1/(s+2)$. A modal realization therefore takes $A_m=\operatorname{diag}(-1,-2)$, $B_m=(1,1)^T$, and $C_m=(2,-1)$. Both modes receive input and contribute to the measured output. The two distinct poles require at least two states for any finite-dimensional ordinary state-space realization, so all three realizations are minimal.

## Kalman decomposition and cancellation

Let $\mathcal R=\operatorname{range}\mathcal C$ be the reachable subspace and $\mathcal N=\ker\mathcal O$ the unobservable subspace. Both are $A$-invariant. Choose a basis for $\mathcal R\cap\mathcal N$, extend it separately within $\mathcal R$ and $\mathcal N$, and complete the resulting independent vectors to a state basis. In these coordinates the four parts have distinct roles.

| State component | Consequence for experiments |
|---|---|
| Reachable and observable | An input can excite it and the sensor can detect it. This part realizes the transfer. |
| Reachable and unobservable | An input can store energy here with no trace in the measured output. |
| Unreachable and observable | An initial condition can affect the sensor, although an input from rest cannot excite it. |
| Unreachable and unobservable | Neither an input from rest nor the sensor accesses this component. |

The minimal state dimension is $\dim\mathcal R-\dim(\mathcal R\cap\mathcal N)$. A realization is minimal exactly when it is both reachable and observable. Every pair of minimal realizations of the same transfer matrix is related by an invertible state coordinate change.

**Check a cancellation.** Append a third state $\dot x_3=x_3+u$ to the modal model and keep $y=2x_1-x_2$. The new input column is $(1,1,1)^T$. The distinct diagonal entries and nonzero input weights give a full-rank reachability matrix, but the third column of $\mathcal O$ is zero. Computing the transfer over the full characteristic denominator introduces a common factor $s-1$. Canceling it recovers the original $G(s)$. Internally, a unit step from rest makes $x_3=e^t-1$, a concrete reason to inspect the realization when judging stability.

**Packet guide.** PDF pp. 495–510 cover decomposition and realization, pp. 511–517 compare realizations of a single transfer function, and pp. 535 and 561–562 connect canonical forms to minimality.
