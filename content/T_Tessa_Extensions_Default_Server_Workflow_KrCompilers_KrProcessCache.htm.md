# KrProcessCache - класс
Кэш данных из карточек подсистемы маршрутов.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrCompilers](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class KrProcessCache : IKrProcessCache, 
    	IDisposable
VB __Копировать
     Public NotInheritable Class KrProcessCache
    	Implements IKrProcessCache, IDisposable
C++ __Копировать
     public ref class KrProcessCache sealed : IKrProcessCache, 
    	IDisposable
F# __Копировать
     [<SealedAttribute>]
    type KrProcessCache = 
        class
            interface IKrProcessCache
            interface IDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ KrProcessCache
Implements
    [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable), [IKrProcessCache](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrProcessCache.htm)
##  __Конструкторы
[KrProcessCache](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrProcessCache__ctor.htm)|
Инициализирует новый экземпляр класса KrProcessCache.  
---|---  
## __Методы
[Dispose](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrProcessCache_Dispose.htm)|
Performs application-defined tasks associated with freeing, releasing, or
resetting unmanaged resources.  
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
[GetActionsByTypeAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrProcessCache_GetActionsByTypeAsync.htm)|
Возвращает коллекцию, содержащую информацию о действиях указанного типа.  
[GetAllActionsAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrProcessCache_GetAllActionsAsync.htm)|
Возвращает словарь, содержащий информацию о всех действиях.  
[GetAllButtonsAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrProcessCache_GetAllButtonsAsync.htm)|
Возвращает словарь, содержащий информацию о всех кнопках вторичных процессов.  
[GetAllCommonMethodsAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrProcessCache_GetAllCommonMethodsAsync.htm)|
Возвращает коллекцию с информацией о всех базовых методах.  
[GetAllPureProcessesAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrProcessCache_GetAllPureProcessesAsync.htm)|
Возвращает информацию о всех вторичных процессах типа "простой процесс".  
[GetAllRuntimeStagesAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrProcessCache_GetAllRuntimeStagesAsync.htm)|
Возвращает словарь, содержащий информацию о всех рантайм скриптах.  
[GetAllStageGroupsAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrProcessCache_GetAllStageGroupsAsync.htm)|
Возвращает информацию о всех группах этапов.  
[GetAllStagesByTemplatesAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrProcessCache_GetAllStagesByTemplatesAsync.htm)|
Возвращает коллекцию, содержащую информацию о этапах, расположенных в шаблонах
этапов.  
[GetAllStageTemplatesAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrProcessCache_GetAllStageTemplatesAsync.htm)|
Возвращает словарь, содержащий информацию о всех шаблонах этапов.  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetOrderedStageGroupsAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrProcessCache_GetOrderedStageGroupsAsync.htm)|
Возвращает список всех групп этапов.  
[GetStageGroupsForSecondaryProcessAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrProcessCache_GetStageGroupsForSecondaryProcessAsync.htm)|
Возвращает коллекцию с информацией о группах этапов для заданного процесса.  
[GetStageTemplatesForGroupAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrProcessCache_GetStageTemplatesForGroupAsync.htm)|
Возвращает коллекцию с информацией о всех шаблонах этапов, входящих в заданную
группу.  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[InvalidateAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrProcessCache_InvalidateAsync.htm)|
Сбрасывает кэш.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetSecondaryProcessAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrProcessCache_TryGetSecondaryProcessAsync.htm)|
Возвращает вторичный процесс по его идентификатору.  
## __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[GetSecondaryProcessAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrProcessCacheExtensions_GetSecondaryProcessAsync.htm)|
Возвращает вторичный процесс по его идентификатору.  
(Определяется
[KrProcessCacheExtensions](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrProcessCacheExtensions.htm))  
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
[Tessa.Extensions.Default.Server.Workflow.KrCompilers - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers.htm)
