# CardRequestExtensions.TryGetTemplateCreatedFromCard - метод
Возвращает признак того, что карточка шаблона создаётся из другой карточки, а
не в результате создания по шаблону из экспортированной карточки шаблона.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool TryGetTemplateCreatedFromCard(
    	this Card card
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryGetTemplateCreatedFromCard ( 
    	card As Card
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    static bool TryGetTemplateCreatedFromCard(
    	Card^ card
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryGetTemplateCreatedFromCard : 
            card : Card -> bool 
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
    Карточка шаблона, для которой требуется получить значение признака.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если карточка шаблона создаётся из другой карточки; false, если карточка
шаблона создаётся в результате создания по шаблону из экспортированной
карточки шаблона.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [Card](T_Tessa_Cards_Card.htm). При вызове метода для экземпляра
следует опускать первый параметр. Дополнительные сведения см. в разделе
[Методы расширения (Visual Basic)](https://docs.microsoft.com/dotnet/visual-
basic/programming-guide/language-features/procedures/extension-methods) или
[Методы расширения (Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardRequestExtensions - ](T_Tessa_Cards_CardRequestExtensions.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
