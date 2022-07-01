## Introduction
\label{sec_micromorphic_introduction}

### Outline
\label{sec_micromorphic_introduction_outline}

\cite{abbas_hybrid_2018}

## Model problem
\label{sec_micromorphic_model_problem}

##### Solid body in the current configuration

Let $\BodyEuler$ a solid body that is subjected to a volumetric load $\tensori{f}{}_v$ in the current configuration at some time $t > 0$.
A displacement $\tensori{u}{}_{d}$ is prescribed
on the Dirichlet boundary $\BodyEulerDirichletBoundary$ and a surface load $\tensori{t}{}_{n}$ is imposed
on the Neumann boundary $\BodyEulerNeumannBoundary$.

##### Transformation mapping

Let $\tensori{\Phi}{}$ the transformation mapping of the solid body from the initial configuration $\BodyLagrange$ to the current configuration $\BodyEuler$.
The displacement field $\DisplacementField$ is such that $\DisplacementField = \tensori{\Phi}{} - \IdentityTensorI$ where $\IdentityTensorI$
is the identity application on $\BodyLagrange$.
The gradient of the transformation is denoted $\TransformationGradientField = \nabla \tensori{\Phi}{} = \IdentityTensorII + \DisplacementGradientField$
where $\DisplacementGradientField = \nabla \DisplacementField$ is the gradient of the displacement.
Let $\BodyLagrangeDirichletBoundary$ and $\BodyLagrangeNeumannBoundary$ the images of $\BodyEulerDirichletBoundary$ and $\BodyEulerNeumannBoundary$ respectively by $\tensori{\Phi}{}^{-1}$.

##### External loads in the reference configuration

In the reference configuration, the solid is subjected to a volumetric load
$\tensori{f}{}_V$, a prescribed displacement $\tensori{u}{}_D$ on $\BodyLagrangeDirichletBoundary$, and a surface load $\tensori{t}{}_N$ on $\BodyLagrangeNeumannBoundary$, where the volumetric and surface loads $\tensori{f}{}_V$ and $\tensori{t}{}_N$ have been obtained from their counterparts
$\tensori{f}{}_v$ and $\tensori{t}{}_n$ respectively, using Nanson formulaes. For the sake of simplicty, they are supposed to be independent
on $\tensorii{F}{}$.

##### State of the solid
the damage field $\DamageField$ and a micromorphic damage field $\MicromorphicDamageField$.
In the following, let $\tensori{g}{}_{\chi} = \nabla \MicromorphicDamageField$ the gradient of the micromorphic damage variable.

##### Free energy potential

The free energy potential $\psi_{\BodyLagrange}$ of the body $\BodyLagrange$ reads as a function of the displacement $\DisplacementField$, the (local) damage $d$ and the micromorphic damage $\MicromorphicDamageField$, in the form
<!---  -->
<!---  -->
<!---  -->
\begin{equation}
    \psi_{\BodyLagrange}
    (\TransformationGradientField, \DamageField, \MicromorphicDamageField, \MicromorphicDamageGradientField)
    =
    \psi_{\tensoriis{F}, \DamageField}
    (\TransformationGradientField, \DamageField)
    +
    \psi_{\DamageField}
    (\DamageField)
    +
    \psi_{\MicromorphicDamageField, \DamageField}
    (\MicromorphicDamageField, \DamageField)
    +
    \psi_{\MicromorphicDamageGradientField}
    (\MicromorphicDamageGradientField)
\end{equation}
<!---  -->
<!---  -->
<!---  -->
where $\psi_{\tensoriis{F}, \DamageField}$ denotes the mechanical contribution that takes into account the damage in the medium,
$\psi_{\DamageField}$ is the energy stored during the fracture process,
$\psi_{\DamageField, \MicromorphicDamageField}$ is a coupling term between the damage and micromorphic damage variables, and
$\psi_{\MicromorphicDamageGradientField}$ defines the micromorphic force.

##### Stresses

The following stresses are introduced
<!---  -->
<!---  -->
<!---  -->
\begin{equation}
    \begin{aligned}
        \PKIStressField = \deriv{\psi_{\BodyLagrange}}{\TransformationGradientField}
        &&
        \MicromorphicDamageStressField = \deriv{\psi_{\BodyLagrange}}{\MicromorphicDamageGradientField}
        &&
        \MicromorphicDamageForceField = \deriv{\psi_{\BodyLagrange}}{\MicromorphicDamageField}
        &&
        \DamageForceField = \deriv{\psi_{\BodyLagrange}}{\DamageField}
    \end{aligned}
\end{equation}
<!---  -->
<!---  -->
<!---  -->
where $\PKIStressField$ is the first Piola-Kirchoff stress tensor, and $\MicromorphicDamageStressField, \MicromorphicDamageForceField$ and $\DamageForceField$ are the thermodynamic
forces associated to $\tensori{g}{}_{\chi}, d_{\chi}$ and $d$ respectively.

##### Dissipation potential

A dissipation potential $\phi_{\bodyLag}(d)$ accounts for the energy dissipated by the fracture process in the medium, and is assumed to be
an homogeneous function of degree one such that
<!---  -->
<!---  -->
<!---  -->
\begin{equation}
    \begin{aligned}
        \Delta \, t \, \phi_{\BodyLagrange}(\frac{\DamageField - \DamageField \TraceOperator{t}} {\Delta \, t}) = \phi_{\BodyLagrange}(\DamageField - \DamageField \TraceOperator{t})
        &&
        \forall \Delta \, t > 0
    \end{aligned}
\end{equation}
<!---  -->
<!---  -->
<!---  -->
In particular, the dissipation potential generally contains an indicator function imposing the irreversibility of the
damage evolution.

##### Total Lagrangian

The total Hu-Washizu Lagrangian of the body $\BodyLagrange$ is defined
<!---  -->
<!---  -->
<!---  -->
\begin{equation}
    \LagrangianOperator{\BodyLagrange}{tot}
    =
    \LagrangianOperator{\BodyLagrange}{HW}
    +
    \int_{\BodyLagrange} \phi_{\BodyLagrange}(\DamageField - \DamageField \TraceOperator{t})
\end{equation}
<!---  -->
<!---  -->
<!---  -->
where
<!---  -->
<!---  -->
<!---  -->
\begin{equation}
    \LagrangianOperator{\BodyLagrange}{HW}
    =
    \int_{\BodyLagrange} \psi_{\BodyLagrange}
    +
    \int_{\BodyLagrange} (\nabla \DisplacementField - \DisplacementGradientField) : \PKIStressField
    +
    \int_{\BodyLagrange} (\nabla \MicromorphicDamageField - \MicromorphicDamageGradientField) \cdot \MicromorphicDamageStressField
    -
    \int_{\BodyLagrange} \tensori{f}{}_V \cdot \DisplacementField
    -
    \int_{\BodyLagrangeNeumannBoundary} \tensori{t}{}_{N} \cdot \DisplacementField \TraceOperator{\BodyLagrangeNeumannBoundary}
\end{equation}
<!---  -->
<!---  -->
<!---  -->
The solution $(\DisplacementField, \DisplacementGradientField, \PKIStressField, \DamageField, \MicromorphicDamageField, \MicromorphicDamageGradientField, \MicromorphicDamageStressField)$
satisfying the mechanical equilibrium minimizes the Lagragian $\LagrangianOperator{\BodyLagrange}{HW}$. The first order variation with respect to each variables yields the weak equations
<!---  -->
<!---  -->
<!---  -->
\begin{subequations}
    \label{eq_micromorphic_hu_washizu_derivative_0}
    \begin{alignat}{3}
      \langle \deriv{\LagrangianOperator{\BodyLagrange}{HW}}{\DisplacementField} , \delta \DisplacementField \rangle
      =
      & \int_{\BodyLagrange} \PKIStressField : \nabla \delta \DisplacementField
      -
      \int_{\BodyLagrange} \tensori{f}_V \cdot \delta \DisplacementField
      -
      \int_{\BodyLagrangeNeumannBoundary} \neumannLag \cdot \delta \DisplacementField \vert_{\BodyLagrangeNeumannBoundary}
      &&
      \ \ \ \ \ \ \ \
      &&
      \forall \delta \DisplacementField
      \label{eq_micromorphic_hu_washizu_derivative_0:eq0}
      \\
      \langle \deriv{\LagrangianOperator{HW}{\BodyLagrange}}{\PKIStressField} , \delta \PKIStressField \rangle
      =
      & \int_{\BodyLagrange} (\nabla \DisplacementField - \DisplacementGradientField ) : \delta \PKIStressField
      &&
      \ \ \ \ \ \ \ \
      &&
      \forall \delta \PKIStressField
      \label{eq_micromorphic_hu_washizu_derivative_0:eq1}
      \\
      \langle \deriv{\LagrangianOperator{\BodyLagrange}{HW}}{\DisplacementGradientField} , \delta \DisplacementGradientField \rangle
      =
      & \int_{\BodyLagrange} (\deriv{\psi_{\BodyLagrange}}{\DisplacementGradientField} - \PKIStressField) : \delta \DisplacementGradientField
      &&
      \ \ \ \ \ \ \ \
      && \forall \delta \DisplacementGradientField
      \label{eq_micromorphic_hu_washizu_derivative_0:eq2}
      \\
      \langle \deriv{\LagrangianOperator{\BodyLagrange}{HW}}{\MicromorphicDamageField} , \delta \MicromorphicDamageField \rangle
      =
      & \int_{\BodyLagrange} \MicromorphicDamageForceField \, \delta \MicromorphicDamageField + \int_{\BodyLagrange} \MicromorphicDamageStressField \cdot \nabla \MicromorphicDamageField
      &&
      \ \ \ \ \ \ \ \
      && \forall \delta d^\chi
      \label{eq_micromorphic_hu_washizu_derivative_0:eq3}
      \\
      \langle \deriv{\LagrangianOperator{\BodyLagrange}{HW}}{\MicromorphicDamageStressField} , \delta \MicromorphicDamageStressField \rangle
      =
      & \int_{\BodyLagrange} (\nabla \MicromorphicDamageField - \MicromorphicDamageGradientField) \cdot \delta \MicromorphicDamageStressField
      &&
      \ \ \ \ \ \ \ \
      && \forall \delta \MicromorphicDamageStressField
      \label{eq_micromorphic_hu_washizu_derivative_0:eq4}
      \\
      \langle \deriv{\LagrangianOperator{\BodyLagrange}{HW}}{\MicromorphicDamageGradientField} , \delta \MicromorphicDamageGradientField \rangle
      =
      & \int_{\BodyLagrange} (\deriv{\mecPotential}{\MicromorphicDamageGradientField} - \MicromorphicDamageStressField) \cdot \delta \MicromorphicDamageGradientField
      &&
      \ \ \ \ \ \ \ \
      && \forall \delta \tensori{g}{}_{\chi}
      \label{eq_micromorphic_hu_washizu_derivative_0:eq5}
    \end{alignat}
