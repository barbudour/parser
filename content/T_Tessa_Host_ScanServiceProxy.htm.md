# ScanServiceProxy - класс
The scan service proxy.
## __Definition
 **Пространство имён:** [Tessa.Host](N_Tessa_Host.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class ScanServiceProxy : IScanServiceProxy, 
    	IAsyncDisposable, IDisposable, INotifyPropertyChanged, IScanServiceCallback
VB __Копировать
     Public Class ScanServiceProxy
    	Implements IScanServiceProxy, IAsyncDisposable, IDisposable, INotifyPropertyChanged, 
    	IScanServiceCallback
C++ __Копировать
     public ref class ScanServiceProxy : IScanServiceProxy, 
    	IAsyncDisposable, IDisposable, INotifyPropertyChanged, IScanServiceCallback
F# __Копировать
     type ScanServiceProxy = 
        class
            interface IScanServiceProxy
            interface IAsyncDisposable
            interface IDisposable
            interface INotifyPropertyChanged
            interface IScanServiceCallback
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ScanServiceProxy
Implements
    [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged), [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable), [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable), [IScanServiceCallback](T_Tessa_Host_IScanServiceCallback.htm), [IScanServiceProxy](T_Tessa_Host_IScanServiceProxy.htm)
##  __Конструкторы
[ScanServiceProxy](M_Tessa_Host_ScanServiceProxy__ctor.htm)| Инициализирует
новый экземпляр класса ScanServiceProxy  
---|---  
##  __Свойства
[State](P_Tessa_Host_ScanServiceProxy_State.htm)|  Gets Текущее состояние  
---|---  
## __Методы
[CancelAsync](M_Tessa_Host_ScanServiceProxy_CancelAsync.htm)|  Осуществляет
отмену операции сканирования  
---|---  
[Dispose](M_Tessa_Host_ScanServiceProxy_Dispose.htm)| Performs application-
defined tasks associated with freeing, releasing, or resetting unmanaged
resources.  
[DisposeAsync](M_Tessa_Host_ScanServiceProxy_DisposeAsync.htm)| Performs
application-defined tasks associated with freeing, releasing, or resetting
unmanaged resources asynchronously.  
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
[GetSourcesAsync](M_Tessa_Host_ScanServiceProxy_GetSourcesAsync.htm)|
Возвращает список источников сканирования  
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
[OnPropertyChanged](M_Tessa_Host_ScanServiceProxy_OnPropertyChanged.htm)|  The
on property changed.  
[StartScanAsync](M_Tessa_Host_ScanServiceProxy_StartScanAsync.htm)|
Отправляет запрос на сканирование  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __События
[PropertyChanged](E_Tessa_Host_ScanServiceProxy_PropertyChanged.htm)| Occurs
when a property value changes.  
---|---  
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
[Tessa.Host - пространство имён](N_Tessa_Host.htm)
