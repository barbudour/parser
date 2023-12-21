# CardRequestExtensions.SetCardToDelete - метод
Устанавливает карточку, для которой выполняется удаление с восстановлением,
окончательное удаление или восстановление, или null, если установленную
карточку требуется удалить.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetCardToDelete(
    	this ICardDeleteExtensionContext context,
    	Card card
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetCardToDelete ( 
    	context As ICardDeleteExtensionContext,
    	card As Card
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetCardToDelete(
    	ICardDeleteExtensionContext^ context, 
    	Card^ card
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetCardToDelete : 
            context : ICardDeleteExtensionContext * 
            card : Card -> unit 
#### Параметры
context
[ICardDeleteExtensionContext](T_Tessa_Cards_Extensions_ICardDeleteExtensionContext.htm)
    Контекст процесса удаления карточки Deleted.
card [Card](T_Tessa_Cards_Card.htm)
     Карточка, для которой выполняется окончательное удаление или восстановление, или null, если установленную карточку требуется удалить. 
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[ICardDeleteExtensionContext](T_Tessa_Cards_Extensions_ICardDeleteExtensionContext.htm).
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