\end{subequations}

##### Strong equation

The following strong equations for the sole displacement problem are deduced from the weak equation
\eqref{eq_micromorphic_hu_washizu_derivative_0:eq1} ,
\eqref{eq_micromorphic_hu_washizu_derivative_0:eq2}
and
\eqref{eq_micromorphic_hu_washizu_derivative_0:eq0}
respectively
<!---  -->
<!---  -->
<!---  -->
\begin{subequations}
    \label{eq_micromorphic_strong_equations_meca}
    \begin{alignat}{3}
    \DisplacementGradientField - \nabla \DisplacementField & = 0
    &&
    \ \ \ \ \ \ \ \
    &&
    \textit{displacement gradient}
    \label{eq_micromorphic_strong_equations_meca:eq0}
    \\
    \PKIStressField - \deriv{\psi_{\BodyLagrange}}{\DisplacementGradientField} & = 0
    &&
    \ \ \ \ \ \ \ \
    &&
    \textit{constitutive equation}
    \label{eq_micromorphic_strong_equations_meca:eq1}
    \\
    \nabla \cdot \PKIStressField + \tensori{f}{}_{V} & = 0
    &&
    \ \ \ \ \ \ \ \
    &&
    \textit{balance of momentum}
    \label{eq_micromorphic_strong_equations_meca:eq2}
    \\
    \PKIStressField \cdot \tensori{n}{} - \neumannLag{} & = 0
    &&
    \ \ \ \ \ \ \ \
    &&
    \textit{continuity of the normal stress}
    \label{eq_micromorphic_strong_equations_meca:eq3}
    \end{alignat}
\end{subequations}
<!---  -->
<!---  -->
<!---  -->
Similarly, the strong equations governing the sole micromorphic damage problem are deduced from
\eqref{eq_micromorphic_hu_washizu_derivative_0:eq4} ,
\eqref{eq_micromorphic_hu_washizu_derivative_0:eq5}
and
\eqref{eq_micromorphic_hu_washizu_derivative_0:eq3}
respectively
<!---  -->
<!---  -->
<!---  -->
\begin{subequations}
    \label{eq_micromorphic_strong_equations_damage}
    \begin{alignat}{3}
        \MicromorphicDamageGradientField - \nabla \MicromorphicDamageField & = 0
        &&
        \ \ \ \ \ \ \ \
        &&
        \textit{micromorphic damage gradient}
        \label{eq_micromorphic_strong_equations_damage:eq0}
        \\
        \MicromorphicDamageStressField - \deriv{\psi_{\BodyLagrange}}{\MicromorphicDamageGradientField} & = 0
        &&
        \ \ \ \ \ \ \ \
        &&
        \textit{micromorphic damage constitutive equation}
        \label{eq_micromorphic_strong_equations_damage:eq1}
        \\
        \nabla \cdot \MicromorphicDamageStressField - \MicromorphicDamageForceField & = 0
        &&
        \ \ \ \ \ \ \ \
        &&
        \textit{balance of micromorphic damage momentum}
        \label{eq_micromorphic_strong_equations_damage:eq2}
        \\
        \MicromorphicDamageStressField \cdot \tensori{n}{} & = 0
        &&
        \ \ \ \ \ \ \ \
        &&
        \textit{micromorphic damage boundary conditions}
        \label{eq_micromorphic_strong_equations_damage:eq3}
        \\
    \end{alignat}
\end{subequations}
<!---  -->
<!---  -->
<!---  -->
where the governing laws of the micromorphic damage variable define a generalized continuum medium as introduced in \cite{forest_micromorphic_2009}.## HHO
\label{sec_micromorphic_hho}

##### Element behaviour

The core of the element $\ElementBulk$ is made out of the same material that composes $\BodyLagrange$ and
behaves according to the free energy potential $\psi_{\BodyLagrange}$. The behaviour of the interface $\ElementInterface$
is defined by the free energy potential $\psi_{\ElementInterface}$ such that
<!---  -->
<!---  -->
<!---  -->
\begin{equation}
    \label{eq_0009}
        \psi_{\ElementInterface}
        =
        \frac{1}{2} \DisplacementStabilizationFactor \frac{\ell}{h_{\ElementCell}} \nabla \Field{\DisplacementField}{\ElementInterface}{} : \nabla \Field{\DisplacementField}{\ElementInterface}{}
        +
        \frac{1}{2} \MicromorphicDamageStabilizationFactor \frac{\ell}{h_{\ElementCell}} \nabla \Field{\MicromorphicDamageField}{\ElementInterface}{} \cdot \nabla \Field{\MicromorphicDamageField}{\ElementInterface}{}
\end{equation}

<!---  --------------------------------------------------------- -->
<!---  PARAGRAPH -->
<!---  --------------------------------------------------------- -->
##### Element loading

The core $\ElementBulk$ is subjected to the volumetric loading $\loadLag{}$,
and to the traction force applied by the interface $\ElementInterface$ onto $\ElementBulkBoundary$.
By continuity, $\ElementBulk$ applies the opposite traction force on $\ElementInterface$ through $\ElementBulkBoundary$.
The interface $\ElementInterface$ is also subjected to the exterior traction force $\neumannCellLoad{}$ acting on $\BodyLagrangeNeumannBoundary$,
that accounts for the action of the rest of the solid $\BodyLagrange$ onto the boundary $\ElementBoundary$.

<!---  --------------------------------------------------------- -->
<!---  PARAGRAPH -->
<!---  --------------------------------------------------------- -->
##### Discplacement, displacement gradient, stress and micromorphic fields

Let
$\Field{\DisplacementField}{\ElementBulk}{}$,
$\Field{\DisplacementGradientField}{\ElementBulk}{}$,
$\Field{\PKIStressField}{\ElementBulk}{}$,
$\Field{\MicromorphicDamageField}{\ElementBulk}{}$,
$\Field{\MicromorphicDamageGradientField}{\ElementBulk}{}$,
$\Field{\MicromorphicDamageStressField}{\ElementBulk}{}$
the displacement and micromorphic damage fields, gradients and stresses in the bulk of the element,
and 
$\Field{\DisplacementField}{\ElementInterface}{}$,
$\Field{\DisplacementGradientField}{\ElementInterface}{}$,
$\Field{\PKIStressField}{\ElementInterface}{}$,
$\Field{\MicromorphicDamageField}{\ElementInterface}{}$,
$\Field{\MicromorphicDamageGradientField}{\ElementInterface}{}$,
$\Field{\MicromorphicDamageStressField}{\ElementInterface}{}$
those in the interface.
The displacement and micromorphic damage of the boundary $\ElementBoundary$ are denoted $\Field{\DisplacementField}{\ElementBoundary}{}$ and $\Field{\MicromorphicDamageField}{\ElementBoundary}{}$ respectively.
By continuity of the displacement and micromorphic damage fields between $\ElementBulk$ and $\ElementBoundary$,
the following relations hold true
<!---  -->
<!---   -->
<!---   -->
\begin{equation}
    \label{eq_ud_conformity}
        \begin{aligned}
        \Field{\DisplacementField}{\ElementInterface}{} \TraceOperator{\ElementBulkBoundary} = \Field{\DisplacementField}{\ElementBulk}{} \TraceOperator{\ElementBulkBoundary}
        && &&
        \Field{\DisplacementField}{\ElementInterface}{} \TraceOperator{\ElementBoundary} = \Field{\DisplacementField}{\ElementBoundary}{}
        && &&
        \Field{\MicromorphicDamageField}{\ElementInterface}{} \TraceOperator{\ElementBulkBoundary} = \Field{\MicromorphicDamageField}{\ElementBulk}{} \TraceOperator{\ElementBulkBoundary}
        && &&
        \Field{\MicromorphicDamageField}{\ElementInterface}{} \TraceOperator{\ElementBoundary} = \Field{\MicromorphicDamageField}{\ElementBoundary}{}
    \end{aligned}
\end{equation}

<!---  --------------------------------------------------------- -->
<!---  PARAGRAPH -->
<!---  --------------------------------------------------------- -->
##### Hu-Washizu Lagrangian of the element

By combining both the Lagragian of the core $\ElementBulk$ and that of the interface $\ElementInterface$, one obtains the total Lagragian $\LagrangianOperator{\ElementCell}{HW}$ over the element such that
<!---  -->
<!---  -->
<!---  -->
\begin{equation}
    \label{eq_hu_washizu_split}
    \LagrangianOperator{\ElementCell}{HW} = \LagrangianOperator{\ElementBulk}{HW} + \LagrangianOperator{\ElementInterface}{HW}
\end{equation}
<!---  -->
<!---  -->
<!---  -->
where
<!---  -->
<!---  -->
<!---  -->
\begin{equation}
    \label{eq_hu_washizu_split2}
    \LagrangianOperator{\ElementBulk}{HW}
    =
    \int_{\ElementBulk} \psi_{\BodyLagrange}
    +
    \int_{\ElementBulk} (\nabla \Field{\DisplacementField}{\ElementBulk}{} - \Field{\DisplacementGradientField}{\ElementBulk}{}) : \Field{\PKIStressField}{\ElementBulk}{}
    +
    \int_{\ElementBulk} (\nabla \Field{\MicromorphicDamageField}{\ElementBulk}{} - \Field{\MicromorphicDamageGradientField}{\ElementBulk}{}) \cdot \Field{\MicromorphicDamageStressField}{\ElementBulk}{}
    -
    \int_{\ElementBulk} \loadLag \cdot \Field{\DisplacementField}{\ElementBulk}{}
\end{equation}
<!---  -->
<!---  -->
<!---  -->
and
<!---  -->
<!---  -->
<!---  -->
\begin{equation}
    \label{eq_hu_washizu_split23}
    \LagrangianOperator{\ElementInterface}{HW}
    =
    \int_{\ElementInterface} \psi_{\ElementInterface}
    +
    \int_{\ElementInterface} (\nabla \Field{\DisplacementField}{\ElementInterface}{} - \Field{\DisplacementGradientField}{\ElementInterface}{}) : \Field{\PKIStressField}{\ElementInterface}{}
    +
    \int_{\ElementInterface} (\nabla \Field{\MicromorphicDamageField}{\ElementInterface}{} - \Field{\MicromorphicDamageGradientField}{\ElementInterface}{}) \cdot \Field{\MicromorphicDamageStressField}{\ElementInterface}{}
    -
    \int_{\neumannCell} \neumannCellLoad \cdot \Field{\DisplacementField}{\ElementBoundary}{}
