# Chapter 1. Mathematical Arguments

Suppose every run of a robot has a bounded tracking error. Does one bound work for all runs? The answer depends on who gets to choose the bound, and when. Quantifiers express that dependence. Proofs establish whether a proposed guarantee follows from its assumptions.

## 1.1 Notation and Quantifiers

The domain determines which values a variable may take. Here $\mathbb N=\{1,2,\ldots\}$ denotes the counting numbers, $\mathbb Z$ the integers, $\mathbb Q$ the ratios of integers with nonzero denominator, $\mathbb R$ the reals, and $\mathbb C$ the complex numbers. The expression $x\in A$ restricts $x$ to the set $A$.

Read $\forall$ as “for every” and $\exists$ as “there exists.” For a universal claim, the proof must work for an arbitrary element of the domain. For an existence claim, one valid choice, called a *witness*, suffices.

**Example: a bound for each run.** Let $e_k$ be the peak tracking error on run $k$. Compare the two guarantees below.

| Guarantee | When is the bound chosen? |
|---|---|
| $\forall k\in\mathbb N,\ \exists B\in\mathbb R,\ e_k\le B$ | After seeing the run index. Each run may have its own bound. |
| $\exists B\in\mathbb R,\ \forall k\in\mathbb N,\ e_k\le B$ | Once, before choosing the run. The same bound must work for every run. |

Set $e_k=k$. For the first guarantee, choose $B=k$. For the second, take any proposed finite $B$ and choose an integer $k>B$. This run violates the bound. Switching the quantifiers has changed what the robot is claimed to guarantee.

## 1.2 Implications, Converses, and Proof Vocabulary

In an implication $P\Rightarrow Q$, $P$ is sufficient for $Q$, and $Q$ is necessary for $P$. Its **contrapositive**, $\neg Q\Rightarrow\neg P$, expresses the same implication. Its **converse**, $Q\Rightarrow P$, requires a separate argument. For example, divisibility by four implies evenness. The integer 6 disproves the converse. To establish $P\Leftrightarrow Q$, prove both directions.

| Term | Role in an argument |
|---|---|
| Definition | Gives a precise meaning. For example, an integer is even exactly when it equals $2k$ for some integer $k$. |
| Axiom | Supplies a starting assumption of the mathematical system. |
| Theorem or proposition | States a result established by proof. |
| Lemma | Establishes an intermediate result that another proof can use. |
| Claim | Identifies an assertion to justify, often within a longer proof. |
| Corollary | Follows from an established result with a short deduction. |
| Conjecture | States a proposed result whose proof is still open in the discussion. |

## 1.3 Proof Techniques

**Direct proof.** To prove that the sum of two odd integers is even, write them as $2a+1$ and $2b+1$. Their sum is $2(a+b+1)$. The integer $a+b+1$ is the witness required by the definition of evenness.

**Contraposition.** Suppose the goal is to show that an integer with an even square must itself be even. Start with an odd integer $n=2k+1$. Its square is $2(2k^2+2k)+1$, which is odd. This proves the contrapositive and hence the claim about even squares.

**Exhaustion.** To show that $n(n+1)$ is even for every integer $n$, split the domain into two cases. If $n$ is even, the first factor is even. If $n$ is odd, the second factor is even. These cases cover every integer.

**Induction.** To show that the first $n$ positive odd integers sum to $n^2$, check the first case: $1=1^2$. Assume the sum through the $k$th term is $k^2$. Adding the next odd integer gives $k^2+(2k+1)=(k+1)^2$. The base case and the step together establish the formula for every $n\ge1$.

**Strong induction.** Every integer $n\ge2$ is a product of primes. The base case is 2. Assume the factorization exists for every integer from 2 through $k$. If $k+1$ is prime, it supplies its own factorization. Otherwise $k+1=ab$, where both factors lie between 2 and $k$. Apply the hypothesis to each factor and concatenate the products. Strong induction is convenient because the proof needs two earlier indices. Ordinary induction gives the same reasoning if its induction statement collects *all* cases through $k$.

