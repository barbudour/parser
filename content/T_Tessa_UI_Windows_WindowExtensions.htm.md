# WindowExtensions - класс
Методы-расширения для класса
[Window](https://learn.microsoft.com/dotnet/api/system.windows.window).
## __Definition
 **Пространство имён:** [Tessa.UI.Windows](N_Tessa_UI_Windows.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public static class WindowExtensions
VB __Копировать
    <ExtensionAttribute>
    Public NotInheritable Class WindowExtensions
C++ __Копировать
    [ExtensionAttribute]
    public ref class WindowExtensions abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    [<ExtensionAttribute>]
    type WindowExtensions = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ WindowExtensions
##  __Методы
[BringWindowToTop](M_Tessa_UI_Windows_WindowExtensions_BringWindowToTop.htm)|
Выводит окно на передний план.  
---|---  
[BringWindowToTopWhenLoaded](M_Tessa_UI_Windows_WindowExtensions_BringWindowToTopWhenLoaded.htm)|
Выводит окно на передний план после того, как оно будет впервые отображено на
экране.  
[CloseOnMiddleButtonDown](M_Tessa_UI_Windows_WindowExtensions_CloseOnMiddleButtonDown.htm)|
Добавляет обработчик события
[MouseDown](https://learn.microsoft.com/dotnet/api/system.windows.uielement.mousedown),
закрывающий окно по клику средней кнопкой мыши.  
[CloseOnPreviewMiddleButtonDown](M_Tessa_UI_Windows_WindowExtensions_CloseOnPreviewMiddleButtonDown.htm)|
Добавляет обработчик события
[PreviewMouseDown](https://learn.microsoft.com/dotnet/api/system.windows.uielement.previewmousedown),
закрывающий окно по клику средней кнопкой мыши.  
[DisableFocusOnClick](M_Tessa_UI_Windows_WindowExtensions_DisableFocusOnClick.htm)|
Отключает перевод фокуса для окна при клике мышью.  
[ForceDragMove](M_Tessa_UI_Windows_WindowExtensions_ForceDragMove.htm)|  
[GetActualTopLeft](M_Tessa_UI_Windows_WindowExtensions_GetActualTopLeft.htm)|
Возвращает точку, соответствующую левому верхнему углу окна для его текущего
состояния. Если точку получить невозможно, то возвращает 0. Когда окно
свёрнуто или развёрнуто, то возвращает левый верхний угол дисплея, на котором
размещается окно.  
[GetIntPtr](M_Tessa_UI_Windows_WindowExtensions_GetIntPtr.htm)|  Возвращает
дескриптор [IntPtr](https://learn.microsoft.com/dotnet/api/system.intptr) для
заданного окна.  
[HideMinimizeAndMaximizeButtons](M_Tessa_UI_Windows_WindowExtensions_HideMinimizeAndMaximizeButtons.htm)|
Скрывает кнопки "Свернуть" и "Развернуть" в окне WPF. Метод рекомендуется
использовать в обработчике события
[SourceInitialized](https://learn.microsoft.com/dotnet/api/system.windows.window.sourceinitialized).  
[HideMinimizeButton](M_Tessa_UI_Windows_WindowExtensions_HideMinimizeButton.htm)|
Скрывает кнопку "Свернуть" в окне WPF. Метод рекомендуется использовать в
обработчике события
[SourceInitialized](https://learn.microsoft.com/dotnet/api/system.windows.window.sourceinitialized).  
[IsAvailable](M_Tessa_UI_Windows_WindowExtensions_IsAvailable.htm)|
Возвращает признак того, что окно не заблокировано другими модальными окнами.  
[IsModal](M_Tessa_UI_Windows_WindowExtensions_IsModal.htm)|  Возвращает
признак того, является ли указанное окно модальным.  
[MaximizeOnOpenInsideCorrespondingScreen](M_Tessa_UI_Windows_WindowExtensions_MaximizeOnOpenInsideCorrespondingScreen.htm)|
Указывает, что окно будет развёрнуто на весь экран сразу при открытии, причём
дисплей, на котором отображается окно, определяется динамически в момент
открытия. Если же просто установить свойство перед открытием window.State =
WindowState.Maximized, то окно будет открыто на том дисплее, на котором было
впервые открыто основное окно приложения (причём неважно, куда окно было
перенесено в дальнейшем). Такое поведение обусловлено ошибкой в WPF, поэтому
используйте этот метод для разворачивания окна на корректном дисплее.  
[PreventFocus](M_Tessa_UI_Windows_WindowExtensions_PreventFocus.htm)|
Предотвращает переход фокуса на окно. Метод рекомендуется использовать в
перегрузке метода
[OnActivated(EventArgs)](https://learn.microsoft.com/dotnet/api/system.windows.window.onactivated#system-
windows-window-onactivated\(system-eventargs\)).  
[RegisterShell](M_Tessa_UI_Windows_WindowExtensions_RegisterShell.htm)|
Выполняет регистрацию API по работе с объектом
[ITessaShell](T_Tessa_UI_Windows_ITessaShell.htm) в заданном контейнере Unity.  
[ResolveOwnerAsActiveWindow](M_Tessa_UI_Windows_WindowExtensions_ResolveOwnerAsActiveWindow.htm)|
Устанавливает последнее активное окно как владельца текущего окна ownedWindow.
Если активное окно отсутствует, то в качестве владельца назначается основное
окно приложения. Рекомендуется вызвать метод после того, как выполнена
инициализация окна (т.е. после вызова конструктора), но перед первым
отображением. Метод не выполняет действий, если вызван из потока, отличного от
основного потока приложения или если текущий объект является активным окном
или главным окном приложения.  
[SetMaximizeOnShow](M_Tessa_UI_Windows_WindowExtensions_SetMaximizeOnShow.htm)|
Устанавливает признак состояния развёрнутости окна на весь экран при повторном
отображении скрытого окна. Метод можно применять только к окну, которое было
скрыто методом
[Hide()](https://learn.microsoft.com/dotnet/api/system.windows.window.hide#system-
windows-window-hide) или через установку скрытия в свойстве
[Visibility](https://learn.microsoft.com/dotnet/api/system.windows.uielement.visibility#system-
windows-uielement-visibility).  
[ShowDialogWithReplace](M_Tessa_UI_Windows_WindowExtensions_ShowDialogWithReplace.htm)|
Производит отображение диалога в модальном режиме с заменой предыдущего
активного окна, если оно есть. Предыдущее активное окно скрывается и
отображается только после закрытия отображаемого диалога. Не производит
скрытие основного окна клиента из [!:Application.Current.MainWindow].  
[TryCloseSafe](M_Tessa_UI_Windows_WindowExtensions_TryCloseSafe.htm)|
Закрывает окно, если этому не препятствует наличие дочерних модальных окно.
Возвращает признак того, что окно успешно закрыто. Используйте метод для
закрытия окна с использованием горячих клавиш.  
[TryGetUIContext](M_Tessa_UI_Windows_WindowExtensions_TryGetUIContext.htm)|
Возвращает объект [IUIContext](T_Tessa_UI_IUIContext.htm), соответствующий
вкладке приложения, или null, если объект не связана со вкладкой.  
## __См. также
#### Ссылки
[Tessa.UI.Windows - пространство имён](N_Tessa_UI_Windows.htm)
