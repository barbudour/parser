# CardRequestExtensions.SetDigestCard - метод
Устанавливает карточку, используемую для получения Digest в расширениях.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetDigestCard(
    	this CardRequest request,
    	Card card
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetDigestCard ( 
    	request As CardRequest,
    	card As Card
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetDigestCard(
    	CardRequest^ request, 
    	Card^ card
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetDigestCard : 
            request : CardRequest * 
            card : Card -> unit 
#### Параметры
request [CardRequest](T_Tessa_Cards_CardRequest.htm)
     Запрос к сервису карточек на получение Digest. Тип запроса [GetDigest](F_Tessa_Cards_CardRequestTypes_GetDigest.htm). 
card [Card](T_Tessa_Cards_Card.htm)
    Карточка, Digest которой должен быть получен в расширениях.
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
