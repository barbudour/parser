# PluginTraceListener - класс
Объект, выполняющий отслеживание событий, происходящих с расширениями
[IPluginExtension](T_Tessa_Platform_Plugins_IPluginExtension.htm). Обычно при
этом изменяется идентификатор запроса
[ServerRequestID](P_Tessa_Platform_Runtime_RuntimeHelper_ServerRequestID.htm).
## __Definition
 **Пространство имён:** [Tessa.Platform.Plugins](N_Tessa_Platform_Plugins.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class PluginTraceListener : ExtensionTraceListener
VB __Копировать
     Public NotInheritable Class PluginTraceListener
    	Inherits ExtensionTraceListener
C++ __Копировать
     public ref class PluginTraceListener sealed : public ExtensionTraceListener
F# __Копировать
     [<SealedAttribute>]
    type PluginTraceListener = 
        class
            inherit ExtensionTraceListener
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ExtensionTraceListener](T_Tessa_Extensions_ExtensionTraceListener.htm) __ PluginTraceListener
##  __Конструкторы
[PluginTraceListener](M_Tessa_Platform_Plugins_PluginTraceListener__ctor.htm)|
Инициализирует новый экземпляр класса PluginTraceListener  
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
[NotifyException](M_Tessa_Platform_Plugins_PluginTraceListener_NotifyException.htm)|
Уведомляет объект о том, что возникло исключение в процессе выполнения метода
расширения, информацию о котором можно получить из заданного контекста.  
(Переопределяет
[ExtensionTraceListener.NotifyException(IExtensionStrategyContext)](M_Tessa_Extensions_ExtensionTraceListener_NotifyException.htm))  
[NotifyExecuted](M_Tessa_Platform_Plugins_PluginTraceListener_NotifyExecuted.htm)|
Уведомляет объект о том, что было завершено выполнение метода расширения,
информацию о котором можно получить из заданного контекста.  
(Переопределяет
[ExtensionTraceListener.NotifyExecuted(IExtensionStrategyContext)](M_Tessa_Extensions_ExtensionTraceListener_NotifyExecuted.htm))  
[NotifyExecuting](M_Tessa_Platform_Plugins_PluginTraceListener_NotifyExecuting.htm)|
Уведомляет объект о том, что следующим шагом будет выполнение метода
расширения, информацию о котором можно получить из заданного контекста.  
(Переопределяет
[ExtensionTraceListener.NotifyExecuting(IExtensionStrategyContext)](M_Tessa_Extensions_ExtensionTraceListener_NotifyExecuting.htm))  
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
