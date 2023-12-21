# UIContextExecutorAsync - делегат
Выполняет заданный метод в контексте [IUIContext](T_Tessa_UI_IUIContext.htm),
который устанавливается как текущий контекст и передаётся как параметр в
заданный метод.
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public delegate ValueTask UIContextExecutorAsync(
    	Func<IUIContext, CancellationToken, ValueTask> actionToExecuteInContextAsync,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Delegate Function UIContextExecutorAsync ( 
    	actionToExecuteInContextAsync As Func(Of IUIContext, CancellationToken, ValueTask),
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask
C++ __Копировать
     public delegate ValueTask UIContextExecutorAsync(
    	Func<IUIContext^, CancellationToken, ValueTask>^ actionToExecuteInContextAsync, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     type UIContextExecutorAsync = 
        delegate of 
            actionToExecuteInContextAsync : Func<IUIContext, CancellationToken, ValueTask> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask
#### Параметры
actionToExecuteInContextAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-3)<[IUIContext](T_Tessa_UI_IUIContext.htm),
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)>
     Метод, который требуется выполнить в контексте [IUIContext](T_Tessa_UI_IUIContext.htm). Метод не должен быть равен null. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)
##  __См. также
#### Ссылки
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
