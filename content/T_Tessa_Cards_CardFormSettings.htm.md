# CardFormSettings - класс
Настройки формы карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class CardFormSettings
VB __Копировать
     Public NotInheritable Class CardFormSettings
C++ __Копировать
     public ref class CardFormSettings abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type CardFormSettings = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardFormSettings
##  __Поля
[BlocksHorizontalPadding](F_Tessa_Cards_CardFormSettings_BlocksHorizontalPadding.htm)|
Горизонтальный отступ по умолчанию между блоками, когда они в ячейках сетки.  
---|---  
[BlocksHorizontalPaddingSetting](F_Tessa_Cards_CardFormSettings_BlocksHorizontalPaddingSetting.htm)|
Название настройки для горизонтального отступа по умолчанию между блоками,
когда они в ячейках сетки.  
[BlocksVerticalPadding](F_Tessa_Cards_CardFormSettings_BlocksVerticalPadding.htm)|
Значение по умолчанию для вертикального интервала между блоками, которые
содержатся в форме.  
[BlocksVerticalPaddingSetting](F_Tessa_Cards_CardFormSettings_BlocksVerticalPaddingSetting.htm)|
Имя настройки, определяющей вертикальный интервал между блоками, которые
содержатся в форме.  
[ColumnsSetting](F_Tessa_Cards_CardFormSettings_ColumnsSetting.htm)|
Настройка с шириной столбцов, добавленных в форму сетку. Это массив
IList<object>, в котором для каждого элемента (столбца) указано null
(автоматическая ширина) или double (ширина в пропорции *).  
[FilePreviewIsDisabled](F_Tessa_Cards_CardFormSettings_FilePreviewIsDisabled.htm)|
Признак того, что область предпросмотра скрыта для этой вкладки и её нельзя
восстановить через меню для списка файлов.  
[FilePreviewIsDisabledSetting](F_Tessa_Cards_CardFormSettings_FilePreviewIsDisabledSetting.htm)|
Название настройки для признака того, что область предпросмотра скрыта для
этой вкладки и её нельзя восстановить через меню для списка файлов.  
[RowsSetting](F_Tessa_Cards_CardFormSettings_RowsSetting.htm)|  Настройка с
высотой строк, добавленных в форму-сетку. Это массив IList<object>, в котором
для каждого элемента (строки) указано null (автоматическая высота) или double
(высота в пропорции *).  
## __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
