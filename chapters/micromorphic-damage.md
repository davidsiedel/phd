# Micromorphic damage behaviours for quasi-brittle materials

## Introduction {.unnumbered}

The variational approach to fracture takes its grounds in the work of
Francfort and Marigo which recasted the Griffith theory into an enery
minimization problem [@francfort_revisiting_1998;@francfort_vers_2002].
This revisted approach of the Griffith theory is however not tractable
with standard numerical methods
[@bourdin_numerical_2000;@chambolle_approximation_2018], in particular
the commonly used finite element method. For this reason, Bourdin *et
al.* developped regularised versions [@bourdin_numerical_2000] following
the works of Ambrosio and Tortorelli [@ambrosio1990approximation].

The so-called phase-field approaches to fracture have since become
widely popular. As pointed by Gerasimov and De Lorenzis in their
excellent review [@gerasimov_numerical_2020], one of the main
difficulties in the implementation of those approaches is the treatment
of the irreversibility constraint (the damage can only increase), a
question on which a considerable amount of works has been published.
Most of the proposed solutions are not directly implemented in standard
FEM or FFT solvers. An noticeable exception to this statement is the
Miehe' alternative based an the so-called history variable
[@miehe_phase_2010]. However, Miehe' alternative is not variationaly
consistent.

Following Forest' micromorphic framework
[@forest_micromorphic_2009;@forest_nonlinear_2016], we propose in
Section @sec:micromorphicdamage:description a class of micromorphic
brittle behaviours which can approximate classical models of britle
fracture in a variationnaly consistent way. Those behaviours treat the
irreversibility constraint locally, at the integration points. Similar
advantages have been highlighted by by Rezaee-Hajidehi et al. in the
context of phase-field approaches to phase transformation
[@rezaee-hajidehi_micromorphic_2021]. The balance equations are
standard partial derivative equations which can readily be solved by
most FEM or FFT solvers.

Such micromorphic models were recently investigated by Bharali *et al.*
[@bharali_computational_2021] to approximate the AT1 and AT2 models
using a monolithic resolution strategy. In this paper, we exploit the
variational basis of the behaviour to derive in Section
@sec:micromorphicdamage:alternate_minimisation three alternate
minimisation schemes whose convergence is garanteed.

Several test cases comparing the prediction of the classical AT2 model
and its micromorphic counterpart are presented in Section
@sec:micromorphicdamage:test_cases. The choice of the penalisation
parameter is discussed in depths.

Two numerical experiments are presented in Section
@sec:micromorphicdamage:numerical_experiments which assess:

- The performance of the micromorphic approach with high order finite
  elements in the case of shear driven fracture.
- The scalability of the micromorphic approach.

## Description of the micromorphic behaviours {#sec:micromorphicdamage:description}

In this paper, we consider the quasi-static evolution of a body
\(\Omega\) made of a brittle material.

The state of this material is characterized, at each time step, by:

- A displacement field \(\vec{u}\).
- A micromorphic damage field \(d_{\chi}\).
- A local damage field \(d\).

In the view of simple generalized standard materials
[@moreau_sur_1970;@halphen_sur_1975;@ehrlacher_principe_1985;@nguyen_standard_2002],
the micromorphic model is defined by the following incremental
Lagrangian [@lorentz_variational_1999;@forest_localization_2004]:
\[
\mathcal{L}\paren{\vec{u}^{\star},d^{\star},d_{\chi}^{\star}}=
\int_{\Omega}
\left[
\freeenergy\paren{\tepsilon^{\star}, d^{\star}, d_{\chi}^{\star},\vnabla\,d_{\chi}^{\star}}+
\Delta\,t\,\dissipationpotential\paren{\Frac{d^{\star}-\bts{d}}{\Delta\,t}}
\right]
\,\dtot\,V
- \int_{\partial\,\Omega_{T}} \vec{T}\,\cdot\,\vec{u}^{\star} \,\dtot\,S
\]

where:

- \(\freeenergy\) is the free energy.
- \(\dissipationpotential\) is the dissipation potential.
- \(\Delta\,t\) is the time increment.
- \(\bts{d}\) is damage at the beginning of the time step.
- \(\vec{T}\) is the imposed traction on the boundary \(\partial\,\Omega_{T}\).
- \(\vec{u}^{\star},d^{\star},d_{\chi}^{\star}\) denotes any admissible
  displacement, damage and micromorphic damage field.
