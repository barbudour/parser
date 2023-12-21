# CardRequestExtensions.SetCard - метод
Устанавливает карточку для использования в универсальном запросе к API
карточек.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetCard(
    	this CardRequest request,
    	Card card
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetCard ( 
    	request As CardRequest,
    	card As Card
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetCard(
    	CardRequest^ request, 
    	Card^ card
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetCard : 
            request : CardRequest * 
            card : Card -> unit 
#### Параметры
request [CardRequest](T_Tessa_Cards_CardRequest.htm)
    Запрос к сервису карточек.
card [Card](T_Tessa_Cards_Card.htm)
     Карточка, устанавливаемая в запросе. Параметр равен null, когда значение требуется удалить. 
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
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
