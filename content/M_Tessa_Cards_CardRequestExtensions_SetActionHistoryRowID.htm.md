# CardRequestExtensions.SetActionHistoryRowID - метод
Устанавливает идентификатор записи в историю действий, которая была записана в
процессе обработки запроса, или null, если требуется удалить предыдущий
идентификатор.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetActionHistoryRowID(
    	this ICardExtensionContext context,
    	Guid? actionHistoryRowID
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetActionHistoryRowID ( 
    	context As ICardExtensionContext,
    	actionHistoryRowID As Guid?
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetActionHistoryRowID(
    	ICardExtensionContext^ context, 
    	Nullable<Guid> actionHistoryRowID
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetActionHistoryRowID : 
            context : ICardExtensionContext * 
            actionHistoryRowID : Nullable<Guid> -> unit 
#### Параметры
context
[ICardExtensionContext](T_Tessa_Cards_Extensions_ICardExtensionContext.htm)
    Контекст обработки запроса.
actionHistoryRowID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
     Идентификатор записи в историю действий, которая была записана в процессе обработки запроса, или null, если требуется удалить предыдущий идентификатор. 
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[ICardExtensionContext](T_Tessa_Cards_Extensions_ICardExtensionContext.htm).
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
