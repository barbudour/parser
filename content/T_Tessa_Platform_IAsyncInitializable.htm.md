# IAsyncInitializable - интерфейс
Интерфейс, предоставляющий средства асинхронной инициализации объекта. Если
объект реализует интерфейс, то метод
[InitializeAsync(CancellationToken)](M_Tessa_Platform_IAsyncInitializable_InitializeAsync.htm)
вызывается сразу после конструктора ровно один раз, он позволяет вынести
асинхронную часть конструктора в асинхронный метод. Интерфейс можно
задействовать в расширениях [IExtension](T_Tessa_Extensions_IExtension.htm) и
в ряде типовых сценариев, связанных с созданием объектов UI (контролов,
блоков, форм и др.), и их редакторов (для TessaAdmin).
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IAsyncInitializable
VB __Копировать
     Public Interface IAsyncInitializable
C++ __Копировать
     public interface class IAsyncInitializable
F# __Копировать
     type IAsyncInitializable = interface end
##  __Методы
[InitializeAsync](M_Tessa_Platform_IAsyncInitializable_InitializeAsync.htm)|
Выполняет асинхронную инициализацию объекта.  
---|---  
##  __См. также
#### Ссылки
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
