# ApplicationMessageBus.ProcessMessageAsync - метод
Осуществляет обработку сообщения
## __Definition
 **Пространство имён:**
[Tessa.Applications.Messages](N_Tessa_Applications_Messages.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<bool> ProcessMessageAsync(
    	ApplicationMessage message,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function ProcessMessageAsync ( 
    	message As ApplicationMessage,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Boolean)
C++ __Копировать
     public:
    virtual ValueTask<bool> ProcessMessageAsync(
    	ApplicationMessage^ message, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract ProcessMessageAsync : 
            message : ApplicationMessage * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<bool> 
    override ProcessMessageAsync : 
            message : ApplicationMessage * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<bool> 
#### Параметры
message
[ApplicationMessage](T_Tessa_Applications_Messages_ApplicationMessage.htm)
     Сообщение 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
Результат обработки сообщения
#### Реализации
[IApplicationMessageBus.ProcessMessageAsync(ApplicationMessage,
CancellationToken)](M_Tessa_Applications_Messages_IApplicationMessageBus_ProcessMessageAsync.htm)  
##  __См. также
#### Ссылки
[ApplicationMessageBus -
](T_Tessa_Applications_Messages_ApplicationMessageBus.htm)
[Tessa.Applications.Messages - пространство
имён](N_Tessa_Applications_Messages.htm)
