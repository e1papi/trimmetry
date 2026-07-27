Направление, UV и Phong
=======================

SEGMENT DIRECTION
-----------------

FIX SEG DIR
~~~~~~~~~~~

Автоматически сравнивает направления сегментов и разворачивает те,
которые выбиваются из общей ориентации.

.. image:: /_static/gifs/additional-settings/additional-settings-seg-dir.gif
   :alt: seg-dir
   :width: 100%
   :align: center

UV
--

UV MODE
~~~~~~~

LOCAL и GLOBAL работают аналогично режимам Scale/Rotation: либо нормализуют значения UV по видимой цепочке, либо привязывают его к общему прогрессу Grow.

UV INVERT
~~~~~~~~~

OFF
   Сохраняет вычисленное направление V.

ON
   Инвертирует вычисленное направление.

AUTO
   Инвертирует V автоматически, когда значение Trim становится больше Grow.

.. image:: /_static/gifs/additional-settings/additional-settings-uv.gif
   :alt: uv
   :width: 100%
   :align: center

PHONG
-----

ANGLE LIMIT
   Включает ограничение сглаживания по углу.

PHONG ANGLE
   Максимальный угол сглаживания. Значение по умолчанию — ``60°``.

USE EDGE BREAKS
   Разрешает Phong-тегу учитывать вручную разорванные рёбра.

