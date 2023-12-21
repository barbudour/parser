# IAdSyncContext.AddGroupToCache - метод
Добавление новой группы в список кешируемых.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.AdSync](N_Tessa_Extensions_Platform_Server_AdSync.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     void AddGroupToCache(
    	Guid groupId,
    	List<Guid> members
    )
VB __Копировать
     Sub AddGroupToCache ( 
    	groupId As Guid,
    	members As List(Of Guid)
    )
C++ __Копировать
     void AddGroupToCache(
    	Guid groupId, 
    	List<Guid>^ members
    )
F# __Копировать
     abstract AddGroupToCache : 
            groupId : Guid * 
            members : List<Guid> -> unit 
#### Параметры
groupId [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
     ID группы. 
members
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
     Список идентификаторов пользователей. 
## __См. также
#### Ссылки
[IAdSyncContext -
](T_Tessa_Extensions_Platform_Server_AdSync_IAdSyncContext.htm)
[Tessa.Extensions.Platform.Server.AdSync - пространство
имён](N_Tessa_Extensions_Platform_Server_AdSync.htm)
