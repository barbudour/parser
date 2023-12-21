# WfResolutionTaskInfo - класс
Информация по резолюции Workflow, которая используется для построения UI
заданий.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Client.Workflow.Wf](N_Tessa_Extensions_Default_Client_Workflow_Wf.htm)  
 **Сборка:** Tessa.Extensions.Default.Client (в
Tessa.Extensions.Default.Client.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class WfResolutionTaskInfo
VB __Копировать
     Public NotInheritable Class WfResolutionTaskInfo
C++ __Копировать
     public ref class WfResolutionTaskInfo sealed
F# __Копировать
     [<SealedAttribute>]
    type WfResolutionTaskInfo = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ WfResolutionTaskInfo
##  __Конструкторы
[WfResolutionTaskInfo](M_Tessa_Extensions_Default_Client_Workflow_Wf_WfResolutionTaskInfo__ctor.htm)|
Создаёт экземпляр класса с указанием значений его свойств.  
---|---  
## __Свойства
[Control](P_Tessa_Extensions_Default_Client_Workflow_Wf_WfResolutionTaskInfo_Control.htm)|
Модель представления для элемента управления, выводящего задание.  
---|---  
[HasChildren](P_Tessa_Extensions_Default_Client_Workflow_Wf_WfResolutionTaskInfo_HasChildren.htm)|
Признак того, что резолюция содержит дочерние резолюции, которые должны
выводиться таблицей.  
[HasIncompleteChildren](P_Tessa_Extensions_Default_Client_Workflow_Wf_WfResolutionTaskInfo_HasIncompleteChildren.htm)|
Признак того, что резолюция содержит незавершённые дочерние резолюции.  
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
[SubscribeToPerformersAndUpdate](M_Tessa_Extensions_Default_Client_Workflow_Wf_WfResolutionTaskInfo_SubscribeToPerformersAndUpdate.htm)|
Выполняет подписку на исполнителей задания performersRows. Перед подпиской
выполняется отписка от предыдущих исполнителей, установленных другим вызовом
этого метода.  
[SubscribeToResolutionSectionAndUpdate](M_Tessa_Extensions_Default_Client_Workflow_Wf_WfResolutionTaskInfo_SubscribeToResolutionSectionAndUpdate.htm)|
Выполняет подписку на основную секции резолюции resolutionSection. Перед
подпиской выполняется отписка от предыдущей секции, установленной другим
вызовом этого метода.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Unsubscribe](M_Tessa_Extensions_Default_Client_Workflow_Wf_WfResolutionTaskInfo_Unsubscribe.htm)|
Выполняет отписку от всех событий, подписка которых контролируется.  
[UnsubscribeFromPerformers](M_Tessa_Extensions_Default_Client_Workflow_Wf_WfResolutionTaskInfo_UnsubscribeFromPerformers.htm)|
Выполняет отписку от исполнителей задания, подписка на которые была выполнена
методом
[SubscribeToPerformersAndUpdate(ListStorage<CardRow>)](M_Tessa_Extensions_Default_Client_Workflow_Wf_WfResolutionTaskInfo_SubscribeToPerformersAndUpdate.htm).  
[UnsubscribeFromResolutionSection](M_Tessa_Extensions_Default_Client_Workflow_Wf_WfResolutionTaskInfo_UnsubscribeFromResolutionSection.htm)|
Выполняет отписку от основной секции резолюции, подписка на которую была
выполнена методом
[SubscribeToPerformersAndUpdate(ListStorage<CardRow>)](M_Tessa_Extensions_Default_Client_Workflow_Wf_WfResolutionTaskInfo_SubscribeToPerformersAndUpdate.htm).  
[Update](M_Tessa_Extensions_Default_Client_Workflow_Wf_WfResolutionTaskInfo_Update.htm)|
Обновляет состояние всех элементов управления, подписка на события которых
контролируется. Выполняется при обновлении формы с элементами управления.  
## __Методы расширения
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
[Tessa.Extensions.Default.Client.Workflow.Wf - пространство
имён](N_Tessa_Extensions_Default_Client_Workflow_Wf.htm)
