# CardRequestExtensions.SetTemplateCard(CardResponse, Card) - метод
Устанавливает карточку шаблона в ответе на универсальный запрос к карточке.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetTemplateCard(
    	this CardResponse response,
    	Card card
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetTemplateCard ( 
    	response As CardResponse,
    	card As Card
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetTemplateCard(
    	CardResponse^ response, 
    	Card^ card
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetTemplateCard : 
            response : CardResponse * 
            card : Card -> unit 
#### Параметры
response [CardResponse](T_Tessa_Cards_CardResponse.htm)
    Ответ на универсальный запрос к карточке.
card [Card](T_Tessa_Cards_Card.htm)
    Карточка шаблона, которую требуется установить в ответе на универсальный запрос к карточке.
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
[SetTemplateCard -
перегрузка](Overload_Tessa_Cards_CardRequestExtensions_SetTemplateCard.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