- \(\partial\,\Omega_{T}\) is the part on the boundary on which external
  traction forces are imposed.

To satisfy the Ilyushin-Drucker postulate, the incremental Lagragian
\(\mathcal{L}\) must be convex with respect to each variables
\(\vec{u}^{\star},d^{\star},d_{\chi}^{\star}\) taken independently. It
can be shown that this condition is ensured if the \(\freeenergy\) and
the dissipation potential \(\dissipationpotential\) are convex with
respect to their respective arguments.

> **Body forces and prescribed micromorphic tractions**
>
> The definition of the Lagragian \(\mathcal{L}\) can be enriched by adding
> body forces (such as gravity) and prescribed micromorphic tractions.

The state of the material minimises the incremental Lagragian:
\[
\paren{\ets{\vec{u}}, \ets{d_{\chi}}, \ets{d}} = \underset{\vec{u}^{\star}\in C.A.}{\argmin}\, \mathcal{L}\paren{\vec{u}^{\star},d^{\star},d_{\chi}^{\star}}
\]

In pratice, this free energy is a differentiable function.

This is not the case of the dissipation potential
\(\dissipationpotential\) for time independent mechanisms for which
\(\dissipationpotential\) is assumed to be an homogeneous function of
degree \(1\) which allows us to eliminate the time increment
\(\Delta\,t\) from the definition of the Lagrangian as:
\[
\Delta\,t\,\dissipationpotential\paren{\Frac{d^{\star}-\bts{d}}{\Delta\,t}} = \dissipationpotential\paren{d^{\star}-\bts{d}}
\]

In particular, the dissipation potential generally contains an indicator
function imposing the *irreversibility of the damage evolution*.

### Equilibrium

Deriving equilibrium equations from the principle of the minimum of the
Lagrangian is non trivial due to the fact that the dissipation potentiel
is not differentiable.

It is then convenient to separate the Lagrangian into two parts
\(\mathcal{L}_{1}\) and \(\mathcal{L}_{2}\) as follows:
\[
\begin{aligned}
\mathcal{L}_{1}\paren{\vec{u}^{\star},d^{\star},d_{\chi}^{\star}} &= 
\int_{\Omega}
\freeenergy\paren{\tepsilon^{\star}, d^{\star}, d_{\chi}^{\star},\vnabla\,d_{\chi}^{\star}}
\,\dtot\,V -
\int_{\partial\,\Omega_{T}} \vec{T}\,\cdot\,\vec{u}^{\star} \,\dtot\,S \\
\mathcal{L}_{2}\paren{d^{\star}} &= 
\int_{\Omega}
\dissipationpotential\paren{d^{\star}-\bts{d}}
\,\dtot\,V
\end{aligned}
\]

In this report, we will admit the following mathematical result which
characterize the minima of Lagrangian [@son_standard_2021]:

- The regular part of Lagrangian \(\mathcal{L}_{1}\) is minimal with
  respect to the displacement field \(\vec{u}\) and the micromorphic
  damage field \(d_{\chi}\).
- At each point, the thermodynamic force \(Y\) associated with the
  damage, is in the subgradient of the dissipation potential:
  \[
  Y \in \partial \dissipationpotential
  \]
  where \(Y\) is defined by:
  \[
  Y = -\deriv{\freeenergy}{d}
  \]

In this section, we only consider the condition on the regular part of
the Lagrangian. The evolution of the damage is discussed in Section
@sec:micromorphicdamage:constitutive_equations.

The variation of \(\var{\mathcal{L}_{1}}\) with respect to the
displacement and micromorphic damage field is defined by:
\[
\var{\mathcal{L}_{1}}=
\mathcal{L}_{1}\paren{\ets{\vec{u}}+\var{\vec{u}},\ets{d}, \ets{d_{\chi}} + \var{d_{\chi}}} - 
\mathcal{L}_{1}\paren{\ets{\vec{u}},\ets{d}, \ets{d_{\chi}}}
\]

where the variation \(\var{\vec{u}}\) is null on the part of the
boundary where imposed displacements are prescribed, i.e. on
\(\partial\Omega\setminus\partial\Omega_{T}\).

