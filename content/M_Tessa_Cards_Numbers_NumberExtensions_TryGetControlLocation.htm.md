# NumberExtensions.TryGetControlLocation - метод
Возвращает информацию по местоположению номера в карточке для элемента
управления номерами, который инициировал событие, происходящее с номером, или
null, если местоположение неизвестно.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static INumberLocation TryGetControlLocation(
    	this INumberContext context
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryGetControlLocation ( 
    	context As INumberContext
    ) As INumberLocation
C++ __Копировать
     public:
    [ExtensionAttribute]
    static INumberLocation^ TryGetControlLocation(
    	INumberContext^ context
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryGetControlLocation : 
            context : INumberContext -> INumberLocation 
#### Параметры
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
     Контекст события, происходящего с номером. Не может быть равен null. 
#### Возвращаемое значение
[INumberLocation](T_Tessa_Cards_Numbers_INumberLocation.htm)  
Информация по местоположению номера в карточке для элемента управления
номерами, который инициировал событие, происходящее с номером, или null, если
местоположение неизвестно.
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
