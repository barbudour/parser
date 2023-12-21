# CardRequestExtensions.TryGetInvalidateCacheNames(CardRequest) - метод
Возвращает имена сбрасываемых кэшей в запросе
[InvalidateCache](F_Tessa_Cards_CardRequestTypes_InvalidateCache.htm) или
null, если имена не заданы, в этом случае инвалидация выполняется для всех
кэшей.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static List<string> TryGetInvalidateCacheNames(
    	this CardRequest request
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryGetInvalidateCacheNames ( 
    	request As CardRequest
    ) As List(Of String)
C++ __Копировать
     public:
    [ExtensionAttribute]
    static List<String^>^ TryGetInvalidateCacheNames(
    	CardRequest^ request
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryGetInvalidateCacheNames : 
            request : CardRequest -> List<string> 
#### Параметры
request [CardRequest](T_Tessa_Cards_CardRequest.htm)
    Запрос к сервису карточек.
#### Возвращаемое значение
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>  
Имена сбрасываемых кэшей в запросе
[InvalidateCache](F_Tessa_Cards_CardRequestTypes_InvalidateCache.htm) или
null, если имена не заданы, в этом случае инвалидация.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [CardRequest](T_Tessa_Cards_CardRequest.htm). При вызове метода
для экземпляра следует опускать первый параметр. Дополнительные сведения см. в
разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardRequestExtensions - ](T_Tessa_Cards_CardRequestExtensions.htm)
[TryGetInvalidateCacheNames -
перегрузка](Overload_Tessa_Cards_CardRequestExtensions_TryGetInvalidateCacheNames.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
