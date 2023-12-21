# IUnityDisposableContainer - интерфейс
Контейнер, содержащий объекты
[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable),
которые будут освобождены при закрытии контейнеров IUnityContainer.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IUnityDisposableContainer
VB __Копировать
     Public Interface IUnityDisposableContainer
C++ __Копировать
     public interface class IUnityDisposableContainer
F# __Копировать
     type IUnityDisposableContainer = interface end
##  __Методы
[DisposeAllAsync](M_Tessa_Platform_IUnityDisposableContainer_DisposeAllAsync.htm)|
Освобождает все экземпляры
[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable) и
[IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable),
которые были зарегистрированы в текущем объекте, в порядке, обратном
регистрации. После вызова невозможны дополнительные регистрации.  
---|---  
[Register(IAsyncDisposable)](M_Tessa_Platform_IUnityDisposableContainer_Register.htm)|
Регистрирует заданный экземпляр
[IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable),
чтобы его метод
[DisposeAsync()](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable.disposeasync#system-
iasyncdisposable-disposeasync) был вызван при освобождении контейнера методом
[DisposeAllAsync()](M_Tessa_Platform_IUnityDisposableContainer_DisposeAllAsync.htm).
Возвращает true, если объект был зарегистрирован, или false, если объект не
может быть зарегистрирован, т.к. все объекты уже были освобождены.  
[Register(IDisposable)](M_Tessa_Platform_IUnityDisposableContainer_Register_1.htm)|
Регистрирует заданный экземпляр
[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable),
чтобы его метод
[Dispose()](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose) был вызван при освобождении контейнера методом
[DisposeAllAsync()](M_Tessa_Platform_IUnityDisposableContainer_DisposeAllAsync.htm).
Возвращает true, если объект был зарегистрирован, или false, если объект не
может быть зарегистрирован, т.к. все объекты уже были освобождены.  
##  __См. также
#### Ссылки
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
