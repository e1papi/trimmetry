"""Build the English gettext catalogs from the Russian Sphinx source.

Run the gettext builder first:
    python -m sphinx -b gettext docs/source docs/_build/gettext
Then run this script from the repository root.
"""

from pathlib import Path
import re

from babel.messages.pofile import read_po, write_po


TRANSLATIONS = {
    # concepts.rst
    "Как устроена анимация": "How the animation works",
    "Диапазон Grow–Trim": "Grow–Trim range",
    "``GROW`` задаёт конец видимого интервала, а ``TRIM`` — его начало. При обычной работе видимая часть находится между этими двумя значениями.": "``GROW`` sets the end of the visible interval, while ``TRIM`` sets its beginning. During normal operation, the visible portion lies between these two values.",
    "Примеры:": "Examples:",
    "Результат": "Result",
    "Полный диапазон.": "The full range.",
    "Первая половина роста.": "The first half of the growth.",
    "Видима средняя часть диапазона.": "The middle portion of the range is visible.",
    "Пустой диапазон.": "An empty range.",
    "``INVERT_TRIM`` оставляет область снаружи выбранного интервала. Поэтому результат может состоять из двух раздельных цепочек.": "``INVERT_TRIM`` keeps the area outside the selected interval. The result may therefore consist of two separate chains.",
    "Глобальное и локальное время": "Global and local time",
    "Сначала глобальные значения Grow и Trim переводятся во время каждой группы сегментов. Затем внутри каждого сегмента выполняется геометрическая обрезка.": "First, the global Grow and Trim values are converted to the time range of each segment group. Geometric trimming is then performed within each segment.",
    "``SPEED_MOD`` управляет этим переводом:": "``SPEED_MOD`` controls this conversion:",
    "Каждая группа получает одинаковую долю времени независимо от длины.": "Each group receives the same share of time regardless of its length.",
    "Время пропорционально суммарной длине сегментов группы.": "Time is proportional to the total length of the segments in the group.",
    "Интерполяция между TIME и LENGTH. Доля задаётся ``SPEED_MIX``.": "Interpolates between TIME and LENGTH. ``SPEED_MIX`` sets the blend amount.",
    "``OVERLAP`` позволяет следующей группе начаться до завершения предыдущей.": "``OVERLAP`` lets the next group start before the previous one finishes.",
    "Anchor и Symmetry": "Anchor and Symmetry",
    "При ``SYMMETRY = ON`` Anchor находится внутри каждого сегмента, а рост может идти в обе стороны.": "With ``SYMMETRY = ON``, the Anchor lies within each segment and growth can proceed in both directions.",
    "При ``SYMMETRY = OFF`` используется однонаправленная обрезка. Для закрытых режимов алгоритм переходит к ``CLOSE``, для открытых — к ``OPEN``.": "With ``SYMMETRY = OFF``, one-way trimming is used. The algorithm switches to ``CLOSE`` for closed modes and to ``OPEN`` for open modes.",

    # index.rst
    "Начало работы": "Getting started",
    "Параметры": "Parameters",
    "Практика и справка": "Guides and reference",
    "**Trimmetry** — генератор Cinema 4D, который протягивает профиль вдоль многосегментного сплайна и позволяет анимировать появление, обрезку, масштаб и вращение полученной полигональной геометрии.": "**Trimmetry** is a Cinema 4D generator that sweeps a profile along a multi-segment spline and lets you animate the reveal, trimming, scale, and rotation of the resulting polygonal geometry.",
    "Плагин рассчитан не только на один сплайн: он умеет сортировать сегменты, объединять их в группы, назначать каждой группе точку старта и управлять очерёдностью анимации.": "The plugin is designed for more than a single spline: it can sort segments, combine them into groups, assign a starting point to each group, and control the animation order.",
    "Быстрый старт": "Quick start",
    "Создайте объект **Trimmetry**.": "Create a **Trimmetry** object.",
    "Поместите сплайн пути первым дочерним объектом.": "Place the path spline as the first child.",
    "Поместите сплайн профиля вторым дочерним объектом.": "Place the profile spline as the second child.",
    "Установите ``GROW = 100%`` и ``TRIM = 0%``.": "Set ``GROW = 100%`` and ``TRIM = 0%``.",
    "Выберите подходящий ``SPLINE_TYPE``.": "Choose an appropriate ``SPLINE_TYPE``.",
    "Порядок дочерних объектов имеет значение: сначала **Path**, затем **Profile**. Подробнее см. :doc:`quickstart`.": "The order of the child objects matters: **Path** first, then **Profile**. See :doc:`quickstart` for details.",

    # installation.rst
    "Установка": "Installation",
    "Совместимость": "Compatibility",
    "Эта документация подготовлена по сборке Trimmetry, установленной в **Cinema 4D 2024**. Совместимость с другими выпусками Cinema 4D зависит от Python API соответствующей версии.": "This documentation is based on a Trimmetry build installed in **Cinema 4D 2024**. Compatibility with other Cinema 4D releases depends on the Python API of the corresponding version.",
    "Установка плагина": "Installing the plugin",
    "Закройте Cinema 4D.": "Close Cinema 4D.",
    "Скопируйте папку ``Trimmetry`` целиком в папку ``plugins`` вашей установки Cinema 4D.": "Copy the entire ``Trimmetry`` folder into the ``plugins`` folder of your Cinema 4D installation.",
    "Убедитесь, что внутри находятся как минимум:": "Make sure it contains at least:",
    "Запустите Cinema 4D.": "Start Cinema 4D.",
    "Найдите **Trimmetry** в списке генераторов или через поиск команд.": "Find **Trimmetry** in the generator list or through command search.",
    "Пример пути для Cinema 4D 2024:": "Example path for Cinema 4D 2024:",
    "Если плагин не появился": "If the plugin does not appear",
    "Проверьте:": "Check that:",
    "скопирована ли вся папка ``res``;": "the entire ``res`` folder was copied;",
    "не оказался ли файл в двойной вложенности ``Trimmetry/Trimmetry/Trimmetry.pyp``;": "the file is not nested as ``Trimmetry/Trimmetry/Trimmetry.pyp``;",
    "соответствует ли сборка версии Cinema 4D;": "the build matches your Cinema 4D version;",
    "есть ли сообщения Python в консоли Cinema 4D.": "the Cinema 4D console does not show Python errors.",

    # introduction.rst
    "Введение": "Introduction",
    "Что делает Trimmetry": "What Trimmetry does",
    "Trimmetry получает два сплайна:": "Trimmetry takes two splines:",
    "**Path** задаёт траекторию и набор сегментов;": "**Path** defines the trajectory and the set of segments;",
    "**Profile** задаёт поперечное сечение.": "**Profile** defines the cross-section.",
    "Для каждого сегмента Path плагин строит последовательность матриц, переносит по ним точки Profile и соединяет соседние кольца полигонами. После этого применяются обрезка, деформация, UV-развёртка и Phong.": "For each Path segment, the plugin builds a sequence of matrices, transforms the Profile points with them, and connects adjacent rings with polygons. Trimming, deformation, UV mapping, and Phong shading are then applied.",
    "В отличие от стандартного Sweep, Trimmetry ориентирован на управляемое появление большого количества сегментов:": "Unlike the standard Sweep, Trimmetry is designed for controlled reveals across many segments:",
    "``GROW`` раскрывает геометрию;": "``GROW`` reveals the geometry;",
    "``TRIM`` срезает начало видимого диапазона;": "``TRIM`` cuts away the beginning of the visible range;",
    "``SPEED_MOD`` распределяет анимацию по времени или длине;": "``SPEED_MOD`` distributes the animation by time or length;",
    "``OVERLAP`` задаёт перекрытие соседних групп;": "``OVERLAP`` sets the overlap between adjacent groups;",
    "**Segment Sort** определяет порядок групп;": "**Segment Sort** determines the group order;",
    "**Anchor Sort** определяет точку, от которой раскрывается каждый сегмент.": "**Anchor Sort** determines the point from which each segment is revealed.",
    "Что создаётся на выходе": "Output",
    "Результатом работы является полигональный объект. Плагин также создаёт:": "The result is a polygon object. The plugin also creates:",
    "UVW-тег с координатами вдоль профиля и пути;": "a UVW tag with coordinates along the profile and path;",
    "Phong-тег с настраиваемым ограничением угла;": "a Phong tag with a configurable angle limit;",
    "топологически замкнутый шов при полном росте закрытого пути, когда выбран совместимый режим.": "a topologically closed seam at full growth of a closed path when a compatible mode is selected.",

    # quickstart.rst
    "Минимальная сцена": "Minimal scene",
    "Создайте сплайн, который будет траекторией.": "Create a spline to use as the path.",
    "Создайте небольшой Circle, Rectangle или собственный сплайн профиля.": "Create a small Circle, Rectangle, or a custom profile spline.",
    "Перетащите Path под Trimmetry первым дочерним объектом.": "Drag Path under Trimmetry as the first child.",
    "Перетащите Profile туда же вторым дочерним объектом.": "Drag Profile there as the second child.",
    "Иерархия должна выглядеть так:": "The hierarchy should look like this:",
    "В исследованной сборке генератор читает первый и второй дочерние объекты напрямую. Поля ``PATH`` и ``PROFILE`` видны в интерфейсе, однако для надёжной работы используйте именно иерархию выше.": "In the tested build, the generator reads the first and second child objects directly. The ``PATH`` and ``PROFILE`` fields are visible in the interface, but use the hierarchy above for reliable operation.",
    "Стартовые настройки": "Initial settings",
    "Для первой проверки используйте:": "For your first test, use:",
    "Параметр": "Parameter",
    "Значение": "Value",
    "Вся доступная геометрия видима.": "All available geometry is visible.",
    "Начало диапазона не срезано.": "The beginning of the range is not trimmed.",
    "Рост идёт от Anchor в обе стороны.": "Growth proceeds from the Anchor in both directions.",
    "Удобный режим для первого открытого пути.": "A convenient mode for your first open path.",
    "Все группы получают равное время.": "All groups receive equal time.",
    "Первая анимация": "First animation",
    "На нулевом кадре установите ``GROW = 0%`` и создайте ключ.": "At frame zero, set ``GROW = 0%`` and create a keyframe.",
    "На последнем кадре установите ``GROW = 100%`` и создайте ключ.": "At the last frame, set ``GROW = 100%`` and create a keyframe.",
    "Если сегментов несколько, настройте ``OVERLAP``.": "If there are multiple segments, adjust ``OVERLAP``.",
    "При необходимости измените их порядок в :doc:`settings/segment-sort`.": "If necessary, change their order in :doc:`settings/segment-sort`.",
    "Настройте точку раскрытия в :doc:`settings/anchor-sort`.": "Set the reveal point in :doc:`settings/anchor-sort`.",
    "Path и Profile": "Path and Profile",
    "Может содержать несколько сегментов. Количество точек каждого сегмента определяет плотность колец и, следовательно, детализацию результата.": "May contain multiple segments. The number of points in each segment determines the ring density and therefore the level of detail in the result.",
    "Должен содержать минимум две точки. Закрытый Profile создаёт замкнутое поперечное сечение, открытый — ленту.": "Must contain at least two points. A closed Profile creates a closed cross-section; an open Profile creates a strip.",

    # recipes.rst
    "Практические рецепты": "Practical recipes",
    "Последовательное появление сегментов": "Sequential segment reveal",
    "Используйте:": "Use:",
    "Сегменты будут появляться в исходном порядке и без перекрытия.": "Segments will appear in their original order with no overlap.",
    "Появление по длине": "Reveal by length",
    "Установите ``SPEED_MOD = LENGTH``. Длинные группы получат больше времени, а визуальная скорость движения границы станет равномернее.": "Set ``SPEED_MOD = LENGTH``. Longer groups receive more time, making the visible boundary move at a more uniform speed.",
    "Плавная передача между сегментами": "Smooth transitions between segments",
    "Увеличьте ``OVERLAP``. Начните с ``10–20%`` и подбирайте значение по количеству групп и желаемому ритму.": "Increase ``OVERLAP``. Start with ``10–20%`` and adjust it for the number of groups and the desired rhythm.",
    "Рост от центра наружу": "Growth from the center outward",
    "Для радиального набора попробуйте ``ANCHOR_MODE = CIRCLE``.": "For a radial arrangement, try ``ANCHOR_MODE = CIRCLE``.",
    "Зеркальная последовательность": "Mirrored sequence",
    "``ID_OFFSET`` позволяет повернуть начальную точку последовательности.": "``ID_OFFSET`` lets you rotate the starting point of the sequence.",
    "Бегущая видимая полоса": "Moving visible strip",
    "Анимируйте Grow и Trim с одинаковым интервалом:": "Animate Grow and Trim with the same interval:",
    "Для циклического движения попробуйте подходящий ``TRIM_BOUNCE_MODE``.": "For cyclic movement, try an appropriate ``TRIM_BOUNCE_MODE``.",
    "Скручивание при появлении": "Twisting during the reveal",
    "Дополнительно задайте Function Curve для ускорения вращения к концу.": "Optionally, use a Function Curve to accelerate the rotation toward the end.",
    "Объединение близких сегментов": "Merging nearby segments",
    "Включите ``MERGE PAIR``.": "Enable ``MERGE PAIR``.",
    "Выберите ``SEARCH METHOD = REAL``.": "Select ``SEARCH METHOD = REAL``.",
    "Установите небольшой ``SEARCH RADIUS REAL``.": "Set a small ``SEARCH RADIUS REAL``.",
    "Ограничьте ``MAX NEIG``, чтобы не получить одну большую группу.": "Limit ``MAX NEIG`` to avoid producing a single large group.",

    # parameter-index.rst
    "Указатель параметров": "Parameter index",
    "Значения по умолчанию": "Default values",
    "По умолчанию": "Default",
    "Раздел": "Section",
    "Динамические параметры": "Context-dependent parameters",
    "Некоторые элементы появляются только в подходящем контексте:": "Some controls only appear in the relevant context:",
    "``SPEED MODE`` и ``BORDER CORRECTION`` — OPEN FAKE + Symmetry;": "``SPEED MODE`` and ``BORDER CORRECTION`` — OPEN FAKE + Symmetry;",
    "``INVERT DIR`` — при включённом Fix Seg Dir;": "``INVERT DIR`` — when Fix Seg Dir is enabled;",
    "параметры Pairs — при включённом Merge Pair;": "Pairs parameters — when Merge Pair is enabled;",
    "``REF OBJECT`` — Distance to Object или Splinora;": "``REF OBJECT`` — Distance to Object or Splinora;",
    "настройки Circle — при Anchor Mode = Circle.": "Circle settings — when Anchor Mode = Circle.",

    # troubleshooting.rst
    "Решение проблем": "Troubleshooting",
    "Trimmetry ничего не создаёт": "Trimmetry creates nothing",
    "Path — первый дочерний объект Trimmetry;": "Path is the first child of Trimmetry;",
    "Profile — второй дочерний объект;": "Profile is the second child;",
    "оба объекта можно преобразовать в сплайн;": "both objects can be converted to splines;",
    "Profile содержит минимум две точки;": "Profile contains at least two points;",
    "Path имеет ненулевую длину;": "Path has a non-zero length;",
    "``GROW`` больше ``TRIM`` при выключенном Invert Trim.": "``GROW`` is greater than ``TRIM`` when Invert Trim is disabled.",
    "Поля PATH и PROFILE заполнены, но результата нет": "PATH and PROFILE are set, but there is no result",
    "В текущей исследованной сборке генератор получает входы через дочернюю иерархию. Используйте:": "In the tested build, the generator receives its inputs through the child hierarchy. Use:",
    "Сегменты растут в разные стороны": "Segments grow in different directions",
    "Включите ``FIX SEG DIR``.": "Enable ``FIX SEG DIR``.",
    "Если весь результат развернулся противоположно ожидаемому, включите ``INVERT DIR``.": "If the entire result is oriented opposite to what you expect, enable ``INVERT DIR``.",
    "После этого проверьте ``ANCHOR SORT MODE`` и ``DIRECTION``.": "Then check ``ANCHOR SORT MODE`` and ``DIRECTION``.",
    "Порядок сегментов выглядит случайным": "The segment order looks random",
    "Для диагностики установите:": "For diagnostics, set:",
    "Затем включайте настройки по одной.": "Then enable the settings one at a time.",
    "Слишком много сегментов объединилось": "Too many segments were merged",
    "Уменьшите ``SEARCH RADIUS LOCAL/REAL`` и ``MAX NEIG``. Помните, что пересекающиеся пары транзитивно сливаются: пары ``0+1`` и ``1+2`` создают общую группу из трёх сегментов.": "Reduce ``SEARCH RADIUS LOCAL/REAL`` and ``MAX NEIG``. Remember that overlapping pairs merge transitively: the pairs ``0+1`` and ``1+2`` create a single group of three segments.",
    "Текстура прыгает при Grow": "The texture jumps during Grow",
    "``UV MODE = LOCAL`` растягивает всю текстуру по текущей видимой части;": "``UV MODE = LOCAL`` stretches the entire texture over the currently visible portion;",
    "``UV MODE = GLOBAL`` сохраняет соответствие общему прогрессу.": "``UV MODE = GLOBAL`` preserves alignment with the overall progress.",
    "Для анимируемого Grow обычно стабильнее GLOBAL. Если направление меняется из-за Trim или Bounce, попробуйте ``UV INVERT = AUTO``.": "GLOBAL is usually more stable for an animated Grow. If the direction changes because of Trim or Bounce, try ``UV INVERT = AUTO``.",
    "На закрытом пути виден шов": "A seam is visible on a closed path",
    "Убедитесь, что:": "Make sure that:",
    "Path действительно закрыт;": "Path is actually closed;",
    "используется закрытый Spline Type;": "a closed Spline Type is used;",
    "``GROW = 100%`` и ``TRIM = 0%``;": "``GROW = 100%`` and ``TRIM = 0%``;",
    "``INVERT TRIM = OFF``;": "``INVERT TRIM = OFF``;",
    "Profile имеет согласованное направление точек.": "Profile has a consistent point direction.",
    "Рывки или заломы профиля": "Profile jitter or kinks",
    "Увеличьте детализацию Path, включите ``FIX SEG DIR`` и сравните ``ROTATION MODE = NORMAL`` с ``MATRIX``. Для сглаживания отображения проверьте Phong Angle и Angle Limit.": "Increase Path detail, enable ``FIX SEG DIR``, and compare ``ROTATION MODE = NORMAL`` with ``MATRIX``. For smoother shading, check Phong Angle and Angle Limit.",
}

