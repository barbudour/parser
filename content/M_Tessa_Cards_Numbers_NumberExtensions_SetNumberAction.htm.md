# NumberExtensions.SetNumberAction - метод
Устанавливает в контексте действие с номером, доступное по заданному ключу.
Значение null, переданное в параметр numberActionAsync, приводит к удалению
ранее заданного действия.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetNumberAction(
    	this INumberContext context,
    	string actionKey,
    	Func<INumberContext, INumberObject, CancellationToken, ValueTask> numberActionAsync
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetNumberAction ( 
    	context As INumberContext,
    	actionKey As String,
    	numberActionAsync As Func(Of INumberContext, INumberObject, CancellationToken, ValueTask)
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetNumberAction(
    	INumberContext^ context, 
    	String^ actionKey, 
    	Func<INumberContext^, INumberObject^, CancellationToken, ValueTask>^ numberActionAsync
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetNumberAction : 
            context : INumberContext * 
            actionKey : string * 
            numberActionAsync : Func<INumberContext, INumberObject, CancellationToken, ValueTask> -> unit 
#### Параметры
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
     Контекст события, происходящего с номером. Не может быть равен null. 
actionKey [String](https://learn.microsoft.com/dotnet/api/system.string)
     Ключ, по которому будет доступно действие с номером. Не может быть равен null. Стандартные ключи можно получить в классе [NumberContextActionKeys](T_Tessa_Cards_Numbers_NumberContextActionKeys.htm). 
numberActionAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-4)<[INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm),
[INumberObject](T_Tessa_Cards_Numbers_INumberObject.htm),
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)>
     Действие с номером, получающее контекст и номер в параметрах, или null, если действие с номером требуется удалить. Переданные в действие параметры гарантированно не равны null. 
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
