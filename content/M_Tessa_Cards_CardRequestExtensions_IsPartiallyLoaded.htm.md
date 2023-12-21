# CardRequestExtensions.IsPartiallyLoaded - метод
Возвращает признак того, что карточка может быть загружена частично (например,
без расширений), поэтому не все её поля могут быть корректно заполнены.
Актуально, например, для карточки, загруженной в контексте для действий с
номерами.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool IsPartiallyLoaded(
    	this Card card
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function IsPartiallyLoaded ( 
    	card As Card
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    static bool IsPartiallyLoaded(
    	Card^ card
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member IsPartiallyLoaded : 
            card : Card -> bool 
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
    Карточка, для которой требуется получить значение.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если карточка может быть загружена частично (например, без расширений),
поэтому не все её поля могут быть корректно заполнены; false в противном
случае.
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
