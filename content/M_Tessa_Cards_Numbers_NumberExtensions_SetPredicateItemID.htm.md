# NumberExtensions.SetPredicateItemID - метод
Устанавливает идентификатор записи в очереди действий
[NumberQueueItem](T_Tessa_Cards_Numbers_NumberQueueItem.htm), который будет
использоваться для предиката в текущей записи.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetPredicateItemID(
    	this NumberQueueItem item,
    	Guid? itemID
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetPredicateItemID ( 
    	item As NumberQueueItem,
    	itemID As Guid?
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetPredicateItemID(
    	NumberQueueItem^ item, 
    	Nullable<Guid> itemID
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetPredicateItemID : 
            item : NumberQueueItem * 
            itemID : Nullable<Guid> -> unit 
#### Параметры
item [NumberQueueItem](T_Tessa_Cards_Numbers_NumberQueueItem.htm)
     Запись, предикат которой использует идентификатор другой записи. Не может быть равна null. 
itemID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
    Идентификатор записи, который используется в предикате текущей записи.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [NumberQueueItem](T_Tessa_Cards_Numbers_NumberQueueItem.htm). При
вызове метода для экземпляра следует опускать первый параметр. Дополнительные
сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[NumberExtensions - ](T_Tessa_Cards_Numbers_NumberExtensions.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
