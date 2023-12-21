# WindowHelper - класс
Вспомогательные методы для взаимодействия с окнами
[Window](https://learn.microsoft.com/dotnet/api/system.windows.window).
## __Definition
 **Пространство имён:** [Tessa.UI.Windows](N_Tessa_UI_Windows.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public static class WindowHelper
VB __Копировать
     Public NotInheritable Class WindowHelper
C++ __Копировать
     public ref class WindowHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type WindowHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ WindowHelper
##  __Методы
[BringModalWindowToTopIfRequired](M_Tessa_UI_Windows_WindowHelper_BringModalWindowToTopIfRequired.htm)|
Выводит текущее доступное модальное окно на передний план.  
---|---  
[ExecuteHwnd](M_Tessa_UI_Windows_WindowHelper_ExecuteHwnd.htm)|  Выполняет
заданное действие для дескриптора окна, который соответствует заданному
объекту. Для объекта Popup это должно быть свойство Popup.Child. Возвращает
признак того, что действие было выполнено, т.к. дескриптор успешно получен.  
[MoveToWorkingArea](M_Tessa_UI_Windows_WindowHelper_MoveToWorkingArea.htm)|
Выполняет перемещение окна с заданным дескриптором в рабочую область, т.е.
так, чтобы оно по-возможности не перекрывало панель задач.  
[SendMinimize](M_Tessa_UI_Windows_WindowHelper_SendMinimize.htm)|  Посылает
событие сворачивания окна. Рекомендуется использовать метод совместно с
[SetMinimizationForWindowStyleNone(Window,
IntPtr)](M_Tessa_UI_Windows_WindowHelper_SetMinimizationForWindowStyleNone.htm).  
[SendResize](M_Tessa_UI_Windows_WindowHelper_SendResize.htm)|  Посылает
событие по изменению размера окна.  
[SetMinimizationForWindowStyleNone](M_Tessa_UI_Windows_WindowHelper_SetMinimizationForWindowStyleNone.htm)|
Устанавливает обработчик на события сворачивания окна в трей и его
разворачивания таким образом, чтобы у окон с
[None](https://learn.microsoft.com/dotnet/api/system.windows.windowstyle)
проигрывалась стандартная анимация сворачивания / разворачивания.
Рекомендуется использовать метод в обработчике
[SourceInitialized](https://learn.microsoft.com/dotnet/api/system.windows.window.sourceinitialized)
окна совместно с
[SendMinimize(IntPtr)](M_Tessa_UI_Windows_WindowHelper_SendMinimize.htm).  
[StartBringModalWindowToTopIfRequired](M_Tessa_UI_Windows_WindowHelper_StartBringModalWindowToTopIfRequired.htm)|
Запускает вывод текущего доступного модального окна на передний план в
ситуации через
[InvokeInUIAsync(Action)](M_Tessa_UI_DispatcherHelper_InvokeInUIAsync.htm).
Запуск может быть отменён через вызов метода
[StopBringModalWindowToTopIfRequired()](M_Tessa_UI_Windows_WindowHelper_StopBringModalWindowToTopIfRequired.htm).  
[StopBringModalWindowToTopIfRequired](M_Tessa_UI_Windows_WindowHelper_StopBringModalWindowToTopIfRequired.htm)|
Производит остановку запущенной операции для вывода текущего доступного
модального окна на передний план, запущенной через
[StartBringModalWindowToTopIfRequired()](M_Tessa_UI_Windows_WindowHelper_StartBringModalWindowToTopIfRequired.htm).  
[TryGetActiveWindow](M_Tessa_UI_Windows_WindowHelper_TryGetActiveWindow.htm)|
Возвращает активное в данный момент окно среди всех окон приложения или null,
если не удалось определить, какое из окон активно.  
## __См. также
#### Ссылки
[Tessa.UI.Windows - пространство имён](N_Tessa_UI_Windows.htm)
