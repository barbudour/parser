# CardExtensions.DeepClone(CardTypeControl) - метод
Выполняет глубокое клонирование метаинформации по элементу управления
[CardTypeControl](T_Tessa_Cards_CardTypeControl.htm) за счёт его полной
сериализации / десериализации.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static CardTypeControl DeepClone(
    	this CardTypeControl obj
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function DeepClone ( 
    	obj As CardTypeControl
    ) As CardTypeControl
C++ __Копировать
     public:
    [ExtensionAttribute]
    static CardTypeControl^ DeepClone(
    	CardTypeControl^ obj
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member DeepClone : 
            obj : CardTypeControl -> CardTypeControl 
#### Параметры
obj [CardTypeControl](T_Tessa_Cards_CardTypeControl.htm)
    Исходный объект.
#### Возвращаемое значение
[CardTypeControl](T_Tessa_Cards_CardTypeControl.htm)  
Глубокая копия исходного объекта.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [CardTypeControl](T_Tessa_Cards_CardTypeControl.htm). При вызове
метода для экземпляра следует опускать первый параметр. Дополнительные
сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardExtensions - ](T_Tessa_Cards_CardExtensions.htm)
[DeepClone - перегрузка](Overload_Tessa_Cards_CardExtensions_DeepClone.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
