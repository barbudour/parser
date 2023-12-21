# UIHelper - класс
Вспомогательные методы для взаимодействия с UI в Tessa.
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public static class UIHelper
VB __Копировать
     Public NotInheritable Class UIHelper
C++ __Копировать
     public ref class UIHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type UIHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ UIHelper
##  __Свойства
[Aero](P_Tessa_UI_UIHelper_Aero.htm)|  Словарь ресурсов с общими ресурсами.  
---|---  
[CurrentUICultureStringComparer](P_Tessa_UI_UIHelper_CurrentUICultureStringComparer.htm)|
Компарер строк с учетом текущей культуры UI.  
[Generic](P_Tessa_UI_UIHelper_Generic.htm)|  Словарь ресурсов с общими
ресурсами.  
[Icons](P_Tessa_UI_UIHelper_Icons.htm)|  Словарь ресурсов со стандартными
иконками.  
[MaxImageProcessingParallelThreads](P_Tessa_UI_UIHelper_MaxImageProcessingParallelThreads.htm)|
Максимальное количество потоков, используемых в параллельных операциях для
обработки изображений, например, в процессе сканирования или редактирования
изображений в TessaClient. Количество потоков влияет на объём потребляемой
памяти, поэтому устанавливать его слишком большим нельзя, даже если у
процессора много ядер. По умолчанию значение не больше 4. При установке
значения больше, чем количество логических ядер, принятым будет количество
логических ядер (т.е. это максимум, который может вернуть свойство).  
[StoredThemeName](P_Tessa_UI_UIHelper_StoredThemeName.htm)|  Имя темы,
сохранённой в настройках.  
[UnknownContextExecutorProvider](P_Tessa_UI_UIHelper_UnknownContextExecutorProvider.htm)|
Объект, предоставляющий доступ к делегату
[UnknownContextExecutorAsync(Func<IUIContext, CancellationToken, ValueTask>,
CancellationToken)](M_Tessa_UI_UIHelper_UnknownContextExecutorAsync.htm),
выполняющему действие в неизвестном контексте
[IUIContext](T_Tessa_UI_IUIContext.htm).  
## __Методы
[CreateBitmapSource](M_Tessa_UI_UIHelper_CreateBitmapSource.htm)|  Создаёт
объект
[BitmapSource](https://learn.microsoft.com/dotnet/api/system.windows.media.imaging.bitmapsource)
по Win32-изображению
[Bitmap](https://learn.microsoft.com/dotnet/api/system.drawing.bitmap).  
---|---  
[CreateThemeBinding(String,
ThemePropertyConversionType)](M_Tessa_UI_UIHelper_CreateThemeBinding.htm)|
Создаёт привязку Binding к заданному свойству темы.  
[CreateThemeBinding(ThemeProperty,
ThemePropertyConversionType)](M_Tessa_UI_UIHelper_CreateThemeBinding_1.htm)|
Создаёт привязку Binding к заданному свойству темы.  
[CreateToolTipStyle](M_Tessa_UI_UIHelper_CreateToolTipStyle.htm)|  Создаёт
стиль, который добавляет задержку между показом всплывающих подсказок.
BetweenShowDelay не подходит, т.к. даже со значением 0 при переходе мыши между
рядом стоящими объектами (например, это рядом расположенные плитки)
всплывающая подсказка всё равно отображается без задержки.  
[ExecutePropertyChangedAsync](M_Tessa_UI_UIHelper_ExecutePropertyChangedAsync.htm)|
Асинхронно выполняет действие по умолчанию, соответствующее вызову события
PropertyChanged в основном потоке UI. Если выполнение уже производится в
потоке UI, то переключения потока не происходит.  
[FindParent<T>](M_Tessa_UI_UIHelper_FindParent__1.htm)|  Возвращает
визуального родителя типа T для reference заданного объекта, используя
особенности визуального дерева, логического дерева и
[ContentElement](https://learn.microsoft.com/dotnet/api/system.windows.contentelement).
Возвращает null, если объект заданного типа (или его наследника) не найден.  
[FindVisualParent<T>](M_Tessa_UI_UIHelper_FindVisualParent__1.htm)|
Возвращает визуального родителя типа T для reference заданного объекта,
используя обход только визуального дерева (не логического и не учитывая
[ContentElement](https://learn.microsoft.com/dotnet/api/system.windows.contentelement)).
Возвращает null, если объект заданного типа (или его наследника) не найден.  
[GenerateThumbnail(String,
Int32)](M_Tessa_UI_UIHelper_GenerateThumbnail_1.htm)|  Возвращает
пропорционально уменьшенное изображение заданной ширины width по содержимому
изображения из файла filePath.  
[GenerateThumbnail(Stream, BitmapEncoder,
Int32)](M_Tessa_UI_UIHelper_GenerateThumbnail.htm)|  Возвращает
пропорционально уменьшенное изображение заданной ширины width по содержимому
изображения из потока stream.  
[GetBitmapImage](M_Tessa_UI_UIHelper_GetBitmapImage.htm)|  Возвращает объект
[BitmapImage](https://learn.microsoft.com/dotnet/api/system.windows.media.imaging.bitmapimage),
созданный по данным в потоке stream.  
[GetBitmapImageAsync](M_Tessa_UI_UIHelper_GetBitmapImageAsync.htm)|
Возвращает объект
[BitmapImage](https://learn.microsoft.com/dotnet/api/system.windows.media.imaging.bitmapimage),
полученный по пути filePath.  
[GetBrushFromArgbString](M_Tessa_UI_UIHelper_GetBrushFromArgbString.htm)|
Возвращает кисть с цветом, полученным из строки в формате #AARRGGBB или из
другой строки, которую можно преобразовать в цвет стандартными средствами.  
[GetColorFromArgbString](M_Tessa_UI_UIHelper_GetColorFromArgbString.htm)|
Возвращает цвет, полученный из строки в формате #AARRGGBB или из другой
строки, которую можно преобразовать в цвет стандартными средствами.  
[GetParent](M_Tessa_UI_UIHelper_GetParent.htm)|  Возвращает визуального
родителя заданного объекта. Является аналогом методов
[GetParent(DependencyObject)](https://learn.microsoft.com/dotnet/api/system.windows.media.visualtreehelper.getparent#system-
windows-media-visualtreehelper-getparent\(system-windows-dependencyobject\)) и
[GetParent(DependencyObject)](https://learn.microsoft.com/dotnet/api/system.windows.logicaltreehelper.getparent#system-
windows-logicaltreehelper-getparent\(system-windows-dependencyobject\)), но
учитывает особенности
[ContentElement](https://learn.microsoft.com/dotnet/api/system.windows.contentelement)
и
[FrameworkElement](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement).  
[GetStreamWithOrientation](M_Tessa_UI_UIHelper_GetStreamWithOrientation.htm)|
Возвращает поток данных и значение поворота
[Rotation](https://learn.microsoft.com/dotnet/api/system.windows.media.imaging.rotation),
который необходимо применить к создаваемому на основе потока изображению
[BitmapImage](https://learn.microsoft.com/dotnet/api/system.windows.media.imaging.bitmapimage)
с учетом ориентации фотографии.  
[InvokeStaAction](M_Tessa_UI_UIHelper_InvokeStaAction.htm)|  Выполняет
заданный метод в потоке
[STA](https://learn.microsoft.com/dotnet/api/system.threading.apartmentstate).
Если текущий поток не подходит для выполнения, то создаётся новый поток, в нём
выполняется метод и ожидается его завершение.  
[Render(UIElement)](M_Tessa_UI_UIHelper_Render_1.htm)|  Выполняет рендеринг
заданного объекта
[UIElement](https://learn.microsoft.com/dotnet/api/system.windows.uielement),
используя его минимальный предпочитаемый размер без ограничений. Возвращает
отрендеренное изображение
[BitmapFrame](https://learn.microsoft.com/dotnet/api/system.windows.media.imaging.bitmapframe),
которое может использоваться, например, в
[PngBitmapEncoder](https://learn.microsoft.com/dotnet/api/system.windows.media.imaging.pngbitmapencoder)
для преобразования в изображение определённого формата. Метод необходимо
вызывать в потоке
[STA](https://learn.microsoft.com/dotnet/api/system.threading.apartmentstate).
Для этого можно использовать метод
[InvokeStaAction(Action)](M_Tessa_UI_UIHelper_InvokeStaAction.htm).  
[Render(Visual, Size)](M_Tessa_UI_UIHelper_Render.htm)|  Выполняет рендеринг
заданного объекта
[Visual](https://learn.microsoft.com/dotnet/api/system.windows.media.visual),
используя заданный размер изображения, в который объект должен быть "вписан".
Возвращает отрендеренное изображение
[BitmapFrame](https://learn.microsoft.com/dotnet/api/system.windows.media.imaging.bitmapframe),
которое может использоваться, например, в
[PngBitmapEncoder](https://learn.microsoft.com/dotnet/api/system.windows.media.imaging.pngbitmapencoder)
для преобразования в изображение определённого формата. Метод необходимо
вызывать в потоке
[STA](https://learn.microsoft.com/dotnet/api/system.threading.apartmentstate).
Для этого можно использовать метод
[InvokeStaAction(Action)](M_Tessa_UI_UIHelper_InvokeStaAction.htm).  
[RenderWindow](M_Tessa_UI_UIHelper_RenderWindow.htm)|  Выполняет рендеринг
содержимого окна по заданному
[IntPtr](https://learn.microsoft.com/dotnet/api/system.intptr) в объект
[BitmapSource](https://learn.microsoft.com/dotnet/api/system.windows.media.imaging.bitmapsource).  
[RenderWindowToBitmap](M_Tessa_UI_UIHelper_RenderWindowToBitmap.htm)|
Выполняет рендеринг содержимого окна по заданному
[IntPtr](https://learn.microsoft.com/dotnet/api/system.intptr) в объект
[Bitmap](https://learn.microsoft.com/dotnet/api/system.drawing.bitmap).  
[SetDefaultWindowStyle](M_Tessa_UI_UIHelper_SetDefaultWindowStyle.htm)|
Устанавливает стиль по умолчанию для всех стандартных окон Tessa, а также для
перечисленных типов, которые унаследованы от
[Window](https://learn.microsoft.com/dotnet/api/system.windows.window). Метод
следует вызывать ровно один раз при старте приложения перед отрисовкой любых
окон.  
[SubscribeWorkspaceClosingEvents](M_Tessa_UI_UIHelper_SubscribeWorkspaceClosingEvents.htm)|
Осуществляет взаимную подписку на события закрытия для окна window и его
модели представления model, которая реализует интерфейс
[IWorkspaceModel](T_Tessa_UI_IWorkspaceModel.htm).  
[TryGetDescendant<T>](M_Tessa_UI_UIHelper_TryGetDescendant__1.htm)|
Возвращает первый объект типа T располагающийся вниз по визуальному дереву в
source  
[UnknownContextExecutorAsync](M_Tessa_UI_UIHelper_UnknownContextExecutorAsync.htm)|
Метод по выполнению действий в неизвестном контексте
[Unknown](P_Tessa_UI_UIContext_Unknown.htm). Для модели представления карточки
[ICardModel](T_Tessa_UI_Cards_ICardModel.htm) метод можно указать посредством
вызова
[SetContextExecutor(UIContextExecutorAsync)](M_Tessa_UI_Cards_ICardModel_SetContextExecutor.htm).  
## __Поля
[BitmapOrientationQueryKey](F_Tessa_UI_UIHelper_BitmapOrientationQueryKey.htm)|
Ключ для получения ориентации фотографии из метаданных изображения.  
---|---  
[DefaultTileAreaClickDelayMilliseconds](F_Tessa_UI_UIHelper_DefaultTileAreaClickDelayMilliseconds.htm)|
Задержка в миллисекундах при открытии боковой панели через нажатие на
специальную область в углу экрана.  
[DefaultTileButtonDelayMilliseconds](F_Tessa_UI_UIHelper_DefaultTileButtonDelayMilliseconds.htm)|
Задержка в миллисекундах при открытии боковой панели через нажатие на кнопку.  
[DefaultTileHotkeyDelayMilliseconds](F_Tessa_UI_UIHelper_DefaultTileHotkeyDelayMilliseconds.htm)|
Задержка в миллисекундах при открытии боковой панели через горячую клавишу.  
## __См. также
#### Ссылки
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
