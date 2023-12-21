# CardRequestExtensions.ClearInvalidateCompletedCacheNames - метод
Очищает имена фактически сброшенных кэшей в контексте запроса
[InvalidateCache](F_Tessa_Cards_CardRequestTypes_InvalidateCache.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void ClearInvalidateCompletedCacheNames(
    	this ICardRequestExtensionContext context
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub ClearInvalidateCompletedCacheNames ( 
    	context As ICardRequestExtensionContext
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void ClearInvalidateCompletedCacheNames(
    	ICardRequestExtensionContext^ context
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member ClearInvalidateCompletedCacheNames : 
            context : ICardRequestExtensionContext -> unit 
#### Параметры
context
[ICardRequestExtensionContext](T_Tessa_Cards_Extensions_ICardRequestExtensionContext.htm)
    Контекст расширения на запрос сброса кэшей.
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
