# CardExtensions.WhereInstanceType(IEnumerable<SchemeTable>,
Nullable<CardInstanceType>) - метод
Выполняет фильтрацию таблиц по признаку их возможной принадлежности карточке
заданного типа экземпляра.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static IEnumerable<SchemeTable> WhereInstanceType(
    	this IEnumerable<SchemeTable> tables,
    	CardInstanceType? instanceType
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function WhereInstanceType ( 
    	tables As IEnumerable(Of SchemeTable),
    	instanceType As CardInstanceType?
    ) As IEnumerable(Of SchemeTable)
C++ __Копировать
     public:
    [ExtensionAttribute]
    static IEnumerable<SchemeTable^>^ WhereInstanceType(
    	IEnumerable<SchemeTable^>^ tables, 
    	Nullable<CardInstanceType> instanceType
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member WhereInstanceType : 
            tables : IEnumerable<SchemeTable> * 
            instanceType : Nullable<CardInstanceType> -> IEnumerable<SchemeTable> 
#### Параметры
tables
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[SchemeTable](T_Tessa_Scheme_SchemeTable.htm)>
    Таблицы, для которых выполняется фильтрация.
instanceType
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[CardInstanceType](T_Tessa_Cards_CardInstanceType.htm)>
     Тип экземпляра карточки, для которого требуется выполнить фильтрацию таблиц, или null, если фильтрация не требуется. 
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
[WhereInstanceType -
перегрузка](Overload_Tessa_Cards_CardExtensions_WhereInstanceType.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
