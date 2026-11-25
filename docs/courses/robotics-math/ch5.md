# Chapter 5. Probability, Estimation, and the Kalman Filter

A distance estimate of 3 m and a new sensor reading of 5 m disagree. How far should the estimate move? The answer depends on the uncertainty of each quantity and on the assumptions that relate them. This chapter builds from a fixed unknown through a random prior to a moving state.

## 5.1 Measurement Error and Estimation

In a probability model $(\Omega,\mathcal F,\mathbb P)$, an outcome describes one possible realization, events collect outcomes, and the probability measure assigns their probabilities. A random variable maps an outcome to a measurable quantity such as a sensor error. Repeating a measurement gives new realizations of that variable.

In $y=x+v$ with fixed $x$, a zero mean for $v$ means the sensor is unbiased. A bias of 0.2 m persists when independent readings are averaged. With independent zero-mean errors of equal variance $R$, the average of $n$ readings instead has variance $R/n$. Independence enters through the vanishing cross terms in the variance of the sum.

## 5.2 Random Variables and Densities

A scalar density $f$ integrates to one. The probability of an interval is its integral over that interval. The mean is $\mu=E[X]$ and the variance is $E[(X-\mu)^2]$. For a vector, $P=E[(X-\mu)(X-\mu)^T]$ contains component variances on its diagonal and cross-covariances elsewhere.

Covariance is positive semidefinite because $a^TPa$ is the variance of $a^TX$ for every direction $a$. If two sensors share the same additive bias, their errors can move together. Stacking the sensor readings into a vector preserves that dependence in its off-diagonal entries.

## 5.3 Estimators

**A fixed unknown.** For $y=Cx+v$ with $E[v]=0$, covariance $R\succ0$, and full-column-rank $C$, a linear estimate $Ky$ is unbiased for every $x$ exactly when $KC=I$. The best linear unbiased estimator (BLUE) is

$$
\hat x=(C^TR^{-1}C)^{-1}C^TR^{-1}y,\qquad
P_e=(C^TR^{-1}C)^{-1}.
$$

This is weighted least squares with inverse covariance as the weight. For independent readings 2 and 4 with variances 1 and 4, respectively, $\hat x=2.4$ with variance $1/(1+1/4)=0.8$. Gaussianity is unnecessary for this linear optimality result.

**A random unknown.** If the state has prior mean $m$ and covariance $P$ and the noise is uncorrelated with it, the best affine estimate is $m+K(y-Cm)$ with $K=PC^T(CPC^T+R)^{-1}$ when the inverse exists. The estimate can now use information about $x$ before observing $y$. Joint Gaussianity further identifies this affine estimate with the conditional mean, which minimizes mean squared error among all estimators.

## 5.4 Marginal and Conditional Distributions

For a joint density $f_{X,Y}$, integrate out $y$ to obtain $f_X(x)$. Conditioning fixes the observed value instead: $f_{X|Y}(x|y)=f_{X,Y}(x,y)/f_Y(y)$ wherever $f_Y(y)>0$. Bayes' rule follows by factoring the same joint density in the opposite order.

Independence gives $f_{X,Y}=f_X f_Y$ when densities exist. With finite second moments it implies zero cross-covariance. The converse can fail: if $X$ is uniform on $[-1,1]$ and $Y=X^2$, symmetry gives $E[XY]=E[X^3]=0$ and $E[X]=0$, yet knowing $X$ fixes $Y$ exactly.

## 5.5 Gaussian Random Vectors

A vector is jointly Gaussian if every linear combination of its components is Gaussian, allowing zero variance. For $X\sim\mathcal N(m,P)$, $AX+b$ is Gaussian with mean $Am+b$ and covariance $APA^T$. Selecting rows of the identity gives marginal Gaussian distributions. The transformed covariance can be singular when the outputs satisfy an exact linear relation.

A jointly Gaussian pair with zero cross-covariance is independent. Knowing that two individual marginals are Gaussian does not by itself establish the joint Gaussian assumption.

## 5.6 Conditioning Gaussian Random Vectors

Write the joint mean of state $X$ and measurement $Y$ as $(m_X,m_Y)$ and their covariance blocks as $P_{XX},P_{XY},P_{YX},P_{YY}$. For a jointly Gaussian pair with invertible $P_{YY}$,

