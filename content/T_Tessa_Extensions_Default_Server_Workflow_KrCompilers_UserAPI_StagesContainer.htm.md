# StagesContainer - класс
Предоставляет методы для манипулирования этапами процесса.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrCompilers.UserAPI](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class StagesContainer
VB __Копировать
     Public NotInheritable Class StagesContainer
C++ __Копировать
     public ref class StagesContainer sealed
F# __Копировать
     [<SealedAttribute>]
    type StagesContainer = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ StagesContainer
##  __Конструкторы
[StagesContainer](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_StagesContainer__ctor.htm)|
Инициализирует новый экземпляр класса StagesContainer.  
---|---  
## __Свойства
[InitialStages](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_StagesContainer_InitialStages.htm)|
Возвращает коллекцию этапов на момент формирования маршрута.  
---|---  
[Stages](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_StagesContainer_Stages.htm)|
Возвращает коллекцию этапов.  
## __Методы
[DeleteUnconfirmedStages](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_StagesContainer_DeleteUnconfirmedStages.htm)|
Удаляет этапы, подставленные из шаблонов ранее, которые при текущем пересчете
не заменены.  
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
[MergeStages(IReadOnlyCollection<Stage>)](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_StagesContainer_MergeStages.htm)|
Объединяет существующие этапы с новыми.  
[MergeStages(Stage[])](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_StagesContainer_MergeStages_1.htm)|
Объединяет существующие этапы с новыми.  
[MergeWithAsync(IEnumerable<IKrStageTemplate>, IReadOnlyDictionary<Guid,
IReadOnlyList<IKrRuntimeStage>>,
CancellationToken)](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_StagesContainer_MergeWithAsync.htm)|
Объединяет существующие этапы с этапами из карточки шаблона этапов.  
[MergeWithAsync(IKrStageTemplate, IReadOnlyList<IKrRuntimeStage>,
CancellationToken)](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_StagesContainer_MergeWithAsync_1.htm)|
Объединяет существующие этапы с этапами из карточки шаблона этапов.  
[ReplaceStage](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_StagesContainer_ReplaceStage.htm)|
Заменяет этап расположенный по индексу index на новый.  
[RestoreFlags](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_StagesContainer_RestoreFlags.htm)|
Восстанавливает всем этапам внутри контейнера значение флага InitialStage.  
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
[Tessa.Extensions.Default.Server.Workflow.KrCompilers.UserAPI - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI.htm)
