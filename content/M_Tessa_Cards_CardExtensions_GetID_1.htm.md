# CardExtensions.GetID(CardTypeExtension) - метод
Получить уникальный идентификатор объекта на основе хэш-кода его типа и
настроек.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static string GetID(
    	this CardTypeExtension obj
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function GetID ( 
    	obj As CardTypeExtension
    ) As String
C++ __Копировать
     public:
    [ExtensionAttribute]
    static String^ GetID(
    	CardTypeExtension^ obj
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member GetID : 
            obj : CardTypeExtension -> string 
#### Параметры
obj [CardTypeExtension](T_Tessa_Cards_CardTypeExtension.htm)
    Расширение типа.
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Уникальный идентификатор объекта.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [CardTypeExtension](T_Tessa_Cards_CardTypeExtension.htm). При
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
