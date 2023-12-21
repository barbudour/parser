# CardRequestExtensions.AddInvalidateCompletedCacheNames - метод
Добавляет имена фактически сброшенных кэшей в контексте запроса
[InvalidateCache](F_Tessa_Cards_CardRequestTypes_InvalidateCache.htm).
Значение null и пустой список идентичны. Пустой список означает, что сброс
кэшей не выполняется.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void AddInvalidateCompletedCacheNames(
    	this ICardRequestExtensionContext context,
    	params string[] cacheNames
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub AddInvalidateCompletedCacheNames ( 
    	context As ICardRequestExtensionContext,
    	ParamArray cacheNames As String()
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void AddInvalidateCompletedCacheNames(
    	ICardRequestExtensionContext^ context, 
    	... array<String^>^ cacheNames
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member AddInvalidateCompletedCacheNames : 
            context : ICardRequestExtensionContext * 
            cacheNames : string[] -> unit 
#### Параметры
context
[ICardRequestExtensionContext](T_Tessa_Cards_Extensions_ICardRequestExtensionContext.htm)
    Контекст расширения на запрос сброса кэшей.
cacheNames [String](https://learn.microsoft.com/dotnet/api/system.string)[]
     Имена кэшей, которые были сброшены. Значение null и пустой список идентичны. 
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
