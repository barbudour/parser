# CardRequestExtensions.SetInvalidateCacheNames(ICardRequestExtensionContext,
IEnumerable<String>) - метод
Устанавливает имена сбрасываемых кэшей в контексте запроса
[InvalidateCache](F_Tessa_Cards_CardRequestTypes_InvalidateCache.htm).
Значение null определяет, что выполняется сброс всех кэшей. Пустой список
означает, что сброс кэшей не выполняется.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetInvalidateCacheNames(
    	this ICardRequestExtensionContext context,
    	IEnumerable<string> cacheNames
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetInvalidateCacheNames ( 
    	context As ICardRequestExtensionContext,
    	cacheNames As IEnumerable(Of String)
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetInvalidateCacheNames(
    	ICardRequestExtensionContext^ context, 
    	IEnumerable<String^>^ cacheNames
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetInvalidateCacheNames : 
            context : ICardRequestExtensionContext * 
            cacheNames : IEnumerable<string> -> unit 
#### Параметры
context
[ICardRequestExtensionContext](T_Tessa_Cards_Extensions_ICardRequestExtensionContext.htm)
    Контекст расширения на запрос сброса кэшей.
cacheNames
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
     Имена кэшей, которые сбрасываются, или null, если ранее установленный ключ будет удалён из контекста. 
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
[SetInvalidateCacheNames -
перегрузка](Overload_Tessa_Cards_CardRequestExtensions_SetInvalidateCacheNames.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
