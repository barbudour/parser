# CardExtensions.AddDistinctFrom(ICollection<CardTypeSchemeItem>,
ICollection<CardTypeSchemeItem>) - метод
Добавляет элементы схемы в текущую коллекцию из заданной коллекции
schemeItems, если таких же элементов уже не было в текущей коллекции.
Возвращает признак того, что хотя бы одна секция или колонка была добавлена.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool AddDistinctFrom(
    	this ICollection<CardTypeSchemeItem> targetItems,
    	ICollection<CardTypeSchemeItem> schemeItems
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function AddDistinctFrom ( 
    	targetItems As ICollection(Of CardTypeSchemeItem),
    	schemeItems As ICollection(Of CardTypeSchemeItem)
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    static bool AddDistinctFrom(
    	ICollection<CardTypeSchemeItem^>^ targetItems, 
    	ICollection<CardTypeSchemeItem^>^ schemeItems
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member AddDistinctFrom : 
            targetItems : ICollection<CardTypeSchemeItem> * 
            schemeItems : ICollection<CardTypeSchemeItem> -> bool 
#### Параметры
targetItems
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[CardTypeSchemeItem](T_Tessa_Cards_CardTypeSchemeItem.htm)>
    Текущая коллекция, в которую добавляются элементы.
schemeItems
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[CardTypeSchemeItem](T_Tessa_Cards_CardTypeSchemeItem.htm)>
    Коллекция, элементы которой добавляются в текущую коллекцию.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если хотя бы один элемент был добавлен в текущую коллекцию; false в
противном случае.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[CardTypeSchemeItem](T_Tessa_Cards_CardTypeSchemeItem.htm)>.
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
[AddDistinctFrom -
перегрузка](Overload_Tessa_Cards_CardExtensions_AddDistinctFrom.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
