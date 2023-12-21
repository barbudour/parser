# PluginGracefulStopTokenAdapter - класс
Адаптер для интерфейса
[IGracefulStopToken](T_Chronos_Contracts_IGracefulStopToken.htm),
инкапсулирующий все его доступные возможности, кроме тех, что определены в
интерфейсе.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Scheduling](N_Chronos_Platform_Scheduling.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class PluginGracefulStopTokenAdapter : IGracefulStopToken
VB __Копировать
     Public NotInheritable Class PluginGracefulStopTokenAdapter
    	Implements IGracefulStopToken
C++ __Копировать
     public ref class PluginGracefulStopTokenAdapter sealed : IGracefulStopToken
F# __Копировать
     [<SealedAttribute>]
    type PluginGracefulStopTokenAdapter = 
        class
            interface IGracefulStopToken
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ PluginGracefulStopTokenAdapter
Implements
    [IGracefulStopToken](T_Chronos_Contracts_IGracefulStopToken.htm)
##  __Заметки
Все открытые методы и свойства класса являются потокобезопасными, если
таковыми являются методы объекта
[IGracefulStopToken](T_Chronos_Contracts_IGracefulStopToken.htm), адаптером
для которого является этот класс.
## __Конструкторы
[PluginGracefulStopTokenAdapter](M_Chronos_Platform_Scheduling_PluginGracefulStopTokenAdapter__ctor.htm)|
Создает экземпляр класса с указанием токена, адаптер для которого будет
создан.  
---|---  
## __Свойства
[CancellationTokenSource](P_Chronos_Platform_Scheduling_PluginGracefulStopTokenAdapter_CancellationTokenSource.htm)|
Объект, посредством которого можно отменить выполнение метода
[EntryPointAsync(CancellationToken)](M_Chronos_Contracts_IPlugin_EntryPointAsync.htm),
а также обычно токен остановки передаётся в метод
[WaitUntilEntryPointFinishedAsync(CancellationToken)](M_Chronos_Platform_Scheduling_PluginGracefulStopTokenAdapter_WaitUntilEntryPointFinishedAsync.htm).  
---|---  
[EntryPointFinished](P_Chronos_Platform_Scheduling_PluginGracefulStopTokenAdapter_EntryPointFinished.htm)|
Признак того, что метод
[EntryPointAsync(CancellationToken)](M_Chronos_Contracts_IPlugin_EntryPointAsync.htm)
плагина был завершён.  
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
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[WaitUntilEntryPointFinishedAsync](M_Chronos_Platform_Scheduling_PluginGracefulStopTokenAdapter_WaitUntilEntryPointFinishedAsync.htm)|
Ожидает, пока метод
[EntryPointAsync(CancellationToken)](M_Chronos_Contracts_IPlugin_EntryPointAsync.htm)
плагина не будет завершён.  
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
