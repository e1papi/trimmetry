Anchor Sort
===========

Anchor Sort вычисляет стартовую позицию внутри каждого сегмента. Раздел
особенно важен при ``SYMMETRY = ON``.

ANCHOR MODE
-----------

BASE
   Начало сегмента с учётом Direction и Anchor Offset.

REVERSE
   Противоположный конец сегмента.

AXIS
   Выбирает Anchor по экстремуму вдоль ``AXIS``.

.. image:: /_static/gifs/anchors-sort/anchor-sort-axis.gif
   :alt: anchor-axis-sort
   :width: 100%
   :align: center

   MIN/MAX
      Выбирает минимальный или максимальный экстремум в режиме ``AXIS``.

AXIS CENTRED
   Размещает Anchor относительно общей центральной плоскости выбранной оси,
   создавая симметричное раскрытие набора сегментов.

.. image:: /_static/gifs/anchors-sort/anchor-sort-axis-center.gif
   :alt: anchor-axis-center-sort
   :width: 100%
   :align: center

CENTER
   Ищет положение относительно общего центра набора. Тип центра сегмента
   задаётся ``SEGMENT CENTER``.

.. image:: /_static/gifs/anchors-sort/anchor-sort-center.gif
   :alt: anchor-center-sort
   :width: 100%
   :align: center

DISTANCE TO OBJECT
   Находит Anchor относительно ``REF OBJECT``. Точный метод выбирается
   параметром ``DISTANCE MODE``.

.. image:: /_static/gifs/anchors-sort/anchor-sort-ref-obj.gif
   :alt: anchor-ref-sort
   :width: 100%
   :align: center

   DISTANCE MODE
      PROJECTION
         Проецирует позицию reference object на геометрическое направление
         сегмента.
   
      SAMPLING
         Семплирует кривую и ищет подходящую точку. Точность задаёт
         ``SAMPLE COUNT``.
   
      MATRIX
         Выбирает ближайшую или дальнюю из уже построенных матриц сегмента.

CIRCLE
   Вычисляет радиальное направление от общего центра и выбирает Anchor
   относительно круговой раскладки.

.. image:: /_static/gifs/anchors-sort/anchor-sort-circle.gif
   :alt: anchor-circle-sort
   :width: 100%
   :align: center

   CIRCLE MODE
      ``AUTO`` определяет рабочую плоскость большинством направлений сегментов.
      ``MANUAL`` открывает параметр ``CORRECTIONAL PLANE``.

   CORRECTIONAL PLANE
      Ручной выбор XY, YZ или XZ для режима ``CIRCLE``.
   
   FIX CIRCLE
      Переключает дополнительную коррекцию радиальной ориентации.

SPLINORA
   Использует ``REF OBJECT`` как пользовательскую позицию разреза.
   Может смешивать специальный разрез с обычным закрытым режимом через
   ``MIX CLOSED``.

.. image:: /_static/gifs/anchors-sort/anchor-sort-axis-splinora-1.gif
   :alt: anchor-splinora-sort-1
   :width: 100%
   :align: center

.. image:: /_static/gifs/anchors-sort/anchor-sort-axis-splinora-2.gif
   :alt: anchor-splinora-sort-2
   :width: 100%
   :align: center

   MIX CLOSED
      Для сегментов с валидным пользовательским
      разрезом применяется специальный двусторонний алгоритм, для остальных —
      обычный закрытый fallback.

PROPORTIONAL
------------

При ``ON`` левая и правая части получают коэффициенты, рассчитанные по
доступной длине вокруг Anchor. Это помогает сторонам завершать рост
согласованно. При ``OFF`` используется равное деление ``0.5 / 0.5``.

ANCHOR SORT MODE
----------------

BASE
   Одинаковое базовое направление.

HALF
   Меняет направление для второй половины списка сегментов.

MOD
   Чередует направление по индексу сегмента.

MIRROR
   Использует зеркальный шаблон направления для симметричных наборов.

AXIS и DIRECTION
----------------

``AXIS`` выбирает X, Y или Z для осевых и центральных вычислений.
``DIRECTION`` меняет выбранную сторону или ближайшую/дальнюю интерпретацию
в режимах, где она применима.

ADVANCED
--------

CORRECTIONAL AXIS
   Вторая ось, используемая для разрешения неоднозначной ориентации.

SEGMENT CENTER
   ``BBOX`` использует центр bounding box сегмента, ``GEO`` — среднее
   положение его выборок.

ANCHOR OFFSET
   Дополнительный дискретный выбор/сдвиг внутри режимов Anchor. Не путать
   с глобальным ``MAIN SETTINGS → ANCHOR OFFSET``.
