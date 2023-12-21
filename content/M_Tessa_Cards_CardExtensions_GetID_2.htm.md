# CardExtensions.GetID(CardTypeValidator) - метод
Получить уникальный идентификатор объекта на основе хэш-кода его типа и
настроек.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static string GetID(
    	this CardTypeValidator obj
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function GetID ( 
    	obj As CardTypeValidator
    ) As String
C++ __Копировать
     public:
    [ExtensionAttribute]
    static String^ GetID(
    	CardTypeValidator^ obj
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member GetID : 
            obj : CardTypeValidator -> string 
#### Параметры
obj [CardTypeValidator](T_Tessa_Cards_CardTypeValidator.htm)
    Валидатор.
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Уникальный идентификатор объекта.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [CardTypeValidator](T_Tessa_Cards_CardTypeValidator.htm). При
вызове метода для экземпляра следует опускать первый параметр. Дополнительные
сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardExtensions - ](T_Tessa_Cards_CardExtensions.htm)
[GetID - перегрузка](Overload_Tessa_Cards_CardExtensions_GetID.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
