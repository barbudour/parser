# IScanServiceProxy - интерфейс
Описание клиента для взаимодействия с сервисом сканирования предоставляемым
Tessa Host
##  __Definition
 **Пространство имён:** [Tessa.Host](N_Tessa_Host.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IScanServiceProxy : IAsyncDisposable, 
    	IDisposable, INotifyPropertyChanged
VB __Копировать
     Public Interface IScanServiceProxy
    	Inherits IAsyncDisposable, IDisposable, INotifyPropertyChanged
C++ __Копировать
     public interface class IScanServiceProxy : IAsyncDisposable, 
    	IDisposable, INotifyPropertyChanged
F# __Копировать
     type IScanServiceProxy = 
        interface
            interface IAsyncDisposable
            interface IDisposable
            interface INotifyPropertyChanged
        end
Implements
    [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged), [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable), [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)
##  __Свойства
[State](P_Tessa_Host_IScanServiceProxy_State.htm)|  Gets Текущее состояние  
---|---  
## __Методы
[CancelAsync](M_Tessa_Host_IScanServiceProxy_CancelAsync.htm)|  Осуществляет
отмену операции сканирования  
---|---  
[Dispose](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose)| Performs application-defined tasks associated with
freeing, releasing, or resetting unmanaged resources.  
(Унаследован от
[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable))  
[DisposeAsync](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable.disposeasync#system-
iasyncdisposable-disposeasync)| Performs application-defined tasks associated
with freeing, releasing, or resetting unmanaged resources asynchronously.  
(Унаследован от
[IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable))  
[GetSourcesAsync](M_Tessa_Host_IScanServiceProxy_GetSourcesAsync.htm)|
Возвращает список источников сканирования  
[StartScanAsync](M_Tessa_Host_IScanServiceProxy_StartScanAsync.htm)|
Отправляет запрос на сканирование  
## __События
[PropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged.propertychanged)|
Occurs when a property value changes.  
(Унаследован от
[INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Host - пространство имён](N_Tessa_Host.htm)
