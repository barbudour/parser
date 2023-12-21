# NumberExtensions.SetControlName - метод
Устанавливает в контексте имя элемента управления номерами, который
инициировал событие, происходящее с номером.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static INumberContext SetControlName(
    	this INumberContext context,
    	string controlName
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function SetControlName ( 
    	context As INumberContext,
    	controlName As String
    ) As INumberContext
C++ __Копировать
     public:
    [ExtensionAttribute]
    static INumberContext^ SetControlName(
    	INumberContext^ context, 
    	String^ controlName
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetControlName : 
            context : INumberContext * 
            controlName : string -> INumberContext 
#### Параметры
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
     Контекст события, происходящего с номером. Не может быть равен null. 
controlName [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя (алиас) для элемента управления номерами, который устанавливается в контексте, или null, если имя элемента управления должно быть удалено из контекста. 
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
