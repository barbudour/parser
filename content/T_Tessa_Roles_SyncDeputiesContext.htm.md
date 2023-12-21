# SyncDeputiesContext - класс
Контекст сихнронизации заместителей.
## __Definition
 **Пространство имён:** [Tessa.Roles](N_Tessa_Roles.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class SyncDeputiesContext
VB __Копировать
     Public Class SyncDeputiesContext
C++ __Копировать
     public ref class SyncDeputiesContext
F# __Копировать
     type SyncDeputiesContext = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ SyncDeputiesContext
##  __Конструкторы
[SyncDeputiesContext](M_Tessa_Roles_SyncDeputiesContext__ctor.htm)|
Инициализирует новый экземпляр класса SyncDeputiesContext  
---|---  
##  __Свойства
[BuilderFactory](P_Tessa_Roles_SyncDeputiesContext_BuilderFactory.htm)|
Объект для построения запросов к базе данных.  
---|---  
[CancellationToken](P_Tessa_Roles_SyncDeputiesContext_CancellationToken.htm)|
Объект, с помозью которого можно отменить асинхронную задачу.  
[CommitDeputiesAsyncFunc](P_Tessa_Roles_SyncDeputiesContext_CommitDeputiesAsyncFunc.htm)|
Метод для коммита текущего контекста.  
[Db](P_Tessa_Roles_SyncDeputiesContext_Db.htm)|  Объект для выполнения
запросов к базе данных.  
[Limit](P_Tessa_Roles_SyncDeputiesContext_Limit.htm)|  Предел загрузки
элементов.  
[Logger](P_Tessa_Roles_SyncDeputiesContext_Logger.htm)|  Логгер.  
[NeedContinue](P_Tessa_Roles_SyncDeputiesContext_NeedContinue.htm)|
Определяет, нужно ли продолжить синхронизацию.  
[NeedContinueNewUsers](P_Tessa_Roles_SyncDeputiesContext_NeedContinueNewUsers.htm)|
Определяет, нужно ли продолжить загрузку новых сотрудников.  
[NeedContinueOldUsers](P_Tessa_Roles_SyncDeputiesContext_NeedContinueOldUsers.htm)|
Определяет, нужно ли продолжить загрузку текущих сотрудников.  
[NewUsersForAdd](P_Tessa_Roles_SyncDeputiesContext_NewUsersForAdd.htm)|
Список новых сотрудников, которые должны быть добавлены в текущей итерации.  
[NewUsersFrom](P_Tessa_Roles_SyncDeputiesContext_NewUsersFrom.htm)|
Определяет, с какого индекса происходит синхронзация сотрудников из списка
[NewUsersList](P_Tessa_Roles_SyncDeputiesContext_NewUsersList.htm).  
[NewUsersFromID](P_Tessa_Roles_SyncDeputiesContext_NewUsersFromID.htm)|
Определяет, с какого идентификатора роли загружены новые сотрудники.  
[NewUsersList](P_Tessa_Roles_SyncDeputiesContext_NewUsersList.htm)|  Список
новых сотрудников.  
[NewUsersTo](P_Tessa_Roles_SyncDeputiesContext_NewUsersTo.htm)|  Определяет,
по какой индекс происходит синхронзация сотрудников из списка
[NewUsersList](P_Tessa_Roles_SyncDeputiesContext_NewUsersList.htm).  
[NewUsersToID](P_Tessa_Roles_SyncDeputiesContext_NewUsersToID.htm)|
Определяет, по какоой идентификатор роли загружены новые сотрудники.  
[OldUsers](P_Tessa_Roles_SyncDeputiesContext_OldUsers.htm)|  Список текущих
сотрудников.  
[OldUsersFrom](P_Tessa_Roles_SyncDeputiesContext_OldUsersFrom.htm)|
Определяет, с какого индекса происходит синхронзация сотрудников из списка
[OldUsers](P_Tessa_Roles_SyncDeputiesContext_OldUsers.htm).  
[OldUsersTo](P_Tessa_Roles_SyncDeputiesContext_OldUsersTo.htm)|  Определяет,
по какой индекс происходит синхронзация сотрудников из списка
[OldUsers](P_Tessa_Roles_SyncDeputiesContext_OldUsers.htm).  
[OldUsersToID](P_Tessa_Roles_SyncDeputiesContext_OldUsersToID.htm)|
Определяет, по какой идентификатор роли загружены списки текущих сотрудников.  
[RoleIDs](P_Tessa_Roles_SyncDeputiesContext_RoleIDs.htm)|  Список
идентификаторов ролей, заместителей которых нужно обновить, или null, если нет
фильтрации по ролям.  
[RolesOnUpdate](P_Tessa_Roles_SyncDeputiesContext_RolesOnUpdate.htm)|  Список
ролей, обновление которых происходит в данный момент.  
[RoleTypes](P_Tessa_Roles_SyncDeputiesContext_RoleTypes.htm)|  Список типов
ролей, заместителей которых нужно обновить, или null, если нет фильтрации по
типу роли.  
[UpdateDate](P_Tessa_Roles_SyncDeputiesContext_UpdateDate.htm)|  Дата
обновления заместителей.  
[UserIDsByRole](P_Tessa_Roles_SyncDeputiesContext_UserIDsByRole.htm)|  Набор
идентификаторов сотрудников по ролям. Заполняется в прцоессе обработки.  
## __Методы
[CommitDeputiesAsync](M_Tessa_Roles_SyncDeputiesContext_CommitDeputiesAsync.htm)|
Метод для коммита текущего состояния контекста в базу. Если не задано действие
для коммита
[CommitDeputiesAsyncFunc](P_Tessa_Roles_SyncDeputiesContext_CommitDeputiesAsyncFunc.htm),
метод выбросит исключение.  
---|---  
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
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[SetOldUsersTo](M_Tessa_Roles_SyncDeputiesContext_SetOldUsersTo.htm)|  Метод
для установки значения
[OldUsersTo](P_Tessa_Roles_SyncDeputiesContext_OldUsersTo.htm) по
идентификатору роли, до которой должна выполняться обработка. Параметр include
определяет, должна ли искомая роль быть включена в список для обработки.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
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
##  __См. также
#### Ссылки
[Tessa.Roles - пространство имён](N_Tessa_Roles.htm)
