# IScanProvider - интерфейс
Объект, выполняющий сканирование.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Scanning](N_Tessa_Extensions_Platform_Client_Scanning.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IScanProvider : INotifyPropertyChanged, 
    	IAsyncDisposable
VB __Копировать
     Public Interface IScanProvider
    	Inherits INotifyPropertyChanged, IAsyncDisposable
C++ __Копировать
     public interface class IScanProvider : INotifyPropertyChanged, 
    	IAsyncDisposable
F# __Копировать
     type IScanProvider = 
        interface
            interface INotifyPropertyChanged
            interface IAsyncDisposable
        end
Implements
    [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged), [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable)
##  __Свойства
[State](P_Tessa_Extensions_Platform_Client_Scanning_IScanProvider_State.htm)|
Текущее состояние сканирования  
---|---  
## __Методы
[CancelAsync](M_Tessa_Extensions_Platform_Client_Scanning_IScanProvider_CancelAsync.htm)|
Вызывает отмену сканирования  
---|---  
[DisposeAsync](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable.disposeasync#system-
iasyncdisposable-disposeasync)| Performs application-defined tasks associated
with freeing, releasing, or resetting unmanaged resources asynchronously.  
(Унаследован от
[IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable))  
[GetSourcesAsync](M_Tessa_Extensions_Platform_Client_Scanning_IScanProvider_GetSourcesAsync.htm)|
Возвращает список доступных источников сканирования. Значение null аналогично
пустому списку.  
[ScanAsync](M_Tessa_Extensions_Platform_Client_Scanning_IScanProvider_ScanAsync.htm)|
Запускает сканирование для заданного источника. Возвращает признак того, что
сканирование было запущено и отсутствовали ошибки при запуске. Ошибки
выводятся на экран средствами текущего объекта.  
[SetProcessAction](M_Tessa_Extensions_Platform_Client_Scanning_IScanProvider_SetProcessAction.htm)|
Устанавливает функцию, вызываемую для отсканированной страницы.  
## __События
[PropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged.propertychanged)|
Occurs when a property value changes.  
(Унаследован от
[INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Extensions.Platform.Client.Scanning - пространство
имён](N_Tessa_Extensions_Platform_Client_Scanning.htm)
