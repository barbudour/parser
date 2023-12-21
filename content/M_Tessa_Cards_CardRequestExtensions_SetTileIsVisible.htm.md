# CardRequestExtensions.SetTileIsVisible - метод
Устанавливает признак того, должна ли плитка быть видимой. Рекомендуется
вызывать метод при создании или загрузке карточки, в т.ч. на сервере.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetTileIsVisible(
    	this Card card,
    	string tileName,
    	bool isVisible = true
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetTileIsVisible ( 
    	card As Card,
    	tileName As String,
    	Optional isVisible As Boolean = true
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetTileIsVisible(
    	Card^ card, 
    	String^ tileName, 
    	bool isVisible = true
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetTileIsVisible : 
            card : Card * 
            tileName : string * 
            ?isVisible : bool 
    (* Defaults:
            let _isVisible = defaultArg isVisible true
    *)
    -> unit 
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
    Карточка, которая содержит данные по видимости плиток.
tileName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя плитки.
isVisible [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
    Признак того, должна ли плитка быть видимой.
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
