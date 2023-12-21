# INotificationSender.SendMessageAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Notices](N_Tessa_Extensions_Default_Shared_Notices.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     Task SendMessageAsync(
    	INotificationContext context,
    	IList<INotification> notifications,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function SendMessageAsync ( 
    	context As INotificationContext,
    	notifications As IList(Of INotification),
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
    Task^ SendMessageAsync(
    	INotificationContext^ context, 
    	IList<INotification^>^ notifications, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract SendMessageAsync : 
            context : INotificationContext * 
            notifications : IList<INotification> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
context
[INotificationContext](T_Tessa_Extensions_Default_Shared_Notices_INotificationContext.htm)
notifications
[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[INotification](T_Tessa_Extensions_Default_Shared_Notices_INotification.htm)>
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)
##  __См. также
#### Ссылки
[INotificationSender -
](T_Tessa_Extensions_Default_Shared_Notices_INotificationSender.htm)
[Tessa.Extensions.Default.Shared.Notices - пространство
имён](N_Tessa_Extensions_Default_Shared_Notices.htm)
