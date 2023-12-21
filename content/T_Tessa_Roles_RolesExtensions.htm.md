# RolesExtensions - класс
Расширения разметки для пространства имён Tessa.Roles.
## __Definition
 **Пространство имён:** [Tessa.Roles](N_Tessa_Roles.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class RolesExtensions
VB __Копировать
    <ExtensionAttribute>
    Public NotInheritable Class RolesExtensions
C++ __Копировать
    [ExtensionAttribute]
    public ref class RolesExtensions abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    [<ExtensionAttribute>]
    type RolesExtensions = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ RolesExtensions
##  __Методы
[CheckUserInCardContextAsync](M_Tessa_Roles_RolesExtensions_CheckUserInCardContextAsync.htm)|
Осуществляет проверку того, что пользователь с идентификатором userID
находится для карточки с идентификатором cardID в составе контекстной роли
role.  
---|---  
[DeleteAllDeputiesAsync](M_Tessa_Roles_RolesExtensions_DeleteAllDeputiesAsync.htm)|
Удаляет все записи о заместителях на указанную роль.  
[DeleteAllUsersAsync](M_Tessa_Roles_RolesExtensions_DeleteAllUsersAsync.htm)|
Удаляет все записи о составе указанной роли.  
[DeleteAsync(IRoleRepository, Role,
CancellationToken)](M_Tessa_Roles_RolesExtensions_DeleteAsync.htm)|  Удаляет
указанную роль, её состав и записи о замещении.  
[DeleteAsync(IRoleRepository, RoleDeputyRecord,
CancellationToken)](M_Tessa_Roles_RolesExtensions_DeleteAsync_1.htm)|  Удаляет
запись о замещении на роль.  
[DeleteAsync(IRoleRepository, RoleGenerator,
CancellationToken)](M_Tessa_Roles_RolesExtensions_DeleteAsync_2.htm)|  Удаляет
генератор метаролей, а также все его метароли.  
[DeleteAsync(IRoleRepository, RoleUserRecord,
CancellationToken)](M_Tessa_Roles_RolesExtensions_DeleteAsync_4.htm)|  Удаляет
запись о составе роли.  
[DeleteAsync(IRoleRepository, RoleType, IEnumerable<Role>,
CancellationToken)](M_Tessa_Roles_RolesExtensions_DeleteAsync_3.htm)|  Удаляет
указанные однотипные роли, их состав и записи о замещении.  
[DeleteUsersAsync](M_Tessa_Roles_RolesExtensions_DeleteUsersAsync.htm)|
Удаляет все записи о составах указанных ролей.  
[ExecuteInRolesLockAsync](M_Tessa_Roles_RolesExtensions_ExecuteInRolesLockAsync.htm)|
Асинхронно выполняет действие actionFunc внутри эксклюзивной блокировки на
вычисление состава ролей или замещений. Никакое другое вычисление не сможет
быть выполнено, пока выполняется действие. При этом создаётся операция
[LockOperationID](F_Tessa_Roles_RoleHelper_LockOperationID.htm) с указанным
описанием operationDescription. Возвращает признак того, что блокировка была
взята и действие было выполнено. Значение false возвращается, если блокировку
взять не удалось из-за таймаута при ожидании блокировки. При взятии блокировки
все операции не обязательно выполняются в одном и том же соединении с базой
данных. Использование нескольких соединений может быть полезно для больших
таймаутов, чтобы не удерживать одно и то же соединение несколько минут. Чтобы
гарантировать выполнение на одном и том же соединении с БД, вызовите метод
внутри блока using(dbScope.Create()) { ... }.  
[GetCardContextUsersAsync](M_Tessa_Roles_RolesExtensions_GetCardContextUsersAsync.htm)|
Возвращает состав контекстной роли для карточки с идентификатором cardID.  
[GetDeputiesAsync](M_Tessa_Roles_RolesExtensions_GetDeputiesAsync.htm)|
Возвращает список объектов
[RoleDeputyRecord](T_Tessa_Roles_RoleDeputyRecord.htm), содержащих информацию
о замещениях для указанной роли.  
[GetDisplayValue(MetaRoleType)](M_Tessa_Roles_RolesExtensions_GetDisplayValue.htm)|
Возвращает отображаемое значение заданного типа метароли.  
[GetDisplayValue(RoleType)](M_Tessa_Roles_RolesExtensions_GetDisplayValue_1.htm)|
Возвращает отображаемое значение заданного типа роли.  
[GetDisplayValue(SchedulingType)](M_Tessa_Roles_RolesExtensions_GetDisplayValue_2.htm)|
Возвращает отображаемое значение заданного способа указания расписания для
выполнения заданий.  
[GetTableName](M_Tessa_Roles_RolesExtensions_GetTableName.htm)|  Возвращает
имя таблицы, содержащей основную информацию по сущности ролевой модели.  
[GetUsersAsync](M_Tessa_Roles_RolesExtensions_GetUsersAsync.htm)|  Возвращает
список объектов [RoleUserRecord](T_Tessa_Roles_RoleUserRecord.htm), содержащих
информацию о сотрудниках, входящих в состав указанной роли.  
[IsActive](M_Tessa_Roles_RolesExtensions_IsActive.htm)|  Возвращает записи о
замещениях, которые активны в настоящий момент.  
[RegisterRolesOnClient](M_Tessa_Roles_RolesExtensions_RegisterRolesOnClient.htm)|
Выполняет регистрацию API ролей на клиенте.  
[RegisterRolesOnServer](M_Tessa_Roles_RolesExtensions_RegisterRolesOnServer.htm)|
Выполняет регистрацию API ролей.  
[UpdateErrorTextAsync(IRoleRepository, DynamicRole,
CancellationToken)](M_Tessa_Roles_RolesExtensions_UpdateErrorTextAsync.htm)|
Обновляет информацию о последней ошибке, произошедшей при пересчёте состава
заданной динамической роли.  
[UpdateErrorTextAsync(IRoleRepository, RoleGenerator,
CancellationToken)](M_Tessa_Roles_RolesExtensions_UpdateErrorTextAsync_1.htm)|
Обновляет информацию о последней ошибке, произошедшей при генерации для
заданного генератора метаролей.  
## __См. также
#### Ссылки
[Tessa.Roles - пространство имён](N_Tessa_Roles.htm)