\end{equation}

<!---  --------------------------------------------------------- -->
<!---  -- SUBSECTION -->
<!---  --------------------------------------------------------- -->
### Hypotheses
\label{sec_assumtions}

<!---  --------------------------------------------------------- -->
<!---  PARAGRAPH -->
<!---  --------------------------------------------------------- -->
##### Displacement in the interface

Since the interface is of negligible volume compared to that of the core, the displacement and micromorphic damage fields in the interface $\ElementInterface$ are assumed to be linear with respect to $\NormalVector$, such that
the gradients are homogeneous in $\ElementInterface$ along $\NormalVector$
<!---  -->
<!---   -->
<!---   -->
\begin{equation}
    \label{eq_crown_displacement}
    \begin{aligned}
        \nabla \Field{\DisplacementField}{\ElementInterface}{}
        =
        \frac{
            \Field{\DisplacementField}{\ElementBoundary}{} - \Field{\DisplacementField}{\ElementBulk}{} \TraceOperator{\ElementBulkBoundary}
        }{\ell}
        \otimes
        \NormalVector
        &&
        &&
        \nabla \Field{\MicromorphicDamageField}{\ElementInterface}{}
        =
        \frac{
            \Field{\MicromorphicDamageField}{\ElementBoundary}{} - \Field{\MicromorphicDamageField}{\ElementBulk}{} \TraceOperator{\ElementBulkBoundary}
        }{\ell}
        \otimes
        \NormalVector
    \end{aligned}
\end{equation}
<!---   -->
<!---   -->
<!---  -->
That is, the displacement and micromorphic damage fields in the interface $\ElementInterface$ linearly bridge those of the boundary $\ElementBoundary$ to those of the bulk $\ElementBulk$.

<!---  --------------------------------------------------------- -->
<!---  PARAGRAPH -->
<!---  --------------------------------------------------------- -->
##### Stress in the interface

Likewise, let assume that $\Field{\PKIStressField}{\ElementInterface}{}$ and $\Field{\MicromorphicDamageStressField}{\ElementInterface}{}$ are constant along the direction $\NormalVector$ in $\ElementInterface$.
By continuity of the traction force across $\ElementBulkBoundary$, the following equalities hold true
<!---  -->
<!---   -->
<!---   -->
\begin{equation}
    \label{eq_continuity_traction_force}
    \begin{aligned}
        (\Field{\PKIStressField}{\ElementInterface}{} - \Field{\PKIStressField}{\ElementBulk}{} \TraceOperator{\ElementBulkBoundary}) \cdot \NormalVector = 0
        &&
        \text{and}
        &&
        (\Field{\MicromorphicDamageStressField}{\ElementInterface}{} - \Field{\MicromorphicDamageStressField}{\ElementBulk}{} \TraceOperator{\ElementBulkBoundary}) \cdot \NormalVector = 0
        &&
        \text{on}
        &&
        \ElementBulkBoundary
    \end{aligned}
\end{equation}

<!---  --------------------------------------------------------- -->
<!---  -- SUBSECTION -->
<!---  --------------------------------------------------------- -->
### Towards Hybrid discontinuous methods from the Hu-Washizu Lagrangian

##### Lagrangian

The total Lagragian is
<!---  -->
<!---  -->
<!---  -->
\begin{equation}
    \label{eq_0015}
    \begin{aligned}
        \LagrangianOperator{\ElementCell}{HW}
        =
        &
        \int_{\ElementCell} \psi_{\BodyLagrange}
        +
        \int_{\ElementCell} (\nabla \Field{\DisplacementField}{\ElementCell}{} - \Field{\DisplacementGradientField}{\ElementCell}{}) : \Field{\PKIStressField}{\ElementCell}{}
        +
        \int_{\ElementCell} (\nabla \Field{\MicromorphicDamageField}{\ElementCell}{} - \Field{\MicromorphicDamageGradientField}{\ElementCell}{}) \cdot \Field{\MicromorphicDamageStressField}{\ElementCell}{}
        \\
        &
        +
        \int_{\ElementBoundary} (\Field{\DisplacementField}{\ElementBoundary}{} - \Field{\DisplacementField}{\ElementCell}{} \TraceOperator{\ElementBoundary}) \cdot \Field{\PKIStressField}{\ElementCell}{} \TraceOperator{\ElementBoundary} \cdot \NormalVector
        +
        \int_{\ElementBoundary} (\Field{\MicromorphicDamageField}{\ElementBoundary}{} - \Field{\MicromorphicDamageField}{\ElementCell}{} \TraceOperator{\ElementBoundary}) \, \Field{\MicromorphicDamageStressField}{\ElementCell}{} \TraceOperator{\ElementBoundary} \cdot \NormalVector
        \\
        &
        +
        \int_{\ElementBoundary} \frac{\DisplacementStabilizationFactor}{2 h_{\ElementCell}} \lVert \Field{\DisplacementField}{\ElementBoundary}{} - \Field{\DisplacementField}{\ElementCell}{} \TraceOperator{\ElementBoundary} \rVert^2
        +
        \int_{\ElementBoundary} \frac{\MicromorphicDamageStabilizationFactor}{2 h_{\ElementCell}} (\Field{\MicromorphicDamageField}{\ElementBoundary}{} - \Field{\MicromorphicDamageField}{\ElementCell}{} \TraceOperator{\ElementBoundary})^2
        -
        \int_{\ElementCell} \loadLag{} \cdot \Field{\DisplacementField}{\ElementCell}{}
        -
        \int_{\BodyLagrangeNeumannBoundary} \neumannCellLoad{} \cdot \Field{\DisplacementField}{\ElementBoundary}{}
    \end{aligned}
\end{equation}

<!---  --------------------------------------------------------- -->
<!---  PARAGRAPH -->
<!---  --------------------------------------------------------- -->
##### Lagrangian variations

By differentiation of the total Lagrangian \eqref{eq_0015} with respect to each variable of the problem, the following weak equations arise
<!---  -->
<!---  -->
<!---  -->
\begin{subequations}
    \label{eq_0017}
        \begin{alignat}{2}
            \langle \deriv{\LagrangianOperator{\ElementCell}{HW}}{\Field{\DisplacementField}{\ElementCell}{}} , \delta \Field{\DisplacementField}{\ElementCell}{} \rangle
            = & \int_{\ElementCell} \Field{\PKIStressField}{\ElementCell}{} : \nabla \delta \Field{\DisplacementField}{\ElementCell}{}
            -
            \int_{\ElementCell} \tensori{f}{}_V \cdot \delta \Field{\DisplacementField}{\ElementCell}{}
            -
            \int_{\ElementBoundary} \Field{\DisplacementTractionField}{\ElementCell}{} \cdot \delta \Field{\DisplacementField}{\ElementCell}{} \TraceOperator{\ElementBoundary}
            &&
            \qquad \forall \delta \Field{\DisplacementField}{\ElementCell}{}
            \label{eq_0017:eq0}
            \\
            \langle \deriv{\LagrangianOperator{\ElementCell}{HW}}{\Field{\DisplacementField}{\ElementBoundary}{}} , \delta \Field{\DisplacementField}{\ElementBoundary}{} \rangle
            = &
            \int_{\neumannCell} (\Field{\DisplacementTractionField}{\ElementCell}{} - \tensori{t}{}_{\neumannCell}) \cdot \delta \Field{\DisplacementField}{\ElementBoundary}{}
            &&
            \qquad \forall \delta \Field{\DisplacementField}{\ElementBoundary}{}
            \label{eq_0017:eq1}
            \\
            \langle \deriv{\LagrangianOperator{\ElementCell}{HW}}{\Field{\PKIStressField}{\ElementCell}{}} , \delta \Field{\PKIStressField}{\ElementCell}{} \rangle
            = & \int_{\ElementCell} (\nabla \Field{\DisplacementField}{\ElementCell}{} - \Field{\DisplacementGradientField}{\ElementCell}{} ) : \delta \Field{\PKIStressField}{\ElementCell}{}
            +
            \int_{\ElementBoundary} (\Field{\DisplacementField}{\ElementBoundary}{} - \Field{\DisplacementField}{\ElementCell}{} \TraceOperator{\ElementBoundary}) \cdot \delta \Field{\PKIStressField}{\ElementCell}{} \TraceOperator{\ElementBoundary} \cdot \NormalVector
            &&
            \qquad \forall \delta \Field{\PKIStressField}{\ElementCell}{}
            \label{eq_0017:eq3}
            \\
            \langle \deriv{\LagrangianOperator{\ElementCell}{HW}}{\Field{\DisplacementGradientField}{\ElementCell}{}} , \delta \Field{\DisplacementGradientField}{\ElementCell}{} \rangle
            = &
            \int_{\ElementCell} (\deriv{\mecPotential_{\BodyLagrange}}{\Field{\DisplacementGradientField}{\ElementCell}{}} - \Field{\PKIStressField}{\ElementCell}{}) : \delta \Field{\DisplacementGradientField}{\ElementCell}{}
            &&
            \qquad \forall \delta \Field{\DisplacementGradientField}{\ElementCell}{}
            \label{eq_0017:eq2}
            \\
            \langle \deriv{\LagrangianOperator{\ElementCell}{HW}}{\Field{\MicromorphicDamageField}{\ElementCell}{}} , \delta \Field{\MicromorphicDamageField}{\ElementCell}{} \rangle
            =
            & \int_{\ElementCell} \Field{\MicromorphicDamageStressField}{\ElementCell}{} \cdot \nabla \delta \Field{\MicromorphicDamageField}{\ElementCell}{}
            +
            \int_{\ElementCell} \Field{\MicromorphicDamageForceField}{\ElementCell}{} \cdot \delta \Field{\MicromorphicDamageField}{\ElementCell}{}
            -
            \int_{\ElementBoundary} \Field{\MicromorphicDamageTractionField}{\ElementCell}{} \, \delta \Field{\MicromorphicDamageField}{\ElementCell}{} \TraceOperator{\ElementBoundary}
            &&
            \qquad \forall \delta \Field{\MicromorphicDamageField}{\ElementCell}{}
            \label{eq_0017:eq04}
            \\
            \langle \deriv{\LagrangianOperator{\ElementCell}{HW}}{\Field{\MicromorphicDamageField}{\ElementBoundary}{}} , \delta \Field{\MicromorphicDamageField}{\ElementBoundary}{} \rangle
            = &
            \int_{\neumannCell} \Field{\MicromorphicDamageTractionField}{\ElementCell}{} \, \delta \Field{\MicromorphicDamageField}{\ElementBoundary}{}
            &&
            \qquad \forall \delta \Field{\MicromorphicDamageField}{\ElementBoundary}{}
            \label{eq_0017:eq12}
            \\
            \langle \deriv{\LagrangianOperator{\ElementCell}{HW}}{\Field{\MicromorphicDamageStressField}{\ElementCell}{}} , \delta \Field{\MicromorphicDamageStressField}{\ElementCell}{} \rangle
            = & \int_{\ElementCell} (\nabla \Field{\MicromorphicDamageField}{\ElementCell}{} - \Field{\MicromorphicDamageGradientField}{\ElementCell}{} ) \cdot \delta \Field{\MicromorphicDamageStressField}{\ElementCell}{}
            +
            \int_{\ElementBoundary} (\Field{\MicromorphicDamageField}{\ElementBoundary}{} - \Field{\MicromorphicDamageField}{\ElementCell}{} \TraceOperator{\ElementBoundary}) \, \delta \Field{\MicromorphicDamageStressField}{\ElementCell}{} \TraceOperator{\ElementBoundary} \cdot \NormalVector
            &&
            \qquad \forall \delta \Field{\MicromorphicDamageStressField}{\ElementCell}{}
            \label{eq_0017:eq31}
            \\
            \langle \deriv{\LagrangianOperator{\ElementCell}{HW}}{\Field{\MicromorphicDamageGradientField}{\ElementCell}{}} , \delta \Field{\MicromorphicDamageGradientField}{\ElementCell}{} \rangle
            = &
            \int_{\ElementCell} (\deriv{\mecPotential_{\BodyLagrange}}{\Field{\MicromorphicDamageGradientField}{\ElementCell}{}} - \Field{\MicromorphicDamageStressField}{\ElementCell}{}) \cdot \delta \Field{\MicromorphicDamageGradientField}{\ElementCell}{}
            &&
            \qquad \forall \delta  \Field{\MicromorphicDamageGradientField}{\ElementCell}{}
            \label{eq_0017:eq22}
    \end{alignat}
