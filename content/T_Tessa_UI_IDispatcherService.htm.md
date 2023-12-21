# IDispatcherService - интерфейс
Сервис вспомогательных методов для диспетчеризации вызовов в потоке UI.
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IDispatcherService
VB __Копировать
     Public Interface IDispatcherService
C++ __Копировать
     public interface class IDispatcherService
F# __Копировать
     type IDispatcherService = interface end
##  __Методы
[CheckAccess](M_Tessa_UI_IDispatcherService_CheckAccess.htm)|  Возвращает
признак того, что код выполняется в потоке диспетчера приложения, т.е. в
основном UI-потоке.  
---|---  
[InvokeInUI(Action)](M_Tessa_UI_IDispatcherService_InvokeInUI.htm)|  Выполняет
делегат в потоке UI. Не возвращает управление, пока делегат не будет выполнен.  
[InvokeInUI(Action,
DispatcherPriority)](M_Tessa_UI_IDispatcherService_InvokeInUI_1.htm)|
Выполняет делегат в потоке UI. Не возвращает управление, пока делегат не будет
выполнен.  
[InvokeInUIAsync(Action)](M_Tessa_UI_IDispatcherService_InvokeInUIAsync.htm)|
Выполняет делегат в потоке UI. Возвращает управление, не дожидаясь его
выполнения.  
[InvokeInUIAsync(Action,
DispatcherPriority)](M_Tessa_UI_IDispatcherService_InvokeInUIAsync_1.htm)|
Выполняет делегат в потоке UI. Возвращает управление, не дожидаясь его
выполнения.  
[InvokeInUIAsync<T>(Func<T>)](M_Tessa_UI_IDispatcherService_InvokeInUIAsync__1.htm)|
Выполняет делегат в потоке UI. Возвращает управление, не дожидаясь его
выполнения.  
[InvokeInUIAsync<T>(Func<T>,
DispatcherPriority)](M_Tessa_UI_IDispatcherService_InvokeInUIAsync__1_1.htm)|
Выполняет делегат в потоке UI. Возвращает управление, не дожидаясь его
выполнения.  
## __См. также
#### Ссылки
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
