# PluginFacade.StartHostInfo - класс
Параметры запуска метода [StartHostAsync(PluginFacade.StartHostInfo,
CancellationToken)](M_Chronos_Platform_Scheduling_PluginFacade_StartHostAsync.htm).
## __Definition
 **Пространство имён:**
[Chronos.Platform.Scheduling](N_Chronos_Platform_Scheduling.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class StartHostInfo
VB __Копировать
     Public NotInheritable Class StartHostInfo
C++ __Копировать
     public ref class StartHostInfo sealed
F# __Копировать
     [<SealedAttribute>]
    type StartHostInfo = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ PluginFacade.StartHostInfo
##  __Конструкторы
[PluginFacade.StartHostInfo](M_Chronos_Platform_Scheduling_PluginFacade_StartHostInfo__ctor.htm)|
Создаёт экземпляр класса, с указанием параметров запуска processHost и
pluginsFolderPath.  
---|---  
## __Свойства
[AwaitGracefulStopSeconds](P_Chronos_Platform_Scheduling_PluginFacade_StartHostInfo_AwaitGracefulStopSeconds.htm)|
Количество секунд, которые выполняется ожидание вежливого завершения всех
плагинов со стороны хоста.  
---|---  
[HostActivityActionAsync](P_Chronos_Platform_Scheduling_PluginFacade_StartHostInfo_HostActivityActionAsync.htm)|
Метод, который должен осуществлять некоторые действия, по окончании которых
хост завершает свою работу. Если значение не задано или равно null, то в
качестве такого метода используется вызов await Task.Delay(Timeout.Infinite,
cancellationToken). Исключение
[OperationCanceledException](https://learn.microsoft.com/dotnet/api/system.operationcanceledexception),
выбрасываемое этим методом, игнорируется, поэтому его можно не перехватывать
внутри метода при ожидании токена.  
[PluginsFolderPath](P_Chronos_Platform_Scheduling_PluginFacade_StartHostInfo_PluginsFolderPath.htm)|
Папка, в которой осуществляется поиск плагинов. Поиск также выполняется в
подпапках первого уровня.  
[ProcessHost](P_Chronos_Platform_Scheduling_PluginFacade_StartHostInfo_ProcessHost.htm)|
Интерфейс запуска дочерних процессов.  
[ShutdownMode](P_Chronos_Platform_Scheduling_PluginFacade_StartHostInfo_ShutdownMode.htm)|
Способ завершения процесса хоста.  
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
[SetAwaitGracefulStopSeconds](M_Chronos_Platform_Scheduling_PluginFacade_StartHostInfo_SetAwaitGracefulStopSeconds.htm)|
Задаёт количество секунд, которые выполняется ожидание вежливого завершения
всех плагинов со стороны хоста.  
[SetHostActivity](M_Chronos_Platform_Scheduling_PluginFacade_StartHostInfo_SetHostActivity.htm)|
Задаёт метод, который должен осуществлять некоторые действия, по окончании
которых хост завершает свою работу.  
[SetShutdownMode](M_Chronos_Platform_Scheduling_PluginFacade_StartHostInfo_SetShutdownMode.htm)|
Задаёт способ завершения процесса хоста.  
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
[Chronos.Platform.Scheduling - пространство
имён](N_Chronos_Platform_Scheduling.htm)
