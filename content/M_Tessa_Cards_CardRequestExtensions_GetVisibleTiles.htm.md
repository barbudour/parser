# CardRequestExtensions.GetVisibleTiles - метод
Возвращает массив, содержащий список всех видимых плиток. Массив всегда не
равен null. Данные видимости обычно устанавливаются при создании или загрузке
карточки, в т.ч. на сервере.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static string[] GetVisibleTiles(
    	this Card card
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function GetVisibleTiles ( 
    	card As Card
    ) As String()
C++ __Копировать
     public:
    [ExtensionAttribute]
    static array<String^>^ GetVisibleTiles(
    	Card^ card
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member GetVisibleTiles : 
            card : Card -> string[] 
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
    Карточка, которая содержит данные по видимости плиток.
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)[]  
Массив, содержащий список всех видимых плиток. Массив всегда не равен null.
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