\end{subequations}
<!---   -->
<!---   -->
<!---  -->
where the \textit{reconstructed tractions} $\Field{\DisplacementTractionField}{\ElementCell}{} = \Field{\PKIStressField}{\ElementCell}{} \TraceOperator{\ElementBoundary} \cdot \NormalVector + (\DisplacementStabilizationFactor / h_{\ElementCell}) \DisplacementJumpField(\Field{\DisplacementField}{\ElementCell}{}, \Field{\DisplacementField}{\ElementBoundary}{})$
and
$\Field{\MicromorphicDamageTractionField}{\ElementCell}{} = \Field{\MicromorphicDamageStressField}{\ElementCell}{} \TraceOperator{\ElementBoundary} \cdot \NormalVector + (\MicromorphicDamageStabilizationFactor / h_{\ElementCell}) \MicromorphicDamageJumpField(\Field{\MicromorphicDamageField}{\ElementCell}{}, \Field{\MicromorphicDamageField}{\ElementBoundary}{})$
are introduced, with
$\DisplacementJumpField(\Field{\DisplacementField}{\ElementCell}{}, \Field{\DisplacementField}{\ElementBoundary}{}) = \Field{\DisplacementField}{\ElementBoundary}{} - \Field{\DisplacementField}{\ElementCell}{} \TraceOperator{\ElementBoundary}$
and
$\MicromorphicDamageJumpField(\Field{\MicromorphicDamageField}{\ElementCell}{}, \Field{\MicromorphicDamageField}{\ElementBoundary}{}) = \Field{\MicromorphicDamageField}{\ElementBoundary}{} - \Field{\MicromorphicDamageField}{\ElementCell}{} \TraceOperator{\ElementBoundary}$
the jump functions on the boundary $\ElementBoundary$.

<!---  --------------------------------------------------------- -->
<!---  -- SUBSECTION -->
<!---  --------------------------------------------------------- -->
### Problem in primal form
\label{sec_hdg_element_equilibrium}

<!---  --------------------------------------------------------- -->
<!---  PARAGRAPH -->
<!---  --------------------------------------------------------- -->
##### Reconstructed gradient

Since minimization of \eqref{eq_0017:eq3} and \eqref{eq_0017:eq31} define linear problems with any displacement and micromorphic damage pairs respectively, they can be eliminated
from the system \eqref{eq_0017}. The resulting equations define the so-called \textit{reconstructed gradients}
$\Field{\DisplacementGradientField}{\ElementCell}{}(\Field{\VirtualField{\DisplacementField}}{\ElementCell}{}, \Field{\VirtualField{\DisplacementField}}{\ElementBoundary}{})$
and
$\Field{\MicromorphicDamageGradientField}{\ElementCell}{}(\Field{\VirtualField{\MicromorphicDamageField}}{\ElementCell}{}, \Field{\VirtualField{\MicromorphicDamageField}}{\ElementBoundary}{})$
associated with any respective displacement and micromorphic damage pairs
$(\Field{\VirtualField{\DisplacementField}}{\ElementCell}{}, \Field{\VirtualField{\DisplacementField}}{\ElementBoundary}{})$
and
$(\Field{\VirtualField{\MicromorphicDamageField}}{\ElementCell}{}, \Field{\VirtualField{\MicromorphicDamageField}}{\ElementBoundary}{})$, that satisfy
<!---  -->
<!---  -->
<!---  -->
\begin{subequations}
    \label{eq_00172}
        \begin{alignat}{2}
            \int_{\ElementCell} \Field{\DisplacementGradientField}{\ElementCell}{} : \Field{\tensorii{\tau}}{\ElementCell}{}
            &
            =
            \int_{\ElementCell}  \nabla \Field{\VirtualField{\DisplacementField}}{\ElementCell}{} : \Field{\tensorii{\tau}}{\ElementCell}{}
            +
            \int_{\ElementBoundary} (\Field{\VirtualField{\DisplacementField}}{\ElementBoundary}{} - \Field{\VirtualField{\DisplacementField}}{\ElementCell}{} \TraceOperator{\ElementBoundary}) \cdot \Field{\tensorii{\tau}}{\ElementCell}{} \TraceOperator{\ElementBoundary} \cdot \NormalVector
            &&
            \qquad \forall \Field{\tensorii{\tau}}{\ElementCell}{}
            \label{eq_00172:eq0}
            \\
            \int_{\ElementCell} \Field{\MicromorphicDamageGradientField}{\ElementCell}{} \cdot \Field{\tensori{\zeta}}{\ElementCell}{} 
            &
            =
            \int_{\ElementCell}  \nabla \Field{\VirtualField{\MicromorphicDamageField}}{\ElementCell}{} \cdot \Field{\tensori{\zeta}}{\ElementCell}{} 
            +
            \int_{\ElementBoundary} (\Field{\VirtualField{\MicromorphicDamageField}}{\ElementBoundary}{} - \Field{\VirtualField{\MicromorphicDamageField}}{\ElementCell}{} \TraceOperator{\ElementBoundary}) \, \Field{\tensori{\zeta}}{\ElementCell}{} \TraceOperator{\ElementBoundary} \cdot \NormalVector
            &&
            \qquad \forall \tensori{\zeta}{}_{\ElementCell}
            \label{eq_00172:eq1}
    \end{alignat}
\end{subequations}
<!---  -->
<!---  -->
<!---  -->
where $\Field{\tensorii{\tau}}{\ElementCell}{}$ denotes an arbitrary kinematically admissible stress field, and $\Field{\tensori{\zeta}}{\ElementCell}{}$ is an arbitrary kinematically admissible micromorphic stress field.

<!---  --------------------------------------------------------- -->
<!---  PARAGRAPH -->
<!---  --------------------------------------------------------- -->
##### Stress tensor

Likewise, \eqref{eq_0017:eq2} and \eqref{eq_0017:eq22} are eliminated from \eqref{eq_0017} since they are linear with $\Field{\DisplacementGradientField}{\ElementCell}{}$ and  $\Field{\MicromorphicDamageGradientField}{\ElementCell}{}$ respectively.
Assuming in addition that the space of kinematically admissible stress fields is included in that of kinematically admissible gradient fields, \eqref{eq_0017:eq2} and \eqref{eq_0017:eq22} hold in a strong sense such that
<!---  -->
<!---  -->
<!---  -->
\begin{subequations}
    \label{eq_stress}
        \begin{alignat}{3}
            \Field{\PKIStressField}{\ElementCell}{} & = \deriv{\mecPotential_{\BodyLagrange}}{\Field{\DisplacementGradientField}{\ElementCell}{}}
            \label{eq_stress:eq0}
            \\
            \Field{\MicromorphicDamageStressField}{\ElementCell}{} & = \deriv{\mecPotential_{\BodyLagrange}}{\Field{\MicromorphicDamageGradientField}{\ElementCell}{}}
            \label{eq_stress:eq1}
    \end{alignat}
\end{subequations}

<!---  --------------------------------------------------------- -->
<!---  PARAGRAPH -->
<!---  --------------------------------------------------------- -->
##### Lagrangian variations in primal form

Using \eqref{eq_stress} and \eqref{eq_00172}, problem \eqref{eq_0017} depends on the displacement unknowns only.
<!---  and the only remaining variations of the total Lagrangian \eqref{eq_0015} are those with respect to both displacement variables. -->
A new total Lagrangian $\LagrangianOperator{\ElementCell}{HDG}$ arises from the simplified problem such that
<!---  -->
<!---  -->
<!---  -->
\begin{equation}
    \label{eq_total_lagragian_bis}
    \begin{aligned}
        \LagrangianOperator{\ElementCell}{HDG}
        =
        &
        \int_{\ElementCell} \mecPotential_{\BodyLagrange}
        +
        \int_{\ElementBoundary} \frac{\DisplacementStabilizationFactor}{2 h_{\ElementCell}} \lVert \DisplacementJumpField(\Field{\DisplacementField}{\ElementCell}{}, \Field{\DisplacementField}{\ElementBoundary}{}) \rVert^2
        +
        \int_{\ElementBoundary} \frac{\MicromorphicDamageStabilizationFactor}{2 h_{\ElementCell}} \MicromorphicDamageJumpField^{2}(\Field{\MicromorphicDamageField}{\ElementCell}{}, \Field{\MicromorphicDamageField}{\ElementBoundary}{})
        -
        \int_{\ElementCell} \loadLag{} \cdot \Field{\DisplacementField}{\ElementCell}{}
        -
        \int_{\BodyLagrangeNeumannBoundary} \neumannCellLoad{} \cdot \Field{\DisplacementField}{\ElementBoundary}{}
    \end{aligned}
