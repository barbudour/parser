# PluginGracefulStopExceptionEventArgs - класс
Аргументы события, возникающего при возникновении исключения в процессе
вежливой остановки плагина методом
[StopAsync(IGracefulStopToken)](M_Chronos_Contracts_ISupportGracefulStop_StopAsync.htm).
## __Definition
 **Пространство имён:**
[Chronos.Platform.Scheduling](N_Chronos_Platform_Scheduling.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class PluginGracefulStopExceptionEventArgs : EventArgs
VB __Копировать
     Public NotInheritable Class PluginGracefulStopExceptionEventArgs
    	Inherits EventArgs
C++ __Копировать
     public ref class PluginGracefulStopExceptionEventArgs sealed : public EventArgs
F# __Копировать
     [<SealedAttribute>]
    type PluginGracefulStopExceptionEventArgs = 
        class
            inherit EventArgs
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[EventArgs](https://learn.microsoft.com/dotnet/api/system.eventargs) __ PluginGracefulStopExceptionEventArgs
##  __Конструкторы
[PluginGracefulStopExceptionEventArgs](M_Chronos_Platform_Scheduling_PluginGracefulStopExceptionEventArgs__ctor.htm)|
Создаёт экземпляр класса с указанием значений всех его свойств.  
---|---  
## __Свойства
[Exception](P_Chronos_Platform_Scheduling_PluginGracefulStopExceptionEventArgs_Exception.htm)|
Исключение, возникшее в методе
[StopAsync(IGracefulStopToken)](M_Chronos_Contracts_ISupportGracefulStop_StopAsync.htm)
объекта
[GracefulPlugin](P_Chronos_Platform_Scheduling_PluginGracefulStopExceptionEventArgs_GracefulPlugin.htm).  
---|---  
[GracefulPlugin](P_Chronos_Platform_Scheduling_PluginGracefulStopExceptionEventArgs_GracefulPlugin.htm)|
Плагин, вежливая остановка которого производится. Значение может быть
приведено к интерфейсу [IPlugin](T_Chronos_Contracts_IPlugin.htm).  
[Token](P_Chronos_Platform_Scheduling_PluginGracefulStopExceptionEventArgs_Token.htm)|
Токен, позволяющий определить состояние плагина. Этот токен был передан в
метод
[StopAsync(IGracefulStopToken)](M_Chronos_Contracts_ISupportGracefulStop_StopAsync.htm)
объекта
[GracefulPlugin](P_Chronos_Platform_Scheduling_PluginGracefulStopExceptionEventArgs_GracefulPlugin.htm).  
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
[IsPropertyChanged](M_Tessa_UI_Controls_PropertyChangedHelper_IsPropertyChanged.htm)|
Проверяет наступление события изменения свойства propertyName  
(Определяется
[PropertyChangedHelper](T_Tessa_UI_Controls_PropertyChangedHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Chronos.Platform.Scheduling - пространство
имён](N_Chronos_Platform_Scheduling.htm)
