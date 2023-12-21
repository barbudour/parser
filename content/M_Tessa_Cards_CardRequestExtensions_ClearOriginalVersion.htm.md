# CardRequestExtensions.ClearOriginalVersion - метод
Удаляет информацию об оригинальной версии карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void ClearOriginalVersion(
    	this Card card
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub ClearOriginalVersion ( 
    	card As Card
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void ClearOriginalVersion(
    	Card^ card
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member ClearOriginalVersion : 
            card : Card -> unit 
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
    Карточка, из которой требуется удалить информацию по оригинальной версии.
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
