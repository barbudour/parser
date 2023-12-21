# CardRequestExtensions.SetOriginalVersion - метод
Устанавливает оригинальную версию карточки, которая была очищена при экспорте.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetOriginalVersion(
    	this Card card,
    	int version
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetOriginalVersion ( 
    	card As Card,
    	version As Integer
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetOriginalVersion(
    	Card^ card, 
    	int version
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetOriginalVersion : 
            card : Card * 
            version : int -> unit 
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
    Карточка, оригинальная версия которой устанавливается.
version [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
    Оригинальная версия карточки, которая была очищена при экспорте.
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
