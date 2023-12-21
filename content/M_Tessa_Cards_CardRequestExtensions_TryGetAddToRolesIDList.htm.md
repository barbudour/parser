# CardRequestExtensions.TryGetAddToRolesIDList - метод
Получает список идентификаторов ролей, в которые должен быть добавлен
создаваемый сотрудник, или null, аналогичный пустому списку.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static List<Guid> TryGetAddToRolesIDList(
    	this CardStoreRequest request
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryGetAddToRolesIDList ( 
    	request As CardStoreRequest
    ) As List(Of Guid)
C++ __Копировать
     public:
    [ExtensionAttribute]
    static List<Guid>^ TryGetAddToRolesIDList(
    	CardStoreRequest^ request
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryGetAddToRolesIDList : 
            request : CardStoreRequest -> List<Guid> 
#### Параметры
request [CardStoreRequest](T_Tessa_Cards_CardStoreRequest.htm)
    Запрос на создание (первое сохранение) карточки сотрудника.
#### Возвращаемое значение
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>  
Список идентификаторов ролей, в которые должен быть добавлен создаваемый
сотрудник, или null, аналогичный пустому списку.
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
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
