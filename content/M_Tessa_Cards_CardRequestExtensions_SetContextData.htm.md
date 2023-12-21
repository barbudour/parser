# CardRequestExtensions.SetContextData - метод
Устанавливает данные в контексте цепочки расширений для заданного объекта-
отправителя sender. Данные существует в пределах цепочки расширений.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetContextData(
    	this ICardExtensionContext context,
    	Object sender,
    	Object data
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetContextData ( 
    	context As ICardExtensionContext,
    	sender As Object,
    	data As Object
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetContextData(
    	ICardExtensionContext^ context, 
    	Object^ sender, 
    	Object^ data
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetContextData : 
            context : ICardExtensionContext * 
            sender : Object * 
            data : Object -> unit 
#### Параметры
context
[ICardExtensionContext](T_Tessa_Cards_Extensions_ICardExtensionContext.htm)
    Контекст цепочки расширений. Не должен быть равен null.
sender [Object](https://learn.microsoft.com/dotnet/api/system.object)
     Объект-отправитель, например, объект текущего расширения this, его тип typeof(MyExtension) или любая строка-ключ "Unique string". Не может быть равен null. 
data [Object](https://learn.microsoft.com/dotnet/api/system.object)
     Устанавливаемые данные. Можно указать null, если данные требуется удалить из контекста. 
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
