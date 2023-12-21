# NumberDirector.ProcessControlRequestAsync - метод
Выполняет обработку запроса к API номеров на сервере, который связан с
элементом управления.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual Task<bool> ProcessControlRequestAsync(
    	INumberContext context,
    	Guid requestType,
    	Func<INumberContext, NumberControlResponse, CancellationToken, Task<bool>> processFuncAsync,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overridable Function ProcessControlRequestAsync ( 
    	context As INumberContext,
    	requestType As Guid,
    	processFuncAsync As Func(Of INumberContext, NumberControlResponse, CancellationToken, Task(Of Boolean)),
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Boolean)
C++ __Копировать
     protected:
    virtual Task<bool>^ ProcessControlRequestAsync(
    	INumberContext^ context, 
    	Guid requestType, 
    	Func<INumberContext^, NumberControlResponse^, CancellationToken, Task<bool>^>^ processFuncAsync, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract ProcessControlRequestAsync : 
            context : INumberContext * 
            requestType : Guid * 
            processFuncAsync : Func<INumberContext, NumberControlResponse, CancellationToken, Task<bool>> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
    override ProcessControlRequestAsync : 
            context : INumberContext * 
            requestType : Guid * 
            processFuncAsync : Func<INumberContext, NumberControlResponse, CancellationToken, Task<bool>> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
#### Параметры
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
    Контекст действия с номером, которое связано с элементом управления.
requestType [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
     Тип запроса. Значение обычно берут из полей класса [Tessa.Cards.Numbers.NumberCardRequestTypes]. 
processFuncAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-4)<[INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm),
[NumberControlResponse](T_Tessa_Cards_Numbers_NumberControlResponse.htm),
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>>
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если функция processFunc успешно выполнила обработку; false, если
функция обработки не была вызвана из-за ошибок в запросе, или она вернула
false при обработке.
## __См. также
#### Ссылки
[NumberDirector - ](T_Tessa_Cards_Numbers_NumberDirector.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
