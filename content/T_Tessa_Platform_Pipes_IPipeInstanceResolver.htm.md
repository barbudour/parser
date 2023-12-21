# IPipeInstanceResolver - интерфейс
Объект, управляющий временем жизни экземпляров объектов, реализующих бизнес-
логику для использования в канале.
## __Definition
 **Пространство имён:** [Tessa.Platform.Pipes](N_Tessa_Platform_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IPipeInstanceResolver : IAsyncDisposable, 
    	IDisposable
VB __Копировать
     Public Interface IPipeInstanceResolver
    	Inherits IAsyncDisposable, IDisposable
C++ __Копировать
     public interface class IPipeInstanceResolver : IAsyncDisposable, 
    	IDisposable
F# __Копировать
     type IPipeInstanceResolver = 
        interface
            interface IAsyncDisposable
            interface IDisposable
        end
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable), [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)
##  __Методы
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
[ResolveAsync](M_Tessa_Platform_Pipes_IPipeInstanceResolver_ResolveAsync.htm)|
Возвращает экземпляр объекта по заданному типу. Для экземпляра выполняется
инициализация [IAsyncInitializable](T_Tessa_Platform_IAsyncInitializable.htm),
а при освобождении текущего экземпляра IPipeInstanceResolver освобождаются все
созданные им объекты, которые реализуют
[IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable)
или [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable).
Тип объекта должен быть предварительно зарегистрирован в фабрике
[IPipeInstanceFactory](T_Tessa_Platform_Pipes_IPipeInstanceFactory.htm).  
## __Методы расширения
[ResolveAsync<T>](M_Tessa_Platform_Pipes_PipesExtensions_ResolveAsync__1.htm)|
Возвращает экземпляр объекта по заданному типу. Для экземпляра выполняется
инициализация [IAsyncInitializable](T_Tessa_Platform_IAsyncInitializable.htm),
а при освобождении текущего экземпляра IPipeInstanceResolver освобождаются все
созданные им объекты, которые реализуют
[IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable)
или [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable).
Тип объекта должен быть предварительно зарегистрирован в фабрике
[IPipeInstanceFactory](T_Tessa_Platform_Pipes_IPipeInstanceFactory.htm).  
(Определяется [PipesExtensions](T_Tessa_Platform_Pipes_PipesExtensions.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Platform.Pipes - пространство имён](N_Tessa_Platform_Pipes.htm)
