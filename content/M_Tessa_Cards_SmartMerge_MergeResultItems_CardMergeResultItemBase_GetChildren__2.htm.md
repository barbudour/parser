# CardMergeResultItemBase.GetChildren<TValue, TIdentifier> \- метод
Находит дочерние элементы для определенного элемента в lookUp, где ключем
являются родительские идентификаторы
## __Definition
 **Пространство имён:**
[Tessa.Cards.SmartMerge.MergeResultItems](N_Tessa_Cards_SmartMerge_MergeResultItems.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected static IEnumerable<TValue> GetChildren<TValue, TIdentifier>(
    	ILookup<TIdentifier, TValue> itemsLookupByParentID,
    	TIdentifier elementID,
    	Func<TValue, TIdentifier> getRowID
    )
    where TIdentifier : struct, new()
VB __Копировать
     Protected Shared Function GetChildren(Of TValue, TIdentifier As {Structure, New}) ( 
    	itemsLookupByParentID As ILookup(Of TIdentifier, TValue),
    	elementID As TIdentifier,
    	getRowID As Func(Of TValue, TIdentifier)
    ) As IEnumerable(Of TValue)
C++ __Копировать
     protected:
    generic<typename TValue, typename TIdentifier>
    where TIdentifier : value class, gcnew()
    static IEnumerable<TValue>^ GetChildren(
    	ILookup<TIdentifier, TValue>^ itemsLookupByParentID, 
    	TIdentifier elementID, 
    	Func<TValue, TIdentifier>^ getRowID
    )
F# __Копировать
     static member GetChildren : 
            itemsLookupByParentID : ILookup<'TIdentifier, 'TValue> * 
            elementID : 'TIdentifier * 
            getRowID : Func<'TValue, 'TIdentifier> -> IEnumerable<'TValue>  when 'TIdentifier : struct, new()
#### Параметры
itemsLookupByParentID
[ILookup](https://learn.microsoft.com/dotnet/api/system.linq.ilookup-2)<TIdentifier,
TValue>
elementID TIdentifier
    Идентификатор элемента для которого происходит поиск дочерних
getRowID [Func](https://learn.microsoft.com/dotnet/api/system.func-2)<TValue,
TIdentifier>
    Функция, позволяющая получать идентификаторы элементов, содержащихся в lookUp
#### Параметры типа
TValue
    Тип элементов в lookUp
TIdentifier
    Тип идентификатора
#### Возвращаемое значение
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<TValue>  
##  __См. также
#### Ссылки
[CardMergeResultItemBase -
](T_Tessa_Cards_SmartMerge_MergeResultItems_CardMergeResultItemBase.htm)
[Tessa.Cards.SmartMerge.MergeResultItems - пространство
имён](N_Tessa_Cards_SmartMerge_MergeResultItems.htm)
