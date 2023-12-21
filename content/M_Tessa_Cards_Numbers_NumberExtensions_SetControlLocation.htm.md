# NumberExtensions.SetControlLocation - метод
Устанавливает в контексте информацию по местоположению номера в карточке для
элемента управления номерами, который инициировал событие, происходящее с
номером.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static INumberContext SetControlLocation(
    	this INumberContext context,
    	INumberLocation location
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function SetControlLocation ( 
    	context As INumberContext,
    	location As INumberLocation
    ) As INumberContext
C++ __Копировать
     public:
    [ExtensionAttribute]
    static INumberContext^ SetControlLocation(
    	INumberContext^ context, 
    	INumberLocation^ location
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetControlLocation : 
            context : INumberContext * 
            location : INumberLocation -> INumberContext 
#### Параметры
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
     Контекст события, происходящего с номером. Не может быть равен null. 
location [INumberLocation](T_Tessa_Cards_Numbers_INumberLocation.htm)
#### Возвращаемое значение
[INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)  
Контекст context для цепочки вызовов.
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
