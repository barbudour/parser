# KrTaskItem - класс
Запись для листа согласования, соответствующая текущему заданию.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class KrTaskItem
VB __Копировать
     Public NotInheritable Class KrTaskItem
C++ __Копировать
     public ref class KrTaskItem sealed
F# __Копировать
     [<SealedAttribute>]
    type KrTaskItem = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ KrTaskItem
##  __Конструкторы
[KrTaskItem](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrTaskItem__ctor.htm)|
Инициализирует новый экземпляр класса KrTaskItem  
---|---  
##  __Свойства
[Created](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrTaskItem_Created.htm)|
Дата создание задания.  
---|---  
[CreatedQuants](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrTaskItem_CreatedQuants.htm)|
Количество квантов календаря с момента создания задания, или null, если кванты
календаря не рассчитаны.  
[InProgress](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrTaskItem_InProgress.htm)|
Дата взятия задания в работу или null, если задание ещё не взято в работу.  
[InProgressQuants](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrTaskItem_InProgressQuants.htm)|
Количество квантов календаря, в течение которых задание находится в работе,
или null, если задание ещё не взято в работу или кванты календаря не
рассчитаны.  
[RemainingQuants](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrTaskItem_RemainingQuants.htm)|
Количество квантов календаря, оставшихся до запланированного завершения
задания, или null, если кванты календаря не рассчитаны.  
[RoleName](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrTaskItem_RoleName.htm)|
Роль, на которую назначено задание.  
[UserName](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrTaskItem_UserName.htm)|
Пользователь, взявший задание в работу, или пустая строка, если задание ещё не
взято в работу.  
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
