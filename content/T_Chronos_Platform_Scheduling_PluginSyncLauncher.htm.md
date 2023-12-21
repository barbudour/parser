# PluginSyncLauncher - класс
Запускает плагин на выполнение, предварительно выполнив синхронизацию между
процессами плагинов.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Scheduling](N_Chronos_Platform_Scheduling.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class PluginSyncLauncher : IPluginLauncher
VB __Копировать
     Public NotInheritable Class PluginSyncLauncher
    	Implements IPluginLauncher
C++ __Копировать
     public ref class PluginSyncLauncher sealed : IPluginLauncher
F# __Копировать
     [<SealedAttribute>]
    type PluginSyncLauncher = 
        class
            interface IPluginLauncher
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ PluginSyncLauncher
Implements
    [IPluginLauncher](T_Chronos_Platform_Scheduling_IPluginLauncher.htm)
##  __Конструкторы
[PluginSyncLauncher](M_Chronos_Platform_Scheduling_PluginSyncLauncher__ctor.htm)|
Инициализирует новый экземпляр класса PluginSyncLauncher  
---|---  
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
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetPluginMutexName](M_Chronos_Platform_Scheduling_PluginSyncLauncher_GetPluginMutexName.htm)|  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[LaunchAsync](M_Chronos_Platform_Scheduling_PluginSyncLauncher_LaunchAsync.htm)|
Асинхронно запускает метод
[EntryPointAsync(CancellationToken)](M_Chronos_Contracts_IPlugin_EntryPointAsync.htm),
если не установлен флаг
[DisallowConcurrency](P_Chronos_Platform_Scheduling_PluginRemoteCreationInfo_DisallowConcurrency.htm)
или не выполняется другого процесса с этим же плагином, запущенным таким же
методом.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __События
[PluginLaunching](E_Chronos_Platform_Scheduling_PluginSyncLauncher_PluginLaunching.htm)|
Событие, возникающее перед запуском плагина.  
---|---  
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
[Chronos.Platform.Scheduling - пространство
имён](N_Chronos_Platform_Scheduling.htm)
