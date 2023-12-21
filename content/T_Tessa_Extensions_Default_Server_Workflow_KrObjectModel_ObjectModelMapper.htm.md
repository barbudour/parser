# ObjectModelMapper - класс
Предоставляет методы для работы с хранилищами Kr процесса и объектной моделью
процесса.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrObjectModel](N_Tessa_Extensions_Default_Server_Workflow_KrObjectModel.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ObjectModelMapper : IObjectModelMapper
VB __Копировать
     Public NotInheritable Class ObjectModelMapper
    	Implements IObjectModelMapper
C++ __Копировать
     public ref class ObjectModelMapper sealed : IObjectModelMapper
F# __Копировать
     [<SealedAttribute>]
    type ObjectModelMapper = 
        class
            interface IObjectModelMapper
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ObjectModelMapper
Implements
    [IObjectModelMapper](T_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_IObjectModelMapper.htm)
##  __Конструкторы
[ObjectModelMapper](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_ObjectModelMapper__ctor.htm)|
Инициализирует новый экземпляр класса ObjectModelMapper.  
---|---  
## __Методы
[CardRowsToObjectModelAsync(Card, ProcessCommonInfo, MainProcessCommonInfo,
String, Boolean,
CancellationToken)](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_ObjectModelMapper_CardRowsToObjectModelAsync.htm)|
Преобразовать секционную модель процесса маршрутов в объектную модель. Метод
предназначен для преобразования карточек документов.  
---|---  
[CardRowsToObjectModelAsync(IKrStageTemplate,
IReadOnlyCollection<IKrRuntimeStage>, MainProcessCommonInfo, Boolean, Boolean,
CancellationToken)](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_ObjectModelMapper_CardRowsToObjectModelAsync_1.htm)|
Преобразует секционную модель процесса маршрутов в объектную модель. Метод
предназначен для преобразования карточек шаблонов этапов.  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[FillWorkflowProcessFromPci](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_ObjectModelMapper_FillWorkflowProcessFromPci.htm)|
Заполняет информацию в объектной модели указанной информацией по текущем и
основному процессу.  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetMainProcessCommonInfo](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_ObjectModelMapper_GetMainProcessCommonInfo.htm)|
Загружает из сателлита-холдера информацию по текущему процессу.  
[GetNestedProcessCommonInfos](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_ObjectModelMapper_GetNestedProcessCommonInfos.htm)|
Загружает из сателлита-холдера основную информацию по вложенным процессам.  
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
[ObjectModelToCardRowsAsync](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_ObjectModelMapper_ObjectModelToCardRowsAsync.htm)|
Преобразует объектную модель процесса маршрутов в секционную модель с
отслеживанием изменений.  
[ObjectModelToPci](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_ObjectModelMapper_ObjectModelToPci.htm)|
Переносит информацию о процессе из объектной модели (process) в: pci, mainPci,
primaryPci.  
[RepairSettings](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_ObjectModelMapper_RepairSettings.htm)|
Исправляет ссылки StageRowID в подставленных настройках, а также выставляет
порядок сортировки.  
[SetMainProcessCommonInfoAsync](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_ObjectModelMapper_SetMainProcessCommonInfoAsync.htm)|
Асинхронно устанавливает в сателлите-холдере процесса информацию по основному
процессу.  
[SetNestedProcessCommonInfos](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_ObjectModelMapper_SetNestedProcessCommonInfos.htm)|
Устанавливает в сателлит-холдер основную информацию по вложенным процессам.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[GetTemplateStagesAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessExtensions_GetTemplateStagesAsync.htm)|
Возвращает этапы из шаблона этапов.  
(Определяется
[KrProcessExtensions](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessExtensions.htm))  
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
