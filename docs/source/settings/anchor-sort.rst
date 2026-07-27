Anchor Sort
===========

Anchor Sort вычисляет стартовую позицию внутри каждого сегмента.

ANCHOR MODE
-----------

BASE
   Начало сегмента с учётом Direction и Anchor Offset.

REVERSE
   Противоположный конец сегмента.

AXIS
   Выбирает Anchor по экстремуму вдоль ОСНОВНОГО ``AXIS``.

.. image:: /_static/gifs/anchors-sort/anchor-sort-axis.gif
   :alt: anchor-axis-sort
   :width: 100%
   :align: center

MIN/MAX
   Выбирает минимальный или максимальный экстремум по ! ``CORRECTIONAL AXIS`` !

AXIS CENTRED
   Размещает Anchor относительно общей центральной плоскости выбранной оси,
   создавая симметричное раскрытие набора сегментов.
   Грубо говоря, ищет экстремумы по ОСНОВНОМУ ``AXIS`` и, если их несколько,
   то выбирает их среднее значение по ``CORRECTIONAL AXIS``

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
   Переключает дополнительную коррекцию радиальной ориентации (в основном когда сегменты расположены радиально в 2d плоскости).


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
   Для сегментов пересекающихся с разрезом  ``REF OBJECT``
   применяется SPLINE_TYPE в режиме ``CLOSE_DUO``, а для остальных —
   обычный ``CLOSE``.

PROPORTIONAL
------------

При ``ON`` левая и правая части получают коэффициенты, рассчитанные по
доступной длине вокруг Anchor. Это помогает сторонам завершать рост
согласованно. При ``OFF`` используется равное деление ``0.5 / 0.5``.

ANCHOR SORT MODE
----------------

BASE
   Базовое направление.

HALF
   Меняет направление для второй половины списка сегментов.

.. image:: /_static/gifs/sort-mode/sort-mode-half.gif
   :alt: sort mode half
   :width: 100%
   :align: center

MOD
   Чередует направление по индексу сегмента. (т.е приницп как у формулы mod(id;2)).


.. note::
   ВАЖНО! Для ANCHOR_SORT_MODE ``BASE``, ``HALF`` и ``MOD`` используятся исходная индексация сегментов.
   Т.е пересортировка и группировка полученная в SEGMENT_SORT не учитывается. (В дальнейшем такая возожность будет добавлена).
   Чтобы воспроизвести поведение режима ``BASE`` и ``HALF`` при кастомной индексации можно использовать ANCHOR_SORT_MODE ``MIRROR``    (читать описание).

MIRROR
   ! Используется только в связке с ANCHOR MODE ``SPLINORA`` и подключенным ``REF OBJECT``.
   Использует зеркальный шаблон направления для симметричных наборов.
   Ниже пример воспроизведения поведениz режима сортировки СЕГМЕТОВ ``MIRROR`` и ANCHOR_SORT_MODE ``HALF``.

.. image:: /_static/gifs/sort-mode/sort-mode-ref.gif
   :alt: sort mode ref
   :width: 100%
   :align: center

AXIS и DIRECTION
----------------

``AXIS`` выбирает X, Y или Z для осевых и центральных вычислений.
``DIRECTION`` меняет выбранную сторону или ближайшую/дальнюю интерпретацию
в режимах, где она применима.

ADVANCED
--------

CORRECTIONAL AXIS
   Вторая ось, необходимая для построения корректной ориентации. (В частных случаях может совпадать с ОСНОВНЫМ ``AXIS``)

SEGMENT CENTER
   ``BBOX`` использует центр bounding box сегмента, ``GEO`` — среднее
   положение его выборок.

ANCHOR OFFSET
   Дополнительный дискретный выбор/сдвиг внутри режимов Anchor. Не путать
   с глобальным ``MAIN SETTINGS → ANCHOR OFFSET``.