\end{equation}
<!---  -->
<!---  -->
<!---  -->
with respective cell and boundary displacement variations:
\begin{subequations}
    \label{eq_final_problem}
        \begin{alignat}{3}
            \langle \deriv{\LagrangianOperator{\ElementCell}{HDG}}{\Field{\DisplacementField}{\ElementCell}{}} , \delta \Field{\DisplacementField}{\ElementCell}{} \rangle
            =
            &
            \int_{\ElementCell} \Field{\PKIStressField}{\ElementCell}{} : \nabla \delta \Field{\DisplacementField}{\ElementCell}{}
            -
            \int_{\ElementCell} \tensori{f}{}_V \cdot \delta \Field{\DisplacementField}{\ElementCell}{}
            -
            \int_{\ElementBoundary} \Field{\DisplacementTractionField}{\ElementCell}{} \cdot \delta \Field{\DisplacementField}{\ElementCell}{} \TraceOperator{\ElementBoundary}
            &&
            \qquad \forall \delta \Field{\DisplacementField}{\ElementCell}{}
            \label{eq_final_problem:eq0}
            \\
            \langle \deriv{\LagrangianOperator{\ElementCell}{HDG}}{\Field{\DisplacementField}{\ElementBoundary}{}} , \delta \Field{\DisplacementField}{\ElementBoundary}{} \rangle
            =
            &
            \int_{\neumannCell} (\Field{\DisplacementTractionField}{\ElementCell}{} - \tensori{t}{}_{\neumannCell}) \cdot \delta \Field{\DisplacementField}{\ElementBoundary}{}
            &&
            \qquad \forall \delta \Field{\DisplacementField}{\ElementBoundary}{}
            \label{eq_final_problem:eq1}
            \\
            \langle \deriv{\LagrangianOperator{\ElementCell}{HW}}{\Field{\MicromorphicDamageField}{\ElementCell}{}} , \delta \Field{\MicromorphicDamageField}{\ElementCell}{} \rangle
            =
            & \int_{\ElementCell} \Field{\MicromorphicDamageStressField}{\ElementCell}{} \cdot \nabla \delta \Field{\MicromorphicDamageField}{\ElementCell}{}
            +
            \int_{\ElementCell} \Field{\MicromorphicDamageForceField}{\ElementCell}{} \cdot \delta \Field{\MicromorphicDamageField}{\ElementCell}{}
            -
            \int_{\ElementBoundary} \Field{\MicromorphicDamageTractionField}{\ElementCell}{} \, \delta \Field{\MicromorphicDamageField}{\ElementCell}{} \TraceOperator{\ElementBoundary}
            &&
            \qquad \forall \delta \Field{\MicromorphicDamageField}{\ElementCell}{}
            \label{eq_final_problem:eq04}
            \\
            \langle \deriv{\LagrangianOperator{\ElementCell}{HW}}{\Field{\MicromorphicDamageField}{\ElementBoundary}{}} , \delta \Field{\MicromorphicDamageField}{\ElementBoundary}{} \rangle
            = &
            \int_{\neumannCell} \Field{\MicromorphicDamageTractionField}{\ElementCell}{} \, \delta \Field{\MicromorphicDamageField}{\ElementBoundary}{}
            &&
            \qquad \forall \delta \Field{\MicromorphicDamageField}{\ElementBoundary}{}
            \label{eq_final_problem:eq12}
    \end{alignat}
\end{subequations}
<!---  -->
<!---  -->
<!---  -->
where $\Field{\PKIStressField}{\ElementCell}{}$ and $\Field{\MicromorphicDamageStressField}{\ElementCell}{}$ are defined by \eqref{eq_stress} and
depend on $\Field{\DisplacementGradientField}{\ElementCell}{}$ and $\Field{\MicromorphicDamageGradientField}{\ElementCell}{}$ which solve \eqref{eq_00172}.<!---  --------------------------------------------------------- -->
<!---  ---- SECTION -->
<!---  --------------------------------------------------------- -->
## Discretization
\label{sec_discretization}

This section specifies the nature of the so-called hybrid mesh,
and introduces the discretization for both cell and faces displacement fields.
The classical \textit{static condensation} cell unknowns elimination strategy is presented, and a novel elimination scheme
based on the previous Lagrangian formulation of hybrid discontinuous methods is then devised.

<!---  --------------------------------------------------------- -->
<!---  -- SUBSECTION -->
<!---  --------------------------------------------------------- -->
### Mesh and skeleton

<!---  --------------------------------------------------------- -->
<!---  PARAGRAPH -->
<!---  --------------------------------------------------------- -->
##### Faces and skeleton of the mesh

The boundary $\ElementBoundary$ of each element is decomposed in faces, such
that a face $\ElementFace$ is a subset of $\BodyLagrange$, and either there are two
cells $\Field{\ElementCell}{F}{1}$ and $\Field{\ElementCell}{F}{2}$ such that $F = \Field{\ElementBoundary}{F}{1} \cap \Field{\ElementBoundary}{F}{2}$
($\ElementFace$ is then an interior face), or there is a single cell $\Field{\ElementCell}{F}{}$ such
that $\ElementFace = \Field{\ElementBoundary}{F}{} \cap \BodyLagrangeBoundary$ ($\ElementFace$ is then an exterior face).
Let $\Skeleton(\BodyLagrange) = \{ \Field{\ElementFace}{i}{} \subset \BodyLagrange \ \vert \ 1 \leq i
\leq \Field{N}{\Skeleton}{} \}$ the skeleton of the mesh, collecting all element faces
$\Field{\ElementFace}{i}{}$ in the mesh, where $\Field{N}{\Skeleton}{}$ denotes the number of faces. The set of
faces subjected to Neumann boundary conditions is denoted
$\SkeletonBoundaryNeumann(\BodyLagrange)$, and $\SkeletonBoundaryDirichlet(\BodyLagrange)$
denotes that subjected to Dirichlet boundary conditions.
Moreover, let
$\SkeletonInterior(\BodyLagrange)$ the set of interior faces
and
$\SkeletonBoundary(\BodyLagrange)$ the set of exterior faces. For any cell
$\ElementCell$, let $\Skeleton(\ElementCell) = \{ \ElementFace \in \Skeleton(\BodyLagrange) \ \vert \ \ElementFace
\subset \ElementBoundary \}$ the set of faces composing the boundary of $\ElementCell$,
and let $\Field{N}{\ElementBoundary}{}$ the number of faces in $\ElementBoundary$.

<!---  --------------------------------------------------------- -->
<!---  PARAGRAPH -->
<!---  --------------------------------------------------------- -->
##### Mesh description

Likewise, one defines the collection of all cells in the mesh
as $\Mesh(\BodyLagrange) = \{ \Field{\ElementCell}{i}{} \subset \BodyLagrange \ \vert \ 1 \leq i
\leq \Field{N}{\Mesh}{} \}$, where $\Field{N}{\Mesh}{}$ denotes the total number of cells.

<!---  --------------------------------------------------------- -->
<!---  -- SUBSECTION -->
<!---  --------------------------------------------------------- -->
### Discretization

<!---  --------------------------------------------------------- -->
<!---  PARAGRAPH -->
<!---  --------------------------------------------------------- -->
##### Discrete functional space

Let $\Field{U}{\ElementCell}{\; h}$ and $\Field{D}{\ElementCell}{\; h}$ denote
approximation spaces of finite dimension for the cell displacement and the micromorphic damage respectively,
and $\Field{U}{\ElementFace}{\; h}$ and $\Field{D}{\ElementFace}{\; h}$ those
on a face $\ElementFace \in \Skeleton(\ElementCell)$.
The displacement and micromorphic damage approximation spaces on $\ElementBoundary$ are
$\Field{U}{\ElementBoundary}{\; h} = \prod_{\ElementFace \in \Skeleton(\ElementCell)} \Field{U}{\ElementFace}{\; h}$
and $\Field{D}{\ElementBoundary}{\; h} = \prod_{\ElementFace \in \Skeleton(\ElementCell)} \Field{D}{\ElementFace}{\; h}$
respectively.

##### Approximation bases and elementary unknowns

Let $\Field{\Vector{B}}{u, \ElementCell}{\; h}, \Field{\Vector{B}}{u, \ElementFace}{\; h}, \Field{\Vector{B}}{d, \ElementCell}{\; h}, \Field{\Vector{B}}{d, \ElementFace}{\; h}$
denote polynomial bases of $\Field{U}{\ElementCell}{\; h}, \Field{U}{\ElementFace}{\; h}, \Field{D}{\ElementCell}{\; h}, \Field{D}{\ElementFace}{\; h}$ respectively.
Using vector notations, the fields $\Field{\DisplacementField}{\ElementCell}{\; h}, \Field{\DisplacementField}{\ElementFace}{\; h}, \Field{\MicromorphicDamageField}{\ElementCell}{\; h}, \Field{\MicromorphicDamageField}{\ElementFace}{\; h}$
can be represented by vectors of coefficients $\Field{\Vector{U}}{\ElementCell}{}, \Field{\Vector{U}}{\ElementFace}{}, \Field{\Vector{D}}{\ElementCell}{}, \Field{\Vector{D}}{\ElementFace}{}$
in their respective bases such that
<!---  -->
<!---  -->
<!---  -->
\begin{equation}
  \label{eq_bases}
  \begin{aligned}
      \Field{\DisplacementField}{\ElementCell}{\; h} = \Field{\Vector{U}}{\ElementCell}{} \cdot \Field{\Vector{B}}{u, \ElementCell}{\; h}
      &&
      &&
      \Field{\DisplacementField}{\ElementFace}{\; h} = \Field{\Vector{U}}{\ElementFace}{} \cdot \Field{\Vector{B}}{u, \ElementFace}{\; h}
      &&
      &&
      \Field{\MicromorphicDamageField}{\ElementCell}{\; h} = \Field{\Vector{D}}{\ElementCell}{} \cdot \Field{\Vector{B}}{d, \ElementCell}{\; h}
      &&
      &&
      \Field{\MicromorphicDamageField}{\ElementFace}{\; h} = \Field{\Vector{D}}{\ElementFace}{} \cdot \Field{\Vector{B}}{d, \ElementFace}{\; h}
  \end{aligned}
