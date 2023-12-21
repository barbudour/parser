# Tessa.Roles.Deputies.Sync - пространство имён
## __Классы
[CalculateDeputiesStrategyNames](T_Tessa_Roles_Deputies_Sync_CalculateDeputiesStrategyNames.htm)|
Имена стратегий
[ICalculateDeputiesStrategy](T_Tessa_Roles_Deputies_Sync_ICalculateDeputiesStrategy.htm),
с которыми они зарегистрированы в Unity.  
---|---  
[LoadNewUsersByRoleDeputiesStrategy](T_Tessa_Roles_Deputies_Sync_LoadNewUsersByRoleDeputiesStrategy.htm)|
Стратегия, которая производит загрузку заместителей через таблицу
[RoleDeputies](F_Tessa_Roles_RoleStrings_RoleDeputies.htm).  
[LoadNewUsersStrategyNames](T_Tessa_Roles_Deputies_Sync_LoadNewUsersStrategyNames.htm)|
Имена стратегий
[ILoadNewUsersStrategy](T_Tessa_Roles_Deputies_Sync_ILoadNewUsersStrategy.htm),
с которыми они зарегистрированы в Unity.  
[LoadOldUsersStrategy](T_Tessa_Roles_Deputies_Sync_LoadOldUsersStrategy.htm)|
Стратегия для для загрузки списка текущих сотрудников при синхронизации
заместителей.  
[LoadOldUsersStrategyNames](T_Tessa_Roles_Deputies_Sync_LoadOldUsersStrategyNames.htm)|
Имена стратегий
[ILoadOldUsersStrategy](T_Tessa_Roles_Deputies_Sync_ILoadOldUsersStrategy.htm),
с которыми они зарегистрированы в Unity.  
[SingleLevelCalculateDeputiesStrategy](T_Tessa_Roles_Deputies_Sync_SingleLevelCalculateDeputiesStrategy.htm)|
Стратегия расчёта заместителей, которая добавляет всех рассчитанных
заместителей. Предполагается, что в
[NewUsersList](P_Tessa_Roles_SyncDeputiesContext_NewUsersList.htm) и
[!:SyncDeputiesContext.NewNestedUsersList] находятся все рассчитанные
заместители.  
## __Интерфейсы
[ICalculateDeputiesStrategy](T_Tessa_Roles_Deputies_Sync_ICalculateDeputiesStrategy.htm)|
Стратегия для расчёта заместителей по данным контекста.  
---|---  
[ILoadNewUsersStrategy](T_Tessa_Roles_Deputies_Sync_ILoadNewUsersStrategy.htm)|
Стратегия для для загрузки списка актуальных сотрудников-заместителей при
синхронизации заместителей.  
[ILoadOldUsersStrategy](T_Tessa_Roles_Deputies_Sync_ILoadOldUsersStrategy.htm)|
Стратегия для для загрузки списка текущих сотрудников при синхронизации
заместителей.
