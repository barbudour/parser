# GetNotificationBodyFuncAsync<TNotification, TNotificationData> \- делегат
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Notices](N_Tessa_Extensions_Default_Server_Notices.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public delegate ValueTask<string> GetNotificationBodyFuncAsync<in TNotification, in TNotificationData>(
    	INotificationContext context,
    	TNotification notification,
    	TNotificationData data,
    	string subject,
    	string cardLink,
    	string webCardLink,
    	CancellationToken cancellationToken = default
    )
    where TNotification : INotification
    where TNotificationData : Object, INotificationData<TNotification>
VB __Копировать
     Public Delegate Function GetNotificationBodyFuncAsync(Of In TNotification As INotification, In TNotificationData As {Object, INotificationData(Of TNotification)}) ( 
    	context As INotificationContext,
    	notification As TNotification,
    	data As TNotificationData,
    	subject As String,
    	cardLink As String,
    	webCardLink As String,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of String)
C++ __Копировать
    generic<typename TNotification, typename TNotificationData>
    where TNotification : INotification
    where TNotificationData : Object, INotificationData<TNotification>
    public delegate ValueTask<String^> GetNotificationBodyFuncAsync(
    	INotificationContext^ context, 
    	TNotification notification, 
    	TNotificationData data, 
    	String^ subject, 
    	String^ cardLink, 
    	String^ webCardLink, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     type GetNotificationBodyFuncAsync = 
        delegate of 
            context : INotificationContext * 
            notification : 'TNotification * 
            data : 'TNotificationData * 
            subject : string * 
            cardLink : string * 
            webCardLink : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<string>
#### Параметры
context
[INotificationContext](T_Tessa_Extensions_Default_Shared_Notices_INotificationContext.htm)
notification TNotification
data TNotificationData
subject [String](https://learn.microsoft.com/dotnet/api/system.string)
cardLink [String](https://learn.microsoft.com/dotnet/api/system.string)
webCardLink [String](https://learn.microsoft.com/dotnet/api/system.string)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Параметры типа
TNotification
TNotificationData
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
##  __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Notices - пространство
имён](N_Tessa_Extensions_Default_Server_Notices.htm)