\end{equation}

##### Global Unknowns

Let $(\Field{\DisplacementField}{\Mesh}{\; h}, \Field{\DisplacementField}{\Skeleton}{\; h}) \in \Field{U}{\Mesh}{\; h} \times \Field{U}{\Skeleton}{\; h}$
and $(\Field{\MicromorphicDamageField}{\Mesh}{\; h}, \Field{\MicromorphicDamageField}{\Skeleton}{\; h}) \in \Field{D}{\Mesh}{\; h} \times \Field{D}{\Skeleton}{\; h}$
the global
unknowns of problem \eqref{eq_final_problem} in discrete form, where
$\Field{\DisplacementField}{\Mesh}{\; h}, \Field{\DisplacementField}{\Skeleton}{\; h}, \Field{\MicromorphicDamageField}{\Mesh}{\; h}, \Field{\MicromorphicDamageField}{\Skeleton}{\; h}$
are the piece-wise continuous fields such that $\forall \ElementCell \in \Mesh, \forall \ElementFace \in \Skeleton$
<!---  -->
<!---  -->
<!---  -->
\begin{equation}
  \begin{aligned}
    \Field{\DisplacementField}{\Mesh}{\; h} \TraceOperator{\ElementCell} = \Field{\DisplacementField}{\ElementCell}{\; h}
    &&
    &&
    \Field{\DisplacementField}{\Skeleton}{\; h} \TraceOperator{\ElementFace} = \Field{\DisplacementField}{\ElementFace}{\; h}
    &&
    &&
    \Field{\MicromorphicDamageField}{\Mesh}{\; h} \TraceOperator{\ElementCell} = \Field{\MicromorphicDamageField}{\ElementCell}{\; h}
    &&
    &&
    \Field{\MicromorphicDamageField}{\Skeleton}{\; h} \TraceOperator{\ElementFace} = \Field{\MicromorphicDamageField}{\ElementFace}{\; h}
  \end{aligned}
\end{equation}
<!---   -->
<!---   -->
<!---   -->
with $
\Field{U}{\Mesh}{\; h} = \prod_{\ElementCell \in \Mesh} \Field{U}{\ElementCell}{\; h}, \;
\Field{U}{\Skeleton}{\; h} = \prod_{\ElementFace \in \Skeleton} \Field{U}{\ElementFace}{\; h}, \;
\Field{D}{\Mesh}{\; h} = \prod_{\ElementCell \in \Mesh} \Field{D}{\ElementCell}{\; h}, \;
\Field{D}{\Skeleton}{\; h} = \prod_{\ElementFace \in \Skeleton} \Field{D}{\ElementFace}{\; h}
$.
In the following, let
$\Field{\Vector{U}}{\Mesh}{}, \Field{\Vector{U}}{\Skeleton}{}, \Field{\Vector{D}}{\Mesh}{}, \Field{\Vector{D}}{\Skeleton}{}$ the unknown coefficient vectors associated
to $\Field{\DisplacementField}{\Mesh}{\; h}, \Field{\DisplacementField}{\Skeleton}{\; h}, \Field{\MicromorphicDamageField}{\Mesh}{\; h}, \Field{\MicromorphicDamageField}{\Skeleton}{\; h}$ respectively.

##### Elementary boundary unknown

Likewise, let $\Field{\DisplacementField}{\ElementBoundary}{\; h} \in \Field{U}{\ElementBoundary}{\; h}$ and $\Field{\MicromorphicDamageField}{\ElementBoundary}{\; h} \in \Field{D}{\ElementBoundary}{\; h}$ such that $\forall \ElementFace \in \Skeleton(\ElementCell)$
<!---  -->
<!---  -->
<!---  -->
\begin{equation}
  \begin{aligned}
    \Field{\DisplacementField}{\ElementBoundary}{\; h} \TraceOperator{\ElementFace} = \Field{\DisplacementField}{\ElementFace}{\; h}
    &&
    &&
    \Field{\MicromorphicDamageField}{\ElementBoundary}{\; h} \TraceOperator{\ElementFace} = \Field{\MicromorphicDamageField}{\ElementFace}{\; h}
  \end{aligned}
\end{equation}
<!---  -->
<!---  -->
<!---  -->
and let $\Field{\Vector{U}}{\ElementBoundary}{}$ and $\Field{\Vector{D}}{\ElementBoundary}{}$
the unknown coefficient vectors associated to $\Field{\DisplacementField}{\ElementBoundary}{\; h}$ and $\Field{\MicromorphicDamageField}{\ElementBoundary}{\; h}$.

<!---  --------------------------------------------------------- -->
<!---  -- SUBSECTION -->
<!---  --------------------------------------------------------- -->
### Local and global discrete problems

<!---  --------------------------------------------------------- -->
<!---  PARAGRAPH -->
<!---  --------------------------------------------------------- -->
#### Local residual

As in a functional space of finite dimension, the restriction of a linear
form can be represented by a vector in the dual space, let
$\Field{\Vector{R}}{u, \ElementCell}{}, \Field{\Vector{R}}{u, \ElementBoundary}{}, \Field{\Vector{R}}{d, \ElementCell}{}, \Field{\Vector{R}}{d, \ElementBoundary}{}$ the residual vectors
associated with the the variations of the total
Lagrangian~\eqref{eq_total_lagragian_bis}
<!---  -->
<!---   -->
<!---   -->
\begin{subequations}
  \label{eq_final_problem_00}
  \begin{alignat}{3}
    \Field{\Vector{R}}{u, \ElementCell}{}(\Field{\Vector{U}}{\ElementCell}{}, \Field{\Vector{U}}{\ElementBoundary}{}) \cdot \Field{\VirtualField{\Vector{U}}}{\ElementCell}{}
    =
    &
    \int_{\ElementCell} \Field{\PKIStressField}{\ElementCell}{\; h} : \nabla \Field{\VirtualField{\DisplacementField}}{\ElementCell}{\; h}
    -
    \int_{\ElementCell} \tensori{f}{}_V \cdot \Field{\VirtualField{\DisplacementField}}{\ElementCell}{\; h}
    -
    \int_{\ElementBoundary} \Field{\DisplacementTractionField}{\ElementCell}{\; h} \cdot \Field{\VirtualField{\DisplacementField}}{\ElementCell}{\; h} \TraceOperator{\ElementBoundary}
    &&
    \qquad \forall \Field{\VirtualField{\DisplacementField}}{\ElementCell}{\; h}
    \label{eq_final_problem_00:eq0}
    \\
    \Field{\Vector{R}}{u, \ElementBoundary}{}(\Field{\Vector{U}}{\ElementCell}{}, \Field{\Vector{U}}{\ElementBoundary}{}) \cdot \Field{\VirtualField{\Vector{U}}}{\ElementBoundary}{}
    =
    &
    \int_{\neumannCell} (\Field{\DisplacementTractionField}{\ElementCell}{\; h} - \tensori{t}{}_{\neumannCell}) \cdot \delta \Field{\DisplacementField}{\ElementBoundary}{\; h}
    &&
    \qquad \forall \Field{\VirtualField{\DisplacementField}}{\ElementBoundary}{\; h}
    \label{eq_final_problem_00:eq1}
    \\
    \Field{\Vector{R}}{d, \ElementCell}{}(\Field{\Vector{D}}{\ElementCell}{}, \Field{\Vector{D}}{\ElementBoundary}{}) \cdot \Field{\VirtualField{\Vector{D}}}{\ElementCell}{}
    =
    & \int_{\ElementCell} \Field{\MicromorphicDamageStressField}{\ElementCell}{\; h} : \nabla \Field{\VirtualField{\MicromorphicDamageField}}{\ElementCell}{\; h}
    +
    \int_{\ElementCell} \Field{\MicromorphicDamageForceField}{\ElementCell}{\; h} \cdot \Field{\VirtualField{\MicromorphicDamageField}}{\ElementCell}{\; h}
    -
    \int_{\ElementBoundary} \Field{\MicromorphicDamageTractionField}{\ElementCell}{\; h} \, \Field{\VirtualField{\MicromorphicDamageField}}{\ElementCell}{\; h} \TraceOperator{\ElementBoundary}
    &&
    \qquad \forall \delta \Field{\VirtualField{\MicromorphicDamageField}}{\ElementCell}{\; h}
    \label{eq_final_problem_00:eq04}
    \\
    \Field{\Vector{R}}{d, \ElementBoundary}{}(\Field{\Vector{D}}{\ElementCell}{}, \Field{\Vector{D}}{\ElementBoundary}{}) \cdot \Field{\VirtualField{\Vector{D}}}{\ElementBoundary}{}
    = &
    \int_{\neumannCell} \Field{\MicromorphicDamageTractionField}{\ElementCell}{\; h} \, \Field{\VirtualField{\MicromorphicDamageField}}{\ElementBoundary}{\; h}
    &&
    \qquad \forall \delta \Field{\VirtualField{\MicromorphicDamageField}}{\ElementBoundary}{\; h}
    \label{eq_final_problem_00:eq12}
  \end{alignat}
