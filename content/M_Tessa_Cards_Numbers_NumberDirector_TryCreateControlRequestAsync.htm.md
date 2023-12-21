# NumberDirector.TryCreateControlRequestAsync - метод
Создаёт и возвращает объект запроса к API номеров на сервере, который связан с
элементом управления. Возвращает null, если запрос не должен быть выполнен.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual ValueTask<CardRequest> TryCreateControlRequestAsync(
    	INumberContext context,
    	Guid requestType,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overridable Function TryCreateControlRequestAsync ( 
    	context As INumberContext,
    	requestType As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of CardRequest)
C++ __Копировать
     protected:
    virtual ValueTask<CardRequest^> TryCreateControlRequestAsync(
    	INumberContext^ context, 
    	Guid requestType, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract TryCreateControlRequestAsync : 
            context : INumberContext * 
            requestType : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<CardRequest> 
    override TryCreateControlRequestAsync : 
            context : INumberContext * 
            requestType : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<CardRequest> 
#### Параметры
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
    Контекст действия с номером, которое связано с элементом управления.
requestType [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
     Тип запроса. Значение обычно берут из полей класса [Tessa.Cards.Numbers.NumberCardRequestTypes]. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[CardRequest](T_Tessa_Cards_CardRequest.htm)>  
Объект запроса к API номеров на сервере, который связан с элементом
управления, или null, если запрос не должен быть выполнен.
## __См. также
#### Ссылки
[NumberDirector - ](T_Tessa_Cards_Numbers_NumberDirector.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
