# ExcelHelper - класс
Класс с вспомогательными методами для обработки Excel
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Cards](N_Tessa_Extensions_Default_Server_Cards.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public static class ExcelHelper
VB __Копировать
     Public NotInheritable Class ExcelHelper
C++ __Копировать
     public ref class ExcelHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type ExcelHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ExcelHelper
##  __Методы
[ColumnNameToInt](M_Tessa_Extensions_Default_Server_Cards_ExcelHelper_ColumnNameToInt.htm)|
Возвращает номер колонки по ее имени. Номер колонки отсчитывается от нуля.  
---|---  
[Compare](M_Tessa_Extensions_Default_Server_Cards_ExcelHelper_Compare.htm)|
Производит сравнение значений колонок Excel между собой  
[GetColumnIndex](M_Tessa_Extensions_Default_Server_Cards_ExcelHelper_GetColumnIndex.htm)|
Метод для получения имени колонки из ссылки ячейки  
[GetColumnName](M_Tessa_Extensions_Default_Server_Cards_ExcelHelper_GetColumnName.htm)|
Возвращает имя колонки в Excel по отсчитываемому от нуля индексу. Например: 0
= A, 1 = B, 2 = C, ..., 26 = AA, 27 = AB, ...  
[GetRowIndex](M_Tessa_Extensions_Default_Server_Cards_ExcelHelper_GetRowIndex.htm)|
Метод для получения номера строки из ссылки ячейки  
[NotSupported](M_Tessa_Extensions_Default_Server_Cards_ExcelHelper_NotSupported.htm)|
Производит действие при отсутствии доступа к операции  
## __Поля
[DoubleExcelFormat](F_Tessa_Extensions_Default_Server_Cards_ExcelHelper_DoubleExcelFormat.htm)|
Настройки форматирования при переводе значения double в строку, обозначающюю
дату/время в Excel  
---|---  
[EmptyPlaceholders](F_Tessa_Extensions_Default_Server_Cards_ExcelHelper_EmptyPlaceholders.htm)|
Пустой список плейсхолдеров  
[FirstColumn](F_Tessa_Extensions_Default_Server_Cards_ExcelHelper_FirstColumn.htm)|
Имя первой колонки в Excel  
[LastColumn](F_Tessa_Extensions_Default_Server_Cards_ExcelHelper_LastColumn.htm)|
Имя последней колонки в Excel  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Cards - пространство
имён](N_Tessa_Extensions_Default_Server_Cards.htm)
