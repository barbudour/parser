# IApplicationMessageBus.ProcessMessageAsync - метод
Осуществляет обработку сообщения
## __Definition
 **Пространство имён:**
[Tessa.Applications.Messages](N_Tessa_Applications_Messages.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     ValueTask<bool> ProcessMessageAsync(
    	[NotNullAttribute] ApplicationMessage message,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function ProcessMessageAsync ( 
    	<NotNullAttribute> message As ApplicationMessage,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Boolean)
C++ __Копировать
     ValueTask<bool> ProcessMessageAsync(
    	[NotNullAttribute] ApplicationMessage^ message, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract ProcessMessageAsync : 
            [<NotNullAttribute>] message : ApplicationMessage * 
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
## __См. также
#### Ссылки
[IApplicationMessageBus -
](T_Tessa_Applications_Messages_IApplicationMessageBus.htm)
[Tessa.Applications.Messages - пространство
имён](N_Tessa_Applications_Messages.htm)
