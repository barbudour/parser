# IWebProxy - интерфейс
Веб-прокси для сервиса ASP.NET Core.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IWebProxy : IAsyncDisposable, 
    	IDisposable, ISealable
VB __Копировать
     Public Interface IWebProxy
    	Inherits IAsyncDisposable, IDisposable, ISealable
C++ __Копировать
     public interface class IWebProxy : IAsyncDisposable, 
    	IDisposable, ISealable
F# __Копировать
     type IWebProxy = 
        interface
            interface IAsyncDisposable
            interface IDisposable
            interface ISealable
        end
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable), [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable), [ISealable](T_Tessa_Platform_ISealable.htm)
##  __Свойства
[BaseUri](P_Tessa_Platform_Runtime_IWebProxy_BaseUri.htm)|  Базовый адрес
папки веб-сервисов системы. Например: https://localhost/tessa. Должен быть
установлен перед вызовом метода у прокси-объекта.  
---|---  
[HttpClient](P_Tessa_Platform_Runtime_IWebProxy_HttpClient.htm)|  Объект,
обеспечивающий соединение с веб-сервисом по протоколам HTTP/HTTPS. Должен быть
установлен перед вызовом метода у прокси-объекта.  
[InstanceName](P_Tessa_Platform_Runtime_IWebProxy_InstanceName.htm)|  Имя
экземпляра сервера, с которым выполняется соединение. Например: default. Если
установлены null или пустая строка, то используется имя экземпляра по
умолчанию. Должен быть установлен перед вызовом метода у прокси-объекта.  
[IsSealed](P_Tessa_Platform_ISealable_IsSealed.htm)| Признак того, что объект
был защищён от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
[SessionTokenHolder](P_Tessa_Platform_Runtime_IWebProxy_SessionTokenHolder.htm)|
Объект, содержащий токен, связанный с текущей сессией, или null, если связь с
сессией не поддерживается.  
[SessionVersionHolder](P_Tessa_Platform_Runtime_IWebProxy_SessionVersionHolder.htm)|
Объект, содержащий версию платформы, связанную с текущей сессией, или null,
если связь с сессией не поддерживается.  
## __Методы
[Dispose](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose)| Performs application-defined tasks associated with
freeing, releasing, or resetting unmanaged resources.  
(Унаследован от
[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable))  
---|---  
[DisposeAsync](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable.disposeasync#system-
iasyncdisposable-disposeasync)| Performs application-defined tasks associated
with freeing, releasing, or resetting unmanaged resources asynchronously.  
(Унаследован от
[IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable))  
[Seal](M_Tessa_Platform_ISealable_Seal.htm)| Защищает объект от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
##  __События
[Disposed](E_Tessa_Platform_Runtime_IWebProxy_Disposed.htm)|  Событие,
выполняемое при освобождении ресурсов, занимаемых объектом, в методе
[System.IDisposable.Dispose].  
---|---  
## __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
