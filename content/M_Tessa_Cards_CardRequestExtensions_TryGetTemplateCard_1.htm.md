# CardRequestExtensions.TryGetTemplateCard(CardRequest) - метод
Возвращает карточку шаблона, заданную в универсальном запросе к карточке, или
null, если карточка шаблона не была задана.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Card TryGetTemplateCard(
    	this CardRequest request
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryGetTemplateCard ( 
    	request As CardRequest
    ) As Card
C++ __Копировать
     public:
    [ExtensionAttribute]
    static Card^ TryGetTemplateCard(
    	CardRequest^ request
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryGetTemplateCard : 
            request : CardRequest -> Card 
#### Параметры
request [CardRequest](T_Tessa_Cards_CardRequest.htm)
    Универсальный запрос к карточке.
#### Возвращаемое значение
[Card](T_Tessa_Cards_Card.htm)  
Карточка шаблона, заданная в универсальном запросе к карточке, или null, если
карточка шаблона не была задана.
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
[TryGetTemplateCard -
перегрузка](Overload_Tessa_Cards_CardRequestExtensions_TryGetTemplateCard.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