By retaining only first order terms, this variation can be computed as follows:
\[
\begin{aligned}
\var{\mathcal{L}_{1}}&=
\int_{\Omega}
\left[
\deriv{\freeenergy}{\tepsilon}\,\colon\,\var{\tepsilon}+
\deriv{\freeenergy}{d_{\chi}}\,\var{d_{\chi}}+
\deriv{\freeenergy}{\vnabla\,d_{\chi}}\,\cdot\,\vnabla\,\var{d_{\chi}}
\right]
\,\dtot\,V -
\int_{\partial\,\Omega_{T}} \vec{T}\,\cdot\,\var{\vec{u}} \,\dtot\,S \\
&=
\int_{\Omega}
\left[
\tsigma\,\colon\,\var{\tepsilon}+
a_{\chi}\,\var{d_{\chi}}+
\vec{b}_{\chi}\,\cdot\,\vnabla\,\var{d_{\chi}}
\right]
\,\dtot\,V -
\int_{\partial\,\Omega_{T}} \vec{T}\,\cdot\,\var{\vec{u}} \,\dtot\,S \\
\end{aligned}
\]

where the following thermodynamic forces were introduced:
\[
\tsigma  = \deriv{\freeenergy}{\tepsilon} \quad\quad
a_{\chi} = \deriv{\freeenergy}{d_{\chi}} \quad\quad
\vec{b}_{\chi} = \deriv{\freeenergy}{\vnabla d_{\chi}}
\]

Applying the divergence theorem leads to:
\[
\var{\mathcal{L}_{1}}=
\int_{\Omega}
\left[
-\divergence\,\tsigma\,\cdot\,\var{\vec{u}}+
  \paren{a_{\chi}-\divergence\,\vec{b}_{\chi}}\,\var{d_{\chi}} \right]
  \,\dtot\,V + \int_{\partial\,\Omega_{T}}
  \paren{\tsigma\,\cdot\,\vec{n}-\vec{T}}\,\cdot\,\var{\vec{u}}
  \,\dtot\,S + \int_{\partial\,\Omega}
  \paren{\vec{b}_{\chi}\,\cdot\,\vec{n}}\,\var{\vec{d}_{\chi}}
  \,\dtot\,S
\]
where we took into account the fact that the variation of the
displacement is null on \(\partial\Omega\setminus\partial\Omega_{T}\).

Classical arguments shows that this variation can characterize a
minimum only if all the integrands are zero.