**Contradiction.** Suppose $\sqrt 2=a/b$ in lowest terms, with $b>0$. Then $a^2=2b^2$, so the even-square result above makes $a$ even. Substituting $a=2k$ gives $b^2=2k^2$, so $b$ is even as well. The common factor 2 contradicts the choice of lowest terms. Therefore $\sqrt 2$ is irrational.

## 1.4 Truth Tables

The operators $\neg$, $\land$, and $\lor$ mean negation, conjunction, and inclusive disjunction. Compare the last two columns to see exactly when an implication fails.

| $P$ | $Q$ | $P\land Q$ | $P\lor Q$ | $P\Rightarrow Q$ | $P\land\neg Q$ |
|---|---|---|---|---|---|
| T | T | T | T | T | F |
| T | F | F | T | F | T |
| F | T | F | T | T | F |
| F | F | F | F | T | F |

A counterexample to $P\Rightarrow Q$ must satisfy the hypothesis and violate the conclusion. This explains why a contradiction proof of an implication begins by assuming $P\land\neg Q$.

## 1.5 Negating Logical Statements

Move the negation inward one operation at a time. Negating “every” gives “some,” and negating “some” gives “every.” Keep the original domains. At the innermost condition, the negation of $a<b$ is $a\ge b$, including equality.

For the uniform tracking guarantee in §1.1, this gives

$$
\neg\big(\exists B\in\mathbb R,\ \forall k\in\mathbb N,\ e_k\le B\big)
\quad\Longleftrightarrow\quad
\forall B\in\mathbb R,\ \exists k\in\mathbb N,\ e_k>B.
$$

**Worked example: failure of continuity.** For a real-valued function on $\mathbb R$, continuity at $x_0$ means that for every tolerance $\varepsilon>0$, some radius $\delta>0$ works for every input within that radius. Negating this statement gives

$$
\exists\varepsilon>0,\ \forall\delta>0,\ \exists x\in\mathbb R:
\quad |x-x_0|<\delta
\quad\land\quad |f(x)-f(x_0)|\ge\varepsilon.
$$

One fixed output tolerance defeats every proposed input radius. The input must be *inside* the proposed neighborhood: this condition survives because negating the original implication requires its hypothesis to hold.

## 1.6 Bounds, Extrema, and Completeness

Let $A$ be a nonempty subset of $\mathbb R$. An **upper bound** $u$ satisfies $a\le u$ for every $a\in A$. The **supremum** is the least such bound. A **maximum** is an upper bound belonging to $A$. Reversing the inequalities gives a lower bound, the **infimum** (greatest lower bound), and a **minimum** belonging to $A$.

**Why does $(0,1)$ have supremum 1?** First, every member is at most 1. Second, take any proposed smaller upper bound $u<1$. The midpoint between $\max\{0,u\}$ and 1 belongs to $(0,1)$ and exceeds $u$. This rules out every smaller candidate. The interval has no maximum because 1 lies outside it. Closing the interval at the right endpoint gives $(0,1]$ the same supremum and a maximum of 1.

**Completeness of the reals.** Every nonempty subset of $\mathbb R$ bounded above has a real supremum. The corresponding statement holds for infima of sets bounded below. The choice of number system matters: the positive rationals whose squares are less than 2 approach $\sqrt 2$ from below. Their supremum in $\mathbb R$ is $\sqrt 2$. Within $\mathbb Q$, every rational upper bound is strictly larger, and there is another rational number between it and $\sqrt 2$. Thus no rational upper bound is the least one.

For an unbounded set, the extended-real conventions are $\sup A=+\infty$ when $A$ is unbounded above and $\inf A=-\infty$ when it is unbounded below. These symbols describe unboundedness. A robot whose peak errors satisfy $e_k=k$ attains a finite peak on every run, yet the supremum over all runs is $+\infty$.
