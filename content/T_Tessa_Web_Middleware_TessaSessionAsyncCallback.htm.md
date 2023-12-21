# TessaSessionAsyncCallback - делегат
Выполняет асинхронные действия, связанные с проверкой сессии и установкой
актуального токена в контексте. Возвращает метод, который задаёт параметры
сессии в ExecutionContext для текущего потока (и его дочерних).
## __Definition
 **Пространство имён:** [Tessa.Web.Middleware](N_Tessa_Web_Middleware.htm)  
 **Сборка:** Tessa.Web (в Tessa.Web.dll) Версия: 3.6.0.17
C# __Копировать
     public delegate Task<Func<CancellationToken, ValueTask>> TessaSessionAsyncCallback(
    	TessaMiddlewareContext context,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Delegate Function TessaSessionAsyncCallback ( 
    	context As TessaMiddlewareContext,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Func(Of CancellationToken, ValueTask))
C++ __Копировать
     public delegate Task<Func<CancellationToken, ValueTask>^>^ TessaSessionAsyncCallback(
    	TessaMiddlewareContext^ context, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     type TessaSessionAsyncCallback = 
        delegate of 
            context : TessaMiddlewareContext * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<Func<CancellationToken, ValueTask>>
#### Параметры
context
[TessaMiddlewareContext](T_Tessa_Web_Middleware_TessaMiddlewareContext.htm)
    Контекст операции.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)>>  
Метод, который задаёт параметры сессии в ExecutionContext для текущего потока
(и его дочерних).
##  __См. также
#### Ссылки
[Tessa.Web.Middleware - пространство имён](N_Tessa_Web_Middleware.htm)
