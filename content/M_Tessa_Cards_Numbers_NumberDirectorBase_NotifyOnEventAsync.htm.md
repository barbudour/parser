# NumberDirectorBase.NotifyOnEventAsync - метод
Выполняет заданное действие с номером.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<bool> NotifyOnEventAsync(
    	INumberContext context,
    	NumberEventType eventType,
    	Func<INumberContext, CancellationToken, Task<bool>> numberActionFuncAsync,
    	Func<INumberContext, CancellationToken, Task<bool>> numberPredicateFuncAsync = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function NotifyOnEventAsync ( 
    	context As INumberContext,
    	eventType As NumberEventType,
    	numberActionFuncAsync As Func(Of INumberContext, CancellationToken, Task(Of Boolean)),
    	Optional numberPredicateFuncAsync As Func(Of INumberContext, CancellationToken, Task(Of Boolean)) = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Boolean)
C++ __Копировать
     public:
    virtual Task<bool>^ NotifyOnEventAsync(
    	INumberContext^ context, 
    	NumberEventType^ eventType, 
    	Func<INumberContext^, CancellationToken, Task<bool>^>^ numberActionFuncAsync, 
    	Func<INumberContext^, CancellationToken, Task<bool>^>^ numberPredicateFuncAsync = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract NotifyOnEventAsync : 
            context : INumberContext * 
            eventType : NumberEventType * 
            numberActionFuncAsync : Func<INumberContext, CancellationToken, Task<bool>> * 
            ?numberPredicateFuncAsync : Func<INumberContext, CancellationToken, Task<bool>> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _numberPredicateFuncAsync = defaultArg numberPredicateFuncAsync null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
    override NotifyOnEventAsync : 
            context : INumberContext * 
            eventType : NumberEventType * 
            numberActionFuncAsync : Func<INumberContext, CancellationToken, Task<bool>> * 
            ?numberPredicateFuncAsync : Func<INumberContext, CancellationToken, Task<bool>> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _numberPredicateFuncAsync = defaultArg numberPredicateFuncAsync null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
#### Параметры
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
     Контекст события, происходящего с номером. Не может быть равен null. 
eventType [NumberEventType](T_Tessa_Cards_Numbers_NumberEventType.htm)
     Тип события, происходящего с номером. Не может быть равен null. 
numberActionFuncAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-3)<[INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm),
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>>
numberPredicateFuncAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-3)<[INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm),
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>>
(Optional)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если действие было успешно выполнено; false, если действие было отменено
или при выполнении действия возникли ошибки.
#### Реализации
[INumberDirectorBase.NotifyOnEventAsync(INumberContext, NumberEventType,
Func<INumberContext, CancellationToken, Task<Boolean>>, Func<INumberContext,
CancellationToken, Task<Boolean>>,
CancellationToken)](M_Tessa_Cards_Numbers_INumberDirectorBase_NotifyOnEventAsync.htm)  
##  __См. также
#### Ссылки
[NumberDirectorBase - ](T_Tessa_Cards_Numbers_NumberDirectorBase.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
