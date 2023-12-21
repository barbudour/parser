# NumberExtensions.ToCardNumberLocation - метод
Преобразует местоположение номера
[INumberLocation](T_Tessa_Cards_Numbers_INumberLocation.htm) типа
[Card](F_Tessa_Cards_Numbers_NumberLocationTypes_Card.htm) в объект
[CardNumberLocation](T_Tessa_Cards_Numbers_CardNumberLocation.htm). Может
вернуть null, если преобразование не удалось.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static CardNumberLocation ToCardNumberLocation(
    	this INumberLocation location
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function ToCardNumberLocation ( 
    	location As INumberLocation
    ) As CardNumberLocation
C++ __Копировать
     public:
    [ExtensionAttribute]
    static CardNumberLocation^ ToCardNumberLocation(
    	INumberLocation^ location
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member ToCardNumberLocation : 
            location : INumberLocation -> CardNumberLocation 
#### Параметры
location [INumberLocation](T_Tessa_Cards_Numbers_INumberLocation.htm)
     Местоположение номера. Не может быть равно null. 
#### Возвращаемое значение
[CardNumberLocation](T_Tessa_Cards_Numbers_CardNumberLocation.htm)  
Местоположение номера, определённое как объект
[CardNumberLocation](T_Tessa_Cards_Numbers_CardNumberLocation.htm), или null,
если преобразование не удалось.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [INumberLocation](T_Tessa_Cards_Numbers_INumberLocation.htm). При
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
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
