# CardRequestExtensions.TryGetTemplateCard(CardResponse) - метод
Возвращает карточку шаблона, заданную ответ на универсальный запрос к
карточке, или null, если карточка шаблона не была задана.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Card TryGetTemplateCard(
    	this CardResponse response
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryGetTemplateCard ( 
    	response As CardResponse
    ) As Card
C++ __Копировать
     public:
    [ExtensionAttribute]
    static Card^ TryGetTemplateCard(
    	CardResponse^ response
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryGetTemplateCard : 
            response : CardResponse -> Card 
#### Параметры
response [CardResponse](T_Tessa_Cards_CardResponse.htm)
    Ответ на универсальный запрос к карточке.
#### Возвращаемое значение
[Card](T_Tessa_Cards_Card.htm)  
Карточка шаблона, заданная в ответе на универсальный запрос к карточке, или
null, если карточка шаблона не была задана.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [CardResponse](T_Tessa_Cards_CardResponse.htm). При вызове метода
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
