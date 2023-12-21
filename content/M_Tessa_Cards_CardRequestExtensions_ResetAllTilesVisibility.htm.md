# CardRequestExtensions.ResetAllTilesVisibility - метод
Удаляет всю информацию по видимости плиток. Плитки, которые используют
информацию по видимости, будут считать себя скрытыми. Возвращает признак того,
что информация присутствовала перед удалением.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool ResetAllTilesVisibility(
    	this Card card
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function ResetAllTilesVisibility ( 
    	card As Card
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    static bool ResetAllTilesVisibility(
    	Card^ card
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member ResetAllTilesVisibility : 
            card : Card -> bool 
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
    Карточка, которая содержит данные по видимости плиток.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если информация присутствовала перед удалением; false в противном
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
