# Unlinked Gamma regression: exact identifiability and optimal cumulant order

Anonymous · 20 September 2026 · Version 0.1.0-candidate

**Unrefereed candidate.** This reading edition follows the authoritative PDF/LaTeX theorem numbering. Mathematical notation is retained in TeX.

## Abstract

Unlinked linear regression asks which coefficient vectors can produce a prescribed response distribution from a known predictor distribution. For a fixed dictionary of independent, centered, standardized Gamma predictors with arbitrary positive shapes, we characterize equality of response laws by a finite measure recording the total shape at each nonzero signed effective scale. This gives all coefficient fibers as finite allocation problems and shows that minimality relative to the given dictionary is equivalent to full support. A three-predictor example therefore contradicts the signed-permutation conclusion of a conjecture of Balabdaoui, Slawski and Steffani while retaining finite identifiability. We give a necessary and sufficient arithmetic condition for every minimal representation to be identifiable up to signs and permutations. The condition requires equal subset sums of shapes to have the same constituent shape multiset; only equal-shape permutations then occur. Cumulants through order $2d+1$ determine the response law and its coefficient fiber, and this consecutive-order cutoff is optimal uniformly over dictionaries with signed coefficients. We also give exact reconstruction, a one-Gaussian extension, and an extension to specified analytic convolution families, including Poisson predictors.

**Keywords:** unlinked regression; identifiability; Gamma convolution;
subset sums; cumulants; Prony reconstruction.

# Introduction and model {#sec:model}

Suppose that the distribution of a predictor vector $X$ and the
distribution of a response $Y$ are known, but the links between their
observations are unavailable. In the noiseless linear model, the
population problem is to determine
$$\mathcal B_X(Y)=\{\beta\in\mathbb R^d:Y\overset{d}{=}\beta^\top X\}.$$
This set can be a singleton, finite with more than one element, or
infinite. These possibilities must be distinguished from uniqueness up
to a prescribed group of symmetries.

