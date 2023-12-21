# NumberExtensions.TryGetControlName - метод
Возвращает имя (алиас) элемента управления номерами, который инициировал
событие, происходящее с номером, или null, если элемент управления неизвестен
или если его тип отличен от заданного.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static string TryGetControlName(
    	this INumberContext context
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryGetControlName ( 
    	context As INumberContext
    ) As String
C++ __Копировать
     public:
    [ExtensionAttribute]
    static String^ TryGetControlName(
    	INumberContext^ context
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryGetControlName : 
            context : INumberContext -> string 
#### Параметры
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
     Контекст события, происходящего с номером. Не может быть равен null. 
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Имя элемента управления номерами, который инициировал событие, происходящее с
номером, или null, если элемент управления неизвестен или если его тип отличен
от заданного.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm). При
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
