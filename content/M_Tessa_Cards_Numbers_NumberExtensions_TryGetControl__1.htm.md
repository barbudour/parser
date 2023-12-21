# NumberExtensions.TryGetControl<T> \- метод
Возвращает элемент управления номерами, который инициировал событие,
происходящее с номером, или null, если элемент управления неизвестен или если
его тип отличен от заданного.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static T TryGetControl<T>(
    	this INumberContext context
    )
    where T : class
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryGetControl(Of T As Class) ( 
    	context As INumberContext
    ) As T
C++ __Копировать
     public:
    [ExtensionAttribute]
    generic<typename T>
    where T : ref class
    static T TryGetControl(
    	INumberContext^ context
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryGetControl : 
            context : INumberContext -> 'T  when 'T : not struct
#### Параметры
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
     Контекст события, происходящего с номером. Не может быть равен null. 
#### Параметры типа
T
    Тип элемента управления, который требуется получить.
#### Возвращаемое значение
T  
Элемент управления номерами, который инициировал событие, происходящее с
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
