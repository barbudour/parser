# DefaultExtensionTraceListener - класс
Объект, выполняющий отслеживание событий, происходящих при выполнении
расширений. События записываются в
[ValidationResult](P_Tessa_Extensions_ITraceableExtensionContext_ValidationResult.htm)
как информационные сообщения.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class DefaultExtensionTraceListener : ExtensionTraceListener
VB __Копировать
     Public NotInheritable Class DefaultExtensionTraceListener
    	Inherits ExtensionTraceListener
C++ __Копировать
     public ref class DefaultExtensionTraceListener sealed : public ExtensionTraceListener
F# __Копировать
     [<SealedAttribute>]
    type DefaultExtensionTraceListener = 
        class
            inherit ExtensionTraceListener
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ExtensionTraceListener](T_Tessa_Extensions_ExtensionTraceListener.htm) __ DefaultExtensionTraceListener
##  __Конструкторы
[DefaultExtensionTraceListener](M_Tessa_Extensions_DefaultExtensionTraceListener__ctor.htm)|
Создаёт экземпляр класса с указанием значений его свойств.  
---|---  
## __Свойства
[Key](P_Tessa_Extensions_DefaultExtensionTraceListener_Key.htm)|  Ключ
валидации, который используется для формирования сообщений трассировки. Не
равен null.  
---|---  
[MinConsiderableMilliseconds](P_Tessa_Extensions_DefaultExtensionTraceListener_MinConsiderableMilliseconds.htm)|
Минимальное количество миллисекунд, которое должно выполняться расширение для
того, чтобы для него было создано сообщение трассировки, если используются
трассировщики
[ServerProfile](T_Tessa_Extensions_ExtensionTraceListenerType.htm) или
[ClientProfile](T_Tessa_Extensions_ExtensionTraceListenerType.htm). Если
значение равно 0 или отрицательное, то сообщения трассировки создаются для
всех объектов. Если значение равно null, то время выполнения расширения не
замеряется.  
## __Методы
[Create](M_Tessa_Extensions_DefaultExtensionTraceListener_Create.htm)|
Создаёт объект, выполняющий отслеживание событий в соответствии с заданным
типом.  
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
[NotifyException](M_Tessa_Extensions_ExtensionTraceListener_NotifyException.htm)|
Уведомляет объект о том, что возникло исключение в процессе выполнения метода
расширения, информацию о котором можно получить из заданного контекста.  
(Унаследован от
[ExtensionTraceListener](T_Tessa_Extensions_ExtensionTraceListener.htm))  
[NotifyExecuted](M_Tessa_Extensions_DefaultExtensionTraceListener_NotifyExecuted.htm)|
Уведомляет объект о том, что было завершено выполнение метода расширения,
информацию о котором можно получить из заданного контекста.  
(Переопределяет
[ExtensionTraceListener.NotifyExecuted(IExtensionStrategyContext)](M_Tessa_Extensions_ExtensionTraceListener_NotifyExecuted.htm))  
[NotifyExecuting](M_Tessa_Extensions_DefaultExtensionTraceListener_NotifyExecuting.htm)|
Уведомляет объект о том, что следующим шагом будет выполнение метода
расширения, информацию о котором можно получить из заданного контекста.  
(Переопределяет
[ExtensionTraceListener.NotifyExecuting(IExtensionStrategyContext)](M_Tessa_Extensions_ExtensionTraceListener_NotifyExecuting.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Поля
[DefaultProfileMinConsiderableMilliseconds](F_Tessa_Extensions_DefaultExtensionTraceListener_DefaultProfileMinConsiderableMilliseconds.htm)|
Минимальное количество миллисекунд по умолчанию, которое должно выполняться
расширение для того, чтобы для него было создано сообщение трассировки, если
используются трассировщики
[ServerProfile](T_Tessa_Extensions_ExtensionTraceListenerType.htm) или
[ClientProfile](T_Tessa_Extensions_ExtensionTraceListenerType.htm).  
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
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
