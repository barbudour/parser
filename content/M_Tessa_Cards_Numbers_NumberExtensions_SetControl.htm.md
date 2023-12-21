# NumberExtensions.SetControl - метод
Устанавливает в контексте элемент управления номерами, который инициировал
событие, происходящее с номером.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static INumberContext SetControl(
    	this INumberContext context,
    	Object control
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function SetControl ( 
    	context As INumberContext,
    	control As Object
    ) As INumberContext
C++ __Копировать
     public:
    [ExtensionAttribute]
    static INumberContext^ SetControl(
    	INumberContext^ context, 
    	Object^ control
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetControl : 
            context : INumberContext * 
            control : Object -> INumberContext 
#### Параметры
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
     Контекст события, происходящего с номером. Не может быть равен null. 
control [Object](https://learn.microsoft.com/dotnet/api/system.object)
     Элемент управления номерами, который устанавливается в контексте, или null, если элемент управления должен быть удалён из контекста. 
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