The integrands associated with variation of the displacement field gives
the classical mechanical equilibrium equation in \(\Omega\) and boundary
conditions on \(\partial\,\Omega_{T}\):
\[
\left\{
\begin{aligned}
\divergence\,\tsigma &= 0       & \text{ in } & \Omega \\
\tsigma\,\cdot\,\vec{n}&=\vec{T} & \text{ on } & \partial\,\Omega_{T}
\end{aligned}
\right.
\]{#eq:micromorphicdamage:mechanical_equilibrium}

The integrands associated with variation of the micromorphic damage field
leads to the following balance equation and boundary conditions:
\[
\left\{
\begin{aligned}
\divergence\,\vec{b}_{\chi} &= a_{\chi} &\text{ in }& \Omega \\
\vec{b}_{\chi}\,\cdot\,\vec{n}&=\vec{0} &\text{ on }& \partial\,\Omega
\end{aligned}
\right.
\]{#eq:micromorphicdamage:d_chi}

### Constitutive equations{#sec:micromorphicdamage:constitutive_equations}

The free energy \(\freeenergy\) is additively decomposed as follows:
\[
\freeenergy\paren{\tepsilon, d, d_{\chi}, \vnabla\,d_{\chi}}=
\freeenergyel\paren{\tepsilon, d}+
\freeenergyd\paren{d}+
\freeenergyddchi\paren{d, d_{\chi}}+
\freeenergygdchi\paren{\vnabla\,d_{\chi}}
\]
where:

- \(\freeenergyel\paren{\tepsilon, d}\) describes the mechanical part of
  the free energy.
- \(\freeenergyd\paren{d}\) defines an stored energy du to damage.
- \(\freeenergyddchi\paren{d, d_{\chi}}\) defines the coupling between
  the damage \(d\) and the micromorphic damage \(d_{\chi}\)
- \(\freeenergygdchi\paren{\vnabla\, d_{\chi}}\) defines the a
  micromorphic force.

#### Choices of $\freeenergyel$ and expression of the stress

$\freeenergyel$ determines the expression of the stress and contributes
to the thermodynamic force driving the damage evolution.

A classical choice is to multiply the free energy of an undamaged
elastic material \(\freeenergyel_{0}\paren{\tepsilon}\) by a degradation
function \(g\paren{d}\) as follows:
\[
\freeenergyel\paren{\tepsilon, d} = 
g\paren{d}\,\freeenergyel_{0}\paren{\tepsilon} = \Frac{g\paren{d}}{2}\,\tepsilon\,\colon\,\tenseurq{D}\,\colon\,\tepsilon
\]{#eq:micromorphicdamage:freeenergygel}
where \(\tenseurq{D}\) is the stiffness matrix of the sound material.

The stresss \(\tsigma\) is thus given by:
\[
\tsigma = g\paren{d}\,\tenseurq{D}\,\colon\,\tepsilon
\]

Another classical choice popularised by Miehe [@miehe_phase_2010] is to
use a spectral decomposition of the strain to split the free energy into
a positive and negative part. The degradation function is only applied
to the positive part of the free energy.

#### Evolution of the micromorphic damage

##### Choice of \(\freeenergyddchi\) 

\[
\freeenergyddchi\paren{d, d_{\chi}}=\Frac{H_{\chi}}{2}\,\paren{d-d_{\chi}}^{2}
\]

which leads to the following expression of \(a_{\chi}\):
\[
a_{\chi} = - H_{\chi}\,\paren{d-d_{\chi}}
\]{#eq:micromorphicdamage:achi}

##### Choice of \(\freeenergygdchi\)

\[
\freeenergygdchi\paren{\vnabla\, d_{\chi}} = \Frac{A_{\chi}}{2}\,\vnabla\, d_{\chi}\,\cdot\,\vnabla\, d_{\chi}
\]{#eq:micromorphicdamage:freeenergygdchi}
which leads to the following expression of \(\vec{b}_{\chi}\):
\[
\vec{b}_{\chi} = A_{\chi}\,\vnabla\, d_{\chi}
\]{#eq:micromorphicdamage:bchi}

Combining Equations @eq:micromorphicdamage:achi and
@eq:micromorphicdamage:bchi shows that the micromorphic damage follows
the equation:
\[
A_{\chi}\,\laplacian\,d_{\chi}+ H_{\chi}\,\paren{d-d_{\chi}}= 0
\]{#eq:micromorphicdamage:d_chi2}
where \(\laplacian\) denotes the Laplacian operator.

#### Evolution of the damage

The thermodynamic forces \(Y\) associated with the damage is given by:
\[
\begin{aligned}
Y &= -\derivtot{g}{d}\,\freeenergyel_{0}\paren{\tepsilon}-\derivtot{\freeenergyd}{d}-\deriv{\freeenergyddchi}{d}
&=-\derivtot{g}{d}\,\freeenergyel_{0}\paren{\tepsilon}-\derivtot{\freeenergyd}{d}-H_{\chi}\,\paren{d-d_{\chi}}\\
&=-\derivtot{g}{d}\,\freeenergyel_{0}\paren{\tepsilon}-\derivtot{\freeenergyd}{d}+a_{\chi}\\
\end{aligned}
\]{#eq:micromorphicdamage:Y}

A simple choice of the dissipation potential is:
\[
\dissipationpotential\paren{\dot{d}} = Y_{0}\,\dot{d}+ \mathrm{I}_{\mathbb{R}_{+}}\paren{\dot{d}} 
\]{#eq:micromorphicdamage:dissipationpotential}
where \(\mathrm{I}_{\mathbb{R}_{+}}\) is the characteristic associated with positive real number, i.e.:
\[
\mathrm{I}_{\mathbb{R}_{+}}=
\left\{
\begin{aligned}
0 &\quad\text{if}\quad x\geq 0 \\
+\infty &\quad\text{if}\quad x< 0 \\
\end{aligned}
\right.
\]

This dissipation potential is equivalent to define the following damage surface:
\[
Y = Y_{0}
\]{#eq:micromorphicdamage:yield}

The evolution of damage is thus driven by the following equations:
\[
\left\{
\begin{aligned}
\Delta\,d\,\paren{Y - Y_{0}}&=0\\
\Delta\,d&\geq 0\\
Y - Y_{0}&\leq 0
\end{aligned}
\right.
\]{#eq:micromorphicdamage:KTT}

Combining Equations @eq:micromorphicdamage:d_chi2,
@eq:micromorphicdamage:Y and @eq:micromorphicdamage:yield, the yield
surface may also be written:
\[
-\derivtot{g}{d}\,\freeenergyel_{0}\paren{\tepsilon}=
Y_{0}+\derivtot{\freeenergyd}{d}+A_{\chi}\,\laplacian\,d_{\chi}
\]

### Link with classical models of brittle fracture

Choices described by Equations @eq:micromorphicdamage:freeenergygel,
@eq:micromorphicdamage:dissipationpotential and
@eq:micromorphicdamage:freeenergygdchi lead to the following expression
of the Lagrangian:
\[
\begin{aligned}
\mathcal{L}\paren{\vec{u}^{\star},d^{\star},d_{\chi}^{\star}}
&=\int_{\Omega}
\left[
g\paren{d^{\star}}\,\freeenergyel_{0}\paren{\tepsilon^{\star}}+
\freeenergyd\paren{d^{\star}}+
Y_{0}\,d^{\star}
+\Frac{A_{\chi}}{2}\,\vnabla\, d_{\chi}^{\star}\,\cdot\,\vnabla\, d_{\chi}^{\star}
\right]
\,\dtot\,V\\
&+\int_{\Omega}
\left[
\Frac{H_{\chi}}{2}\,\paren{d^{\star}-d_{\chi}^{\star}}^{2}+
\mathrm{I}_{\mathbb{R}_{+}}\paren{d^{\star}-\ets{d}} 
\right]
\,\dtot\,V
- \int_{\partial\,\Omega_{T}} \vec{T}\,\cdot\,\vec{u}^{\star} \,\dtot\,S
\end{aligned}
\]{#eq:micromorphicdamage:Lagrangian}
Note that the constant term \(Y_{0}\,\ets{d}\), which thus does not have
any influence of the solution, has been removed from the expression of
the Lagrangian.

For high values of the \(H_{\chi}\) coefficient, the contribution to the
\(\freeenergyddchi\paren{d,
d_{\chi}}=\Frac{H_{\chi}}{2}\,\paren{d-d_{\chi}}^{2}\) may be seen as a
penalisation term which ensures that the damage \(d\) and the
micromorphic damage \(d_{\chi}\) are close. Intuitively, if the
coefficient \(H_{\chi}\) tends to infinity, those variables must become
equal to ensure a finite energy.

Hence, we expect the Lagrangian to have the following limit:
\[
\begin{aligned}
\mathcal{L}\paren{\vec{u}^{\star},d^{\star}}
&=\int_{\Omega}
\left[
g\paren{d^{\star}}\,\freeenergyel_{0}\paren{\tepsilon^{\star}}+
\freeenergyd\paren{d^{\star}}+
Y_{0}\,d^{\star}
+\Frac{A_{\chi}}{2}\,\vnabla\, d^{\star}\,\cdot\,\vnabla\, d^{\star}
\right]
\,\dtot\,V\\
&+\int_{\Omega}
\left[
\mathrm{I}_{\mathbb{R}_{+}}\paren{d^{\star}-\ets{d}} 
\right]
\,\dtot\,V
- \int_{\partial\,\Omega_{T}} \vec{T}\,\cdot\,\vec{u}^{\star} \,\dtot\,S
\end{aligned}
\]{#eq:micromorphicdamage:LagrangianLimit}

: Parameters of the AT1, AT2 and Lorentz models. {#tbl:micromorphicdamage:ATparameters}

+---------------------------+----------------------------------+-----------------------------------+------------------------------------------------+
|                           | AT1                              | AT2                               | Lorentz                                        |
+:=========================:+:================================:+:=================================:+:==============================================:+
| \(g\paren{d}\)            | \(\paren{1-d}^{2}\)              | \(\paren{1-d}^{2}\)               | \(\paren{\Frac{1-d}{1+\gamma\,d}}^{2}\)        |
+----------------------------------+----------------------------------+-----------------------------------+-----------------------------------------+
| \(\freeenergyd\paren{d}\) | \(\Frac{3\,G_{c}}{8\,l_{0}}\,d\) | \(\Frac{G_{c}}{2\,l_{0}}\,d^{2}\) | \(\Frac{3\,G_{c}}{8\,l_{0}}\,d\)               |
+----------------------------------+----------------------------------+-----------------------------------+-----------------------------------------+
| \(A_{\chi}\)              | \(\Frac{3}{4}\,G_{c}\,l_{0}\)    | \(G_{c}\,l_{0}\)                  | \(\Frac{3}{4}\,G_{c}\,l_{0}\)                  |
+----------------------------------+----------------------------------+-----------------------------------+-----------------------------------------+
| \(Y_{0}\)                 | \(0\)                            | \(0\)                             |  \(0\)                                         |
+---------------------------+----------------------------------+-----------------------------------+------------------------------------------------+

Lagrangian @eq:micromorphicdamage:Lagrangian can be identified with
Lagrangians of many classical models of brittle fracture with
appropriate choices of \(g\paren{d}\), \(\freeenergyd\paren{d}\),
\(A_{\chi}\) and \(Y_{0}\).

The cases of AT1 and AT2 models, originating from the work of Ambrosio
and Tortorelli (AT) [@ambrosio_approximation_1990] and the case of
Lorentz's model [@lorentz_gradient_2011;@lorentz_convergence_2011], are
treated in Table @tbl:micromorphicdamage:ATparameters where the
following quantities were introduced:

- \(G_{c}\) is the fracture energy.
- \(l_{0}\) is a characteristic length.
- \(\gamma\) is a parameter of the Lorentz' model.

Note that we made that for the AT1 and Lorentz' models, an alternative choice, can be made:
\[
\freeenergyd\paren{d}= 0  \quad\text{and}\quad Y_{0}=\Frac{3}{8}\,G_{c}\,l_{0}
\]
While leading the same Lagrangian, this alternative choice has a totally
different physical meaning, since part of the fracture energy is now
considered as dissipated rather than stored. Since neither crack healing
nor coupling with heat transfer are considered, those choices are
equivalent in the context of this paper.

## Alternate minimisation schemes {#sec:micromorphicdamage:alternate_minimisation}

### A first alternate minimization scheme

The Lagrangian \(\mathcal{L}\) is not convex, but convex with respect to
each variables taken independantly.

Thus, in the spirit of the alternate minimization scheme proposed by
Bourdin et al. [@bourdin_numerical_2000], the following iterative scheme
can be proposed:
\[
\left\{
\begin{aligned}
\iter{n+1}{\vec{u}} &= \underset{\vec{u}^{\star}\in C.A.}{\argmin}\, \mathcal{L}\paren{\vec{u}^{\star},\iter{n}{d},\iter{n}{d_{\chi}}}\\
\iter{n+1}{d_{\chi}} &= \argmin \,\mathcal{L}\paren{\iter{n+1}{\vec{u}},\iter{n}{d},d_{\chi}^{\star}} \\
\iter{n+1}{d} &= \argmin \,\mathcal{L}\paren{\iter{n+1}{\vec{u}},d^{\star},\iter{n+1}{d_{\chi}}} \\
\end{aligned}
\right.
\]
where \(\iter{n}{\vec{u}}\), \(\iter{n}{d_{\chi}}\) and
\(\iter{n}{d_{\chi}}\) denote respectively the estimates of the
displacement field, micromorphic damage field and damage field at the
n\textsuperscript{th} iteration of the algorithm.

Each steps of the algorithm diminishes the value of the Lagrangian,
ensuring the convergence of the scheme.

Minimisation with respect to \(\vec{u}\) and \(d_{\chi}\) leads to a
solve two standard Partial Differential Equations (PDE), see Equation
@eq:micromorphicdamage:mechanical_equilibrium and
@eq:micromorphicdamage:d_chi. Note that:

- The PDE associated with \(\vec{u}\) is a linear elastic problem with
  spatially variable mechanical coefficients. This problem becomes non
  linear if unilateral effects are taking into account.
- The PDE associated with \(d_{\chi}\) is always linear and
  \(\iter{n+1}{d_{\chi}}\) is the solution of (see Equation
  @eq:micromorphicdamage:d_chi2):
  \[
  -A_{\chi}\,\laplacian\,\iter{n+1}{d_{\chi}}+H_{\chi}\,\iter{n+1}{d_{\chi}}=
  H_{\chi}\,\iter{n}{d}
  \]
  Note that this PDE is close to the PDE describing heat transfer and can
  thus be solved in most finite element solvers. See @azinpour_simple_2018
  for an alternative implementation of the phase-field model based on this analogy.

Minimisation with respect to \(d\) is local and depends on the model
considered. Appendix @sec:micromorphicdamage:damage_evolution describes
the local equations that must be solved in each case.

<!--

> **Note**
>
> Since the incremental Lagragian is convex in \(\vec{u}\) and
> \(d_{\chi}\), another scheme may be considered:
> 
> \[
> \left\{
> \begin{aligned}
> \paren{\iter{n+1}{\vec{u}},\iter{n+1}{d_{\chi}}} &= \underset{\vec{u}^{\star}\in C.A.}{\argmin}\, \mathcal{L}\paren{\vec{u}^{\star},\iter{n}{d},d_{\chi}^{\star}} \\
> \iter{n+1}{d} &= \argmin \,\mathcal{L}\paren{\iter{n+1}{\vec{u}},d^{\star},\iter{n+1}{d_{\chi}}} \\
> \end{aligned}
> \right.
> \]
>
> However, as the balance equations
> @eq:micromorphicdamage:mechanical_equilibrium and
> @eq:micromorphicdamage:d_chi are uncoupled (for a constant damage),
> such scheme does not seem very attractive.

-->

### A second alternate minimization scheme

Since an update of the damage variable is computationaly inexpensive,
compared to the computation of the displacement and micromorphic damage,
one may consider evalutating its value twice, as follows:
\[
\left\{
\begin{aligned}
\iter{n+1}{\vec{u}} &= \underset{\vec{u}^{\star}\in C.A.}{\argmin}\, \mathcal{L}\paren{\vec{u}^{\star},\iter{n}{d},\iter{n}{d_{\chi}}}\\
\iter{n+1/2}{d} &= \argmin \,\mathcal{L}\paren{\iter{n+1}{\vec{u}},d^{\star},\iter{n}{d_{\chi}}} \\
\iter{n+1}{d_{\chi}} &= \argmin \,\mathcal{L}\paren{\iter{n+1}{\vec{u}},\iter{n+1/2}{d},d_{\chi}^{\star}} \\
\iter{n+1}{d} &= \argmin \,\mathcal{L}\paren{\iter{n+1}{\vec{u}},d^{\star},\iter{n+1}{d_{\chi}}} \\
\end{aligned}
\right.
\]

The damage estimates \(\iter{n+1/2}{d}\) is given by an appropriate
modification of Equation @eq:micromorphicdamage:damage_estimate.

### A third alternate minimization scheme

The third alternate minimization scheme is based on the fact that the
minimisation with respect to \(d\) and \(d_{\chi}\) is convex:
\[
\left\{
\begin{aligned}
\iter{n+1}{\vec{u}} &= \underset{\vec{u}^{\star}\in C.A.}{\argmin}\, \mathcal{L}\paren{\vec{u}^{\star},\iter{n}{d},\iter{n}{d_{\chi}}}\\
\paren{\iter{n+1}{d},\iter{n+1}{d_{\chi}}} &= \argmin \,\mathcal{L}\paren{\iter{n+1}{\vec{u}},d^{\star},d_{\chi}^{\star}}
\end{aligned}
\right.
\]

The evolution of \(d_{\chi}\) is still given by Equation
@eq:micromorphicdamage:d_chi but the determination of the conjugated
force \(a_{\chi}\) relies locally on the resolution of Equation
@eq:micromorphicdamage:damage_estimate. As this equation is only linear
by part, Equation @eq:micromorphicdamage:d_chi is indeed non linear and
its resolution is performed in this work using a Newton algorithm.

To be more specific, the computation of the stiffness matrix associated
with Problem @eq:micromorphicdamage:d_chi requires the derivative
\(\deriv{a_{\chi}}{\Delta\,d_{\chi}}\) which is piece-wise constant. In
our numerical experiments, this Newton algorithm usually converges in
less than 10 iterations.

