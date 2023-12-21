# UIExtensions - класс
Методы-расширения для пространства имён Tessa.UI.
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public static class UIExtensions
VB __Копировать
    <ExtensionAttribute>
    Public NotInheritable Class UIExtensions
C++ __Копировать
    [ExtensionAttribute]
    public ref class UIExtensions abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    [<ExtensionAttribute>]
    type UIExtensions = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ UIExtensions
##  __Методы
[AddCombined](M_Tessa_UI_UIExtensions_AddCombined.htm)|  Добавляет привязку на
заданный жест для выполнения команды, причём выполняется агрегация команд при
совпадении жестов.  
---|---  
[AddInputBinding](M_Tessa_UI_UIExtensions_AddInputBinding.htm)|  Добавляет
привязку на заданный жест для выполнения команды плитки, если выполнение такой
команды разрешено.  
[AddKeyBinding](M_Tessa_UI_UIExtensions_AddKeyBinding.htm)|  Добавляет
привязку на горячую клавишу для выполнения команды плитки, если выполнение
такой команды разрешено.  
[AddOrReplaceInputBinding(ICardToolbarItemCollection, ICardToolbarItem,
InputGesture)](M_Tessa_UI_UIExtensions_AddOrReplaceInputBinding.htm)|  
[AddOrReplaceInputBinding(ICardToolbarViewModel, ICardToolbarItem,
InputGesture)](M_Tessa_UI_UIExtensions_AddOrReplaceInputBinding_1.htm)|  
[AsEventArgs](M_Tessa_UI_UIExtensions_AsEventArgs.htm)|  Приводит текущий
объект к [TabSelectedEventArgs](T_Tessa_UI_Cards_TabSelectedEventArgs.htm),
при необходимости создаётся объект-копия.  
[CreateFromTemplateAsync(IAdvancedCardDialogManager, Guid, CreateCardOptions,
CancellationToken)](M_Tessa_UI_UIExtensions_CreateFromTemplateAsync.htm)|
Создаёт карточку по шаблону и открывает её в диалоге. При создании по шаблону
используются и клиентские, и серверные расширения. Возвращает вкладку с
карточкой, созданной по шаблону, или null, если карточку не удалось создать.  
[CreateFromTemplateAsync(IUIHost, Guid, CreateCardOptions,
CancellationToken)](M_Tessa_UI_UIExtensions_CreateFromTemplateAsync_1.htm)|
Создаёт карточку по шаблону и открывает её в новой вкладке. При создании по
шаблону используются и клиентские, и серверные расширения. Возвращает вкладку
с карточкой, созданной по шаблону, или null, если карточку не удалось создать.  
[CreateLinearGradientBrush(Theme, String,
Boolean)](M_Tessa_UI_UIExtensions_CreateLinearGradientBrush.htm)|  Создаёт
кисть
[LinearGradientBrush](https://learn.microsoft.com/dotnet/api/system.windows.media.lineargradientbrush)
с заданным цветом из темы.  
[CreateLinearGradientBrush(Theme, ThemeProperty,
Boolean)](M_Tessa_UI_UIExtensions_CreateLinearGradientBrush_1.htm)|  Создаёт
кисть
[LinearGradientBrush](https://learn.microsoft.com/dotnet/api/system.windows.media.lineargradientbrush)
с заданным цветом из темы.  
[CreatePixelCopy](M_Tessa_UI_UIExtensions_CreatePixelCopy.htm)|  Создаёт
попиксельную копию объекта
[BitmapSource](https://learn.microsoft.com/dotnet/api/system.windows.media.imaging.bitmapsource).
Исходный объект после этого может быть уничтожен.  
[CreateSolidColorBrush(Theme, String,
Boolean)](M_Tessa_UI_UIExtensions_CreateSolidColorBrush.htm)|  Создаёт кисть
[SolidColorBrush](https://learn.microsoft.com/dotnet/api/system.windows.media.solidcolorbrush)
с заданным цветом из темы.  
[CreateSolidColorBrush(Theme, ThemeProperty,
Boolean)](M_Tessa_UI_UIExtensions_CreateSolidColorBrush_1.htm)|  Создаёт кисть
[SolidColorBrush](https://learn.microsoft.com/dotnet/api/system.windows.media.solidcolorbrush)
с заданным цветом из темы.  
[CreateWpfBinding](M_Tessa_UI_UIExtensions_CreateWpfBinding.htm)|  Создаёт
объект привязки
[InputBinding](https://learn.microsoft.com/dotnet/api/system.windows.input.inputbinding)
для использования в WPF. Вызывайте в потоке диспетчера WPF.  
[ExecuteWithExceptionCheckAsync<TExtension,
TExtensionContext>](M_Tessa_UI_UIExtensions_ExecuteWithExceptionCheckAsync__2.htm)|
Выполняет заданный метод расширений с обработкой исключений, при возникновении
которых они логируются и выводятся пользователю.  
[Get<T>](M_Tessa_UI_UIExtensions_Get__1.htm)|  Возвращает значение поля в
строковой секции, заданной в пользовательских настройках. Если секция или поле
не найдены, то выбрасывается
[KeyNotFoundException](https://learn.microsoft.com/dotnet/api/system.collections.generic.keynotfoundexception).  
[GetColor(Theme, String)](M_Tessa_UI_UIExtensions_GetColor.htm)|  Создаёт цвет
[Color](https://learn.microsoft.com/dotnet/api/system.windows.media.color) с
заданным цветом из темы.  
[GetColor(Theme, ThemeProperty)](M_Tessa_UI_UIExtensions_GetColor_1.htm)|
Возвращает цвет
[Color](https://learn.microsoft.com/dotnet/api/system.windows.media.color) с
заданным цветом из темы.  
[GetSection](M_Tessa_UI_UIExtensions_GetSection.htm)|  Возвращает секцию,
заданную в пользовательских настройках.  
[GetTaskColors](M_Tessa_UI_UIExtensions_GetTaskColors.htm)|  Возвращает цвета
заданий, задействуемые для функциональной роли с идентификатором
functionRoleID в соответствии с настройками пользователя. Если в настройках
отсутствует информация по роли, то возвращается объект, содержащий все
свойства как null.  
[GetVisibleSize](M_Tessa_UI_UIExtensions_GetVisibleSize.htm)|  Возвращает
размер области элемента, который сейчас отображается на экране. В обработчике
события
[SizeChanged](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.sizechanged)
можно получить актуальные отображаемые размеры, которые могут быть меньше
ActualWidth/ActualHeight, например, в случае, если элементу явно указаны
Width/Height, но размеры рабочей области (окна) не позволяют контролу
разместиться полностью, и края контрола "обрезаются". В этом случае свойства
ActualWidth/ActualHeight возвращают размеры контролы без учёта "обрезания", а
этот метод - размеры "после обрезания", т.е. те размеры, которые фактически
видит пользователь.  
[Has](M_Tessa_UI_UIExtensions_Has.htm)| Возвращает признак того, что заданный
флаг установлен.  
[HasAny](M_Tessa_UI_UIExtensions_HasAny.htm)| Возвращает признак того, что
один из заданных флагов установлен.  
[HasNot](M_Tessa_UI_UIExtensions_HasNot.htm)| Возвращает признак того, что
заданный флаг не установлен.  
[InitializeByDefault](M_Tessa_UI_UIExtensions_InitializeByDefault.htm)|
Добавляет обработчик события для инициализации дескриптора приложения. Метод
можно безопасно вызывать несколько раз.  
[InvokeNullableDeferredWithExceptionCheckAsync<TEventArgs>](M_Tessa_UI_UIExtensions_InvokeNullableDeferredWithExceptionCheckAsync__1.htm)|
Выполняет заданные обработчики события с обработкой исключений, при
возникновении которых они логируются и выводятся пользователю.  
[InvokeWithExceptionCheck(EventHandler, Object, EventArgs,
Boolean)](M_Tessa_UI_UIExtensions_InvokeWithExceptionCheck.htm)|  Выполняет
заданные обработчики события с обработкой исключений, при возникновении
которых они логируются и выводятся пользователю.  
[InvokeWithExceptionCheck<TEventArgs>(EventHandler<TEventArgs>, Object,
TEventArgs,
Boolean)](M_Tessa_UI_UIExtensions_InvokeWithExceptionCheck__1.htm)|  Выполняет
заданные обработчики события с обработкой исключений, при возникновении
которых они логируются и выводятся пользователю.  
[ModifyBrightness](M_Tessa_UI_UIExtensions_ModifyBrightness.htm)|  Создаёт
цвет, полученный из исходного с коррекцией яркости.  
[RegisterClient](M_Tessa_UI_UIExtensions_RegisterClient.htm)|  Выполняет
регистрацию всех основных API, требуемых на клиенте, в заданном контейнере
Unity. Регистрация для [IUIHost](T_Tessa_UI_IUIHost.htm) не выполняется.  
[RegisterClientExtensionTypes](M_Tessa_UI_UIExtensions_RegisterClientExtensionTypes.htm)|
Выполняет регистрацию клиентских типов расширений в контейнере
[IExtensionContainer](T_Tessa_Extensions_IExtensionContainer.htm).  
[RegisterExtensionTracingOnClient](M_Tessa_UI_UIExtensions_RegisterExtensionTracingOnClient.htm)|
Регистрирует зависимости, связанные с трассировкой расширений со стороны
клиента.  
[RegisterFakeUIHost](M_Tessa_UI_UIExtensions_RegisterFakeUIHost.htm)|
Выполняет регистрацию объекта [IUIHost](T_Tessa_UI_IUIHost.htm), не
выполняющего действий.  
[RegisterFormUIExtensionTypes](M_Tessa_UI_UIExtensions_RegisterFormUIExtensionTypes.htm)|
Выполняет регистрацию стандартных типов расширений для диалогов, построенных
по формам карточек [IFormUIExtension](T_Tessa_UI_IFormUIExtension.htm).  
[RegisterUI](M_Tessa_UI_UIExtensions_RegisterUI.htm)|  Выполняет регистрацию
базового API для работе с UI, в т.ч. API для настроек пользователя и для
иконок, в заданном контейнере Unity.  
[RegisterUIHost](M_Tessa_UI_UIExtensions_RegisterUIHost.htm)|  Выполняет
регистрацию объекта [IUIHost](T_Tessa_UI_IUIHost.htm), выполняющий все
требуемые от него действия.  
[RegisterWorkplaceFilterPolicy](M_Tessa_UI_UIExtensions_RegisterWorkplaceFilterPolicy.htm)|  
[RemoveCombined](M_Tessa_UI_UIExtensions_RemoveCombined.htm)|  Удаляет
привязку на заданный жест для определенной команды. Поиск старой команды
выполняется с помощью commandComparer, либо с помощью ReferenceEquals с
oldCommand. В случае отсутствия старой команды новая команда будет добавлена.  
[RemoveDefaultInitialization](M_Tessa_UI_UIExtensions_RemoveDefaultInitialization.htm)|
Удаляет обработчик события, добавленный методом
[InitializeByDefault(IApplicationDescriptor)](M_Tessa_UI_UIExtensions_InitializeByDefault.htm).  
[RemoveInputBinding(ICardToolbarItemCollection, ICardToolbarItem,
InputGesture)](M_Tessa_UI_UIExtensions_RemoveInputBinding.htm)|  
[RemoveInputBinding(ICardToolbarViewModel, ICardToolbarItem,
InputGesture)](M_Tessa_UI_UIExtensions_RemoveInputBinding_1.htm)|  
[ReplaceCombined](M_Tessa_UI_UIExtensions_ReplaceCombined.htm)|  Заменяет
привязку на заданный жест для выполнения команды, причём выполняется агрегация
команд при совпадении жестов. Поиск старой команды выполняется с помощью
commandComparer, либо с помощью ReferenceEquals с oldCommand. В случае
отсутствия старой команды новая команда будет добавлена.  
[SetAlpha](M_Tessa_UI_UIExtensions_SetAlpha.htm)|  Создаёт цвет с указанным
альфа-каналом alpha, остальные компоненты цвета сохраняются.  
[SetupFromJsonAsync](M_Tessa_UI_UIExtensions_SetupFromJsonAsync.htm)|
Устанавливает настройки в соответствии с сериализованными в текстовый JSON
значениями.  
[ToArgbString](M_Tessa_UI_UIExtensions_ToArgbString.htm)|  Преобразует цвет в
строку в формате #AARRGGBB.  
[ToColor](M_Tessa_UI_UIExtensions_ToColor.htm)|  Возвращает цвет заданного
значение [StorageColor](T_Tessa_Platform_Storage_StorageColor.htm).  
[ToGradientStop](M_Tessa_UI_UIExtensions_ToGradientStop.htm)|  Возвращает
точку градиента для заданного значения
[StorageGradientStop](T_Tessa_Platform_Storage_StorageGradientStop.htm).  
[ToLinearGradientBrush](M_Tessa_UI_UIExtensions_ToLinearGradientBrush.htm)|
Возвращает линейную градиентную кисть для заданного значения
[StorageLinearGradientBrush](T_Tessa_Platform_Storage_StorageLinearGradientBrush.htm).  
[ToPoint](M_Tessa_UI_UIExtensions_ToPoint.htm)|  Возвращает точку для
заданного значения [StoragePoint](T_Tessa_Platform_Storage_StoragePoint.htm).  
[ToStorageColor](M_Tessa_UI_UIExtensions_ToStorageColor.htm)|  Возвращает
значение [StorageColor](T_Tessa_Platform_Storage_StorageColor.htm) по
заданному цвету.  
[ToStorageGradientStop](M_Tessa_UI_UIExtensions_ToStorageGradientStop.htm)|
Возвращает значение [StoragePoint](T_Tessa_Platform_Storage_StoragePoint.htm)
по заданной точке градиента.  
[ToStorageLinearGradientBrush](M_Tessa_UI_UIExtensions_ToStorageLinearGradientBrush.htm)|
Возвращает значение
[StorageLinearGradientBrush](T_Tessa_Platform_Storage_StorageLinearGradientBrush.htm)
по заданной линейной градиентной кисти.  
[ToStoragePoint](M_Tessa_UI_UIExtensions_ToStoragePoint.htm)|  Возвращает
значение [StoragePoint](T_Tessa_Platform_Storage_StoragePoint.htm) по заданной
точке.  
[TryGet<T>](M_Tessa_UI_UIExtensions_TryGet__1.htm)|  Возвращает значение поля
в строковой секции, заданной в пользовательских настройках, или значение по
умолчанию defaultValue, если секция или поле не найдены.  
[TryGetFields<TFrom, TTo>](M_Tessa_UI_UIExtensions_TryGetFields__2.htm)|
Возвращает список значений указанной секции  
[TryGetSection](M_Tessa_UI_UIExtensions_TryGetSection.htm)|  Возвращает
секцию, заданную в пользовательских настройках, или null, если секцию не
удалось получить.  
[UnloadAsync](M_Tessa_UI_UIExtensions_UnloadAsync.htm)|  Выполняет выгрузку
объекта. Если объект уже был выгружен, то повторная выгрузка не выполняется.
Возвращает объект, содержащий сообщения, возникшие в процессе выгрузки, в т.ч.
ошибки.  
[WhenFormUIFunc](M_Tessa_UI_UIExtensions_WhenFormUIFunc.htm)|  Регистрирует
политику фильтрации выполнения методов расширений
[IFormUIExtension](T_Tessa_UI_IFormUIExtension.htm) в соответствии с функцией
isAllowedFunc, которая проверяет контекст расширений. Если зарегистрировано
несколько политик, то должны выполняться все из них.  
## __См. также
#### Ссылки
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