$$
m_{X|y}=m_X+P_{XY}P_{YY}^{-1}(y-m_Y),\qquad
P_{X|y}=P_{XX}-P_{XY}P_{YY}^{-1}P_{YX}.
$$

To derive this, subtract $P_{XY}P_{YY}^{-1}(Y-m_Y)$ from $X-m_X$. The remainder has zero covariance with $Y$. Joint Gaussianity makes it independent of $Y$, so its conditional mean is zero and its covariance is the Schur complement above. The measured value shifts the mean; the covariance reduction is determined by the model.

## 5.7 The Discrete-Time Kalman Filter

Take $x_k=Ax_{k-1}+Bu_{k-1}+w_{k-1}$ and $y_k=Cx_k+v_k$, with known input. Assume a Gaussian initial state and mutually independent zero-mean Gaussian process and measurement noises, independent across time and of the initial state. Here $Q$ is process covariance and $R\succ0$ is measurement covariance. Start from the initial mean and covariance.

| Step | Calculation |
|---|---|
| Predict from the previous posterior | $m^-=Am_{k-1}+Bu_{k-1}$ and $P^-=AP_{k-1}A^T+Q$ |
| Compare prediction with observation | Innovation $d=y_k-Cm^-$, covariance $S=CP^-C^T+R$ |
| Condition on the observation | $K=P^-C^TS^{-1}$, $m_k=m^-+Kd$, $P_k=P^--KSK^T$ |

The recursion works because the prediction and measurement are jointly Gaussian given past data. Their cross-covariance is $P^-C^T$. Conditioning therefore gives exactly the update from the preceding section. Feeding the posterior into the next prediction carries the effect of earlier measurements forward.

**One update by hand.** A predicted position of 3 m has variance 4 m². An independent direct sensor reports 5 m with noise variance 1 m². Then $S=5$, $K=4/5$, $m_k=4.6$ m and $P_k=0.8$ m². A sensor with variance 16 m² would give $K=1/5$, moving the estimate only to 3.4 m.

**Nonlinear extension.** An extended Kalman filter propagates the mean through nonlinear dynamics and uses Jacobians of the dynamics and measurement at their respective linearization points to propagate covariance and compute the gain. The resulting posterior is an approximation.

## 5.8 The Luenberger Observer (Optional)

For a noiseless linear model, consider $\hat x_{k+1}=A\hat x_k+Bu_k+L(y_k-C\hat x_k)$. Subtracting from the true dynamics gives $e_{k+1}=(A-LC)e_k$. In discrete time the error decays for every initial error exactly when all eigenvalues of $A-LC$ lie strictly inside the unit circle.

For an $n$-state model the observability matrix stacks $C,CA,\dots,CA^{n-1}$. Full column rank means the initial state is uniquely recoverable from the noiseless outputs with known inputs, and permits arbitrary observer pole placement. The Kalman gain instead follows from the assumed noise and prior covariances.

## 5.9 The Information Matrix (Optional)

For nonsingular Gaussian covariance, define precision $\Lambda=P^{-1}$ and information vector $\eta=\Lambda m$. The quadratic term of the log density is $-x^T\Lambda x/2+\eta^Tx$. An independent linear Gaussian observation adds its log likelihood, giving

$$
\Lambda^+=\Lambda^-+C^TR^{-1}C,\qquad
\eta^+=\eta^-+C^TR^{-1}y .
$$

Solve $\Lambda^+m^+=\eta^+$ to recover the mean. In the scalar example the prior contributes precision $1/4$ and information $3/4$. The measurement contributes 1 and 5. Thus $m^+=(3/4+5)/(1/4+1)=4.6$, the same result as the covariance update.

## 5.10 Deriving the Minimum Variance Estimator (Optional)

For centered variables, minimize the error covariance of an estimate $Ky$. Put $S=CPC^T+R$ and $K_*=PC^TS^{-1}$. Expanding the error and completing the square gives

$$
P_e(K)=P-PC^TS^{-1}CP+(K-K_*)S(K-K_*)^T .
$$

The last term is positive semidefinite for every $K$, establishing optimality in every direction. Equivalently, the optimal error is orthogonal in expectation to the observation: $E[(x-K_*y)y^T]=0$. This is the probabilistic counterpart of the residual orthogonality used in [deterministic least squares](ch3.md). For nonzero means, center the variables before the calculation and add the prior mean back afterward.
