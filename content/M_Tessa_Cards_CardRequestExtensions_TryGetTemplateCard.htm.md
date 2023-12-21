# CardRequestExtensions.TryGetTemplateCard(CardNewRequest) - метод
Возвращает карточку шаблона, заданную в запросе на создание структуры
карточки, или null, если карточка шаблона не была задана.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Card TryGetTemplateCard(
    	this CardNewRequest request
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryGetTemplateCard ( 
    	request As CardNewRequest
    ) As Card
C++ __Копировать
     public:
    [ExtensionAttribute]
    static Card^ TryGetTemplateCard(
    	CardNewRequest^ request
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryGetTemplateCard : 
            request : CardNewRequest -> Card 
#### Параметры
request [CardNewRequest](T_Tessa_Cards_CardNewRequest.htm)
    Запрос на создание структуры карточки.
#### Возвращаемое значение
[Card](T_Tessa_Cards_Card.htm)  
Карточка шаблона, заданная в запросе на создание структуры карточки, или null,
если карточка шаблона не была задана.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [CardNewRequest](T_Tessa_Cards_CardNewRequest.htm). При вызове
метода для экземпляра следует опускать первый параметр. Дополнительные
сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardRequestExtensions - ](T_Tessa_Cards_CardRequestExtensions.htm)
[TryGetTemplateCard -
перегрузка](Overload_Tessa_Cards_CardRequestExtensions_TryGetTemplateCard.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
