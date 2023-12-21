# IWebProxyFactory - интерфейс
Фабрика объектов [IWebProxy](T_Tessa_Platform_Runtime_IWebProxy.htm) для
обращения к веб-сервисам системы.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IWebProxyFactory : IAsyncDisposable
VB __Копировать
     Public Interface IWebProxyFactory
    	Inherits IAsyncDisposable
C++ __Копировать
     public interface class IWebProxyFactory : IAsyncDisposable
F# __Копировать
     type IWebProxyFactory = 
        interface
            interface IAsyncDisposable
        end
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable)
##  __Методы
[DisposeAsync](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable.disposeasync#system-
iasyncdisposable-disposeasync)| Performs application-defined tasks associated
with freeing, releasing, or resetting unmanaged resources asynchronously.  
(Унаследован от
[IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable))  
---|---  
[UseProxyAsync<T>](M_Tessa_Platform_Runtime_IWebProxyFactory_UseProxyAsync__1.htm)|
Получает или создаёт потокобезопасный экземпляр прокси-объекта заданного типа
T, который инициализирован для использования.  
## __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
