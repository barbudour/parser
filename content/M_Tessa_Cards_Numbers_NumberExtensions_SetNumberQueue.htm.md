# NumberExtensions.SetNumberQueue - метод
Устанавливает очередь действий с номерами для текущей карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetNumberQueue(
    	this Card card,
    	NumberQueue numberQueue
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetNumberQueue ( 
    	card As Card,
    	numberQueue As NumberQueue
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetNumberQueue(
    	Card^ card, 
    	NumberQueue^ numberQueue
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetNumberQueue : 
            card : Card * 
            numberQueue : NumberQueue -> unit 
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
     Карточка, для которой требуется установить очередь действий с номерами. Не может быть равна null. 
numberQueue [NumberQueue](T_Tessa_Cards_Numbers_NumberQueue.htm)
     Очередь действий с номерами, которую требуется установить. Не может быть равна null. 
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
[NumberExtensions - ](T_Tessa_Cards_Numbers_NumberExtensions.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
