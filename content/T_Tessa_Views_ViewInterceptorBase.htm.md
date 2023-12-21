# ViewInterceptorBase - класс
Базовый класс перехватчика представлений
## __Definition
 **Пространство имён:** [Tessa.Views](N_Tessa_Views.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class ViewInterceptorBase : IViewInterceptor
VB __Копировать
     Public MustInherit Class ViewInterceptorBase
    	Implements IViewInterceptor
C++ __Копировать
     public ref class ViewInterceptorBase abstract : IViewInterceptor
F# __Копировать
     [<AbstractClassAttribute>]
    type ViewInterceptorBase = 
        class
            interface IViewInterceptor
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ViewInterceptorBase
Derived
[Tessa.Extensions.Default.Server.EDS.EdsManagerInterceptor](T_Tessa_Extensions_Default_Server_EDS_EdsManagerInterceptor.htm)
[Tessa.Extensions.Default.Server.Views.ChangeConnectionInterceptor](T_Tessa_Extensions_Default_Server_Views_ChangeConnectionInterceptor.htm)
[Tessa.Extensions.Default.Server.Views.ExampleInterceptor](T_Tessa_Extensions_Default_Server_Views_ExampleInterceptor.htm)
[Tessa.Extensions.Default.Server.Views.TaskHistoryInterceptor](T_Tessa_Extensions_Default_Server_Views_TaskHistoryInterceptor.htm)
[Tessa.Extensions.Default.Server.Views.TopicParticipantsInterceptor](T_Tessa_Extensions_Default_Server_Views_TopicParticipantsInterceptor.htm)
[Tessa.Extensions.Default.Server.Views.ViewsInterceptor](T_Tessa_Extensions_Default_Server_Views_ViewsInterceptor.htm)
[Tessa.Extensions.Default.Server.Workflow.KrPermissions.KrPermissionsFlagsViewInterceptor](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsFlagsViewInterceptor.htm)
[Tessa.Extensions.Default.Server.Workflow.KrPermissions.KrPermissionsViewInterceptor](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsViewInterceptor.htm)
[Tessa.Extensions.Platform.Server.Views.AvailableApplicationsViewInterceptor](T_Tessa_Extensions_Platform_Server_Views_AvailableApplicationsViewInterceptor.htm)
[Tessa.Extensions.Platform.Server.Views.WebApplicationsViewInterceptor](T_Tessa_Extensions_Platform_Server_Views_WebApplicationsViewInterceptor.htm)
[Tessa.Extensions.Platform.Server.Workflow.WorkflowEngineCompiledTypesViewInterceptor](T_Tessa_Extensions_Platform_Server_Workflow_WorkflowEngineCompiledTypesViewInterceptor.htm)
[Tessa.Extensions.Platform.Server.Workflow.WorkflowEngineTileManagerExtensionsViewInterceptor](T_Tessa_Extensions_Platform_Server_Workflow_WorkflowEngineTileManagerExtensionsViewInterceptor.htm)
[Tessa.Extensions.Platform.Server.Workflow.WorkflowViewsInterceptor](T_Tessa_Extensions_Platform_Server_Workflow_WorkflowViewsInterceptor.htm)
Подробнее __Less __
Implements
    [IViewInterceptor](T_Tessa_Views_IViewInterceptor.htm)
##  __Конструкторы
[ViewInterceptorBase](M_Tessa_Views_ViewInterceptorBase__ctor.htm)|
Конструктор класса  
---|---  
## __Свойства
[InterceptedViews](P_Tessa_Views_ViewInterceptorBase_InterceptedViews.htm)|
Перехватываемые IViewInterceptor представления  
---|---  
[Order](P_Tessa_Views_ViewInterceptorBase_Order.htm)|  Очередность выполнения
IViewInterceptor. Значение по умолчанию в
[Order](P_Tessa_Views_ViewInterceptorBase_Order.htm) равно 0  
##  __Методы
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
[GetDataAsync](M_Tessa_Views_ViewInterceptorBase_GetDataAsync.htm)|
Осуществляет выполнение запроса на получение данных  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetInterceptedViewAliasesAsync](M_Tessa_Views_ViewInterceptorBase_GetInterceptedViewAliasesAsync.htm)|
Возвращает алиасы представлений, которые будет перехватывать данный
Interceptor. Стандартная реализация
[!:GetInterceptedViewAliasesAsync(IList<ITessaView>)] возвращет алиасы
полученных в конструкторе представлений. При перегрузке данного метода в
классе наследние в конструктор
[ViewInterceptorBase(String[])](M_Tessa_Views_ViewInterceptorBase__ctor.htm)
можно ничего не передавать.  
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
[Tessa.Views - пространство имён](N_Tessa_Views.htm)
