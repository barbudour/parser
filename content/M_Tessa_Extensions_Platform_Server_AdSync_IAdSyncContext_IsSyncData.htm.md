# IAdSyncContext.IsSyncData - метод
Проверяет необходимо ли синхронизировать подразделение.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.AdSync](N_Tessa_Extensions_Platform_Server_AdSync.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     bool IsSyncData(
    	Guid objectGuid
    )
VB __Копировать
     Function IsSyncData ( 
    	objectGuid As Guid
    ) As Boolean
C++ __Копировать
     bool IsSyncData(
    	Guid objectGuid
    )
F# __Копировать
     abstract IsSyncData : 
            objectGuid : Guid -> bool 
#### Параметры
objectGuid [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
     Идентификатор объекта. 
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
Нужно ли синхронизировать объект.
##  __См. также
#### Ссылки
[IAdSyncContext -
](T_Tessa_Extensions_Platform_Server_AdSync_IAdSyncContext.htm)
[Tessa.Extensions.Platform.Server.AdSync - пространство
имён](N_Tessa_Extensions_Platform_Server_AdSync.htm)
