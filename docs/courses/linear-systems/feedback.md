# Chapter 7. Feedback, Observers, and Optimal Control

The moving axis has two integrators and only one position sensor. We can first design feedback assuming velocity is available, then build an observer that estimates velocity from the known acceleration command and the measured position.

## Pole placement and stabilizability

Adopt the sign convention $u=-Kx+r$ throughout this chapter. The closed-loop state matrix is $A-BK$, and $r$ enters through $B$. For a controllable pair, feedback can assign the closed-loop characteristic polynomial arbitrarily, with conjugate pairs for real gains. Under the convention $u=Kx+r$ used in some exercises, reverse the sign of the gain.

For the moving axis, $K=(k_q,k_v)$ gives

$$
A-BK=\begin{bmatrix}0&1\\-k_q&-k_v\end{bmatrix},\qquad
\det(sI-A+BK)=s^2+k_v s+k_q.
$$

Poles at $-2$ and $-3$ require $K=(6,5)$. The position error for regulation to zero then satisfies $\ddot q+5\dot q+6q=0$. To hold a nonzero constant $q_r$, use $u=-6(q-q_r)-5v$. Substitution at $q=q_r,v=0$ gives zero acceleration, as required.

For asymptotic stabilization, only the modes outside the strictly stable region must be controllable. If $w^*A=\lambda w^*$ and $w^*B=0$, then $w^*(A-BK)=\lambda w^*$ for every $K$. Thus stabilizability requires full PBH rank for $\operatorname{Re}\lambda\ge0$ in continuous time, or $|\lambda|\ge1$ in discrete time. An uncontrollable stable mode can decay on its own.

## Estimating the state

A full-order observer combines a model prediction with a correction from the measurement residual,

$$
\dot{\hat x}=A\hat x+Bu+L(y-C\hat x-Du),\qquad
\dot e=(A-LC)e,\quad e=x-\hat x.
$$

For the position sensor $C=(1,0)$, let $L=(\ell_1,\ell_2)^T$. Then $\det(sI-A+LC)=s^2+\ell_1s+\ell_2$. Selecting observer poles $-4$ and $-5$ gives $L=(9,20)^T$. A positive position residual raises the velocity estimate as well as correcting the position estimate. Arbitrary error pole placement requires observability. Convergent estimation requires detectability, meaning that all unobservable modes decay.

With $u=-K\hat x$ and zero reference, use $(x,e)$ as coordinates. The plant and estimation error evolve according to

$$
\begin{bmatrix}\dot x\\\dot e\end{bmatrix}
=\begin{bmatrix}A-BK&BK\\0&A-LC\end{bmatrix}
\begin{bmatrix}x\\e\end{bmatrix}.
$$

The block triangular matrix has the union of the controller and observer poles. For this carriage they are $-2,-3,-4,-5$. This **separation principle** lets us choose the two gains independently. Faster observer poles can require larger gains, which also multiply sensor noise in the correction term.

## Choosing gains from a cost

The continuous-time linear quadratic regulator (LQR) chooses feedback to minimize

$$
J=\int_0^\infty (x^TQx+u^TRu)\,dt,\qquad Q\succeq0,\quad R\succ0.
$$

If $(A,B)$ is stabilizable and the state dynamics are detectable through the output $Q^{1/2}x$, the stabilizing solution $P\succeq0$ of the algebraic Riccati equation gives

$$
A^TP+PA-PBR^{-1}B^TP+Q=0,\qquad K=R^{-1}B^TP.
$$

For one integrator $\dot x=u$ and scalar weights $Q=q>0$, $R=r>0$, the stabilizing solution is $P=\sqrt{qr}$. The feedback is $u=-\sqrt{q/r}\,x$. Multiplying the state penalty by four doubles the decay rate and the initial control effort for the same starting error.

The final lecture also introduces linear quadratic Gaussian (LQG) control. With linear dynamics, a quadratic objective, and the usual independent Gaussian process and measurement noise, a Kalman filter supplies the state estimate used by the regulator. The regulator weights encode the cost of motion and effort. The filter covariances encode the uncertainty in the model and measurements. The [Kalman filter notes](../robotics-math/ch5.md) work through the prediction and measurement update.

**Packet guide.** PDF pp. 512–513 and 520–521 explore feedback in discrete and continuous time. Pages 523–529 cover canonical pole placement, observer design, separation, LQR, and LQG. Pages 537–538 and 553–560 apply the modal tests for stabilization and detection.
