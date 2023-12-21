# PluginExtension - класс
Базовый класс для расширения плагина Chronos.
## __Definition
 **Пространство имён:** [Tessa.Platform.Plugins](N_Tessa_Platform_Plugins.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class PluginExtension : IPluginExtension, 
    	IExtension
VB __Копировать
     Public MustInherit Class PluginExtension
    	Implements IPluginExtension, IExtension
C++ __Копировать
     public ref class PluginExtension abstract : IPluginExtension, 
    	IExtension
F# __Копировать
     [<AbstractClassAttribute>]
    type PluginExtension = 
        class
            interface IPluginExtension
            interface IExtension
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ PluginExtension
Derived
[Tessa.Extensions.Default.Chronos.Notices.NoticeMailerPlugin](T_Tessa_Extensions_Default_Chronos_Notices_NoticeMailerPlugin.htm)
[Tessa.Extensions.Default.Chronos.OnlyOffice.OnlyOfficeRemoveFileCacheInfoPlugin](T_Tessa_Extensions_Default_Chronos_OnlyOffice_OnlyOfficeRemoveFileCacheInfoPlugin.htm)
[Tessa.Extensions.Default.Chronos.Workflow.KrAutoApprovePlugin](T_Tessa_Extensions_Default_Chronos_Workflow_KrAutoApprovePlugin.htm)
[Tessa.Extensions.Default.Chronos.Workflow.MobileApprovalPlugin](T_Tessa_Extensions_Default_Chronos_Workflow_MobileApprovalPlugin.htm)
[Tessa.Extensions.Default.Chronos.Workflow.ReturnTasksFromPostponedPlugin](T_Tessa_Extensions_Default_Chronos_Workflow_ReturnTasksFromPostponedPlugin.htm)
[Tessa.Extensions.Platform.Server.Plugins.RemoveActionHistoryPlugin](T_Tessa_Extensions_Platform_Server_Plugins_RemoveActionHistoryPlugin.htm)
[Tessa.Extensions.Platform.Server.Plugins.RemoveCompiledViews](T_Tessa_Extensions_Platform_Server_Plugins_RemoveCompiledViews.htm)
[Tessa.Extensions.Platform.Server.Plugins.RemoveDeletedCardsPlugin](T_Tessa_Extensions_Platform_Server_Plugins_RemoveDeletedCardsPlugin.htm)
[Tessa.Extensions.Platform.Server.Plugins.RemoveErrorCardsPlugin](T_Tessa_Extensions_Platform_Server_Plugins_RemoveErrorCardsPlugin.htm)
[Tessa.Extensions.Platform.Server.Plugins.RemoveInactiveSessionsPlugin](T_Tessa_Extensions_Platform_Server_Plugins_RemoveInactiveSessionsPlugin.htm)
[Tessa.Extensions.Platform.Server.Plugins.RemoveOperationsPlugin](T_Tessa_Extensions_Platform_Server_Plugins_RemoveOperationsPlugin.htm)
Подробнее __Less __
Implements
    [IExtension](T_Tessa_Extensions_IExtension.htm), [IPluginExtension](T_Tessa_Platform_Plugins_IPluginExtension.htm)
##  __Конструкторы
[PluginExtension](M_Tessa_Platform_Plugins_PluginExtension__ctor.htm)|
Инициализирует новый экземпляр класса PluginExtension  
---|---  
##  __Свойства
[Name](P_Tessa_Platform_Plugins_PluginExtension_Name.htm)|  Основной
выполняемый метод плагина. Переопределите этот метод в первую очередь, чтобы
определить поведение плагина.  
---|---  
## __Методы
[EntryPoint](M_Tessa_Platform_Plugins_PluginExtension_EntryPoint.htm)|
Основной выполняемый метод плагина. Переопределите этот метод в первую
очередь, чтобы определить поведение плагина.  
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
[Tessa.Platform.Plugins - пространство имён](N_Tessa_Platform_Plugins.htm)
