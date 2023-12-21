# CardBlockSettings - класс
Настройки блоков карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class CardBlockSettings
VB __Копировать
     Public NotInheritable Class CardBlockSettings
C++ __Копировать
     public ref class CardBlockSettings abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type CardBlockSettings = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardBlockSettings
##  __Поля
[AlwaysMultipleColumn](F_Tessa_Cards_CardBlockSettings_AlwaysMultipleColumn.htm)|
Значение по умолчанию для признака того, что всегда выводится многоколоночный
блок.  
---|---  
[AlwaysMultipleColumnSetting](F_Tessa_Cards_CardBlockSettings_AlwaysMultipleColumnSetting.htm)|
Имя настройки, определяющей признак того, что всегда выводится многоколоночный
блок.  
[CaptionStyleSetting](F_Tessa_Cards_CardBlockSettings_CaptionStyleSetting.htm)|
Имя группы настроек, определяющих стиль заголовка.  
[CollapsedByDefault](F_Tessa_Cards_CardBlockSettings_CollapsedByDefault.htm)|
Значение по умолчанию для признака того, что блок свёрнут по умолчанию.  
[CollapsedByDefaultSetting](F_Tessa_Cards_CardBlockSettings_CollapsedByDefaultSetting.htm)|
Имя настройки, определяющей признак того, что блок свёрнут по умолчанию.  
[ColumnsCount](F_Tessa_Cards_CardBlockSettings_ColumnsCount.htm)| Значение по
умолчанию для количества колонок в блоке.  
[ColumnsCountSetting](F_Tessa_Cards_CardBlockSettings_ColumnsCountSetting.htm)|
Имя настройки, определяющей количество колонок в блоке.  
[ColumnSetting](F_Tessa_Cards_CardBlockSettings_ColumnSetting.htm)|  Столбец,
в котором выводится блок при рисовании в сетке. Индекс столбца отсчитывается
от нуля. Если отсутствует или отрицательный, то блок не выводится в сетке.  
[ColumnSpanSetting](F_Tessa_Cards_CardBlockSettings_ColumnSpanSetting.htm)|
Растяжение блока на несколько колонок. По умолчанию равно 1 \- блок выводится
шириной в одну колонку. Если отсутствует, равно нулю или отрицательное, то
блок не выводится в сетке.  
[DoNotCollapseWithTopBlock](F_Tessa_Cards_CardBlockSettings_DoNotCollapseWithTopBlock.htm)|
Значение по умолчанию для признака того, что блок не должен сворачиваться
вместе с верхним блоком, если у него скрыт заголовок.  
[DoNotCollapseWithTopBlockSetting](F_Tessa_Cards_CardBlockSettings_DoNotCollapseWithTopBlockSetting.htm)|
Имя настройки, определяющей признак того, что блок не должен сворачиваться
вместе с верхним блоком, если у него скрыт заголовок.  
[DoNotOptimizeBlock](F_Tessa_Cards_CardBlockSettings_DoNotOptimizeBlock.htm)|
Значение по умолчанию для признака того, что не следует оптимизировать
размещение единственного элемента управления в блоке. Укажите, если количество
элементов управления может динамически изменяться.  
[DoNotOptimizeBlockSetting](F_Tessa_Cards_CardBlockSettings_DoNotOptimizeBlockSetting.htm)|
Признак того, что не следует оптимизировать размещение единственного элемента
управления в блоке. Укажите, если количество элементов управления может
динамически изменяться.  
[HorizontalAlignmentSetting](F_Tessa_Cards_CardBlockSettings_HorizontalAlignmentSetting.htm)|
Выравнивание по горизонтали при выводе в узлах сетки (расположение блоков). По
умолчанию блок выравнивается по ширине.  
[HorizontalInterval](F_Tessa_Cards_CardBlockSettings_HorizontalInterval.htm)|
Значение по умолчанию для горизонтального интервала между элементами
управления, которые содержатся в блоке.  
[HorizontalIntervalSetting](F_Tessa_Cards_CardBlockSettings_HorizontalIntervalSetting.htm)|
Горизонтальный интервал между элементами управления, которые содержатся в
блоке.  
[IsHidden](F_Tessa_Cards_CardBlockSettings_IsHidden.htm)| Значение по
умолчанию для признака того, что форма или блок скрыты от пользователя.  
[IsHiddenSetting](F_Tessa_Cards_CardBlockSettings_IsHiddenSetting.htm)| Имя
настройки, определяющей признак того, что форма или блок скрыты от
пользователя.  
[LeftCaptions](F_Tessa_Cards_CardBlockSettings_LeftCaptions.htm)|  Значение по
умолчанию для признака того, что заголовки элементов управления выводятся
слева, а не сверху.  
[LeftCaptionsSetting](F_Tessa_Cards_CardBlockSettings_LeftCaptionsSetting.htm)|
Признак того, что заголовки элементов управления выводятся слева, а не сверху.  
[RightToLeftAlignment](F_Tessa_Cards_CardBlockSettings_RightToLeftAlignment.htm)|
Значение по умолчанию для признака того, что вывод элементов управления
выполняется справа налево, а не слева направо.  
[RightToLeftAlignmentSetting](F_Tessa_Cards_CardBlockSettings_RightToLeftAlignmentSetting.htm)|
Признак того, что вывод элементов управления выполняется справа налево, а не
слева направо.  
[RowSetting](F_Tessa_Cards_CardBlockSettings_RowSetting.htm)|  Строка, к
которой относится блок при рисовании в сетке. Индекс строки отсчитывается от
нуля. Если отсутствует или отрицательный, то блок не выводится в сетке.  
[RowSpanSetting](F_Tessa_Cards_CardBlockSettings_RowSpanSetting.htm)|
Растяжение блока на несколько строк. По умолчанию равно 1 \- блок выводится
высотой в одну строку. Если отсутствует, равно нулю или отрицательное, то блок
не выводится в сетке.  
[StretchVertically](F_Tessa_Cards_CardBlockSettings_StretchVertically.htm)|
Значение по умолчанию для признака того, что единственный элемент управления
растягивается по вертикали на максимальную доступную высоту.  
[StretchVerticallySetting](F_Tessa_Cards_CardBlockSettings_StretchVerticallySetting.htm)|
Признак того, что единственный элемент управления растягивается по вертикали
на максимальную доступную высоту. Рекомендуется для предпросмотра файлов и
других элементов управления, которые должны сразу занять максимум места.  
[TextColorSetting](F_Tessa_Cards_CardBlockSettings_TextColorSetting.htm)| Имя
настройки, определяющей цвет текста.  
[TextStyleSetting](F_Tessa_Cards_CardBlockSettings_TextStyleSetting.htm)| Имя
настройки, определяющей настройки визуального стиля текста.  
[VerticalAlignmentSetting](F_Tessa_Cards_CardBlockSettings_VerticalAlignmentSetting.htm)|
Выравнивание по вертикали при выводе в узлах сетки (расположение блоков). По
умолчанию блок выравнивается по высоте.  
[VerticalInterval](F_Tessa_Cards_CardBlockSettings_VerticalInterval.htm)|
Значение по умолчанию для вертикального интервала между элементами управления,
которые содержатся в блоке.  
[VerticalIntervalSetting](F_Tessa_Cards_CardBlockSettings_VerticalIntervalSetting.htm)|
Вертикальный интервал между элементами управления, которые содержатся в блоке.  
##  __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
