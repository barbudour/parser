# WebBackgroundServiceQueue - класс
Очередь действий для асинхронной обработки в фоновом режиме веб-сервером.
## __Definition
 **Пространство имён:** [Tessa.Web.Services](N_Tessa_Web_Services.htm)  
 **Сборка:** Tessa.Web (в Tessa.Web.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class WebBackgroundServiceQueue : IWebBackgroundServiceQueue, 
    	IBackgroundServiceQueue
VB __Копировать
     Public NotInheritable Class WebBackgroundServiceQueue
    	Implements IWebBackgroundServiceQueue, IBackgroundServiceQueue
C++ __Копировать
     public ref class WebBackgroundServiceQueue sealed : IWebBackgroundServiceQueue, 
    	IBackgroundServiceQueue
F# __Копировать
     [<SealedAttribute>]
    type WebBackgroundServiceQueue = 
        class
            interface IWebBackgroundServiceQueue
            interface IBackgroundServiceQueue
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ WebBackgroundServiceQueue
Implements
    [IBackgroundServiceQueue](T_Tessa_Platform_IBackgroundServiceQueue.htm), [IWebBackgroundServiceQueue](T_Tessa_Web_Services_IWebBackgroundServiceQueue.htm)
##  __Конструкторы
[WebBackgroundServiceQueue](M_Tessa_Web_Services_WebBackgroundServiceQueue__ctor.htm)|
Инициализирует новый экземпляр класса WebBackgroundServiceQueue  
---|---  
##  __Методы
[DequeAsync](M_Tessa_Web_Services_WebBackgroundServiceQueue_DequeAsync.htm)|
Возвращает следующее действие для обработки и соответствующий отправке данного
действия контекст обработки. Если на момент вызова метода очередь пустая,
метод будет ожидать, пока в очередь не поместят следующее действие.  
---|---  
[EnqueueAsync](M_Tessa_Web_Services_WebBackgroundServiceQueue_EnqueueAsync.htm)|
Помещает действие в очередь асинхронной обработки в фономов режиме.  
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
[Tessa.Web.Services - пространство имён](N_Tessa_Web_Services.htm)
