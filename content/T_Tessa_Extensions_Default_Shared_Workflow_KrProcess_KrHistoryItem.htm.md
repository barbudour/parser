# KrHistoryItem - класс
Запись для листа согласования, соответствующая выполненному заданию.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class KrHistoryItem
VB __Копировать
     Public NotInheritable Class KrHistoryItem
C++ __Копировать
     public ref class KrHistoryItem sealed
F# __Копировать
     [<SealedAttribute>]
    type KrHistoryItem = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ KrHistoryItem
##  __Конструкторы
[KrHistoryItem](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrHistoryItem__ctor.htm)|
Инициализирует новый экземпляр класса KrHistoryItem  
---|---  
##  __Свойства
[AuthorName](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrHistoryItem_AuthorName.htm)|
Имя пользователя, который считается автором задания.  
---|---  
[Completed](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrHistoryItem_Completed.htm)|
Фактическая дата выполнения задания.  
[CompletedQuants](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrHistoryItem_CompletedQuants.htm)|
Количество квантов календаря, которое потребовалось для завершения задания,
или null, если кванты календаря не рассчитаны.  
[Created](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrHistoryItem_Created.htm)|
Дата создания задания.  
[Cycle](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrHistoryItem_Cycle.htm)|
Номер цикла согласования.  
[Files](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrHistoryItem_Files.htm)|
Список информации по файлам, изменённым в процессе выполнения задания, или
null, если файлы отсутствуют.  
[OptionCaption](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrHistoryItem_OptionCaption.htm)|
Выбранный вариант завершения.  
[Planned](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrHistoryItem_Planned.htm)|
Запланированная дата выполнения задания.  
[Result](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrHistoryItem_Result.htm)|
Описание результата выполненного задания. Строка никогда не равна null.  
[RoleName](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrHistoryItem_RoleName.htm)|
Роль, на которую было назначено задание.  
[RowID](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrHistoryItem_RowID.htm)|
Идентификатор задания.  
[TaskTypeID](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrHistoryItem_TaskTypeID.htm)|
Тип задания  
[UserDepartment](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrHistoryItem_UserDepartment.htm)|
Департамент сотрудника на которого назначено задание.  
[UserName](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrHistoryItem_UserName.htm)|
Имя пользователя, который завершил задание.  
[UserPosition](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrHistoryItem_UserPosition.htm)|
Должность сотрудника на которого назначено задание.  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
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
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
