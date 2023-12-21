# DispatcherHelper - класс
Вспомогательные методы для диспетчеризации вызовов в потоке UI.
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public static class DispatcherHelper
VB __Копировать
     Public NotInheritable Class DispatcherHelper
C++ __Копировать
     public ref class DispatcherHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type DispatcherHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ DispatcherHelper
##  __Свойства
[DispatcherService](P_Tessa_UI_DispatcherHelper_DispatcherService.htm)|
Реализация IDispatcherService.  
---|---  
## __Методы
[CheckAccess](M_Tessa_UI_DispatcherHelper_CheckAccess.htm)|  Возвращает
признак того, что код выполняется в потоке диспетчера приложения, т.е. в
основном UI-потоке.  
---|---  
[InvokeInUI(Action)](M_Tessa_UI_DispatcherHelper_InvokeInUI.htm)|  Выполняет
делегат в потоке UI. Не возвращает управление, пока делегат не будет выполнен.  
[InvokeInUI(Action,
DispatcherPriority)](M_Tessa_UI_DispatcherHelper_InvokeInUI_1.htm)|  Выполняет
делегат в потоке UI. Не возвращает управление, пока делегат не будет выполнен.  
[InvokeInUIAsync(Action)](M_Tessa_UI_DispatcherHelper_InvokeInUIAsync.htm)|
Выполняет делегат в потоке UI. Возвращает управление, не дожидаясь его
выполнения.  
[InvokeInUIAsync(Action,
DispatcherPriority)](M_Tessa_UI_DispatcherHelper_InvokeInUIAsync_1.htm)|
Выполняет делегат в потоке UI. Возвращает управление, не дожидаясь его
выполнения.  
[InvokeInUIAsync<T>(Func<T>)](M_Tessa_UI_DispatcherHelper_InvokeInUIAsync__1.htm)|
Выполняет делегат в потоке UI. Возвращает управление, не дожидаясь его
выполнения.  
[InvokeInUIAsync<T>(Func<T>,
DispatcherPriority)](M_Tessa_UI_DispatcherHelper_InvokeInUIAsync__1_1.htm)|
Выполняет делегат в потоке UI. Возвращает управление, не дожидаясь его
выполнения.  
## __См. также
#### Ссылки
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
