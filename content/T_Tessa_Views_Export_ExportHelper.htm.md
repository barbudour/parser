# ExportHelper - класс
Вспомогательные методы для экспорта
## __Definition
 **Пространство имён:** [Tessa.Views.Export](N_Tessa_Views_Export.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class ExportHelper
VB __Копировать
     Public NotInheritable Class ExportHelper
C++ __Копировать
     public ref class ExportHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type ExportHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ExportHelper
##  __Методы
[BuildColumnsInfo](M_Tessa_Views_Export_ExportHelper_BuildColumnsInfo.htm)|
Осуществляет построение списка описаний столбцов  
---|---  
[GetVisibleColumns](M_Tessa_Views_Export_ExportHelper_GetVisibleColumns.htm)|
Возвращает список псевдонимов столбцов доступных для экспорта  
[SplitByColon](M_Tessa_Views_Export_ExportHelper_SplitByColon.htm)|  Разбивает
входную строку на массив используя в качестве разделителя двоеточие  
[SplitByComma](M_Tessa_Views_Export_ExportHelper_SplitByComma.htm)|  Разбивает
входную строку параметров на массив используя в качестве разделителей запятую  
[SplitByCommaParams](M_Tessa_Views_Export_ExportHelper_SplitByCommaParams.htm)|
Возвращает словарь параметров разобранный из строки вида Alias, Value1 ...
[,ValueN]  
[SplitParams](M_Tessa_Views_Export_ExportHelper_SplitParams.htm)|  Возвращает
словарь параметров разобранный из строки вида Alias:Values ... [,
AliasN:ValueN]  
## __См. также
#### Ссылки
[Tessa.Views.Export - пространство имён](N_Tessa_Views_Export.htm)
