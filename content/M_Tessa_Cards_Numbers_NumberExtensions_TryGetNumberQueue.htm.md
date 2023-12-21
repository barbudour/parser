# NumberExtensions.TryGetNumberQueue - метод
Возвращает очередь действий с номерами, отложенных для выполнения на сервере
для текущей карточки, или null, если для текущей карточки очередь ещё не была
создана.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static NumberQueue TryGetNumberQueue(
    	this Card card
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryGetNumberQueue ( 
    	card As Card
    ) As NumberQueue
C++ __Копировать
     public:
    [ExtensionAttribute]
    static NumberQueue^ TryGetNumberQueue(
    	Card^ card
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryGetNumberQueue : 
            card : Card -> NumberQueue 
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
     Карточка, для которой возвращается очередь действий с номерами. Не может быть равна null. 
#### Возвращаемое значение
[NumberQueue](T_Tessa_Cards_Numbers_NumberQueue.htm)  
Очередь действий с номерами, отложенных для выполнения на сервере для текущей
карточки, или null, если для текущей карточки очередь ещё не была создана.
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
