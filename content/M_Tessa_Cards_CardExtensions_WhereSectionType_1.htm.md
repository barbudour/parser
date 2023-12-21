# CardExtensions.WhereSectionType(IEnumerable<SchemeTable>, CardSectionType) -
метод
Выполняет фильтрацию таблиц по типу секции в карточке.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static IEnumerable<SchemeTable> WhereSectionType(
    	this IEnumerable<SchemeTable> tables,
    	CardSectionType sectionType
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function WhereSectionType ( 
    	tables As IEnumerable(Of SchemeTable),
    	sectionType As CardSectionType
    ) As IEnumerable(Of SchemeTable)
C++ __Копировать
     public:
    [ExtensionAttribute]
    static IEnumerable<SchemeTable^>^ WhereSectionType(
    	IEnumerable<SchemeTable^>^ tables, 
    	CardSectionType sectionType
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member WhereSectionType : 
            tables : IEnumerable<SchemeTable> * 
            sectionType : CardSectionType -> IEnumerable<SchemeTable> 
#### Параметры
tables
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[SchemeTable](T_Tessa_Scheme_SchemeTable.htm)>
    Таблицы, для которых выполняется фильтрация.
sectionType [CardSectionType](T_Tessa_Cards_CardSectionType.htm)
    Тип секции карточки, для которого требуется выполнить фильтрацию таблиц.
#### Возвращаемое значение
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[SchemeTable](T_Tessa_Scheme_SchemeTable.htm)>  
Список таблиц, отфильтрованный по заданному типу экземпляра карточки.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[SchemeTable](T_Tessa_Scheme_SchemeTable.htm)>.
При вызове метода для экземпляра следует опускать первый параметр.
Дополнительные сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardExtensions - ](T_Tessa_Cards_CardExtensions.htm)
[WhereSectionType -
перегрузка](Overload_Tessa_Cards_CardExtensions_WhereSectionType.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
