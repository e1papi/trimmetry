Segment Sort
============

Segment Sort определяет порядок, в котором сегменты или группы (пары) сегментов будут обрабатываться.
Сортировка не меняет форму исходного Path — она меняет последовательность
анимации.

REINDEX SEGMENTS
----------------

SORT MODE
~~~~~~~~~

BASE
   Исходный порядок индексов сегментов.

REVERS
   Обратный порядок индексов.

X / Y / Z
   Сортировка по координате центра сегмента вдоль выбранной мировой оси.

.. image:: /_static/gifs/segment-sort/segment-axis.gif
   :alt: seg-axis-sort
   :width: 100%
   :align: center

CIRCLE
   Сортировка по полярному углу центра. ``CORRECTIONAL PLANE`` задаёт
   проекцию: XY, YZ или XZ.

.. image:: /_static/gifs/segment-sort/segment-circle.gif
   :alt: seg-circle-sort
   :width: 100%
   :align: center

OBJ
   Сортировка по расстоянию от центра сегмента до ``REF OBJ``.

.. image:: /_static/gifs/segment-sort/segment-ref-obj.gif
   :alt: seg-ref-obj-sort
   :width: 100%
   :align: center

MIRROR
   Берёт элементы с начала и конца ИСХОДНОГО списка попарно, создавая зеркальную
   последовательность. Т.е если изначальная последовательность сегментов имела кастомную индексацию,
   то данный режим может работать некорректно. 
   Ниже пример сортировки MIRROR при изначально корректной индексации

.. image:: /_static/gifs/segment-sort/segment-mirror.gif
   :alt: seg-mirror-sort
   :width: 100%
   :align: center

Пример того, как можно воспроизвести поведение режима MIRROR используя режим REF OBJ
.. image:: /_static/gifs/sort-mode/sort-mode-ref.gif
   :alt: seg-ref-sort_fix
   :width: 100%
   :align: center

INVERT
   Разворачивает итоговый список групп после основной сортировки.

REF OBJ
   Показывается для ``OBJ`` и служит точкой отсчёта расстояния.

CORRECTIONAL PLANE
   Показывается для ``CIRCLE`` и определяет плоскость расчёта угла.

ADVANCED SETTINGS
-----------------

GAP
   Объединяет каждые ``GAP + 1`` соседних групп в одну временную группу.
   Например, ``GAP = 1`` объединяет группы попарно.

.. image:: /_static/gifs/segment-sort/segment-gap.gif
   :alt: seg-gap
   :width: 100%
   :align: center

ID OFFSET
   Циклически сдвигает отсортированный список. Значения могут быть как положительные, так и отрицательные.

MIRROR DIR
   Меняет порядок левой и правой части каждой пары в режиме ``MIRROR``.
   (В основном используется когда кол-во групп четное и надо изменить порядок обработки последних групп).

.. image:: /_static/gifs/segment-sort/segment-mirror-dir.gif
   :alt: seg-mirror-dir
   :width: 100%
   :align: center

PAIRS
-----

MERGE PAIR
   Включает объединение близких или вручную перечисленных сегментов в
   общие группы до сортировки.

SEARCH METHOD
~~~~~~~~~~~~~

LOCAL
   Сравнивает расстояния между центрами в нормализованной шкале относительно
   максимальной дистанции между сегментами.

REAL
   Использует реальное расстояние сцены.

SEARCH RADIUS LOCAL / REAL
   Порог автоматического поиска для выбранного метода.

MAX NEIG
   Максимальное число ближайших соседей, добавляемых для каждого сегмента.

.. image:: /_static/gifs/segment-sort/segment-pair.gif
   :alt: seg-pair
   :width: 100%
   :align: center

ADD EXTRA и PAIR IDS
~~~~~~~~~~~~~~~~~~~~

Позволяют вручную дописать группы. Синтаксис:

.. code-block:: text

   0+5, 1+2, 6+7+8

Числа — нулевые индексы сегментов. Запятая разделяет группы, знак ``+``
объединяет индексы внутри группы. Пересекающиеся группы автоматически
сливаются: ``0+1, 1+2`` превращается в одну группу ``0+1+2``.

.. image:: /_static/gifs/segment-sort/segment-add-extra.gif
   :alt: seg-add-extra
   :width: 100%
   :align: center

