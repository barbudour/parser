# IRoleManagerService - интерфейс
Объект, выполняющий задания, связанные с пересчётом ролей и замещений.
Доступен на сервере, а также на клиенте при условии, что на клиенте
зарегистрированы API карточек и платформенные расширения.
## __Definition
 **Пространство имён:** [Tessa.Roles](N_Tessa_Roles.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IRoleManagerService
VB __Копировать
     Public Interface IRoleManagerService
C++ __Копировать
     public interface class IRoleManagerService
F# __Копировать
     type IRoleManagerService = interface end
##  __Методы
[RecalcAllDynamicRolesAsync](M_Tessa_Roles_IRoleManagerService_RecalcAllDynamicRolesAsync.htm)|
Выполняет пересчёт всех динамических ролей. Возвращает результат операции.  
---|---  
[RecalcAllRoleGeneratorsAsync](M_Tessa_Roles_IRoleManagerService_RecalcAllRoleGeneratorsAsync.htm)|
Выполняет пересчёт всех генераторов метаролей. Возвращает результат операции.  
[RecalcDynamicRoleAsync](M_Tessa_Roles_IRoleManagerService_RecalcDynamicRoleAsync.htm)|
Выполняет пересчёт указанной динамической роли. Возвращает результат операции.  
[RecalcRoleGeneratorAsync](M_Tessa_Roles_IRoleManagerService_RecalcRoleGeneratorAsync.htm)|
Выполняет пересчёт метаролей для указанного генератора. Возвращает результат
операции.  
[SyncAllDeputiesAsync](M_Tessa_Roles_IRoleManagerService_SyncAllDeputiesAsync.htm)|
Выполняет пересчёт замещений для всех ролей, кроме динамических ролей и
метаролей. Возвращает результат операции.  
## __См. также
#### Ссылки
[Tessa.Roles - пространство имён](N_Tessa_Roles.htm)