\end{subequations}
where the discrete stress tensor $\Field{\PKIStressField}{\ElementCell}{\; h}$ and the
discrete reconstructed gradient
$\Field{\DisplacementGradientField}{\ElementCell}{\; h}(\Field{\DisplacementField}{\ElementCell}{\; h}, \Field{\DisplacementField}{\ElementBoundary}{\; h})$ are defined by the discrete forms of
equations \eqref{eq_stress} and \eqref{eq_00172} respectively such that
<!---  -->
<!---  -->
<!---  -->
\begin{equation}
  \label{eq_stress_discrete}
  \begin{aligned}
    \Field{\PKIStressField}{\ElementCell}{\; h}
    =
    \deriv{\psi_{\BodyLagrange}}{\Field{\DisplacementGradientField}{\ElementCell}{\; h}}
    &&
    \text{with}
    &&
    \int_{\ElementCell} \Field{\DisplacementGradientField}{\ElementCell}{\; h} : \Field{\tensorii{\tau}}{\ElementCell}{\; h}
    =
    \int_{\ElementCell}  \nabla \Field{\VirtualField{\DisplacementField}}{\ElementCell}{\; h} : \Field{\tensorii{\tau}}{\ElementCell}{\; h}
    +
    \int_{\ElementBoundary} (\Field{\VirtualField{\DisplacementField}}{\ElementBoundary}{\; h} - \Field{\VirtualField{\DisplacementField}}{\ElementCell}{\; h} \TraceOperator{\ElementBoundary}) \cdot \Field{\tensorii{\tau}}{\ElementCell}{\; h} \TraceOperator{\ElementBoundary} \cdot \NormalVector
    &&
    \qquad \forall \Field{\tensorii{\tau}}{\ElementCell}{\; h}
    \\
    \Field{\MicromorphicDamageStressField}{\ElementCell}{\; h} = \deriv{\mecPotential_{\BodyLagrange}}{\Field{\MicromorphicDamageGradientField}{\ElementCell}{\; h}}
    &&
    \text{with}
    &&
    \int_{\ElementCell} \Field{\MicromorphicDamageGradientField}{\ElementCell}{\; h} \cdot \Field{\tensori{\zeta}}{\ElementCell}{\; h}
    =
    \int_{\ElementCell}  \nabla \Field{\VirtualField{\MicromorphicDamageField}}{\ElementCell}{\; h} \cdot \Field{\tensori{\zeta}}{\ElementCell}{\; h}
    +
    \int_{\ElementBoundary} (\Field{\VirtualField{\MicromorphicDamageField}}{\ElementBoundary}{\; h} - \Field{\VirtualField{\MicromorphicDamageField}}{\ElementCell}{\; h} \TraceOperator{\ElementBoundary}) \, \Field{\tensori{\zeta}}{\ElementCell}{\; h} \TraceOperator{\ElementBoundary} \cdot \NormalVector
    &&
    \qquad \forall \Field{\tensori{\zeta}}{\ElementCell}{\; h}
  \end{aligned}
\end{equation}
<!---  -->
<!---  -->
<!---  -->
and the discrete reconstructed tractions write
$\Field{\DisplacementTractionField}{\ElementCell}{\; h} = \Field{\PKIStressField}{\ElementCell}{\; h} \TraceOperator{\ElementBoundary} \cdot \NormalVector + (\DisplacementStabilizationFactor / h_{\ElementCell}) \Field{\DisplacementJumpField}{}{\; h}(\Field{\DisplacementField}{\ElementCell}{\; h}, \Field{\DisplacementField}{\ElementBoundary}{\; h})$
and
$\Field{\MicromorphicDamageTractionField}{\ElementCell}{\; h} = \Field{\MicromorphicDamageStressField}{\ElementCell}{\; h} \TraceOperator{\ElementBoundary} \cdot \NormalVector + (\MicromorphicDamageStabilizationFactor / h_{\ElementCell}) \Field{\MicromorphicDamageJumpField}{}{\; h}(\Field{\MicromorphicDamageField}{\ElementCell}{\; h}, \Field{\MicromorphicDamageField}{\ElementBoundary}{\; h})$ respectively.
In particular, the expression of the discrete jump function $\Field{\DisplacementJumpField}{}{\; h}$
is the key ingredient that defines the HHO method (see Section \ref{sec_appendix_implementation} for more details on this note).
The solution of the discrete problem $(\Field{\DisplacementField}{\ElementCell}{\; h}, \Field{\DisplacementField}{\ElementBoundary}{\; h}, \Field{\MicromorphicDamageField}{\ElementCell}{\; h}, \Field{\MicromorphicDamageField}{\ElementBoundary}{\; h})$
<!---  $(\mathfrak{U}_{\ElementCell}, \mathfrak{U}_{\ElementBoundary})$ -->
is defined by the fact that the
residuals $\Field{\Vector{R}}{u, \ElementCell}{}, \Field{\Vector{R}}{u, \ElementBoundary}{}, \Field{\Vector{R}}{d, \ElementCell}{}, \Field{\Vector{R}}{d, \ElementBoundary}{}$ must be
zero.

<!---  --------------------------------------------------------- -->
<!---  PARAGRAPH -->
<!---  --------------------------------------------------------- -->
#### Global residuals and face assembly

##### Global problem

At the global scale, the solution
$(\Field{\Vector{U}}{\Mesh}{}, \Field{\Vector{U}}{\Skeleton}{}, \Field{\Vector{D}}{\Mesh}{}, \Field{\Vector{D}}{\Skeleton}{})$ of the
discrete problem satisfies
<!---  -->
<!---   -->
<!---   -->
\begin{subequations}
  \label{eq_final_problem_003}
  \begin{alignat}{3}
    \Field{\Vector{R}}{u, \ElementCell}{}(\Field{\Vector{U}}{\ElementCell}{}, \Field{\Vector{U}}{\ElementBoundary}{})
    \cdot
    \Field{\VirtualField{\Vector{U}}}{\ElementCell}{} & = 0
    &&
    \qquad \forall \ElementCell \in \Mesh(\BodyLagrange), \; \forall \Field{\VirtualField{\Vector{U}}}{\ElementCell}{} \;
    \label{eq_final_problem_003:eq0}
    \\
    \Field{\Vector{R}}{d, \ElementCell}{}(\Field{\Vector{D}}{\ElementCell}{}, \Field{\Vector{D}}{\ElementBoundary}{})
    \cdot
    \Field{\VirtualField{\Vector{D}}}{\ElementCell}{} & = 0
    &&
    \qquad \forall \ElementCell \in \Mesh(\BodyLagrange), \; \forall \Field{\VirtualField{\Vector{U}}}{\ElementCell}{} \;
    \label{eq_final_problem_003:eq1}
    \\
    \Field{\Vector{R}}{u, \Skeleton}{}(\Field{\Vector{U}}{\Mesh}{}, \Field{\Vector{U}}{\Skeleton}{})
    \cdot
    \Field{\VirtualField{\Vector{U}}}{\Skeleton}{} & = 0
    &&
    \qquad \forall \Field{\VirtualField{\Vector{U}}}{\Skeleton}{} \;
    \label{eq_final_problem_003:eq2}
    \\
    \Field{\Vector{R}}{u, \Skeleton}{}(\Field{\Vector{D}}{\Mesh}{}, \Field{\Vector{D}}{\Skeleton}{})
    \cdot
    \Field{\VirtualField{\Vector{D}}}{\Skeleton}{} & = 0
    &&
    \qquad \forall \Field{\VirtualField{\Vector{D}}}{\Skeleton}{} \;
    \label{eq_final_problem_003:eq3}
  \end{alignat}
\end{subequations}
<!---  -->
<!---  -->
<!---  -->
where the vectors
$\Field{\Vector{R}}{u, \Skeleton}{}(\Field{\Vector{U}}{\Mesh}{}, \Field{\Vector{U}}{\Skeleton}{})$ and $\Field{\Vector{R}}{d, \Skeleton}{}(\Field{\Vector{D}}{\Mesh}{}, \Field{\Vector{D}}{\Skeleton}{})$ are the skeleton residuals such that
<!---  -->
<!---   -->
<!---   -->
\begin{subequations}
  \label{eq_final_problem_00333}
  \begin{alignat}{3}
    \Field{\Vector{R}}{u, \Skeleton}{}(\Field{\Vector{U}}{\Mesh}{}, \Field{\Vector{U}}{\Skeleton}{})
    \cdot
    \Field{\VirtualField{\Vector{U}}}{\Skeleton}{}
    &
    =
    \sum_{\ElementFace \in \SkeletonInterior(\BodyLagrange)} \int_{\ElementFace}
    (
      \Field{\DisplacementTractionField}{\Field{\ElementCell}{\ElementFace}{1}}{\; h}
      +
      \Field{\DisplacementTractionField}{\Field{\ElementCell}{\ElementFace}{2}}{\; h}
    )
    \cdot \Field{\VirtualField{\DisplacementField}}{\ElementFace}{\; h}
    +
    \sum_{\ElementFace \in \SkeletonBoundaryNeumann(\BodyLagrange)}
    \int_{\ElementFace}
    (
      \Field{\DisplacementTractionField}{\Field{\ElementCell}{\ElementFace}{}}{\; h}
      - \neumannLag
    )
    \cdot \Field{\VirtualField{\DisplacementField}}{\ElementFace}{\; h}
    &&
    \qquad \forall \Field{\VirtualField{\Vector{U}}}{\ElementFace}{}
    \label{eq_final_problem_00333:eq0}
    \\
    \Field{\Vector{R}}{d, \Skeleton}{}(\Field{\Vector{D}}{\Mesh}{}, \Field{\Vector{D}}{\Skeleton}{})
    \cdot
    \Field{\VirtualField{\Vector{U}}}{\Skeleton}{}
    &
    =
    \sum_{\ElementFace \in \SkeletonInterior(\BodyLagrange)} \int_{\ElementFace}
    (
      \Field{\MicromorphicDamageTractionField}{\Field{\ElementCell}{\ElementFace}{1}}{\; h}
      +
      \Field{\MicromorphicDamageTractionField}{\Field{\ElementCell}{\ElementFace}{2}}{\; h}
    )
    \,
    \Field{\VirtualField{\MicromorphicDamageField}}{\ElementFace}{\; h}
    +
    \sum_{\ElementFace \in \SkeletonBoundary(\BodyLagrange)}
    \int_{\ElementFace}
    \Field{\MicromorphicDamageTractionField}{\Field{\ElementCell}{\ElementFace}{}}{\; h}
    \,
    \Field{\VirtualField{\MicromorphicDamageField}}{\ElementFace}{\; h}
    &&
    \qquad \forall \Field{\VirtualField{\Vector{D}}}{\ElementFace}{}
    \label{eq_final_problem_00333:eq1}
  \end{alignat}
\end{subequations}
<!---  -->
<!---  -->
<!---  -->
and which result in the assembly of faces unknowns only.

##### Assembly over the skeleton

An interior face $\ElementFace$ is linked to two adjacent cells $\Field{\ElementCell}{}{1}$ and $\Field{\ElementCell}{}{2}$, and
each of these cells applies to the other a surface load $\pm
\tensori{t}{}_{\Field{\ElementCell}{}{1} \cap \Field{\ElementCell}{}{2}}$ through $\ElementFace$, which is identified with
$\tensori{t}{}_{\neumannCell}$ on $\ElementFace$ in \eqref{eq_final_problem_00:eq1} for the displacement field, and which is zero
for the micromorphic damage field.
By summation over each face of the structure, these equal contributions
cancel out, which yields the expression of the first argument in the
right-hand side of \eqref{eq_final_problem_00333:eq0} and \eqref{eq_final_problem_00333:eq1}.
<!---  -->
<!---  -->
<!---  -->
Since exterior faces subjected to Neumann boundary conditions are
linked to a single cell only, the local surface forces $\tensori{t}{}_{\neumannCell}$ are equal to $\neumannLag$ on $\neumannBoundaryLag{}$,
which yields the expression of
the second argument in the right-hand side of
\eqref{eq_final_problem_00333:eq0}.## Description

