# IScopeContextInstance<TContext> \- интерфейс
Экземпляр области операции с контекстом. Вызов
[Dispose()](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose) завершает операцию, причём текущей назначается предыдущая
операция.
## __Definition
 **Пространство имён:** [Tessa.Platform.Scopes](N_Tessa_Platform_Scopes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IScopeContextInstance<out TContext> : IScopeContextInstanceBase<TContext>, 
    	IDisposable, IAsyncDisposable
VB __Копировать
     Public Interface IScopeContextInstance(Of Out TContext)
    	Inherits IScopeContextInstanceBase(Of TContext), IDisposable, IAsyncDisposable
C++ __Копировать
    generic<typename TContext>
    public interface class IScopeContextInstance : IScopeContextInstanceBase<TContext>, 
    	IDisposable, IAsyncDisposable
F# __Копировать
     type IScopeContextInstance<'TContext> = 
        interface
            interface IScopeContextInstanceBase<'TContext>
            interface IDisposable
            interface IAsyncDisposable
        end
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable), [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable), [IScopeContextInstanceBase](T_Tessa_Platform_Scopes_IScopeContextInstanceBase_1.htm)<TContext>
#### Параметры типа
TContext
    Тип контекста операции.
##  __Свойства
[Context](P_Tessa_Platform_Scopes_IScopeContextInstanceBase_1_Context.htm)|
Контекст, установленный внутри текущей операции.  
(Унаследован от
[IScopeContextInstanceBase<TContext>](T_Tessa_Platform_Scopes_IScopeContextInstanceBase_1.htm))  
---|---  
[Parent](P_Tessa_Platform_Scopes_IScopeContextInstanceBase_1_Parent.htm)|
Информация по родительскому контексту или null, если родительский контекст
отсутствует.  
(Унаследован от
[IScopeContextInstanceBase<TContext>](T_Tessa_Platform_Scopes_IScopeContextInstanceBase_1.htm))  
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
