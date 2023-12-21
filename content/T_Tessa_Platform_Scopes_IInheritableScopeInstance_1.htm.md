# IInheritableScopeInstance<T> \- интерфейс
Экземпляр для наследуемой области видимости объекта заданного типа. Область
видимости существует в контексте текущего потока. Наследуемость определяется
тем, что во вложенных областях видимости возвращается тот же объект, что был
создан для внешней области видимости.
## __Definition
 **Пространство имён:** [Tessa.Platform.Scopes](N_Tessa_Platform_Scopes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IInheritableScopeInstance<out T> : IDisposable, 
    	IAsyncDisposable
    where T : class
VB __Копировать
     Public Interface IInheritableScopeInstance(Of Out T As Class)
    	Inherits IDisposable, IAsyncDisposable
C++ __Копировать
    generic<typename T>
    where T : ref class
    public interface class IInheritableScopeInstance : IDisposable, 
    	IAsyncDisposable
F# __Копировать
     type IInheritableScopeInstance<'T when 'T : not struct> = 
        interface
            interface IDisposable
            interface IAsyncDisposable
        end
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable), [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)
#### Параметры типа
T
    Ссылочный тип значения, область видимости которого определяется.
##  __Свойства
[Value](P_Tessa_Platform_Scopes_IInheritableScopeInstance_1_Value.htm)|
Значение, область видимости которого определяется.  
---|---  
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
##  __См. также
#### Ссылки
[Tessa.Platform.Scopes - пространство имён](N_Tessa_Platform_Scopes.htm)
