# NumberExtensions.IsRegistered(NumberEventType) - метод
Возвращает признак того, что тип события, происходящего с номером,
зарегистрирован в реестре типов, который используется в стандартном API.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool IsRegistered(
    	this NumberEventType type
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function IsRegistered ( 
    	type As NumberEventType
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    static bool IsRegistered(
    	NumberEventType^ type
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member IsRegistered : 
            type : NumberEventType -> bool 
#### Параметры
type [NumberEventType](T_Tessa_Cards_Numbers_NumberEventType.htm)
    Тип события, происходящего с номером.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
Признак того, что тип события, происходящего с номером, зарегистрирован в
реестре типов, который используется в стандартном API.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [NumberEventType](T_Tessa_Cards_Numbers_NumberEventType.htm). При
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
