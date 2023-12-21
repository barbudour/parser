# CardRequestExtensions.TileIsVisible - метод
Возвращает признак того, что плитка с заданным именем должна быть видимой.
Данные видимости обычно устанавливаются при создании или загрузке карточки, в
т.ч. на сервере.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool TileIsVisible(
    	this Card card,
    	string tileName
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TileIsVisible ( 
    	card As Card,
    	tileName As String
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    static bool TileIsVisible(
    	Card^ card, 
    	String^ tileName
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TileIsVisible : 
            card : Card * 
            tileName : string -> bool 
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
    Карточка, которая содержит данные по видимости плиток.
tileName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя проверяемой плитки.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если плитка с заданным именем должна быть видимой; false в противном
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
