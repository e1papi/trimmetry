Основные параметры
==================

MAIN SETTINGS
-------------

PATH / PROFILE
~~~~~~~~~~~~~~

Ссылки на траекторию и профиль. В текущей исследованной сборке
рекомендуется использовать дочернюю иерархию:

.. code-block:: text

   Trimmetry
   ├── Path
   └── Profile

.. image:: /_static/gifs/main-settings/path-profile.gif
   :alt: Настройка Path и Profile в Trimmetry
   :width: 100%
   :align: center

GROW
~~~~

Конец видимого диапазона, от ``0%`` до ``100%``.

* ``0%`` — рост ещё не начался;
* ``100%`` — достигнут конец доступного диапазона.

TRIM
~~~~

Начало видимого диапазона. Рост между Trim и Grow остаётся видимым.
Параметр отключается при выборе автоматического ``TRIM_BOUNCE_MODE``.

SPLINE TYPE
~~~~~~~~~~~

CLOSE DUO
   Двусторонний режим для замкнутого пути. Рост идёт от Anchor в двух
   направлениях с поддержкой разреза закрытой цепочки.

   .. image:: /_static/gifs/main-settings/spline-close-duo.gif
      :alt: Режим Close Duo
      :width: 100%
      :align: center

CLOSE
   Закрытый путь с обычной двусторонней обрезкой.

   .. image:: /_static/gifs/main-settings/spline-close.gif
      :alt: Режим Close
      :width: 100%
      :align: center

OPEN
   Открытая логика, в которой обе стороны используют одинаковую
   нормализованную дистанцию относительно Anchor.

   .. image:: /_static/gifs/main-settings/spline-open.gif
      :alt: Режим Open
      :width: 100%
      :align: center

OPEN PROPORTIONAL
   Каждая сторона нормализуется по собственной доступной длине. При
   нецентральном Anchor левая и правая части достигают концов одновременно.

   .. image:: /_static/gifs/main-settings/spline-open-proportional.gif
      :alt: Режим Open Proportional
      :width: 100%
      :align: center

OPEN EXTRAPOLATED
   Открытый режим с виртуальными крайними кольцами. Он помогает продолжить
   обрезку за вычисленную границу сегмента. Дополнительно доступен
   ``SNAP EXTRAPOLATED``.

   .. image:: /_static/gifs/main-settings/spline-open-extrapolated.gif
      :alt: Режим Open Extrapolated
      :width: 100%
      :align: center

OPEN FAKE
   Режим с виртуальной скоростью крайних областей и сохранением разрывов
   полигонов. Для него доступны ``SPEED MODE`` и ``BORDER CORRECTION``.

   .. image:: /_static/gifs/main-settings/spline-open-fake.gif
      :alt: Режим Open Fake
      :width: 100%
      :align: center

.. note::

   Режимы ``CLOSE DUO``, ``CLOSE`` и ``OPEN FAKE`` принудительно
   обрабатывают Path как закрытый. ``OPEN``, ``OPEN PROPORTIONAL`` и
   ``OPEN EXTRAPOLATED`` — как открытый.

INVERT TRIM
~~~~~~~~~~~

* ``OFF`` — оставить интервал между Trim и Grow;
* ``ON`` — удалить этот интервал и оставить внешние части.

ANCHOR OFFSET
~~~~~~~~~~~~~

Сдвигает вычисленный Anchor вдоль сегмента. Значение хранится как
нормализованная доля, несмотря на процентное отображение интерфейса.

SYMMETRY
~~~~~~~~

* ``ON`` — двусторонний рост относительно Anchor;
* ``OFF`` — однонаправленная обрезка.

.. image:: /_static/gifs/main-settings/symmetry-undir.gif
   :alt: Однонаправленная обрезка при выключенной Symmetry
   :width: 100%
   :align: center

SPEED & OVERLAP
---------------

SPEED MOD
~~~~~~~~~

``TIME`` распределяет одинаковое время на группу, ``LENGTH`` учитывает
её длину, ``MIX`` смешивает оба результата.

OVERLAP
~~~~~~~

Определяет, насколько временные диапазоны соседних групп перекрываются.
При ``0%`` группы идут последовательно; увеличение значения запускает
следующие группы раньше.

.. image:: /_static/gifs/speed-settings/overlap.gif
   :alt: overlap
   :width: 100%
   :align: center

SPEED MIX
~~~~~~~~~

Доступен по смыслу режима ``MIX``:

* ``0%`` соответствует TIME;
* ``100%`` соответствует LENGTH;
* промежуточные значения смешивают две шкалы.

TRIM BOUNCE MODE
~~~~~~~~~~~~~~~~

Автоматически превращает один параметр Grow в цикл роста и сжатия.
При любом режиме, кроме ``NO AUTO BOUNCE``, ручной ``TRIM`` отключён.

Названия вариантов напрямую описывают первую и вторую половины цикла:
``SHRINK OUT / GROW IN``, ``SHRINK IN / GROW OUT``,
``GROW IN / SHRINK IN``, ``GROW IN / SHRINK OUT``,
``GROW OUT / SHRINK IN`` и ``GROW OUT / SHRINK OUT``.

.. image:: /_static/gifs/speed-settings/trim-bounce.gif
   :alt: trim bounce
   :width: 100%
   :align: center

EXTRA
-----

SNAP EXTRAPOLATED
   Показывается только для ``OPEN EXTRAPOLATED`` при включённой Symmetry.
   Привязывает экстраполированную границу к расчётному краю.

SPEED MODE
   Показывается только для ``OPEN FAKE`` при включённой Symmetry.
   ``MOMENTAL`` использует виртуальную коррекцию скорости крайних частей,
   ``DEFAULT`` оставляет обычный ход.

BORDER CORRECTION
   Показывается только для ``OPEN FAKE``. В режиме ``ON`` применяется
   специальная коррекция крайних матриц и масштаба.

