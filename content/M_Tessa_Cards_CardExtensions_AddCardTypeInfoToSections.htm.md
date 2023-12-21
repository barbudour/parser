# CardExtensions.AddCardTypeInfoToSections - метод
Добавляет информацию по типу карточки cardTypeID для колонок в метаинформации
sections, которые перечислены в schemeItem, если этого типа ещё нет в
соответствующих колонках. Возвращает признак того, что метод внёс изменения в
метаинформацию.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool AddCardTypeInfoToSections(
    	this CardTypeSchemeItem schemeItem,
    	CardMetadataSectionCollection sections,
    	Guid cardTypeID
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function AddCardTypeInfoToSections ( 
    	schemeItem As CardTypeSchemeItem,
    	sections As CardMetadataSectionCollection,
    	cardTypeID As Guid
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    static bool AddCardTypeInfoToSections(
    	CardTypeSchemeItem^ schemeItem, 
    	CardMetadataSectionCollection^ sections, 
    	Guid cardTypeID
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member AddCardTypeInfoToSections : 
            schemeItem : CardTypeSchemeItem * 
            sections : CardMetadataSectionCollection * 
            cardTypeID : Guid -> bool 
#### Параметры
schemeItem [CardTypeSchemeItem](T_Tessa_Cards_CardTypeSchemeItem.htm)
    Объект типа карточки, перечисляющий включённые в него колонки для одной из секций.
sections
[CardMetadataSectionCollection](T_Tessa_Cards_Metadata_CardMetadataSectionCollection.htm)
    Объекты секций в метаинформации, для колонок которых надо включить тип карточки.
cardTypeID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор типа карточки.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если метаинформация была изменена; false в противном случае.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [CardTypeSchemeItem](T_Tessa_Cards_CardTypeSchemeItem.htm). При
вызове метода для экземпляра следует опускать первый параметр. Дополнительные
сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardExtensions - ](T_Tessa_Cards_CardExtensions.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
