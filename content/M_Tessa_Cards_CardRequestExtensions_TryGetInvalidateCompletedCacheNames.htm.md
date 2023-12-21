# CardRequestExtensions.TryGetInvalidateCompletedCacheNames - метод
Возвращает имена сбрасываемых кэшей в контексте запроса
[InvalidateCache](F_Tessa_Cards_CardRequestTypes_InvalidateCache.htm) или
null, если имена не заданы, в этом случае инвалидация выполняется для всех
кэшей.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static HashSet<string> TryGetInvalidateCompletedCacheNames(
    	this ICardRequestExtensionContext context
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryGetInvalidateCompletedCacheNames ( 
    	context As ICardRequestExtensionContext
    ) As HashSet(Of String)
C++ __Копировать
     public:
    [ExtensionAttribute]
    static HashSet<String^>^ TryGetInvalidateCompletedCacheNames(
    	ICardRequestExtensionContext^ context
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryGetInvalidateCompletedCacheNames : 
            context : ICardRequestExtensionContext -> HashSet<string> 
#### Параметры
context
[ICardRequestExtensionContext](T_Tessa_Cards_Extensions_ICardRequestExtensionContext.htm)
    Контекст расширения на запрос сброса кэшей.
#### Возвращаемое значение
[HashSet](https://learn.microsoft.com/dotnet/api/system.collections.generic.hashset-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>  
Имена сбрасываемых кэшей в запросе
[InvalidateCache](F_Tessa_Cards_CardRequestTypes_InvalidateCache.htm) или
null, если имена не заданы, в этом случае инвалидация выполняется для всех
кэшей.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[ICardRequestExtensionContext](T_Tessa_Cards_Extensions_ICardRequestExtensionContext.htm).
При вызове метода для экземпляра следует опускать первый параметр.
Дополнительные сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardRequestExtensions - ](T_Tessa_Cards_CardRequestExtensions.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
