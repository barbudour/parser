# IApplicationMessageBus.RegisterAsync - метод
Выполняет регистрацию шины обработки сообщений в Tessa Applications
## __Definition
 **Пространство имён:**
[Tessa.Applications.Messages](N_Tessa_Applications_Messages.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     ValueTask<ApplicationMessage> RegisterAsync(
    	string apiVersion,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function RegisterAsync ( 
    	apiVersion As String,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of ApplicationMessage)
C++ __Копировать
     ValueTask<ApplicationMessage^> RegisterAsync(
    	String^ apiVersion, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract RegisterAsync : 
            apiVersion : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<ApplicationMessage> 
#### Параметры
apiVersion [String](https://learn.microsoft.com/dotnet/api/system.string)
    Версия API из констант [ApplicationApiVersionNames](T_Tessa_Applications_ApplicationApiVersionNames.htm).
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[ApplicationMessage](T_Tessa_Applications_Messages_ApplicationMessage.htm)>  
Сообщение, обработка которого инициировала запуск приложения
##  __См. также
#### Ссылки
[IApplicationMessageBus -
](T_Tessa_Applications_Messages_IApplicationMessageBus.htm)
[Tessa.Applications.Messages - пространство
имён](N_Tessa_Applications_Messages.htm)
