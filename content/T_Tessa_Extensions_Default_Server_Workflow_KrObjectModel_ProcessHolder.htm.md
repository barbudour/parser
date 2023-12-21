# ProcessHolder - класс
Предоставляет информацию по текущему и основному процессу.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrObjectModel](N_Tessa_Extensions_Default_Server_Workflow_KrObjectModel.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ProcessHolder
VB __Копировать
     Public NotInheritable Class ProcessHolder
C++ __Копировать
     public ref class ProcessHolder sealed
F# __Копировать
     [<SealedAttribute>]
    type ProcessHolder = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ProcessHolder
##  __Конструкторы
[ProcessHolder](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_ProcessHolder__ctor.htm)|
Инициализирует новый экземпляр класса ProcessHolder  
---|---  
##  __Свойства
[MainProcessCommonInfo](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_ProcessHolder_MainProcessCommonInfo.htm)|
Возвращает или задаёт информацию о текущем процессе.  
---|---  
[MainProcessType](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_ProcessHolder_MainProcessType.htm)|
Возвращает или задаёт имя типа родительского процесса.  
[MainWorkflowProcess](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_ProcessHolder_MainWorkflowProcess.htm)|
Возвращает или задаёт объектную модель текущего и основного процесса.  
[NestedProcessCommonInfos](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_ProcessHolder_NestedProcessCommonInfos.htm)|
Возвращает или задаёт набор объектов типа
[NestedProcessCommonInfo](T_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_NestedProcessCommonInfo.htm)
содержащих информацию о вложенных процессах. Ключ - идентификатор вложенного
процесса, значение - информация о вложенном процессе.  
[NestedWorkflowProcesses](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_ProcessHolder_NestedWorkflowProcesses.htm)|
Возвращает словарь содержащий информацию по вложенным процессам. Ключ -
идентификатор процесса, значение - объектная модель процесса.  
[Persistent](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_ProcessHolder_Persistent.htm)|
Возвращает или задаёт значение, показывающее, что текущий объект является
персистентным.  
[PrimaryProcessCommonInfo](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_ProcessHolder_PrimaryProcessCommonInfo.htm)|
Возвращает или задаёт информацию об основном процессе.  
[ProcessHolderID](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_ProcessHolder_ProcessHolderID.htm)|
Возвращает или задаёт идентификатор по которому можно получить процессный
сателлит.  
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
[SetNestedProcessCommonInfosList](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_ProcessHolder_SetNestedProcessCommonInfosList.htm)|
Устанавливает значение свойства
[NestedProcessCommonInfos](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_ProcessHolder_NestedProcessCommonInfos.htm)
указанным списком объектов типа
[NestedProcessCommonInfo](T_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_NestedProcessCommonInfo.htm)
содержащих информацию по вложенным процессам.  
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
[Tessa.Extensions.Default.Server.Workflow.KrObjectModel - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrObjectModel.htm)
