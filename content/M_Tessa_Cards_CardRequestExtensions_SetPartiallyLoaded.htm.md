# CardRequestExtensions.SetPartiallyLoaded - метод
Устанавливает признак того, что карточка может быть загружена частично
(например, без расширений), поэтому не все её поля могут быть корректно
заполнены. Актуально, например, для карточки, загруженной в контексте для
действий с номерами.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetPartiallyLoaded(
    	this Card card,
    	bool value
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetPartiallyLoaded ( 
    	card As Card,
    	value As Boolean
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetPartiallyLoaded(
    	Card^ card, 
    	bool value
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetPartiallyLoaded : 
            card : Card * 
            value : bool -> unit 
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
    Карточка, для которой требуется установить значение.
value [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
    Признак того, что карточка может быть загружена частично.
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
