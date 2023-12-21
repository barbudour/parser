# ILdapUnitProvider.SetSyncDateAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.AdSync](N_Tessa_Extensions_Platform_Server_AdSync.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task SetSyncDateAsync(
    	Guid adSyncID,
    	DateTime syncDate,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function SetSyncDateAsync ( 
    	adSyncID As Guid,
    	syncDate As DateTime,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
    Task^ SetSyncDateAsync(
    	Guid adSyncID, 
    	DateTime syncDate, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract SetSyncDateAsync : 
            adSyncID : Guid * 
            syncDate : DateTime * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
adSyncID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
syncDate [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)
##  __См. также
#### Ссылки
[ILdapUnitProvider -
](T_Tessa_Extensions_Platform_Server_AdSync_ILdapUnitProvider.htm)
[Tessa.Extensions.Platform.Server.AdSync - пространство
имён](N_Tessa_Extensions_Platform_Server_AdSync.htm)
