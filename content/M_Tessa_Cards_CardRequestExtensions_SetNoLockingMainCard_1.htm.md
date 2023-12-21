# CardRequestExtensions.SetNoLockingMainCard(CardStoreRequest, Boolean) -
метод
Устанавливает признак того, что не следует выполнять блокировку основной
карточки при создании или изменении сателлита.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetNoLockingMainCard(
    	this CardStoreRequest request,
    	bool value
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetNoLockingMainCard ( 
    	request As CardStoreRequest,
    	value As Boolean
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetNoLockingMainCard(
    	CardStoreRequest^ request, 
    	bool value
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetNoLockingMainCard : 
            request : CardStoreRequest * 
            value : bool -> unit 
#### Параметры
request [CardStoreRequest](T_Tessa_Cards_CardStoreRequest.htm)
     Запрос на загрузку или изменение карточки-сателлита, для которого требуется установить признак того, что не следует выполнять блокировку основной карточки при создании или изменении сателлита. 
value [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
     Признак того, что не следует выполнять блокировку основной карточки при создании или изменении сателлита. 
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [CardStoreRequest](T_Tessa_Cards_CardStoreRequest.htm). При
вызове метода для экземпляра следует опускать первый параметр. Дополнительные
сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardRequestExtensions - ](T_Tessa_Cards_CardRequestExtensions.htm)
[SetNoLockingMainCard -
перегрузка](Overload_Tessa_Cards_CardRequestExtensions_SetNoLockingMainCard.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
