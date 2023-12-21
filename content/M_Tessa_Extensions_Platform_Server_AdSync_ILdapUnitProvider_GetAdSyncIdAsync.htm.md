# ILdapUnitProvider.GetAdSyncIdAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.AdSync](N_Tessa_Extensions_Platform_Server_AdSync.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    Task<Guid?> GetAdSyncIdAsync(
    	Guid cardId,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function GetAdSyncIdAsync ( 
    	cardId As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Guid?)
C++ __Копировать
    Task<Nullable<Guid>>^ GetAdSyncIdAsync(
    	Guid cardId, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract GetAdSyncIdAsync : 
            cardId : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<Nullable<Guid>> 
#### Параметры
cardId [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>>
##  __См. также
#### Ссылки
[ILdapUnitProvider -
](T_Tessa_Extensions_Platform_Server_AdSync_ILdapUnitProvider.htm)
[Tessa.Extensions.Platform.Server.AdSync - пространство
имён](N_Tessa_Extensions_Platform_Server_AdSync.htm)
