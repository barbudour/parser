# CardRequestExtensions.ShouldInvalidateCache - метод
Проверяет необходимость сброса кэша в контексте запроса
[InvalidateCache](F_Tessa_Cards_CardRequestTypes_InvalidateCache.htm).
Возвращает true, если был запрошен сброс указанного кэша или всех кэшей.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool ShouldInvalidateCache(
    	this ICardRequestExtensionContext context,
    	string cacheName
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function ShouldInvalidateCache ( 
    	context As ICardRequestExtensionContext,
    	cacheName As String
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    static bool ShouldInvalidateCache(
    	ICardRequestExtensionContext^ context, 
    	String^ cacheName
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member ShouldInvalidateCache : 
            context : ICardRequestExtensionContext * 
            cacheName : string -> bool 
#### Параметры
context
[ICardRequestExtensionContext](T_Tessa_Cards_Extensions_ICardRequestExtensionContext.htm)
    Контекст расширения на запрос сброса кэшей.
cacheName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя кэша, для которого проверяется необходимость сброса. Имя проверяется без учёта регистра символов.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
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
