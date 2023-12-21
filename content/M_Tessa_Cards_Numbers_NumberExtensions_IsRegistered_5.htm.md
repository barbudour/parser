# NumberExtensions.IsRegistered(NumberType) - метод
Возвращает признак того, что тип номера зарегистрирован в реестре типов,
который используется в стандартном API.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool IsRegistered(
    	this NumberType type
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function IsRegistered ( 
    	type As NumberType
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    static bool IsRegistered(
    	NumberType^ type
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member IsRegistered : 
            type : NumberType -> bool 
#### Параметры
type [NumberType](T_Tessa_Cards_Numbers_NumberType.htm)
    Тип номера.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
Признак того, что тип номера зарегистрирован в реестре типов, который
используется в стандартном API.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [NumberType](T_Tessa_Cards_Numbers_NumberType.htm). При вызове
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
[IsRegistered -
перегрузка](Overload_Tessa_Cards_Numbers_NumberExtensions_IsRegistered.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
