# SatelliteHandlerBase - класс
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.Cards.Satellites.Handlers](N_Tessa_Extensions_Platform_Server_Cards_Satellites_Handlers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class SatelliteHandlerBase : ISatelliteHandler
VB __Копировать
     Public MustInherit Class SatelliteHandlerBase
    	Implements ISatelliteHandler
C++ __Копировать
     public ref class SatelliteHandlerBase abstract : ISatelliteHandler
F# __Копировать
     [<AbstractClassAttribute>]
    type SatelliteHandlerBase = 
        class
            interface ISatelliteHandler
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ SatelliteHandlerBase
Derived
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Satellite.KrSatelliteHandler](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Satellite_KrSatelliteHandler.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Satellite.KrSecondarySatelliteHandler](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Satellite_KrSecondarySatelliteHandler.htm)
[Tessa.Extensions.Default.Server.Workflow.Wf.WfSatelliteHandler](T_Tessa_Extensions_Default_Server_Workflow_Wf_WfSatelliteHandler.htm)
[Tessa.Extensions.Default.Server.Workflow.Wf.WfTaskSatelliteHandler](T_Tessa_Extensions_Default_Server_Workflow_Wf_WfTaskSatelliteHandler.htm)
[Tessa.Extensions.Platform.Server.Cards.Satellites.Handlers.FileSatelliteHandler](T_Tessa_Extensions_Platform_Server_Cards_Satellites_Handlers_FileSatelliteHandler.htm)
[Tessa.Extensions.Platform.Server.Cards.Satellites.Handlers.ForumSatelliteHandler](T_Tessa_Extensions_Platform_Server_Cards_Satellites_Handlers_ForumSatelliteHandler.htm)
[Tessa.Extensions.Platform.Server.Cards.Satellites.Handlers.PersonalRoleSatelliteHandler](T_Tessa_Extensions_Platform_Server_Cards_Satellites_Handlers_PersonalRoleSatelliteHandler.htm)
Подробнее __Less __
Implements
    [ISatelliteHandler](T_Tessa_Extensions_Platform_Server_Cards_Satellites_Handlers_ISatelliteHandler.htm)
##  __Конструкторы
[SatelliteHandlerBase](M_Tessa_Extensions_Platform_Server_Cards_Satellites_Handlers_SatelliteHandlerBase__ctor.htm)|
Инициализирует новый экземпляр класса SatelliteHandlerBase  
---|---  
##  __Методы
[CheckFileAccessAsync](M_Tessa_Extensions_Platform_Server_Cards_Satellites_Handlers_SatelliteHandlerBase_CheckFileAccessAsync.htm)|  
---|---  
[CheckFileVersionsAccessAsync](M_Tessa_Extensions_Platform_Server_Cards_Satellites_Handlers_SatelliteHandlerBase_CheckFileVersionsAccessAsync.htm)|  
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
[GetExternalFileSourcesAsync](M_Tessa_Extensions_Platform_Server_Cards_Satellites_Handlers_SatelliteHandlerBase_GetExternalFileSourcesAsync.htm)|  
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
[IsMainCardFileAsync](M_Tessa_Extensions_Platform_Server_Cards_Satellites_Handlers_SatelliteHandlerBase_IsMainCardFileAsync.htm)|  
[IsMainCardTypeAsync](M_Tessa_Extensions_Platform_Server_Cards_Satellites_Handlers_SatelliteHandlerBase_IsMainCardTypeAsync.htm)|  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[PrepareMainCardFileToStoreAsync](M_Tessa_Extensions_Platform_Server_Cards_Satellites_Handlers_SatelliteHandlerBase_PrepareMainCardFileToStoreAsync.htm)|  
[PrepareSatelliteForBackupAsync](M_Tessa_Extensions_Platform_Server_Cards_Satellites_Handlers_SatelliteHandlerBase_PrepareSatelliteForBackupAsync.htm)|  
[PrepareSatelliteForCreateAsync](M_Tessa_Extensions_Platform_Server_Cards_Satellites_Handlers_SatelliteHandlerBase_PrepareSatelliteForCreateAsync.htm)|  
[PrepareSatelliteForDeleteAsync](M_Tessa_Extensions_Platform_Server_Cards_Satellites_Handlers_SatelliteHandlerBase_PrepareSatelliteForDeleteAsync.htm)|  
[PrepareSatelliteForExportAsync](M_Tessa_Extensions_Platform_Server_Cards_Satellites_Handlers_SatelliteHandlerBase_PrepareSatelliteForExportAsync.htm)|  
[PrepareSatelliteForGetAsync](M_Tessa_Extensions_Platform_Server_Cards_Satellites_Handlers_SatelliteHandlerBase_PrepareSatelliteForGetAsync.htm)|  
[PrepareSatelliteForImportAsync](M_Tessa_Extensions_Platform_Server_Cards_Satellites_Handlers_SatelliteHandlerBase_PrepareSatelliteForImportAsync.htm)|  
[PrepareSatelliteForRepareAsync](M_Tessa_Extensions_Platform_Server_Cards_Satellites_Handlers_SatelliteHandlerBase_PrepareSatelliteForRepareAsync.htm)|  
[PrepareSatelliteForRestoreAsync](M_Tessa_Extensions_Platform_Server_Cards_Satellites_Handlers_SatelliteHandlerBase_PrepareSatelliteForRestoreAsync.htm)|  
[SetupSatelliteFileAsync](M_Tessa_Extensions_Platform_Server_Cards_Satellites_Handlers_SatelliteHandlerBase_SetupSatelliteFileAsync.htm)|  
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
[Tessa.Extensions.Platform.Server.Cards.Satellites.Handlers - пространство
имён](N_Tessa_Extensions_Platform_Server_Cards_Satellites_Handlers.htm)
