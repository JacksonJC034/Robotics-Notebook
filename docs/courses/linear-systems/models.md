# Chapter 1. State-Space Models and Linearization

A position sensor reports the same value when a carriage passes the origin at speed and when it rests there. The two situations have different futures under the same force. Including velocity in the state makes the future motion predictable from the present state and the subsequent input.

## Continuous and discrete time

Let $x$ have $n$ states, $u$ have $m$ inputs, and $y$ have $p$ outputs. A continuous-time linear model has the form

$$
\dot x(t)=A(t)x(t)+B(t)u(t),\qquad y(t)=C(t)x(t)+D(t)u(t).
$$

$A$ maps state to state rate, $B$ maps actuator commands to that rate, $C$ selects measured combinations, and $D$ represents a direct input contribution to the measurement. Their shapes are $n\times n$, $n\times m$, $p\times n$, and $p\times m$. In discrete time the first equation becomes $x_{k+1}=A_k x_k+B_k u_k$. Constant matrices give a linear time-invariant (LTI) model. A prescribed coefficient such as $\sin(t)$ multiplying $x$ gives a linear time-varying (LTV) model.

**Superposition check.** If $(x_1,u_1)$ and $(x_2,u_2)$ satisfy the equations, then $(a x_1+b x_2,a u_1+b u_2)$ satisfies them with initial state $a x_1(0)+b x_2(0)$. Thus the map from input to output is linear for zero initial state. A fixed nonzero initial state adds its own free response.

## A moving axis

Take $x=(q,v)^T$, command acceleration $u$, and measure position $y=q$. Integrating $\dot q=v$ and $\dot v=u$ over one sampling interval of length $h$, with $u=u_k$ held constant, gives

$$
A=\begin{bmatrix}0&1\\0&0\end{bmatrix},\quad
B=\begin{bmatrix}0\\1\end{bmatrix},\quad C=\begin{bmatrix}1&0\end{bmatrix},\quad D=0,
$$

$$
x_{k+1}=\begin{bmatrix}1&h\\0&1\end{bmatrix}x_k+
\begin{bmatrix}h^2/2\\h\end{bmatrix}u_k.
$$

Starting from rest, one unit of acceleration for one second gives $q=1/2$ and $v=1$. The $h^2/2$ term captures the distance traveled while velocity builds up during the sample.

## Linearizing about a motion or an equilibrium

For $\dot x=f(x,u)$, $y=g(x,u)$, first choose a nominal solution $(\bar x(t),\bar u(t))$. Define $\delta x=x-\bar x$, $\delta u=u-\bar u$, and $\delta y=y-g(\bar x,\bar u)$. To first order,

$$
\delta\dot x=A\delta x+B\delta u,\quad
\delta y=C\delta x+D\delta u,\qquad
(A,B,C,D)=(f_x,f_u,g_x,g_u)\big|_{(\bar x,\bar u)}.
$$

The constant term cancels because $\dot{\bar x}=f(\bar x,\bar u)$. At a fixed operating point this requires $f(\bar x,\bar u)=0$. Expanding around a fixed point with nonzero drift leaves an affine term. For a time-invariant nonlinear plant, the Jacobians are constant at equilibrium and can vary along a nominal motion.

**Pendulum with applied torque.** Write $I\ddot\theta=-b\dot\theta-mg\ell\sin\theta+u$, measuring angle from the downward vertical. A resting angle $\bar\theta$ requires $\bar u=mg\ell\sin\bar\theta$. The perturbations satisfy

$$
I\delta\ddot\theta+b\delta\dot\theta+mg\ell\cos\bar\theta\,\delta\theta=\delta u.
$$

The restoring coefficient is positive at $0$ and negative at $\pi$. To compare a simulated perturbation with an encoder reading near the upright pose, recover the physical angle as $\pi+\delta\theta$.

**Packet guide.** PDF pp. 2–4 introduce the four model classes. Pages 123–127 and 172–179 work through equilibrium choices and Jacobians for nonlinear systems.
