Указатель параметров
====================

Значения по умолчанию
---------------------

.. list-table::
   :header-rows: 1
   :widths: 42 23 35

   * - Параметр
     - По умолчанию
     - Раздел
   * - GROW
     - 100%
     - :doc:`settings/main`
   * - TRIM
     - 0%
     - :doc:`settings/main`
   * - SPLINE TYPE
     - CLOSE DUO
     - :doc:`settings/main`
   * - INVERT TRIM
     - OFF
     - :doc:`settings/main`
   * - ANCHOR OFFSET
     - 0%
     - :doc:`settings/main`
   * - SYMMETRY
     - ON
     - :doc:`settings/main`
   * - SPEED MOD
     - TIME
     - :doc:`settings/main`
   * - OVERLAP
     - 100%
     - :doc:`settings/main`
   * - TRIM BOUNCE MODE
     - NO AUTO BOUNCE
     - :doc:`settings/main`
   * - SNAP EXTRAPOLATED
     - ON
     - :doc:`settings/main`
   * - SPEED MODE
     - MOMENTAL
     - :doc:`settings/main`
   * - BORDER CORRECTION
     - ON
     - :doc:`settings/main`
   * - SCALE START / END
     - 100% / 100%
     - :doc:`settings/deformation`
   * - FIX SEG DIR
     - OFF
     - :doc:`settings/output`
   * - UV MODE
     - LOCAL
     - :doc:`settings/output`
   * - UV INVERT
     - OFF
     - :doc:`settings/output`
   * - Phong Angle
     - 60°
     - :doc:`settings/output`
   * - SORT MODE
     - BASE
     - :doc:`settings/segment-sort`
   * - GAP / ID OFFSET
     - 0 / 0
     - :doc:`settings/segment-sort`
   * - MERGE PAIR
     - OFF
     - :doc:`settings/segment-sort`
   * - SEARCH RADIUS LOCAL
     - 5%
     - :doc:`settings/segment-sort`
   * - SEARCH RADIUS REAL
     - 30 m
     - :doc:`settings/segment-sort`
   * - MAX NEIG
     - 1
     - :doc:`settings/segment-sort`
   * - PAIR IDS
     - ``0+5``
     - :doc:`settings/segment-sort`
   * - ANCHOR MODE
     - BASE
     - :doc:`settings/anchor-sort`
   * - PROPORTIONAL
     - ON
     - :doc:`settings/anchor-sort`
   * - ANCHOR SORT MODE
     - BASE
     - :doc:`settings/anchor-sort`
   * - SAMPLE COUNT
     - 100
     - :doc:`settings/anchor-sort`

Динамические параметры
----------------------

Некоторые элементы появляются только в подходящем контексте:

* ``SNAP EXTRAPOLATED`` — OPEN EXTRAPOLATED + Symmetry;
* ``SPEED MODE`` и ``BORDER CORRECTION`` — OPEN FAKE + Symmetry;
* ``INVERT DIR`` — при включённом Fix Seg Dir;
* параметры Pairs — при включённом Merge Pair;
* ``REF OBJECT`` — Distance to Object или Splinora;
* ``SAMPLE COUNT`` — Distance to Object + Sampling;
* настройки Circle — при Anchor Mode = Circle.