Balabdaoui, Slawski and Steffani [BSS](#ref-BSS) discuss these distinctions and,
in the concluding conjecture of their version 1, propose
signed-permutation identifiability for independent unit-variance
predictors with at most one Gaussian component, assuming that the
representation is minimal. Here minimality excludes a representation
using a proper subvector of the given predictors. Their paper also
identifies convolution as an obstruction and proves a positive mixed
Gamma--Gaussian result under distinct labeled subset sums of the Gamma
shapes.

We analyze the fixed Gamma dictionary completely. Throughout
Sections [1](#sec:model)--[5](#sec:reconstruction), let $d\ge1$, let
$\alpha_1,\ldots,\alpha_d>0$ be known, and let $$\begin{equation}
\label{eq:model}
 G_i\sim\operatorname{Gamma}(\alpha_i,1)\quad\text{independently},\qquad
 X_i=\frac{G_i-\alpha_i}{\sqrt{\alpha_i}}.
\end{equation}$$ The Gamma parameters are shape and rate. Each $X_i$ has
mean zero and variance one. Set $$\begin{equation}
\label{eq:scales}
 Y_\beta=\beta^\top X,\qquad a_i=\frac{\beta_i}{\sqrt{\alpha_i}},\qquad
 \mathcal B(\beta)=\{\gamma\in\mathbb R^d:Y_\gamma\overset{d}{=}Y_\beta\}.
\end{equation}$$ Coefficients can be positive, negative, or zero. The
dictionary, including its labels and shapes, remains fixed.

## Contribution and relation to classical results

The analytic invariant used below is closely related to the classical
Thorin measure of a positive Gamma convolution [JRY](#ref-JRY). For positive
$a_i$, the uncentered sum $\sum_i a_iG_i$ has Thorin measure
$\sum_i\alpha_i\delta_{1/a_i}$. We use the signed scales $a_i$ directly
and give a short proof based on rational logarithmic derivatives that
also handles centering and negative coefficients. The distinction
between this aggregate invariant and its allocation to a fixed list of
predictors is central to the identifiability results.

The statistical context includes deconvolution-based estimation with
unmatched data. Azadkia and Balabdaoui [AB](#ref-AB) study coefficient
estimation under identification and a distance-to-solution-set
formulation in nonidentifiable cases. Balabdaoui, Di Noia and
Durot [BDD](#ref-BDD) study recovery of the latent linear-predictor distribution
in unlinked linear models, obtaining parametric-rate results under their
assumptions. Our population classification makes the coefficient
ambiguity explicit for a known Gamma dictionary. Recovery of a latent
distribution and identification of its coefficient vector are different
targets. Exact cumulant sufficiency alone does not validate a
sample-cumulant estimator or transfer these statistical rates to every
Gamma configuration.

Finite-atomic moment reconstruction is classical Prony theory [KPR](#ref-KPR).
Our reconstruction argument applies that theory after weighting each
scale by its square. The additional lower-bound construction respects a
single fixed Gamma dictionary on both sides. Neither the
rational-function method nor the abstract moment-reconstruction method
is presented as new. The literature comparison accompanying this
manuscript records bounded uncertainty about historical priority of the
particular allocation criterion and optimal-cutoff formulation.

Theorem [2.1](#thm:invariant) identifies the invariant;
Theorem [2.2](#thm:fiber)
gives every fiber and characterizes minimality.
Section [3](#sec:counterexample) verifies the minimal counterexample.
Theorem [4.1](#thm:sharp)
gives the sharp arithmetic replacement for the conjectured conclusion.
Theorems [5.1](#thm:cumulants) and [5.2](#thm:optimal) establish the optimal consecutive cumulant
cutoff. Section [6](#sec:extensions) states the precise scope of the extensions.

# The aggregate measure and all coefficient fibers

Define the finite positive measure on $\mathbb R\setminus\{0\}$
$$\begin{equation}
\label{eq:measure}
 \mu_\beta=\sum_{i:a_i\ne0}\alpha_i\delta_{a_i}.
\end{equation}$$ Repeated scales are combined by adding their shape
weights. The measure is positive even when its support contains negative
numbers.

::: {#thm:invariant .theorem}
**Theorem 2.1** (Exact distributional invariant). *For all
$\beta,\gamma\in\mathbb R^d$,
$$Y_\beta\overset{d}{=}Y_\gamma\quad\Longleftrightarrow\quad \mu_\beta=\mu_\gamma.$$*
:::

::: proof
*Proof.* There is an open interval about zero on which all factors
$1-a_it$ are positive and the moment-generating function exists. On that
interval the cumulant-generating function and its derivative are
$$\begin{align}
 K_\beta(t)&=\sum_i\alpha_i\{-a_it-\log(1-a_it)\},\label{eq:cgf}\\
 K'_\beta(t)&=\sum_{i:a_i\ne0}\alpha_i
 \left\{\frac{a_i}{1-a_it}-a_i\right\}.\label{eq:derivative}
\end{align}$$ If the laws agree, the two derivatives agree on a common
interval. Their difference is rational. Multiplying by the product of
its denominators produces a polynomial that vanishes on an interval,
hence vanishes identically. The rational functions therefore agree
everywhere they are defined, including outside the common real domain of
the original moment-generating functions.

At the pole $t=1/s$, the residue
of [5](#eq:derivative) is $$-\sum_{i:a_i=s}\alpha_i.$$ Every summand
before the minus sign is positive. Thus the pole cannot cancel, and its
residue determines the aggregate shape at $s$. Equality of poles and
residues gives equality of the measures. This argument concerns the
rational logarithmic derivative; it does not treat a Gamma transform
with a noninteger shape as meromorphic.

Conversely, the measure determines
$$K_\beta(t)=\int_{\mathbb R\setminus\{0\}}[-\log(1-st)-st]\,d\mu_\beta(s)$$
on a neighborhood of zero. Equal measures give equal moment-generating
functions there and hence equal laws. The empty measure occurs only when
every coefficient is zero. ◻
:::

Let $\mu_\beta=\sum_{j=1}^k w_j\delta_{s_j}$, where the $s_j$ are
distinct and nonzero and $w_j>0$.

::: {#thm:fiber .theorem}
**Theorem 2.2** (Exact fiber and minimality). *The fiber
$\mathcal B(\beta)$ is in bijection with ordered partitions
$(I_0,I_1,\ldots,I_k)$ of $\{1,\ldots,d\}$ satisfying the following
conditions: $I_0$ may be empty, every $I_j$ for $1\le j\le k$ is
nonempty, and $$\begin{equation}
\label{eq:allocation}
 \sum_{i\in I_j}\alpha_i=w_j,\qquad 1\le j\le k.
\end{equation}$$ The corresponding coefficients are $$\begin{equation}
\label{eq:backmap}
 \gamma_i=\begin{cases}
 0,&i\in I_0,\\
 s_j\sqrt{\alpha_i},&i\in I_j,\quad 1\le j\le k.
 \end{cases}
\end{equation}$$ In particular $|\mathcal B(\beta)|\le(k+1)^d$. A
representation is minimal relative to the fixed dictionary if and only
if every $\beta_i$ is nonzero. In that case $I_0$ is empty in every
alternative and $|\mathcal B(\beta)|\le k^d$. When $k=0$, the fiber is
$\{0\}$.*
:::

::: proof
*Proof.* Theorem [2.1](#thm:invariant) forces every nonzero effective scale in an
alternative representation to be one of the $s_j$, and forces
precisely [6](#eq:allocation). Its converse shows that all such allocations
work. Each label has at most $k+1$ destinations, which proves
finiteness.

If a coefficient is zero, that coordinate can be omitted. We allow the
empty subvector and empty sum, so this includes the zero response when
$d=1$. If every coefficient is nonzero, the total mass
of [3](#eq:measure) equals $A=\sum_i\alpha_i$. Any linear
combination of a proper subvector has active measure of total mass at
most the sum of that subvector's shapes, which is strictly below $A$. It
cannot have the same law. The same mass argument shows that every
alternative to a full-support vector also has full support. ◻
:::

This notion of minimality does not permit replacing the dictionary by
different Gamma variables or splitting its components into additional
independent variables. For a particular response, labeled uniqueness is
equivalent to the existence of exactly one feasible allocation
in [6](#eq:allocation). The uniform criteria below concern all
responses for the given dictionary.

# A minimal counterexample {#sec:counterexample}

Take $\alpha=(1,1,2)$ and
$$\beta=(1,1,2\sqrt2),\qquad \widetilde\beta=(2,2,\sqrt2).$$ The
effective scales are respectively $(1,1,2)$ and $(2,2,1)$, so both
aggregate measures equal $2\delta_1+2\delta_2$. More directly, the
independent variables $$A=G_1+G_2-2,\qquad B=G_3-2$$ are identically
distributed. Thus
$$Y_\beta=A+2B\overset{d}{=}2A+B=Y_{\widetilde\beta},\qquad
 M_{Y_\beta}(t)=\frac{e^{-6t}}{(1-t)^2(1-2t)^2},\quad t<\tfrac12.$$ The
squared coefficient multisets are $\{\!\{1,1,8\}\!\}$ and
$\{\!\{4,4,2\}\!\}$, so no combination of signs and permutations relates
the vectors. Both have full support and hence are minimal by
Theorem [2.2](#thm:fiber). The
only subsets of the dictionary with total shape 2 are $\{1,2\}$ and
$\{3\}$. Because all the available shape is used, there can be no zero
block. Consequently
$$\mathcal B(\beta)=\{(1,1,2\sqrt2),(2,2,\sqrt2)\}.$$ This contradicts
the literal signed-permutation conclusion in the Discussion of [BSS](#ref-BSS),
version 1. It does not contradict finite identifiability, called weak
identifiability there. The Gamma convolution relation underlying the
example is already recognized in that paper; the full-support allocation
makes the minimality issue explicit.

# A sharp arithmetic replacement

Let $H_\alpha$ be the group of permutations preserving the shapes:
$\pi\in H_\alpha$ if $\alpha_{\pi(i)}=\alpha_i$ for every $i$. Its
action on coefficients is $(\pi\beta)_i=\beta_{\pi(i)}$. These
permutations are actual symmetries of the joint predictor law; arbitrary
sign flips need not be.

Consider the condition $$\begin{equation}
\tag{SR}\label{eq:SR}
 \sum_{i\in I}\alpha_i=\sum_{i\in J}\alpha_i
 \quad\Longrightarrow\quad
 \{\!\{\alpha_i:i\in I\}\!\}=\{\!\{\alpha_j:j\in J\}\!\}
 \quad(I,J\subseteq\{1,\ldots,d\}).
\end{equation}$$ Equality here is equality of multisets, with
multiplicities. The subsets need not contain the same labels.

::: {#thm:sharp .theorem}
**Theorem 4.1** (Sharp uniform criterion). *For a fixed positive shape
dictionary, the following statements are equivalent:*

1.  *Condition [SR](#eq:SR) holds.*

2.  *For every $\beta\in\mathbb R^d$,
    $\mathcal B(\beta)=H_\alpha\beta$.*

3.  *For every minimal $\beta$, every $\gamma\in\mathcal B(\beta)$ is a
    signed permutation of $\beta$.*
:::

::: proof
*Proof.* Suppose [SR](#eq:SR) holds. Equivalent representations assign equal total
shape to each nonzero scale.
By [SR](#eq:SR), the
constituent shape multisets at that scale agree. Match equal-shape
indices within each scale block. The unused indices also have matching
shape multisets because the full dictionary is fixed. These matches give
a permutation in $H_\alpha$. Conversely, permuting equal-shape
independent coordinates leaves their joint law unchanged. This proves
(i)$\Rightarrow$(ii), and (ii)$\Rightarrow$(iii) is immediate.

For the contrapositive of (iii)$\Rightarrow$(i),
suppose [SR](#eq:SR)
fails. Remove the common indices from a witnessing pair of subsets. The
resulting sets $U,V$ are disjoint, nonempty, have equal total shape, and
have different shape multisets. Write $C$ for their complement and set
$$M=\frac{\max_i\alpha_i}{\min_i\alpha_i}.$$ Choose $q>\sqrt M$ and, if
$C\ne\varnothing$, choose $h>q\sqrt M$. Define two effective-scale
vectors by $$(a_i,b_i)=\begin{cases}
 (1,q),&i\in U,\\
 (q,1),&i\in V,\\
 (h,h),&i\in C.
 \end{cases}$$ Their aggregate measures agree because $U,V$ have equal
total shape. Every scale is nonzero, so both representations are
minimal. The squared coefficients at scales $1,q,h$ lie in pairwise
disjoint intervals. In the lowest interval their multisets are exactly
the shape multisets of $U$ and $V$, which differ. Thus the complete
squared coefficient multisets differ, excluding signed-permutation
equivalence. ◻
:::

If $\lambda_1,\ldots,\lambda_r$ are the distinct shapes and
$m_1,\ldots,m_r$ their multiplicities,
condition [SR](#eq:SR)
is equivalently injectivity of $$\begin{equation}
\label{eq:counts}
 (n_1,\ldots,n_r)\longmapsto\sum_{\ell=1}^r n_\ell\lambda_\ell
 \quad\text{on }\prod_{\ell=1}^r\{0,\ldots,m_\ell\}.
\end{equation}$$ It is also equivalent to the absence of a nonzero
integer vector $z$ with $|z_\ell|\le m_\ell$ and
$\sum_\ell z_\ell\lambda_\ell=0$. To see the converse formulation, use
the positive and negative parts of $z$ as subset multiplicities.

Repeated shapes are compatible
with [SR](#eq:SR):
every iid Gamma dictionary satisfies it, as does $(1,1,3)$. Rational
independence of the distinct shape values is sufficient but unnecessary.
Pairwise distinct shapes alone are insufficient: for $(1,2,3)$ the
allocations $(1,1,2)$ and $(2,2,1)$ have equal measures, while their
squared coefficient multisets are $\{\!\{1,2,12\}\!\}$ and
$\{\!\{4,8,3\}\!\}$.

::: {#cor:labeled .corollary}
**Corollary 4.2** (Labeled uniqueness). *The map
$\beta\mapsto\mathcal L(Y_\beta)$ is injective on $\mathbb R^d$ if and
only if all labeled subset sums of $(\alpha_i)$ are distinct. The same
condition is necessary and sufficient if injectivity is demanded only
among minimal representations.*
:::

::: proof
*Proof.* If labeled subset sums are distinct, the mass at every scale
identifies its index block uniquely. Conversely, distinct equal-sum
subsets reduce, after deleting their intersection, to disjoint nonempty
equal-sum subsets. Swap two distinct nonzero scales on these subsets and
keep nonzero scales on the complement. The two labeled vectors differ,
have full support, and have the same aggregate measure. ◻
:::

The distinct-labeled-subset-sum hypothesis is the same arithmetic
hypothesis used in the mixed Gamma--Gaussian theorem of [@BSS
Theorem 5]. Corollary [4.2](#cor:labeled) treats a centered, standardized Gamma
dictionary and proves necessity as well as sufficiency there.
Theorem [4.1](#thm:sharp)
permits precisely those subset collisions that preserve shape
multiplicities. Neither statement is an unqualified strengthening of the
entire mixed-model theorem, whose Gaussian mean and original Gamma
normalization differ.

::: {#cor:generic .corollary}
**Corollary 4.3** (Generic identification). *For arbitrary positive
shapes, if all $a_i$ are nonzero and pairwise distinct, then
$\mathcal B(\beta)=H_\alpha\beta$. This conclusion therefore holds for
Lebesgue-almost every $\beta\in\mathbb R^d$.*
:::

::: proof
*Proof.* There are $d$ distinct observed nonzero scales and only $d$
predictors. Every scale must receive a predictor, so all blocks are
singletons and there is no zero block. Each mass identifies the
singleton's shape. The excluded vectors lie in the finite union of
hyperplanes $\beta_i=0$ and
$\beta_i/\sqrt{\alpha_i}=\beta_j/\sqrt{\alpha_j}$. ◻
:::

# Finite cumulants and an optimal cutoff {#sec:reconstruction}

Write $\kappa_n(Y)$ for the $n$th cumulant of $Y$. For the
model [1](#eq:model), differentiation
of [4](#eq:cgf)
gives $$\begin{equation}
\label{eq:cumulants}
 c_n(\beta):=\frac{\kappa_n(Y_\beta)}{(n-1)!}
 =\sum_i\alpha_i a_i^n,\qquad n\ge2.
\end{equation}$$ The first cumulant is always zero.

::: {#thm:cumulants .theorem}
**Theorem 5.1** (Finite cumulant characterization). *For any two vectors
in a fixed $d$-predictor Gamma dictionary, equality of their response
cumulants of orders $2,\ldots,2d+1$ is equivalent to equality of their
response laws.*
:::

::: proof
*Proof.* Define
$$\nu_\beta=\sum_{i:a_i\ne0}\alpha_i a_i^2\delta_{a_i}.$$ This positive
measure has at most $d$ atoms, and its moments of orders
$m=0,\ldots,2d-1$ are $c_{m+2}(\beta)$. If these moments agree for two
vectors, the difference of the measures is supported at $r\le2d$
distinct points $x_1,\ldots,x_r$. Write its weights as $u_j$. Its first
$r$ zero moments give $$\sum_{j=1}^r u_jx_j^m=0,\qquad 0\le m\le r-1.$$
The square Vandermonde matrix is invertible, so all $u_j$ vanish.
Division of the weight at every nonzero atom by the square of that atom
recovers $\mu_\beta$. Apply
Theorem [2.1](#thm:invariant). Equality of laws implies equality of
cumulants, proving the reverse direction. ◻
:::

## Exact reconstruction

Let $m_\ell=c_{\ell+2}(\beta)$ and form the Hankel matrix
$$H_d=(m_{p+q})_{p,q=0}^{d-1}.$$ If
$\mu_\beta=\sum_{j=1}^k w_j\delta_{s_j}$, then
$$H_d=V\operatorname{diag}(w_1s_1^2,\ldots,w_ks_k^2)V^\top,
 \qquad V_{p,j}=s_j^p.$$ Positive weights and the Vandermonde rank imply
$\mathop{\mathrm{rank}}H_d=k$. If $k=0$, the response is zero. Otherwise
the leading $k\times k$ block is positive definite. Solve
$$\begin{equation}
\label{eq:prony}
 \sum_{j=0}^{k-1}q_jm_{\ell+j}=-m_{\ell+k},\qquad 0\le\ell<k.
\end{equation}$$ The monic polynomial $Q(z)=z^k+\sum_{j=0}^{k-1}q_jz^j$
vanishes at each $s_j$:
equation [10](#eq:prony) is a Vandermonde system for the quantities
$w_js_j^2Q(s_j)$. Recover the weights $w_js_j^2$ from the first $k$
moments, divide by $s_j^2$, and solve the finite allocation
equations [6](#eq:allocation).

For the counterexample, $(c_2,c_3,c_4,c_5)=(10,18,34,66)$ and
$$H_2=\begin{pmatrix}10&18\\18&34\end{pmatrix},\qquad
 \det H_2=16,\qquad Q(z)=z^2-3z+2.$$ The roots are $1,2$; the weights of
$\nu$ are $2,8$; and the weights of $\mu$ are $2,2$. The allocation step
yields the two coefficient vectors already displayed.

This is exact population reconstruction, not a stability or
efficient-computation guarantee. The finite-atomic stage is a standard
Prony construction [KPR](#ref-KPR), and near-colliding nodes can amplify
perturbations [AGY](#ref-AGY). Exact allocation for arbitrary real shapes
requires an exact number representation or equality oracle. Estimated
cumulants and approximate subset sums require a separate statistical
analysis.

## Sharpness of the highest required order

::: {#thm:optimal .theorem}
**Theorem 5.2** (Optimal consecutive cumulant cutoff). *For every $d\ge1$,
there is a fixed positive Gamma shape dictionary and two full-support
coefficient vectors whose response cumulants agree through order $2d$
and differ at order $2d+1$. Consequently $2d+1$ is the smallest uniform
highest order in a consecutive initial cumulant segment that determines
the response law over all such dictionaries with signed coefficients.
The lower-bound examples can have integer shapes.*
:::

::: proof
*Proof.* For $1\le i\le d$, set $$\begin{equation}
\label{eq:lowerconstruction}
 \alpha_i=\frac{2}{i(d-i)!(d+i)!},\qquad
 a_i=(-1)^{d-i}i,\qquad
 \beta_i=\sqrt{\alpha_i}\,a_i,\qquad
 \widetilde\beta_i=-\beta_i.
\end{equation}$$ All shapes are positive and all coefficients are
nonzero. For $$Q(z)=\prod_{j=1}^d(z-j^2)$$ we have $$\begin{align*}
 Q'(i^2)&=\prod_{j\ne i}(i-j)(i+j)
       =\frac{(-1)^{d-i}(d-i)!(d+i)!}{2i^2},\\
 \alpha_i a_i^3&=\frac{1}{Q'(i^2)}.
\end{align*}$$ For $0\le k\le d-1$, Lagrange interpolation of $z^k$ at
the $d$ nodes $i^2$, followed by comparison of the coefficient of
$z^{d-1}$, gives $$\begin{equation}
\label{eq:lagrange}
 \sum_{i=1}^d\frac{(i^2)^k}{Q'(i^2)}=
 \begin{cases}0,&0\le k\le d-2,\\1,&k=d-1.\end{cases}
\end{equation}$$ The first case is empty when $d=1$.
Equations [11](#eq:lowerconstruction)--[12](#eq:lagrange) imply
$$\sum_i\alpha_i a_i^{2k+3}=0\quad(0\le k\le d-2),\qquad
 \sum_i\alpha_i a_i^{2d+1}=1.$$ Reflection preserves every even
cumulant. The odd cumulants of orders $3,5,\ldots,2d-1$ vanish by the
preceding identity, and both means vanish by centering. At the next
order, $$\kappa_{2d+1}(Y_\beta)=(2d)!,\qquad
 \kappa_{2d+1}(Y_{\widetilde\beta})=-(2d)!.$$ Thus the two laws are
different despite agreement through order $2d$. Their representations
are minimal by Theorem [2.2](#thm:fiber).

Finally, choose a positive integer $L$ clearing all denominators of the
rational shapes
in [11](#eq:lowerconstruction). Replace $\alpha_i$ by $L\alpha_i$,
retain the effective scales $a_i$, and recompute the coefficients as
$\sqrt{L\alpha_i}\,a_i$. Every normalized cumulant is multiplied by $L$,
preserving the cancellation and the first discrepancy. This gives
integer-shape examples in the same dimension. ◻
:::

::: remark
*Remark 5.3* (Meaning of sharpness). The theorem concerns reconstruction
of the response law and hence its full coefficient fiber from a
consecutive initial cumulant segment. It does not claim optimality for
every dictionary, for nonnegative coefficients, for arbitrary
nonconsecutive cumulant selections, or for identification only modulo
signs. The reflected examples belong to different distributional fibers.
:::

For $d=3$, multiplying the shapes
in [11](#eq:lowerconstruction) by $1080$ gives
$$\alpha=(45,9,1),\qquad a=(1,-2,3),\qquad
 \beta=(3\sqrt5,-6,3),\qquad\widetilde\beta=-\beta.$$ The first
distinguishing cumulant has order seven:

::: center
    Order   $\kappa_n(Y_\beta)$   $\kappa_n(Y_{\widetilde\beta})$
  ------- --------------------- ---------------------------------
        2                    90                                90
        3                     0                                 0
        4                 1,620                             1,620
        5                     0                                 0
        6               162,000                           162,000
        7               777,600                        $-777,600$
:::

The variance also equals $\|\beta\|^2=45+36+9=90$.

# Extensions {#sec:extensions}

## One Gaussian predictor

::: {#prop:gaussian .proposition}
**Proposition 6.1**. *Let $Z\sim N(0,1)$ be independent of the Gamma
dictionary. For $c,e\in\mathbb R$, $$Y_\beta+cZ\overset{d}{=}Y_\gamma+eZ
 \quad\Longleftrightarrow\quad
 \mu_\beta=\mu_\gamma\ \text{and}\ c^2=e^2.$$*
:::

::: proof
*Proof.* The logarithmic derivative of the joint transform
is [5](#eq:derivative) plus $c^2t$. Comparing poles and residues
again identifies $\mu_\beta$, since the added polynomial has no poles.
Subtracting the now identical Gamma terms identifies $c^2$. The converse
follows from equality of the transforms near zero. ◻
:::

Under [SR](#eq:SR), the
only ambiguities are equal-shape Gamma permutations and the Gaussian
sign. Every fiber is finite even
without [SR](#eq:SR).
For several independent standard Gaussian coordinates, the Gaussian part
determines only the squared coefficient norm; a nonzero norm then gives
a continuous ambiguity. If a single Gaussian has known mean $\eta\ne0$
and variance $\sigma^2>0$, its coefficient is recovered from the
remaining mean after the Gamma part is determined.

## An analytic convolution-family theorem

::: {#thm:family .theorem}
**Theorem 6.2**. *Suppose a known family $(Z_\alpha)_{\alpha>0}$ has
moment-generating functions on neighborhoods of zero satisfying
$$\log\mathbb Ee^{tZ_\alpha}=\alpha\psi(t),$$ where $\psi$ is analytic,
$\psi(0)=0$, and $v=\psi''(0)>0$. Fix $d$ and positive
$\alpha_1,\ldots,\alpha_d$, take independent $Z_{\alpha_i}$, and put
$$\begin{equation}
\label{eq:family}
 X_i=\frac{Z_{\alpha_i}-\alpha_i\psi'(0)}{\sqrt{\alpha_i v}},
 \qquad a_i=\frac{\beta_i}{\sqrt{\alpha_i v}}.
\end{equation}$$ Assume $\psi^{(n)}(0)\ne0$ for $n=2,\ldots,2d+1$. Then
equality of response laws is equivalent to equality of
$\sum_{a_i\ne0}\alpha_i\delta_{a_i}$, and is determined by cumulants of
those orders. The fiber, minimality, arithmetic-criterion,
labeled-uniqueness, and generic-identification conclusions above
continue to hold, with coefficient reconstruction
$$\gamma_i=s_j\sqrt{\alpha_i v}\quad(i\in I_j),\qquad
 \gamma_i=0\quad(i\in I_0).$$*
:::

::: proof
*Proof.* The response cumulant-generating function is
$$K_\beta(t)=\sum_i\alpha_i[\psi(a_it)-a_it\psi'(0)].$$ For every
required order,
$$\frac{\kappa_n(Y_\beta)}{\psi^{(n)}(0)}=\sum_i\alpha_i a_i^n.$$ The
nonvanishing assumption permits division. The Vandermonde argument of
Theorem [5.1](#thm:cumulants) recovers the aggregate measure from these
normalized cumulants. Conversely, that measure determines $K_\beta$
locally. The finite allocation and total-positive-mass arguments
therefore apply unchanged. For the necessity part of
Theorem [4.1](#thm:sharp), the
squared coefficients are now $\alpha_i v a_i^2$; the common positive
factor $v$ preserves the separated-interval construction. ◻
:::

The assumptions are sufficient and are not asserted to be necessary. A
finite set of nonzero derivatives suffices for a fixed $d$. Gamma
variables have $\psi(t)=-\log(1-t)$ and $v=1$. Poisson variables have
$\psi(t)=e^t-1$ and $v=1$, so every required derivative is nonzero. Pure
Gaussian convolution families have zero higher cumulants and do not
satisfy this hypothesis. No worst-case cutoff claim for each individual
convolution family is inferred from the Gamma lower bound.

## Direct verification for Poisson predictors

For independent $P_i\sim\operatorname{Poisson}(\lambda_i)$ and
$X_i=(P_i-\lambda_i)/\sqrt{\lambda_i}$, put
$a_i=\beta_i/\sqrt{\lambda_i}$. Then
$$K''_\beta(t)=\sum_{a_i\ne0}\lambda_i a_i^2e^{a_it}.$$ Distinct real
exponentials are linearly independent: if their linear combination
vanishes near zero, its successive derivatives at zero give an
invertible Vandermonde system. Thus $K''_\beta$ determines the scales
and the weights $\lambda_i a_i^2$. Division by $a_i^2$ recovers
$\sum_{a_i\ne0}\lambda_i\delta_{a_i}$. Equality of this measure gives
equality of the centered transforms. This supplies a direct proof of the
Poisson case without Gamma pole calculations.

# Scope, reproducibility, and research status

The results distinguish three questions: recovering a distributional
aggregate, allocating that aggregate to a fixed predictor dictionary,
and reconstructing it from finitely many cumulants. Minimality excludes
unused predictors but does not guarantee unique allocation.
Condition [SR](#eq:SR)
is the exact uniform replacement for signed-permutation identification
in the Gamma model. Finite ambiguity holds without that condition.

The unrestricted finite-identifiability question for arbitrary
independent standardized non-Gaussian predictors is not resolved here.
Neither are finite-sample estimation, noisy-response deconvolution,
unknown shape parameters, numerical conditioning guarantees, or
efficient exact subset-sum algorithms. The lower bound permits signed
coefficients and concerns the highest order of a consecutive cumulant
segment.

The accompanying public package contains the manuscript source, original
standard-library exact checkers, machine-readable outputs, a response to
the supplied review, and provenance records. The original finite grid
covers 2,055 scale vectors. Additional polynomial checks test the
lower-bound identity in dimensions 1 through 20. Semantic negative
controls reject changed signs, shape allocations, cumulant
normalization, and a missing variance factor. These finite calculations
detect implementation errors; the all-dimensional claims rest on the
written proofs.

#### Research status and disclosure.

This is an unrefereed candidate. AI tools assisted proof development,
manuscript preparation, exact-check orchestration, and internal
adversarial review. The cumulant lower-bound construction originated in
a supplied review and was checked before inclusion. Supplied review
identities and processes have not been authenticated; local replay does
not establish external independence or endorsement. Historical novelty
is not certified, and no proof-assistant formalization is supplied.
Anonymous is the scholarly creator under the Evidence Press publication
protocol.

#### Data and code availability.

All computational inputs are explicit rational constants or formulas in
this paper. The public package contains original Python checkers and
reproduction instructions. No empirical or personal data are used.
Original prose and data are released under CC0-1.0 and original code
under MIT. Supplied third-party review files are not redistributed.
Repository: <https://github.com/ipitchford/unlinked-gamma-regression>.
Version 0.1.0-candidate archive:
<https://doi.org/10.5281/zenodo.22858495>.

## References

<a id="ref-AB"></a>

**[AB]** M. Azadkia and F. Balabdaoui. Linear regression with unmatched data: A
deconvolution perspective. *Journal of Machine Learning Research*,
25(197):1--55, 2024. <https://jmlr.org/papers/v25/22-0930.html>.

<a id="ref-BDD"></a>

**[BDD]** F. Balabdaoui, A. Di Noia, and C. Durot. Deconvolution in unlinked
linear models. *Journal of Machine Learning Research*, 27(101):1--39,
2026. <https://jmlr.org/papers/v27/25-0516.html>.

<a id="ref-BSS"></a>

**[BSS]** F. Balabdaoui, M. Slawski, and J. Steffani. Identifiability in unlinked
linear regression: Some results and open problems. arXiv:2507.14986v1,
2025. <https://arxiv.org/abs/2507.14986v1>.

<a id="ref-JRY"></a>

**[JRY]** L. F. James, B. Roynette, and M. Yor. Generalized Gamma convolutions,
Dirichlet means, Thorin measures, with explicit examples. *Probability
Surveys*, 5:346--415, 2008.
[doi:10.1214/07-PS118](https://doi.org/10.1214/07-PS118).

<a id="ref-KPR"></a>

**[KPR]** S. Kunis, T. Peter, T. Römer, and U. von der Ohe. A multivariate
generalization of Prony's method. *Linear Algebra and its Applications*,
490:31--47, 2016.
[doi:10.1016/j.laa.2015.10.023](https://doi.org/10.1016/j.laa.2015.10.023).

<a id="ref-AGY"></a>

**[AGY]** A. Akinshin, G. Goldman, and Y. Yomdin. Geometry of error amplification
in solving Prony system with near-colliding nodes. arXiv:1701.04058v5,
2019 (first version 2017). <https://arxiv.org/abs/1701.04058v5>.

