# KrPermissionsFlagsViewInterceptor - класс
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrPermissions](N_Tessa_Extensions_Default_Server_Workflow_KrPermissions.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class KrPermissionsFlagsViewInterceptor : ViewInterceptorBase
VB __Копировать
     Public NotInheritable Class KrPermissionsFlagsViewInterceptor
    	Inherits ViewInterceptorBase
C++ __Копировать
     public ref class KrPermissionsFlagsViewInterceptor sealed : public ViewInterceptorBase
F# __Копировать
     [<SealedAttribute>]
    type KrPermissionsFlagsViewInterceptor = 
        class
            inherit ViewInterceptorBase
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ViewInterceptorBase](T_Tessa_Views_ViewInterceptorBase.htm) __ KrPermissionsFlagsViewInterceptor
##  __Конструкторы
[KrPermissionsFlagsViewInterceptor](M_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsFlagsViewInterceptor__ctor.htm)|
Инициализирует новый экземпляр класса KrPermissionsFlagsViewInterceptor  
---|---  
##  __Свойства
[InterceptedViews](P_Tessa_Views_ViewInterceptorBase_InterceptedViews.htm)|
Перехватываемые IViewInterceptor представления  
(Унаследован от [ViewInterceptorBase](T_Tessa_Views_ViewInterceptorBase.htm))  
---|---  
[Order](P_Tessa_Views_ViewInterceptorBase_Order.htm)|  Очередность выполнения
IViewInterceptor. Значение по умолчанию в
[Order](P_Tessa_Views_ViewInterceptorBase_Order.htm) равно 0  
(Унаследован от [ViewInterceptorBase](T_Tessa_Views_ViewInterceptorBase.htm))  
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
[GetDataAsync](M_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsFlagsViewInterceptor_GetDataAsync.htm)|
Осуществляет выполнение запроса на получение данных  
(Переопределяет [ViewInterceptorBase.GetDataAsync(ITessaViewRequest,
CancellationToken)](M_Tessa_Views_ViewInterceptorBase_GetDataAsync.htm))  
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
(Унаследован от [ViewInterceptorBase](T_Tessa_Views_ViewInterceptorBase.htm))  
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
[Tessa.Extensions.Default.Server.Workflow.KrPermissions - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrPermissions.htm)
