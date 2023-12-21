# IApplicationManagerMessageBus.PublishAsync - метод
Осуществляет публикацию сообщения. При публикации сообщение предоставляется на
обработку обозревателям
## __Definition
 **Пространство имён:**
[Tessa.Applications.Messages](N_Tessa_Applications_Messages.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     ValueTask PublishAsync(
    	[NotNullAttribute] ApplicationMessage message,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function PublishAsync ( 
    	<NotNullAttribute> message As ApplicationMessage,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask
C++ __Копировать
     ValueTask PublishAsync(
    	[NotNullAttribute] ApplicationMessage^ message, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract PublishAsync : 
            [<NotNullAttribute>] message : ApplicationMessage * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
#### Параметры
message
[ApplicationMessage](T_Tessa_Applications_Messages_ApplicationMessage.htm)
     Публикуемое сообщение 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)  
Асинхронная задача.
##  __См. также
#### Ссылки
[IApplicationManagerMessageBus -
](T_Tessa_Applications_Messages_IApplicationManagerMessageBus.htm)
[Tessa.Applications.Messages - пространство
имён](N_Tessa_Applications_Messages.htm)
