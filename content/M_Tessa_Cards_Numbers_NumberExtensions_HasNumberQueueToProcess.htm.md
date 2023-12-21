# NumberExtensions.HasNumberQueueToProcess - метод
Возвращает признак того, что в карточке присутствует непустая очередь для
обработки.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool HasNumberQueueToProcess(
    	this Card card
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function HasNumberQueueToProcess ( 
    	card As Card
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    static bool HasNumberQueueToProcess(
    	Card^ card
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member HasNumberQueueToProcess : 
            card : Card -> bool 
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
     Карточка, для которой требуется проверять наличие непустой очереди. Не может быть равна null. 
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если в карточке присутствует непустая очередь для обработки; false в
противном случае.
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
