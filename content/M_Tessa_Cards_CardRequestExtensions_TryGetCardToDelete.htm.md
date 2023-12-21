# CardRequestExtensions.TryGetCardToDelete - метод
Возвращает карточку, для которой выполняется удаление с восстановлением,
окончательное удаление или восстановление, или null, если карточка неизвестна.
Рекомендуется использовать метод в цепочке расширений на удаление карточки,
для которой выполняется удаление с восстановлением, или на удаление карточки
Deleted, причём значение заполнено начиная с
[AfterBeginTransaction(ICardDeleteExtensionContext)](M_Tessa_Cards_Extensions_ICardDeleteExtension_AfterBeginTransaction.htm)
этапа [AfterPlatform](T_Tessa_Extensions_ExtensionStage.htm)
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Card TryGetCardToDelete(
    	this ICardDeleteExtensionContext context
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryGetCardToDelete ( 
    	context As ICardDeleteExtensionContext
    ) As Card
C++ __Копировать
     public:
    [ExtensionAttribute]
    static Card^ TryGetCardToDelete(
    	ICardDeleteExtensionContext^ context
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryGetCardToDelete : 
            context : ICardDeleteExtensionContext -> Card 
#### Параметры
context
[ICardDeleteExtensionContext](T_Tessa_Cards_Extensions_ICardDeleteExtensionContext.htm)
    Контекст процесса удаления карточки Deleted.
#### Возвращаемое значение
[Card](T_Tessa_Cards_Card.htm)  
Карточка, для которой выполняется окончательное удаление или восстановление,
или null, если карточка неизвестна.
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
