# Numerical implementations using standard finite elements

## Comparison of the micromorphic solutions to the phase-field solutions on selected test cases  using `mgis.fenics` {#sec:micromorphicdamage:test_cases}

In this section, the
[`mgis.fenics`](https://thelfer.github.io/mgis/web/mgis_fenics.html)
python module is used [@bleyer_overview_2020].


We consider in this section three classical test cases:

- a fiber reinforced matrix in tension, as proposed by Bourdin *et al.*
  [@bourdin_numerical_2000],
- a precracked specimen loaded by applying a tangential displacement on
  the top boundary, as proposed by Miehe *et al.* [@miehe_phase_2010],
- a precracked specimen loaded by applying a normal displacement on the
  top boundary, as proposed by Miehe *et al.* [@miehe_phase_2010].

![Damage patterns at the end of the unit tests.](img/DamagePattern.pdf){#fig:micromorphicdamage:damage_patterns}

Those tests are performed using the AT2 model and its micromorphic
counterparts using a spectral decomposition of the elastic free energy.
The damage patterns at the end of those tests are reported on Figure
@fig:micromorphicdamage:damage_patterns.

The `python` scripts are available in this repository:
<https://github.com/thelfer/micromorphic-damage-giens-2022>.

Those scripts contains the geometry, material properties and loadings
required to reproduce those tests.

For those tests, the penalisation parameter \(H_{\chi}\) is chosen of
the form:
\[
H_{\chi}= \beta\,\Frac{G_{c}}{l_{0}}
\]

where \(\beta\) is a normalised penalisation parameter [@bharali_computational_2021].

### Choice of the convergence criterion of the staggered schemes

In this paper, the staggered schemes are stopped when the damage becomes
stationnary, i.e. when the absolute difference between two estimates of
the damge is below a given threshold \(\varepsilon_{d}\) at each
integration point.

This criterion is not totally satisfying as it does not ensure that a
true minimun of the Lagrangian is found. We carefully checked that this
is the case for each steps of the numerical experiments described in
this section.

### Discussion

Those three tests lead to similar conclusions:

![Evolution of the force as a function of the imposed displacement for
the fiber reinforced matrix test for the third scheme with \(\beta=150\)
and the standard phase-field schemes based on the resolution of the
variational inegality or based on Miehe' history
function](img/FiberReinforcedMatrix-force.pdf){#fig:micromorphic_damage:force
width=75%}

![Evolution of the force as a function of the imposed displacement for
\(\beta=50\), \(\beta=100\), \(\beta=150\) for the shear test using the
third staggered scheme.](img/shear-force.pdf){width=75%
#fig:micromorphic_damage:beta}

![Evolution of the fracture energy as a function of the imposed
displacement for \(\beta=50\), \(\beta=100\), \(\beta=150\) for the
shear test using the third staggered
scheme.](img/DissipatedEnergies.pdf){width=75%
#fig:micromorphic_damage:beta2}

![Number of iterations of the fixed point algorithm for the shear test
as a function of the step number for the standard AT2 model and the
third scheme for \(\beta=150\) and
\(\beta=300\).](img/shear-iterations.pdf){width=75%
#fig:micromorphic_damage:shear:iterations}

- The two first schemes converges very slowly (several thousand of fixed
  point iterations) even in the quasi-elastic range. A threshold as
  small as \(10^{-5}\) is required to ensure converged results. Those
  schemes are considered unsuable in pratice.
- The third scheme converges much faster. A threshold value of
  \(10^{-3}\) is sufficient to have converged results. The same
  threshold value is used for the standard AT2 model.
- As illustrated by Figure @fig:micromorphic_damage:force, the
  force-displacement curve of the third scheme is very similar to the
  standard AT2 model.
- As illustrated by Figure @fig:micromorphic_damage:beta, the
  penalisation factor plays a major role on the overall
  force-displacement curve. Our experiments shows that a value of
  \(150\) leads to results undistinguishable with the one of the AT2
  model for every tests. However, an higher value of \(300\) is
  required to reproduce closely the evolution of the fracture energy.
- The number of iteration of the fixed point algorithm is roughly
  similar between the standard AT2 model and the third scheme, altough a
  bit higher in general, as depicted on Figure
  @fig:micromorphic_damage:shear:iterations.

## Numerical Experiments {#sec:micromorphicdamage:numerical_experiments}

In this section, the [`MFEM/MGIS`]() solver is used.

### Shear driven fracture

Alessi et al. proposed a model to describe deviatoric driven fracture
using the following choice of the elastic free energy
[@alessi_phase-field_2020]:
\[
\freeenergyel\paren{\tepsilon, d}=
\Frac{K}{2}\,\paren{\trace{\tepsilon}}^{2}+
\mu\,g\paren{d}\,\tenseur{s}^{\varepsilon}\,\colon\,\tenseur{s}^{\varepsilon}
\]
where \(K\) is the bulk modulus, \(\tenseur{s}^{\varepsilon}\) is the
deviatoric part of the elastic strain. The degradation function
\(g\paren{d}\) and the other terms of the Lagrangian are the same as in
the AT2 model.

As stated by Alessi et al., this model lead to quasi-incompressible
behaviour in highly damaged zones and proposed a simple tensile test on
a bar which demonstrated that standard Lagrange elements are not able to
properly describe the damage localisation band and the dissipated energy
by the crack propagation. Alessi et al. then showed that various
classical approaches (selective reduced integration and mixed
displacement/pressure formulation) can overcome this issue.

This test is adapted in this section to demonstrate that the
micromorphic approaches can be used with higher order finite elements.
The same order of approximation will be used to solve the mechanical and
the micromorphic problems.

#### Geometry, loadings and meshes

The specimen is a \(2D\) plate of width \(w\) and height \(h\) treaten
under the plane strain hypothesis. The axial displacement of the lower
boundary is set to zero, while the axial displacement of the upper
boundary is imposed. The point at the lower left corner is fixed in the
lateral direction to avoid rigid body motion.

: Geometry and material parameters for the shear driven fracture test.
{#tbl:micromorphicdamage:shear_driven_fracture_test_parameters}

+----------------------------------+-----------------------------+
| Plate width \(w\)                | \(10^{-3}\, m\)             |
+----------------------------------+-----------------------------+
| Plate height \(h\)               | \(2\,\cdot\,10^{-3}\, m\)   |
+----------------------------------+-----------------------------+
| Young's modulus \(E\)            | \(210\,\cdot\,10^{9}\, Pa\) |
+----------------------------------+-----------------------------+
| Poisson's ratio \(\nu\)          | \(0.3\)                     |
+----------------------------------+-----------------------------+
| Fracture energy \(G_{c}\)        | \(2.7\,J.m^{-2}\)           |
+----------------------------------+-----------------------------+
| Characteristic length  \(l_{0}\) | \(2.5\,\cdot\,10^{-5}\,m\)  |
+----------------------------------+-----------------------------+
| Penalisation factor \(\beta\)    | \(300\)                     |
+----------------------------------+-----------------------------+

The geometry and the material parameters used for this test are
summarized in Table
@tbl:micromorphicdamage:shear_driven_fracture_test_parameters. In order
to localize the damage, the fracture energy is assumed uniform in the
plate except in a small square of size \(5\,\cdot\,10^{-2}\,\cdot\,w\)
located at the center of the plate where the fracture energy value is
\(G_{c}\,\cdot\,\paren{1-10^{-2}}\).

: Number of elements for the shear driven fracture test. A very fine
mesh is used for low order finite elements (\(1\) and \(2\)) with
several dozen elements inside the damage band (See Figure
@fig:micromorphicdamage:shear_driven_fracture_test_order1). A coarser
mesh is used for higher order elements (\(4\) and \(6\)) with \(4\) to
\(6\) elements inside the damage band.
{#tbl:micromorphicdamage:shear_driven_fracture_test_elements}

+---------+-----------------------+
| Order 1 | \(102\,272\) elements |
+---------+-----------------------+
| Order 2 | \(409\,088\) elements |
+---------+-----------------------+
| Order 4 | \(25\,568\) elements  |
+---------+-----------------------+
| Order 6 | \(25\,568\) elements  |
+---------+-----------------------+

The plate is discretized with triangle elements. The number of elements
used as a function of the finite element order is given in Table
@tbl:micromorphicdamage:shear_driven_fracture_test_elements. In
practice, this number of elements have little influence on the results
and the conclusions drawn in the next paragraph.

#### Results

![Spurious damage map obtained with linear elements (left). Zoom on the shear fracture (right)](img/shear-driven-fracture-damage-results-order-1.pdf){#fig:micromorphicdamage:shear_driven_fracture_test_order1 width=75%}

Figure @fig:micromorphicdamage:shear_driven_fracture_test_order1
describes the damage map pattern after the propagation of the crack. As
described by Alessi et al., volumetric locking leads to a spurious
damage localisation band with excessive thickness, i.e. a thickness
largely greater than the characteristic length \(l_{0}\). A very fine
mesh is used to demonstrate that the issue is not solved by mesh
refinement.

![Damage map for higher order elements. Quadradic elements (left), fourth order elements (center), sixth order elements (right). The quadratic mesh is too fine to be shown without hiding the results.](img/shear-driven-fracture-damage-results-higher-orders.pdf){#fig:micromorphicdamage:shear_driven_fracture_test_higher_order width=100%}

Figure @fig:micromorphicdamage:shear_driven_fracture_test_higher_order
show the results obtained with higher order elements. While the
simulation with quadratic elements still exhibit a spurious damage
localisation band, similar to the one observed with linear elements in
Figure @fig:micromorphicdamage:shear_driven_fracture_test_order1, higher
order elements lead to satisfying results, i.e. higher order elements
alleviate issues related to volumetric locking.

![Traction curve](img/shear-driven-fracture-damage-results-force.pdf){#fig:micromorphicdamage:traction_curve width=75%}

Figure @fig:micromorphicdamage:traction_curve presents the
force/displacement curves as a function of the finite element order.
Quadratic results, which are intermediate between linear and quadratic
results are not reproduced for the sake of clarity. The following
observations can be made:

- All order of approximations give similar results up to the crack
  progation.
- The traction curve given by linear elements exhibits a residual
  stifness and a spurious dissipation after the crack propagation.
- Fourth order and sixth order give undistinguishable results. In both
  cases, the force drops to zero after the crack propagation.

<!--
#### Linear results

-->

### Industrial test case: nuclear fuel pellet fragmentation

In this section, the fragmentation of a nuclear fuel pellet during the
reactor start-up. 

#### Geometry, material and loadings

: Geometry, material parameters and loading parameters for the fuel pellet fragementation test.
{#tbl:micromorphicdamage:fuel_pellet_fragmentation_test_parameters}

+--------------------------------------------------------------+-----------------------------+
| Pellet radius \(r_{p}\)                                      | \(4.085\,\cdot\,10^{-3}\)   |
+--------------------------------------------------------------+-----------------------------+
| Pellet height \(h_{p}\)                                      | \(6.7\,\cdot\,10^{-3}\)     |
+--------------------------------------------------------------+-----------------------------+
| Dishing radius \(r_{d}\)                                     | \(3.05\,\cdot\,10^{-3}\)    |
+--------------------------------------------------------------+-----------------------------+
| Dishing height \(h_{d}\)                                     | \(3.2\,\cdot\,10^{-4}\)     |
+--------------------------------------------------------------+-----------------------------+
| Young's modulus \(E\)                                        | \(150\,\cdot\,10^{9}\, Pa\) |
+--------------------------------------------------------------+-----------------------------+
| Poisson's ratio \(\nu\)                                      | \(0.3\)                     |
+--------------------------------------------------------------+-----------------------------+
| Linear mean thermal expansion coefficient \(\alpha\)         | \(1\,\cdot\,10^{-5}\)       |
+--------------------------------------------------------------+-----------------------------+
| Thermal expansion reference temperature \(T_{\mathrm{ref}}\) | \(1\,\cdot\,10^{-5}\)       |
+--------------------------------------------------------------+-----------------------------+
| Fracture energy \(G_{c}\)                                    | \(xxx\,J.m^{-2}\)           |
+--------------------------------------------------------------+-----------------------------+
| Characteristic length  \(l_{0}\)                             | \(xxx\,\cdot\,10^{-xx}\,m\) |
+--------------------------------------------------------------+-----------------------------+
| Penalisation factor \(\beta\)                                | \(300\)                     |
+--------------------------------------------------------------+-----------------------------+
| Core temperature\(T_{c}\)                                    | \(1500\,K\)                 |
+--------------------------------------------------------------+-----------------------------+
| Outer surface temperature \(T_{o}\)                          | \(600\,K\)                  |
+--------------------------------------------------------------+-----------------------------+

##### Thermal expansion

The strain \(\tepsilonth\) associated with the thermal expansion is
computed as follows:
\[
\tepsilonth\paren{T}=\alpha\,\paren{T-T_{\mathrm{ref}}}\,\tenseur{I}
\]
where:

- \(T\) is the temperature.
- \(T_{\mathrm{ref}}\) is a reference temperature.
- \(\alpha\) is the mean linear thermal expansion coefficient.

##### Modification of the free energy

To take thermal expansion into account, the free energy
\(\freeenergyel\paren{\tepsilon, d}\) is modified as follows:
\[
\freeenergyel\paren{\tepsilon, T, d} = 
g\paren{d}\,\freeenergyel_{0}\paren{\tepsilon-\tepsilonth} =
\Frac{g\paren{d}}{2}\,\paren{\tepsilon-\tepsilonth}\,\colon\,\tenseurq{D}\,\colon\,\paren{\tepsilon-\tepsilonth}
\]{#eq:micromorphicdamage:freeenergygel}

##### Temperature profile

Under the approximation of a constant thermal conductivity, the
temperature profile in a PWR fuel pellet is axisymmetric and parabolic:
\[
T\paren{r, t}=\Delta\,T\paren{t}\,\paren{1-r^{2}}+T_{\mathrm{o}}
\]
where:

- \(t\) is a loading parameter in the range \([0:1]\).
- \(T_{\mathrm{o}}\) is the temperature at the outer boundary of the
  fuel pellet.
- The temperature increase \(\Delta\,T\paren{t}\) is chosen as a linear
  function of the loading parameter as follows:
  \[
  \Delta\,T\paren{t} = \paren{T_{\mathrm{c}}-T_{\mathrm{o}}}\, t
  \]

#### Results

\(33\,230\,848\) triangles, \(132'923'392\) nodes, \(4.10^8\) degrees of freedom for the mechanical problem.

![Crack pattern](img/FuelPelletCracking-results.pdf){width=75%}

