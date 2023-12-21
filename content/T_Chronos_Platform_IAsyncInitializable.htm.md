# IAsyncInitializable - интерфейс
Интерфейс, предоставляющий средства асинхронной инициализации объекта. Если
объект реализует интерфейс, то метод
[InitializeAsync(CancellationToken)](M_Chronos_Platform_IAsyncInitializable_InitializeAsync.htm)
вызывается сразу после конструктора ровно один раз, он позволяет вынести
асинхронную часть конструктора в асинхронный метод.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IAsyncInitializable
VB __Копировать
     Public Interface IAsyncInitializable
C++ __Копировать
     public interface class IAsyncInitializable
F# __Копировать
     type IAsyncInitializable = interface end
##  __Методы
[InitializeAsync](M_Chronos_Platform_IAsyncInitializable_InitializeAsync.htm)|  
---|---  
## __См. также
#### Ссылки
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
