Trimmetry
=========

.. image:: _static/LOGO.png
   :width: 420px
   :align: center
   :alt: Trimmetry

**Trimmetry** — генератор Cinema 4D, который протягивает профиль вдоль
многосегментного сплайна и позволяет анимировать появление, обрезку,
масштаб и вращение полученной полигональной геометрии.

Плагин рассчитан не только на один сплайн: он умеет сортировать сегменты,
объединять их в группы, назначать каждой группе точку старта и управлять
очерёдностью анимации.

Быстрый старт
-------------

#. Создайте объект **Trimmetry**.
#. Поместите сплайн пути первым дочерним объектом.
#. Поместите сплайн профиля вторым дочерним объектом.
#. Установите ``GROW = 100%`` и ``TRIM = 0%``.
#. Выберите подходящий ``SPLINE_TYPE``.

.. important::

   Порядок дочерних объектов имеет значение: сначала **Path**, затем
   **Profile**. Подробнее см. :doc:`quickstart`.

.. toctree::
   :maxdepth: 3
   :caption: Начало работы

   introduction
   installation
   quickstart
   concepts

.. toctree::
   :maxdepth: 3
   :caption: Параметры

   settings/main
   settings/deformation
   settings/output
   settings/segment-sort
   settings/anchor-sort

.. toctree::
   :maxdepth: 2
   :caption: Практика и справка

   recipes
   troubleshooting
   parameter-index

