# CardRequestExtensions.SetTemplateCard(CardNewRequest, Card) - метод
Устанавливает карточку шаблона в запросе на создание структуры карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetTemplateCard(
    	this CardNewRequest request,
    	Card card
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetTemplateCard ( 
    	request As CardNewRequest,
    	card As Card
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetTemplateCard(
    	CardNewRequest^ request, 
    	Card^ card
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetTemplateCard : 
            request : CardNewRequest * 
            card : Card -> unit 
#### Параметры
request [CardNewRequest](T_Tessa_Cards_CardNewRequest.htm)
    Запрос на создание структуры карточки.
card [Card](T_Tessa_Cards_Card.htm)
    Карточка шаблона, которую требуется установить в запросе на создание структуры карточки.
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
[SetTemplateCard -
перегрузка](Overload_Tessa_Cards_CardRequestExtensions_SetTemplateCard.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
