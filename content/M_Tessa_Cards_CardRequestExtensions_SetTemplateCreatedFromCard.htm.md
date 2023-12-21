# CardRequestExtensions.SetTemplateCreatedFromCard - метод
Устанавливает признак того, что карточка шаблона создаётся из другой карточки,
а не в результате создания по шаблону из экспортированной карточки шаблона.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetTemplateCreatedFromCard(
    	this Card card,
    	bool templateCreatedFromCard
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetTemplateCreatedFromCard ( 
    	card As Card,
    	templateCreatedFromCard As Boolean
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetTemplateCreatedFromCard(
    	Card^ card, 
    	bool templateCreatedFromCard
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetTemplateCreatedFromCard : 
            card : Card * 
            templateCreatedFromCard : bool -> unit 
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
    Карточка шаблона, для которой требуется установить значение признака.
templateCreatedFromCard
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
     Признак того, что карточка шаблона создаётся из другой карточки, а не в результате создания по шаблону из экспортированной карточки шаблона. 
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
