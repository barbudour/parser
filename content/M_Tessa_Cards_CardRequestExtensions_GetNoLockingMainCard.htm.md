# CardRequestExtensions.GetNoLockingMainCard(CardRequestBase) - метод
Возвращает признак того, что не следует выполнять блокировку основной карточки
при создании или изменении сателлита.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool GetNoLockingMainCard(
    	this CardRequestBase request
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function GetNoLockingMainCard ( 
    	request As CardRequestBase
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    static bool GetNoLockingMainCard(
    	CardRequestBase^ request
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member GetNoLockingMainCard : 
            request : CardRequestBase -> bool 
#### Параметры
request [CardRequestBase](T_Tessa_Cards_CardRequestBase.htm)
     Запрос на загрузку или изменение карточки-сателлита, для которого требуется получить признак того, что не следует выполнять блокировку основной карточки при создании или изменении сателлита. 
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
Признак того, что не следует выполнять блокировку основной карточки при
создании или изменении сателлита.
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
[GetNoLockingMainCard -
перегрузка](Overload_Tessa_Cards_CardRequestExtensions_GetNoLockingMainCard.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
