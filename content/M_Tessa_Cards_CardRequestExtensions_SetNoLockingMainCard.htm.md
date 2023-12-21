# CardRequestExtensions.SetNoLockingMainCard(CardRequestBase, Boolean) - метод
Устанавливает признак того, что не следует выполнять блокировку основной
карточки при создании или изменении сателлита.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetNoLockingMainCard(
    	this CardRequestBase request,
    	bool value
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetNoLockingMainCard ( 
    	request As CardRequestBase,
    	value As Boolean
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetNoLockingMainCard(
    	CardRequestBase^ request, 
    	bool value
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetNoLockingMainCard : 
            request : CardRequestBase * 
            value : bool -> unit 
#### Параметры
request [CardRequestBase](T_Tessa_Cards_CardRequestBase.htm)
     Запрос на загрузку или изменение карточки-сателлита, для которого требуется установить признак того, что не следует выполнять блокировку основной карточки при создании или изменении сателлита. 
value [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
     Признак того, что не следует выполнять блокировку основной карточки при создании или изменении сателлита. 
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [CardRequestBase](T_Tessa_Cards_CardRequestBase.htm). При вызове
метода для экземпляра следует опускать первый параметр. Дополнительные
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
