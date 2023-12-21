# NumberExtensions.IsKnown(NumberLocationType) - метод
Возвращает признак того, что тип местоположения номера является известным для
стандартного API.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool IsKnown(
    	this NumberLocationType type
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function IsKnown ( 
    	type As NumberLocationType
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    static bool IsKnown(
    	NumberLocationType^ type
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member IsKnown : 
            type : NumberLocationType -> bool 
#### Параметры
type [NumberLocationType](T_Tessa_Cards_Numbers_NumberLocationType.htm)
    Тип местоположения номера.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
Признак того, что тип местоположения номера является известным для
стандартного API.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[NumberLocationType](T_Tessa_Cards_Numbers_NumberLocationType.htm). При вызове
метода для экземпляра следует опускать первый параметр. Дополнительные
сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[NumberExtensions - ](T_Tessa_Cards_Numbers_NumberExtensions.htm)
[IsKnown -
перегрузка](Overload_Tessa_Cards_Numbers_NumberExtensions_IsKnown.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
