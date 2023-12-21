# NumberExtensions.IsRegistered(NumberQueueEventType) - метод
Возвращает признак того, что тип события по вызову действия с номером в
очереди [NumberQueue](T_Tessa_Cards_Numbers_NumberQueue.htm) зарегистрирован в
реестре типов, который используется в стандартном API.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool IsRegistered(
    	this NumberQueueEventType type
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function IsRegistered ( 
    	type As NumberQueueEventType
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    static bool IsRegistered(
    	NumberQueueEventType^ type
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member IsRegistered : 
            type : NumberQueueEventType -> bool 
#### Параметры
type [NumberQueueEventType](T_Tessa_Cards_Numbers_NumberQueueEventType.htm)
    Тип события по вызову действия с номером в очереди.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
Признак того, что тип события по вызову действия с номером в очереди
зарегистрирован в реестре типов, который используется в стандартном API.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[NumberQueueEventType](T_Tessa_Cards_Numbers_NumberQueueEventType.htm). При
вызове метода для экземпляра следует опускать первый параметр. Дополнительные
сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[NumberExtensions - ](T_Tessa_Cards_Numbers_NumberExtensions.htm)
[IsRegistered -
перегрузка](Overload_Tessa_Cards_Numbers_NumberExtensions_IsRegistered.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
