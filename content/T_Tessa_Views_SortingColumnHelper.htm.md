# SortingColumnHelper - класс
Вспомогательные методы для работы с установленными значениями сортировок
столбцов [ISortingColumn](T_Tessa_Views_ISortingColumn.htm)
##  __Definition
 **Пространство имён:** [Tessa.Views](N_Tessa_Views.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class SortingColumnHelper
VB __Копировать
    <ExtensionAttribute>
    Public NotInheritable Class SortingColumnHelper
C++ __Копировать
    [ExtensionAttribute]
    public ref class SortingColumnHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    [<ExtensionAttribute>]
    type SortingColumnHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ SortingColumnHelper
##  __Методы
[TryGetColumn](M_Tessa_Views_SortingColumnHelper_TryGetColumn.htm)|
Осуществляет попытку получения столбца с псевдонимом columnAlias из коллекции
columnsCollection, если столбец с указанным псевдонимом отсутствует в
коллекции, то возвращает null. Поиск не учитывает регистр символов.  
---|---  
##  __См. также
#### Ссылки
[Tessa.Views - пространство имён](N_Tessa_Views.htm)
