# WfTaskSatelliteHandler - класс
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.Wf](N_Tessa_Extensions_Default_Server_Workflow_Wf.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class WfTaskSatelliteHandler : SatelliteHandlerBase
VB __Копировать
     Public NotInheritable Class WfTaskSatelliteHandler
    	Inherits SatelliteHandlerBase
C++ __Копировать
     public ref class WfTaskSatelliteHandler sealed : public SatelliteHandlerBase
F# __Копировать
     [<SealedAttribute>]
    type WfTaskSatelliteHandler = 
        class
            inherit SatelliteHandlerBase
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[SatelliteHandlerBase](T_Tessa_Extensions_Platform_Server_Cards_Satellites_Handlers_SatelliteHandlerBase.htm) __ WfTaskSatelliteHandler
##  __Конструкторы
[WfTaskSatelliteHandler](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfTaskSatelliteHandler__ctor.htm)|
Инициализирует новый экземпляр класса WfTaskSatelliteHandler  
---|---  
##  __Методы
[CheckFileAccessAsync](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfTaskSatelliteHandler_CheckFileAccessAsync.htm)|  
(Переопределяет
[SatelliteHandlerBase.CheckFileAccessAsync(ICardGetFileContentExtensionContext,
Guid)](M_Tessa_Extensions_Platform_Server_Cards_Satellites_Handlers_SatelliteHandlerBase_CheckFileAccessAsync.htm))  
---|---  
[CheckFileVersionsAccessAsync](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfTaskSatelliteHandler_CheckFileVersionsAccessAsync.htm)|  
(Переопределяет
[SatelliteHandlerBase.CheckFileVersionsAccessAsync(ICardGetFileVersionsExtensionContext,
Guid)](M_Tessa_Extensions_Platform_Server_Cards_Satellites_Handlers_SatelliteHandlerBase_CheckFileVersionsAccessAsync.htm))  
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
[GetExternalFileSourcesAsync](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfTaskSatelliteHandler_GetExternalFileSourcesAsync.htm)|  
(Переопределяет
[SatelliteHandlerBase.GetExternalFileSourcesAsync(ICardGetExtensionContext,
Card, Guid,
Nullable<Guid>)](M_Tessa_Extensions_Platform_Server_Cards_Satellites_Handlers_SatelliteHandlerBase_GetExternalFileSourcesAsync.htm))  
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
[IsMainCardFileAsync](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfTaskSatelliteHandler_IsMainCardFileAsync.htm)|  
(Переопределяет
[SatelliteHandlerBase.IsMainCardFileAsync(ICardStoreExtensionContext, Card,
CardFile)](M_Tessa_Extensions_Platform_Server_Cards_Satellites_Handlers_SatelliteHandlerBase_IsMainCardFileAsync.htm))  
[IsMainCardTypeAsync](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfTaskSatelliteHandler_IsMainCardTypeAsync.htm)|  
(Переопределяет [SatelliteHandlerBase.IsMainCardTypeAsync(CardType,
CancellationToken)](M_Tessa_Extensions_Platform_Server_Cards_Satellites_Handlers_SatelliteHandlerBase_IsMainCardTypeAsync.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[PrepareMainCardFileToStoreAsync](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfTaskSatelliteHandler_PrepareMainCardFileToStoreAsync.htm)|  
(Переопределяет
[SatelliteHandlerBase.PrepareMainCardFileToStoreAsync(ICardStoreExtensionContext,
Card,
CardFile)](M_Tessa_Extensions_Platform_Server_Cards_Satellites_Handlers_SatelliteHandlerBase_PrepareMainCardFileToStoreAsync.htm))  
[PrepareSatelliteForBackupAsync](M_Tessa_Extensions_Platform_Server_Cards_Satellites_Handlers_SatelliteHandlerBase_PrepareSatelliteForBackupAsync.htm)|  
(Унаследован от
[SatelliteHandlerBase](T_Tessa_Extensions_Platform_Server_Cards_Satellites_Handlers_SatelliteHandlerBase.htm))  
[PrepareSatelliteForCreateAsync](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfTaskSatelliteHandler_PrepareSatelliteForCreateAsync.htm)|  
(Переопределяет
[SatelliteHandlerBase.PrepareSatelliteForCreateAsync(ICardGetExtensionContext,
Card, Guid,
Nullable<Guid>)](M_Tessa_Extensions_Platform_Server_Cards_Satellites_Handlers_SatelliteHandlerBase_PrepareSatelliteForCreateAsync.htm))  
[PrepareSatelliteForDeleteAsync](M_Tessa_Extensions_Platform_Server_Cards_Satellites_Handlers_SatelliteHandlerBase_PrepareSatelliteForDeleteAsync.htm)|  
(Унаследован от
[SatelliteHandlerBase](T_Tessa_Extensions_Platform_Server_Cards_Satellites_Handlers_SatelliteHandlerBase.htm))  
[PrepareSatelliteForExportAsync](M_Tessa_Extensions_Platform_Server_Cards_Satellites_Handlers_SatelliteHandlerBase_PrepareSatelliteForExportAsync.htm)|  
(Унаследован от
[SatelliteHandlerBase](T_Tessa_Extensions_Platform_Server_Cards_Satellites_Handlers_SatelliteHandlerBase.htm))  
[PrepareSatelliteForGetAsync](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfTaskSatelliteHandler_PrepareSatelliteForGetAsync.htm)|  
(Переопределяет
[SatelliteHandlerBase.PrepareSatelliteForGetAsync(ICardGetExtensionContext,
Card, Guid, Nullable<Guid>, Func<CancellationToken,
ValueTask<Card>>)](M_Tessa_Extensions_Platform_Server_Cards_Satellites_Handlers_SatelliteHandlerBase_PrepareSatelliteForGetAsync.htm))  
[PrepareSatelliteForImportAsync](M_Tessa_Extensions_Platform_Server_Cards_Satellites_Handlers_SatelliteHandlerBase_PrepareSatelliteForImportAsync.htm)|  
(Унаследован от
[SatelliteHandlerBase](T_Tessa_Extensions_Platform_Server_Cards_Satellites_Handlers_SatelliteHandlerBase.htm))  
[PrepareSatelliteForRepareAsync](M_Tessa_Extensions_Platform_Server_Cards_Satellites_Handlers_SatelliteHandlerBase_PrepareSatelliteForRepareAsync.htm)|  
(Унаследован от
[SatelliteHandlerBase](T_Tessa_Extensions_Platform_Server_Cards_Satellites_Handlers_SatelliteHandlerBase.htm))  
[PrepareSatelliteForRestoreAsync](M_Tessa_Extensions_Platform_Server_Cards_Satellites_Handlers_SatelliteHandlerBase_PrepareSatelliteForRestoreAsync.htm)|  
(Унаследован от
[SatelliteHandlerBase](T_Tessa_Extensions_Platform_Server_Cards_Satellites_Handlers_SatelliteHandlerBase.htm))  
[SetupSatelliteFileAsync](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfTaskSatelliteHandler_SetupSatelliteFileAsync.htm)|  
(Переопределяет
[SatelliteHandlerBase.SetupSatelliteFileAsync(ICardGetExtensionContext,
CardFile,
Boolean)](M_Tessa_Extensions_Platform_Server_Cards_Satellites_Handlers_SatelliteHandlerBase_SetupSatelliteFileAsync.htm))  
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
[Tessa.Extensions.Default.Server.Workflow.Wf - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_Wf.htm)