### Free energy potential description

##### Mechanical energy

The mechanical energy is the product of the pure mechanical contribution to which is added
an adimensional \textit{degradation function} $g(d)$ such that
<!---  -->
<!---  -->
<!---  -->
\begin{equation}
    \begin{aligned}
        \psi_{\tensoriis{F}, d} = g(d) \, \psi_{mec}(\tensorii{F}{})
    \end{aligned}
\end{equation}
<!---  -->
<!---  -->
<!---  -->
where different choices arise in terms of the definition of the degradation function.

##### Dissipation potential

A dissipation potential $\phi_{\bodyLag}(d)$ accounts for the energy dissipated by the fracture process of the medium, and is assumed to be
an homogeneous function of degree one such that
<!---  -->
<!---  -->
<!---  -->
\begin{equation}
    \begin{aligned}
        \Delta \, t \, \phi_{\bodyLag}(\frac{\hat{d} - d} {\Delta \, t}) = \phi_{\bodyLag}(\hat{d} - d)
        &&
        \forall (\hat{d}, \Delta \, t > 0)
    \end{aligned}
\end{equation}
<!---  -->
<!---  -->
<!---  -->
In particular, the dissipation potential generally contains an indicator function imposing the irreversibility of the
damage evolution.

\begin{equation}
    \begin{aligned}
        \psi_{\bodyLag} = 
    \end{aligned}
\end{equation}
<!---  --------------------------------------------------------- -->
<!---  -- SUBSECTION -->
<!---  --------------------------------------------------------- -->
## Resolution scheme
\label{sec_cell_unknowns_elimination}

### Irreversibility condition
\label{sec:discretization:extension_to_non_linear_materials}

This section is devoted to the extending the proposed formulation to the non-linear case that takes into account the dissipation potential $\psi_{\BodyLagrange}$ and the damage variable.

##### Total Lagrangian for the proposed HDG formulation
The proposed elementary Lagragian \eqref{eq_total_lagragian_bis} depends now on a dissipative term, such that
<!---  -->
<!---  -->
<!---  -->
\begin{equation}
    \begin{aligned}
        L_{\ElementCell}^{HDG}
        =
        &
        \int_{\ElementCell} \psi_{\BodyLagrange}
        +
        \int_{\ElementCell} \phi_{\BodyLagrange} \paren{\DamageField - \DamageField \TraceOperator{t}}
        +
        \int_{\ElementBoundary} \frac{\DisplacementStabilizationFactor}{2 h_{\ElementCell}} \lVert \DisplacementJumpField(\Field{\DisplacementField}{\ElementCell}{}, \Field{\DisplacementField}{\ElementBoundary}{}) \rVert^2
        +
        \int_{\ElementBoundary} \frac{\MicromorphicDamageStabilizationFactor}{2 h_{\ElementCell}} \Field{\MicromorphicDamageJumpField}{}{2}(\Field{\MicromorphicDamageField}{\ElementCell}{}, \Field{\MicromorphicDamageField}{\ElementBoundary}{})
        \\
        &
        -
        \int_{\ElementCell} \loadLag{} \cdot \tensori{u}{}_{\ElementCell}
        -
        \int_{\neumannCell{}} \neumannCellLoad{} \cdot \tensori{u}{}_{\ElementBoundary}
    \end{aligned}
\end{equation}
<!---  -->
<!---  -->
<!---  -->

##### Standard Generalized dissipation of the damage

At each point, the thermodynamic force $\DamageForceField$ associated with the damage is in the subgradient of the
dissipation potential $\phi_{\BodyLagrange}$.

##### Damage unknown elminiation

\begin{equation}
    \derivtot{\MicromorphicDamageForceField}{\MicromorphicDamageField}
    =
    \deriv{\MicromorphicDamageForceField}{\MicromorphicDamageField}
    +
    \deriv{\MicromorphicDamageForceField}{\DamageField}
    \deriv{\DamageField}{\MicromorphicDamageField}
\end{equation}## Numerical examples

In this section, the proposed coupled mechanical-micromorphic damage HHO method is evaluated on
classical test cases taken from the literature.
The reader can refer to XXX regarding technical aspects. 
The notation
HHO($k,l$) relates to the HHO element of order $k$ on faces, and order $l$ in the
cell.

The tests presented in this section have been performed using an
\texttt{python} implementation freely available on github: \url{https://github.com/davidsiedel/h2o_paper}.

<!---  --------------------------------------------------------- -->
<!---  PARAGRAPH -->
<!---  --------------------------------------------------------- -->
##### Stabilization parameter

To ensure coercivity of the HHO method, the so-called \textit{stabilization} parameters
$\DisplacementStabilizationFactor$ and $\MicromorphicDamageStabilizationFactor$, that relate to the stiffness of the elastic interface introduced in Section \ref{sec_hdg_element_equilibrium}, needs be chosen according to the material under study. In \cite{di_pietro_hybrid_2015}, a value of
order $2 \mu$ is advocated for the displacement problem, where $\mu$ denotes the shear modulus of the
material. This value is used for all test cases in the present section. Similarly the micromorphic damage stabilization parameter $\MicromorphicDamageStabilizationFactor$
is chosen in agreement with the stiffness of the micromorphic damage problem, and is equal to $G_c$.

### Uniaxial rod
\label{sec_uniaxial_rod}

##### Specimen and loading

This benchmark is a tensile test on a uniform rod, with an imperfection at the center.
The rod has an length $L = 1$ mm and a width $l = 0.1$ mm.
A vertical displacement $u$ is imposed at the top of the rod.
The simulation is performed until the limit load corresponding to an internal displacement of $0.2$ mm is reached.

<!---  --------------------------------------------------------- -->
<!---  PARAGRAPH -->
<!---  --------------------------------------------------------- -->
##### Material behaviour

The mechanical potential involves a degradation function $g(d)$ acting on the spherical part of the elastic energy of the material such that
<!---  -->
<!---  -->
<!---  -->
\begin{equation}
    \psi_{\tensoriis{F}, \DamageField} (\TransformationGradientField, \DamageField) = g(\DamageField) \, \psi_{sph}(\TransformationGradientField) + \psi_{dev}(\TransformationGradientField)
\end{equation}
<!---  -->
<!---  -->
<!---  -->
where $g(d) = (1 - d)^2$ in order to recover the AT2 model \cite{bourdin_numerical_2000}.
The potentials $\psi_{sph}$ and $\psi_{sph}$ are based on a devatoric-spherical split of the
Hooke tensor for a linear elastic material.
<!---  -->
<!---  -->
<!---  -->
The micromorphic damage and damage potentials are chosen such that
<!---  -->
<!---  -->
<!---  -->
\begin{subequations}
    \label{eq_micromorphic_rod_damage_potentials}
    \begin{alignat}{1}
        \psi_{\DamageField, \MicromorphicDamageField} (\DamageField, \MicromorphicDamageField)
        &
        =
        \frac{1}{2} H_{\chi}(\DamageField - \MicromorphicDamageField)^2
        \label{eq_micromorphic_rod_damage_potentials:eq0}
        \\
        \psi_{\DamageField} (\DamageField)
        &
        =
        \frac{G_c}{2 \ell_c} \DamageField^2
        \label{eq_micromorphic_rod_damage_potentials:eq1}
        \\
        \psi_{\MicromorphicDamageGradientField} (\MicromorphicDamageGradientField)
        &
        =
        A_{\chi} \MicromorphicDamageGradientField \cdot \MicromorphicDamageGradientField
        \label{eq_micromorphic_rod_damage_potentials:eq2}
    \end{alignat}
\end{subequations}
Moreover, the small strain hypothesis is assumed for this test case.
<!---  -->
<!---   -->
<!---   -->
\begin{figure}[H]
    \centering
    \includegraphics[width=5.cm]{../article_02/figures/rod.png}
    \caption{Mesh and micromorphic damage at the last time step}
    \label{fig_rod_micromirphic}
\end{figure}

<!---  --------------------------------------------------------- -->
<!---  PARAGRAPH -->
<!---  --------------------------------------------------------- -->
##### Displacement along the radius

The force deflection curve of the experiment is given in Figure \ref{fig_rod_micromirphic_cruve}. The results obtained with the HHO formulation are compared to those provided by
the \texttt{MFEM} library, and are in agreement with those provided by a standard Lagrange discretization.
<!---  -->
<!---   -->
<!---   -->
\begin{figure}[H]
    \centering
    \includegraphics[width=7.cm]{../article_02/figures/rod_curve.png}
    \caption{...}
    \label{fig_rod_micromirphic_cruve}
\end{figure}

### Matrix fiber specimen

<!---  --------------------------------------------------------- -->
<!---  PARAGRAPH -->
<!---  --------------------------------------------------------- -->
##### Specimen and loading

The last application consists of a two dimensional plate that is subjected to uniaxial
extension. The plate (or matrix) is clamped around a fiber of radius $0.2$ mm (representated by the hole in the mesh).
The matrix is a square of length of $1$ mm. A vertical
displacement $u_y = 0.2$ mm is imposed at the top, as shown in Figure \ref{fig_matrix}.

<!---  --------------------------------------------------------- -->
<!---  PARAGRAPH -->
<!---  --------------------------------------------------------- -->
##### Behaviour law

The same behavior law as that in \ref{sec_uniaxial_rod} is considered for the present test case.
<!---  -->
<!---   -->
<!---   -->
\begin{figure}[H]
    \centering
    \includegraphics[width=7.cm]{../article_02/figures/plate.png}
    \caption{...}
    \label{fig_matrix}
\end{figure}

<!---  --------------------------------------------------------- -->
<!---  PARAGRAPH -->
<!---  --------------------------------------------------------- -->
##### Load deflection curve

The load-displacement curve is plotted
in Figure \ref{fig_matrix_curve}, and gives similar results to that obtained with a standard Lagrange discretization.
<!---  -->
<!---   -->
<!---   -->
\begin{figure}[H]
    \centering
    \includegraphics[width=7.cm]{../article_02/figures/plate_curve.png}
    \caption{...}
    \label{fig_matrix_curve}
\end{figure}
