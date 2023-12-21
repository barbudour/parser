# WfGetResolutionVisualizationDataRequestExtension - класс
Возвращает сжатую карточку для визуализации резолюций Workflow. Карточка
содержит все задания резолюций с их секциями (без календаря), а также все
записи в истории заданий, относящиеся к заданиям резолюций. Не содержит секций
карточки, файлов и прочих заданий.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.Wf](N_Tessa_Extensions_Default_Server_Workflow_Wf.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class WfGetResolutionVisualizationDataRequestExtension : CardRequestExtension
VB __Копировать
     Public NotInheritable Class WfGetResolutionVisualizationDataRequestExtension
    	Inherits CardRequestExtension
C++ __Копировать
     public ref class WfGetResolutionVisualizationDataRequestExtension sealed : public CardRequestExtension
F# __Копировать
     [<SealedAttribute>]
    type WfGetResolutionVisualizationDataRequestExtension = 
        class
            inherit CardRequestExtension
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[CardRequestExtension](T_Tessa_Cards_Extensions_CardRequestExtension.htm) __ WfGetResolutionVisualizationDataRequestExtension
##  __Заметки
Расширение должно быть зарегистрировано по типу
[GetResolutionVisualizationData](F_Tessa_Extensions_Default_Shared_DefaultRequestTypes_GetResolutionVisualizationData.htm).
## __Конструкторы
[WfGetResolutionVisualizationDataRequestExtension](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfGetResolutionVisualizationDataRequestExtension__ctor.htm)|
Инициализирует новый экземпляр класса
WfGetResolutionVisualizationDataRequestExtension  
---|---  
##  __Методы
[AfterRequest](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfGetResolutionVisualizationDataRequestExtension_AfterRequest.htm)|  
(Переопределяет
[CardRequestExtension.AfterRequest(ICardRequestExtensionContext)](M_Tessa_Cards_Extensions_CardRequestExtension_AfterRequest.htm))  
---|---  
[AfterRequestFinally](M_Tessa_Cards_Extensions_CardRequestExtension_AfterRequestFinally.htm)|
Действие, выполняемое при возникновении исключения или после универсального
взаимодействия с сервисом карточек как при успешном, так и при неудачном
результате. Необработанные исключения не прерывают выполнение цепочки
расширений.  
(Унаследован от
[CardRequestExtension](T_Tessa_Cards_Extensions_CardRequestExtension.htm))  
[BeforeRequest](M_Tessa_Cards_Extensions_CardRequestExtension_BeforeRequest.htm)|
Действие, выполняемое перед универсальным взаимодействием с сервисом карточек
стандартными средствами. Может установить ответ на запрос для того, чтобы
взаимодействие с сервисом карточек стандартными средствами не выполнялось.  
(Унаследован от
[CardRequestExtension](T_Tessa_Cards_Extensions_CardRequestExtension.htm))  
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