# RoleRepository - класс
Репозиторий для управления ролевой моделью.
## __Definition
 **Пространство имён:** [Tessa.Roles](N_Tessa_Roles.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class RoleRepository : IRoleRepository
VB __Копировать
     Public NotInheritable Class RoleRepository
    	Implements IRoleRepository
C++ __Копировать
     public ref class RoleRepository sealed : IRoleRepository
F# __Копировать
     [<SealedAttribute>]
    type RoleRepository = 
        class
            interface IRoleRepository
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ RoleRepository
Implements
    [IRoleRepository](T_Tessa_Roles_IRoleRepository.htm)
##  __Конструкторы
[RoleRepository](M_Tessa_Roles_RoleRepository__ctor.htm)|  Создаёт экземпляр
класса с указанием области видимости объекта [Tessa.Platform.Data.DbManager].  
---|---  
## __Методы
[CheckUserInCardContextAsync](M_Tessa_Roles_RoleRepository_CheckUserInCardContextAsync.htm)|
Осуществляет проверку того, что пользователь с идентификатором userID
находится для карточки с идентификатором cardID в составе контекстной роли,
определяемой запросом sqlTextForUser.  
---|---  
[DeleteAllDeputiesAsync](M_Tessa_Roles_RoleRepository_DeleteAllDeputiesAsync.htm)|
Удаляет все записи о замещениях на указанную роль.  
[DeleteAllUsersAsync](M_Tessa_Roles_RoleRepository_DeleteAllUsersAsync.htm)|
Удаляет все записи о составе указанной роли.  
[DeleteDeputiesAsync](M_Tessa_Roles_RoleRepository_DeleteDeputiesAsync.htm)|
Удаляет все записи о замещениях на указанные роли.  
[DeleteDeputyAsync](M_Tessa_Roles_RoleRepository_DeleteDeputyAsync.htm)|
Удаляет указанную запись о замещении на роль.  
[DeleteRoleAsync](M_Tessa_Roles_RoleRepository_DeleteRoleAsync.htm)| Удаляет
роль с указанными типом и идентификатором, её состав и записи о замещении.  
[DeleteRoleGeneratorAsync](M_Tessa_Roles_RoleRepository_DeleteRoleGeneratorAsync.htm)|
Удаляет генератор метаролей с указанным идентификатором, а также все его
метароли.  
[DeleteRolesAsync](M_Tessa_Roles_RoleRepository_DeleteRolesAsync.htm)| Удаляет
однотипные роли с указанными типом и идентификаторами, их состав и записи о
замещении.  
[DeleteUserAsync](M_Tessa_Roles_RoleRepository_DeleteUserAsync.htm)| Удаляет
указанную запись о составе роли.  
[DeleteUsersAsync](M_Tessa_Roles_RoleRepository_DeleteUsersAsync.htm)| Удаляет
все записи о составах указанных ролей.  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetAllContextRolesAsync](M_Tessa_Roles_RoleRepository_GetAllContextRolesAsync.htm)|
Возвращает список всех контекстных ролей [Tessa.Roles.ContextRole].  
[GetAllDepartmentRolesAsync](M_Tessa_Roles_RoleRepository_GetAllDepartmentRolesAsync.htm)|
Возвращает список всех ролей департаментов [Tessa.Roles.DepartmentRole].  
[GetAllDeputiesAsync](M_Tessa_Roles_RoleRepository_GetAllDeputiesAsync.htm)|
Возвращает список всех записей о замещениях на роли
[Tessa.Roles.RoleDeputyRecord].  
[GetAllDynamicRolesAsync](M_Tessa_Roles_RoleRepository_GetAllDynamicRolesAsync.htm)|
Возвращает список всех динамических ролей [Tessa.Roles.DynamicRole].  
[GetAllMetaRolesAsync](M_Tessa_Roles_RoleRepository_GetAllMetaRolesAsync.htm)|
Возвращает список всех метаролей [Tessa.Roles.MetaRole].  
[GetAllPersonalRolesAsync](M_Tessa_Roles_RoleRepository_GetAllPersonalRolesAsync.htm)|
Возвращает список всех персональных ролей [Tessa.Roles.PersonalRole].  
[GetAllRoleGeneratorsAsync](M_Tessa_Roles_RoleRepository_GetAllRoleGeneratorsAsync.htm)|
Возвращает список всех генераторов метаролей [Tessa.Roles.RoleGenerator].  
[GetAllRolesAsync](M_Tessa_Roles_RoleRepository_GetAllRolesAsync.htm)|
Возвращает список с базовой информацией по всем ролям [Tessa.Roles.Role].  
[GetAllStaticRolesAsync](M_Tessa_Roles_RoleRepository_GetAllStaticRolesAsync.htm)|
Возвращает список всех статических ролей [Tessa.Roles.StaticRole].  
[GetAllTaskRolesAsync](M_Tessa_Roles_RoleRepository_GetAllTaskRolesAsync.htm)|
Возвращает список всех ролей заданий [Tessa.Roles.TaskRole].  
[GetAllUsersAsync](M_Tessa_Roles_RoleRepository_GetAllUsersAsync.htm)|
Возвращает список всех записей о составах ролей [Tessa.Roles.RoleUserRecord].  
[GetCardContextUsersAsync](M_Tessa_Roles_RoleRepository_GetCardContextUsersAsync.htm)|
Возвращает состав контекстной роли, определяемой запросом cardID, для карточки
с идентификатором cardID.  
[GetContextRoleAsync](M_Tessa_Roles_RoleRepository_GetContextRoleAsync.htm)|
Возвращает объект [Tessa.Roles.ContextRole], содержащий информацию о
контекстной роли с указанным идентификатором, или null, если роль отсутствует
или не является контекстной.  
[GetDepartmentRoleAsync](M_Tessa_Roles_RoleRepository_GetDepartmentRoleAsync.htm)|
Возвращает объект [Tessa.Roles.DepartmentRole], содержащий информацию о роли
департамента с указанным идентификатором, или null, если роль отсутствует или
не является ролью департамента.  
[GetDeputiesAsync](M_Tessa_Roles_RoleRepository_GetDeputiesAsync.htm)|
Возвращает список объектов [Tessa.Roles.RoleDeputyRecord], содержащих
информацию о замещениях для роли с указанным идентификатором.  
[GetDynamicRoleAsync](M_Tessa_Roles_RoleRepository_GetDynamicRoleAsync.htm)|
Возвращает объект [Tessa.Roles.DynamicRole], содержащий информацию о
динамической роли с указанным идентификатором, или null, если роль отсутствует
или не является динамической.  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetMetaRoleAsync](M_Tessa_Roles_RoleRepository_GetMetaRoleAsync.htm)|
Возвращает объект [Tessa.Roles.MetaRole], содержащий информацию о метароли с
указанным идентификатором, или null, если роль отсутствует или не является
метаролью.  
[GetPersonalRoleAsync](M_Tessa_Roles_RoleRepository_GetPersonalRoleAsync.htm)|
Возвращает объект [Tessa.Roles.PersonalRole], содержащий информацию о
персональной роли с указанным идентификатором, или null, если роль отсутствует
или не является персональной.  
[GetRoleAsync](M_Tessa_Roles_RoleRepository_GetRoleAsync.htm)|  Возвращает
объект [Tessa.Roles.Role], содержащий базовую информацию о роли с указанным
идентификатором, или null, если роль отсутствует.  
[GetRoleGeneratorAsync](M_Tessa_Roles_RoleRepository_GetRoleGeneratorAsync.htm)|
Возвращает объект [Tessa.Roles.RoleGenerator], содержащий информацию о
генераторе метаролей с указанным идентификатором.  
[GetRoleIDListAsync](M_Tessa_Roles_RoleRepository_GetRoleIDListAsync.htm)|
Возвращает идентификаторов ролей, найденных по имени. Не производит поиск
среди временных ролей.  
[GetStaticRoleAsync](M_Tessa_Roles_RoleRepository_GetStaticRoleAsync.htm)|
Возвращает объект [Tessa.Roles.StaticRole], содержащий информацию о
статической роли с указанным идентификатором, или null, если роль отсутствует
или не является статической.  
[GetTaskRoleAsync](M_Tessa_Roles_RoleRepository_GetTaskRoleAsync.htm)|
Возвращает объект [Tessa.Roles.TaskRole], содержащий информацию о роли задания
с указанным идентификатором, или null, если роль отсутствует или не является
ролью задания.  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetUsersAsync](M_Tessa_Roles_RoleRepository_GetUsersAsync.htm)|  Возвращает
список объектов [Tessa.Roles.RoleUserRecord], содержащих информацию о
сотрудниках, входящих в состав роли с указанным идентификатором.  
[InsertAsync(ContextRole,
CancellationToken)](M_Tessa_Roles_RoleRepository_InsertAsync.htm)|  Добавляет
информацию по указанной контекстной роли. Записи о составе и замещениях
игнорируются. Устанавливает поле [Tessa.Roles.Role.RoleType] указанной роли
после добавления.  
[InsertAsync(DepartmentRole,
CancellationToken)](M_Tessa_Roles_RoleRepository_InsertAsync_1.htm)|
Добавляет информацию по указанной роли департамента. Добавляет записи о
составе и замещениях при их наличии. Устанавливает поле
[Tessa.Roles.Role.RoleType] указанной роли после добавления.  
[InsertAsync(DynamicRole,
CancellationToken)](M_Tessa_Roles_RoleRepository_InsertAsync_2.htm)|
Добавляет информацию по указанной динамической роли. Добавляет записи о
составе и замещениях при их наличии. Устанавливает поле
[Tessa.Roles.Role.RoleType] указанной роли после добавления.  
[InsertAsync(MetaRole,
CancellationToken)](M_Tessa_Roles_RoleRepository_InsertAsync_3.htm)|
Добавляет информацию по указанной метароли. Добавляет записи о составе и
замещениях при их наличии. Устанавливает поле [Tessa.Roles.Role.RoleType]
указанной роли после добавления.  
[InsertAsync(PersonalRole,
CancellationToken)](M_Tessa_Roles_RoleRepository_InsertAsync_4.htm)|
Добавляет информацию по указанной персональной роли. Добавляет записи о
составе и замещениях при их наличии. Устанавливает поле
[Tessa.Roles.Role.RoleType] указанной роли после добавления.  
[InsertAsync(RoleDeputyRecord,
CancellationToken)](M_Tessa_Roles_RoleRepository_InsertAsync_5.htm)| Добавляет
запись о замещении на роль.  
[InsertAsync(RoleGenerator,
CancellationToken)](M_Tessa_Roles_RoleRepository_InsertAsync_6.htm)| Добавляет
информацию по указанному генератору метаролей.  
[InsertAsync(RoleUserRecord,
CancellationToken)](M_Tessa_Roles_RoleRepository_InsertAsync_7.htm)| Добавляет
запись о составе роли.  
[InsertAsync(StaticRole,
CancellationToken)](M_Tessa_Roles_RoleRepository_InsertAsync_8.htm)|
Добавляет информацию по указанной статической роли. Добавляет записи о составе
и замещениях при их наличии. Устанавливает поле [Tessa.Roles.Role.RoleType]
указанной роли после добавления.  
[InsertAsync(TaskRole,
CancellationToken)](M_Tessa_Roles_RoleRepository_InsertAsync_9.htm)|
Добавляет информацию по указанной роли задания. Добавляет записи о составе и
замещениях при их наличии. Устанавливает поле [Tessa.Roles.Role.RoleType]
указанной роли после добавления.  
[InsertDeputiesAsync](M_Tessa_Roles_RoleRepository_InsertDeputiesAsync.htm)|
Добавляет несколько записей о замещениях на роли.  
[InsertUsersAsync](M_Tessa_Roles_RoleRepository_InsertUsersAsync.htm)|
Добавляет несколько записей о составах ролей.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[UpdateAsync(ContextRole,
CancellationToken)](M_Tessa_Roles_RoleRepository_UpdateAsync.htm)| Обновляет
информацию по указанной контекстной роли.  
[UpdateAsync(DepartmentRole,
CancellationToken)](M_Tessa_Roles_RoleRepository_UpdateAsync_1.htm)| Обновляет
информацию по указанной роли департамента.  
[UpdateAsync(DynamicRole,
CancellationToken)](M_Tessa_Roles_RoleRepository_UpdateAsync_2.htm)| Обновляет
информацию по указанной динамической роли.  
[UpdateAsync(MetaRole,
CancellationToken)](M_Tessa_Roles_RoleRepository_UpdateAsync_3.htm)| Обновляет
информацию по указанной метароли.  
[UpdateAsync(PersonalRole,
CancellationToken)](M_Tessa_Roles_RoleRepository_UpdateAsync_4.htm)| Обновляет
информацию по указанной персональной роли.  
[UpdateAsync(RoleDeputyRecord,
CancellationToken)](M_Tessa_Roles_RoleRepository_UpdateAsync_5.htm)| Обновляет
запись о замещении на роль.  
[UpdateAsync(RoleGenerator,
CancellationToken)](M_Tessa_Roles_RoleRepository_UpdateAsync_6.htm)| Обновляет
информацию по указанному генератору метаролей.  
[UpdateAsync(RoleUserRecord,
CancellationToken)](M_Tessa_Roles_RoleRepository_UpdateAsync_7.htm)| Обновляет
запись о составе роли.  
[UpdateAsync(StaticRole,
CancellationToken)](M_Tessa_Roles_RoleRepository_UpdateAsync_8.htm)| Обновляет
информацию по указанной статической роли.  
[UpdateAsync(TaskRole,
CancellationToken)](M_Tessa_Roles_RoleRepository_UpdateAsync_9.htm)| Обновляет
информацию по указанной роли задания.  
[UpdateBasicRoleAsync](M_Tessa_Roles_RoleRepository_UpdateBasicRoleAsync.htm)|
Обновляет базовую информацию по указанной роли.  
[UpdateDynamicRoleLastErrorAsync](M_Tessa_Roles_RoleRepository_UpdateDynamicRoleLastErrorAsync.htm)|
Обновляет информацию о последней ошибке, произошедшей при пересчёте состава
заданной динамической роли.  
[UpdateDynamicRoleLastSuccessfulRecalcAsync](M_Tessa_Roles_RoleRepository_UpdateDynamicRoleLastSuccessfulRecalcAsync.htm)|
Обновляет дату последней успешной операции расчта состава заданной
динамической роли  
[UpdateRoleGeneratorLastErrorAsync](M_Tessa_Roles_RoleRepository_UpdateRoleGeneratorLastErrorAsync.htm)|
Обновляет информацию о последней ошибке, произошедшей при генерации для
заданного генератора метаролей.  
[UpdateRoleGeneratorLastSuccessfulRecalcDateAsync](M_Tessa_Roles_RoleRepository_UpdateRoleGeneratorLastSuccessfulRecalcDateAsync.htm)|
Обновляет дату последней успешной операции расчёта метаролей, для заданного
генератора метаролей.  
##  __Методы расширения
[CheckUserInCardContextAsync](M_Tessa_Roles_RolesExtensions_CheckUserInCardContextAsync.htm)|
Осуществляет проверку того, что пользователь с идентификатором userID
находится для карточки с идентификатором cardID в составе контекстной роли
role.  
(Определяется [RolesExtensions](T_Tessa_Roles_RolesExtensions.htm))  
---|---  
[DeleteAllDeputiesAsync](M_Tessa_Roles_RolesExtensions_DeleteAllDeputiesAsync.htm)|
Удаляет все записи о заместителях на указанную роль.  
(Определяется [RolesExtensions](T_Tessa_Roles_RolesExtensions.htm))  
[DeleteAllUsersAsync](M_Tessa_Roles_RolesExtensions_DeleteAllUsersAsync.htm)|
Удаляет все записи о составе указанной роли.  
(Определяется [RolesExtensions](T_Tessa_Roles_RolesExtensions.htm))  
[DeleteAsync](M_Tessa_Roles_RolesExtensions_DeleteAsync.htm)|  Удаляет
указанную роль, её состав и записи о замещении.  
(Определяется [RolesExtensions](T_Tessa_Roles_RolesExtensions.htm))  
[DeleteAsync](M_Tessa_Roles_RolesExtensions_DeleteAsync_1.htm)|  Удаляет
запись о замещении на роль.  
(Определяется [RolesExtensions](T_Tessa_Roles_RolesExtensions.htm))  
[DeleteAsync](M_Tessa_Roles_RolesExtensions_DeleteAsync_2.htm)|  Удаляет
генератор метаролей, а также все его метароли.  
(Определяется [RolesExtensions](T_Tessa_Roles_RolesExtensions.htm))  
[DeleteAsync](M_Tessa_Roles_RolesExtensions_DeleteAsync_4.htm)|  Удаляет
запись о составе роли.  
(Определяется [RolesExtensions](T_Tessa_Roles_RolesExtensions.htm))  
[DeleteAsync](M_Tessa_Roles_RolesExtensions_DeleteAsync_3.htm)|  Удаляет
указанные однотипные роли, их состав и записи о замещении.  
(Определяется [RolesExtensions](T_Tessa_Roles_RolesExtensions.htm))  
[DeleteUsersAsync](M_Tessa_Roles_RolesExtensions_DeleteUsersAsync.htm)|
Удаляет все записи о составах указанных ролей.  
(Определяется [RolesExtensions](T_Tessa_Roles_RolesExtensions.htm))  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[GetCardContextUsersAsync](M_Tessa_Roles_RolesExtensions_GetCardContextUsersAsync.htm)|
Возвращает состав контекстной роли для карточки с идентификатором cardID.  
(Определяется [RolesExtensions](T_Tessa_Roles_RolesExtensions.htm))  
[GetDeputiesAsync](M_Tessa_Roles_RolesExtensions_GetDeputiesAsync.htm)|
Возвращает список объектов
[RoleDeputyRecord](T_Tessa_Roles_RoleDeputyRecord.htm), содержащих информацию
о замещениях для указанной роли.  
(Определяется [RolesExtensions](T_Tessa_Roles_RolesExtensions.htm))  
[GetUsersAsync](M_Tessa_Roles_RolesExtensions_GetUsersAsync.htm)|  Возвращает
список объектов [RoleUserRecord](T_Tessa_Roles_RoleUserRecord.htm), содержащих
информацию о сотрудниках, входящих в состав указанной роли.  
(Определяется [RolesExtensions](T_Tessa_Roles_RolesExtensions.htm))  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[UpdateErrorTextAsync](M_Tessa_Roles_RolesExtensions_UpdateErrorTextAsync.htm)|
Обновляет информацию о последней ошибке, произошедшей при пересчёте состава
заданной динамической роли.  
(Определяется [RolesExtensions](T_Tessa_Roles_RolesExtensions.htm))  
[UpdateErrorTextAsync](M_Tessa_Roles_RolesExtensions_UpdateErrorTextAsync_1.htm)|
Обновляет информацию о последней ошибке, произошедшей при генерации для
заданного генератора метаролей.  
(Определяется [RolesExtensions](T_Tessa_Roles_RolesExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Roles - пространство имён](N_Tessa_Roles.htm)