from settings_translations import SETTINGS_TRANSLATIONS

TRANSLATIONS.update(SETTINGS_TRANSLATIONS)
from literal_translations import LITERAL_TRANSLATIONS
TRANSLATIONS.update(LITERAL_TRANSLATIONS)


def main() -> None:
    root = Path(__file__).resolve().parents[2]
    pot_dir = root / "docs" / "_build" / "gettext"
    out_dir = root / "docs" / "source" / "locale" / "en" / "LC_MESSAGES"
    out_dir.mkdir(parents=True, exist_ok=True)

    missing: list[str] = []
    for pot_path in sorted(pot_dir.glob("*.pot")):
        with pot_path.open(encoding="utf-8") as stream:
            catalog = read_po(stream, locale="en")

        for message in catalog:
            if not message.id:
                continue
            source = message.id if isinstance(message.id, str) else message.id[0]
            if source in TRANSLATIONS:
                message.string = TRANSLATIONS[source]
            elif re.search(r"[А-Яа-яЁё]", source):
                missing.append(source)
            else:
                message.string = source

        catalog.header_comment = (
            "# English translations for the Trimmetry documentation.\n"
            "# Generated from the Russian source catalog."
        )
        catalog.fuzzy = False
        catalog.revision_date = "2026-07-27 00:00+0300"
        catalog.last_translator = "e1papi"
        catalog.language_team = "English"
        po_path = out_dir / f"{pot_path.stem}.po"
        with po_path.open("wb") as stream:
            write_po(stream, catalog, width=0, omit_header=False)
        po_path.write_bytes(po_path.read_bytes().rstrip() + b"\n")

    if missing:
        unique = list(dict.fromkeys(missing))
        raise SystemExit(
            f"Missing {len(unique)} translations:\n"
            + "\n".join(f"- {text}" for text in unique)
        )

    print(f"Wrote English catalogs to {out_dir}")


if __name__ == "__main__":
    main()
