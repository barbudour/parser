# Tessa.UI.Tiles - пространство имён
API для плиток.
##  __Классы
[Tile](T_Tessa_UI_Tiles_Tile.htm)|  Плитка на панели.  
---|---  
[TileCloningContext](T_Tessa_UI_Tiles_TileCloningContext.htm)|  Контекст
операции по клонированию плиток.  
[TileCollection](T_Tessa_UI_Tiles_TileCollection.htm)|  Коллекция плиток.
Поддерживает защиту от изменений.  
[TileCommandEventArgs](T_Tessa_UI_Tiles_TileCommandEventArgs.htm)|  Аргументы
события, определяющего возможность выполнения команды плитки. Если свойство
[Cancel](https://learn.microsoft.com/dotnet/api/system.componentmodel.canceleventargs.cancel#system-
componentmodel-canceleventargs-cancel) устанавливается равным true, то
выполнение команды отменяется.  
[TileContext](T_Tessa_UI_Tiles_TileContext.htm)|  Объект, содержащий
информацию по контексту операции, связанной с исполнением команды плитки.
Контекст доступен только внутри команды плитки
[Command](P_Tessa_UI_Tiles_ITile_Command.htm).  
[TileContextProxy](T_Tessa_UI_Tiles_TileContextProxy.htm)|  Источник контекста
для плиток, предоставляющий доступ к контексту через делегаты.  
[TileContextSource](T_Tessa_UI_Tiles_TileContextSource.htm)|  Источник
контекста для плиток.  
[TileEvaluationEventArgs](T_Tessa_UI_Tiles_TileEvaluationEventArgs.htm)|
Аргументы события, выполняющего вычисления для изменений состояния и видимости
плиток. Событие распространяется по иерархии плиток.  
[TileEvaluationResult](T_Tessa_UI_Tiles_TileEvaluationResult.htm)|  Результат
вычисления для изменений состояния и видимости плиток.  
[TileExtensions](T_Tessa_UI_Tiles_TileExtensions.htm)|  Расширения для
пространства имён Tessa.UI.Tiles.  
[TileGenerator](T_Tessa_UI_Tiles_TileGenerator.htm)|  Создаёт элементы UI для
отображения плиток.  
[TileGroups](T_Tessa_UI_Tiles_TileGroups.htm)|  Имена стандартных групп
плиток, которые создаются платформенными расширениями.  
[TileHelper](T_Tessa_UI_Tiles_TileHelper.htm)|  Вспомогательный класс для
взаимодействия с плитками.  
[TileManager](T_Tessa_UI_Tiles_TileManager.htm)|  Объект, управляющий
жизненным циклом локальной рабочей области с плитками.  
[TileOrderComparer](T_Tessa_UI_Tiles_TileOrderComparer.htm)|  Выполняет
сравнение порядка следования плиток на основании свойств
[Group](P_Tessa_UI_Tiles_ITile_Group.htm) и
[Order](P_Tessa_UI_Tiles_ITile_Order.htm).  
[TilePanel](T_Tessa_UI_Tiles_TilePanel.htm)|  Панель с плитками.  
[TilePanelContentSource](T_Tessa_UI_Tiles_TilePanelContentSource.htm)|
Источник контента и команд для боковой панели, реализованной посредством
элемента управления [TileSlider](T_Tessa_UI_Tiles_Controls_TileSlider.htm).  
[TileProperties](T_Tessa_UI_Tiles_TileProperties.htm)|  Присоединённые
свойства зависимостей, используемые при отрисовке плиток.  
[TileQueueExecutor](T_Tessa_UI_Tiles_TileQueueExecutor.htm)|  Объект,
используемый для отложенного выполнения команд после закрытия панели с
плитками.  
[TileSource](T_Tessa_UI_Tiles_TileSource.htm)|  Базовый класс для объектов,
предоставляющих доступ к коллекции дочерних плиток и текущему контексту.  
[TileSourceEventArgs](T_Tessa_UI_Tiles_TileSourceEventArgs.htm)|  Аргументы
события, распространяемого по иерархии плиток.  
[TileUIContext](T_Tessa_UI_Tiles_TileUIContext.htm)|  Объект, управляющий
информацией по плиткам, которая может быть связана с контекстом
[IUIContext](T_Tessa_UI_IUIContext.htm).  
[TileWorkspace](T_Tessa_UI_Tiles_TileWorkspace.htm)|  Рабочее место с панелями
плиток.  
[TileWorkspaceModel](T_Tessa_UI_Tiles_TileWorkspaceModel.htm)|  Модель
представления для рабочей области с боковыми панелями плиток.  
[TileWorkspaceNames](T_Tessa_UI_Tiles_TileWorkspaceNames.htm)|  Определяет
имена для регистрации фабрик рабочих областей в контейнере Unity по типу
данных Func<CancellationToken, Task<ITileWorkspace>>.  
## __Структуры
[TileEvaluationAction](T_Tessa_UI_Tiles_TileEvaluationAction.htm)|  Действие
по изменению состояния или видимости плитки.  
---|---  
## __Интерфейсы
[ITile](T_Tessa_UI_Tiles_ITile.htm)|  Плитка на панели.  
---|---  
[ITileCloningContext](T_Tessa_UI_Tiles_ITileCloningContext.htm)|  Контекст
операции по клонированию плиток.  
[ITileContext](T_Tessa_UI_Tiles_ITileContext.htm)|  Объект, содержащий
информацию по контексту операции, связанной с исполнением команды плитки.
Контекст доступен только внутри команды плитки
[Command](P_Tessa_UI_Tiles_ITile_Command.htm).  
[ITileContextSource](T_Tessa_UI_Tiles_ITileContextSource.htm)|  Источник
контекста для плиток. Изменение контекста влияет на все плитки
[ITile](T_Tessa_UI_Tiles_ITile.htm) и панели плиток
[ITilePanel](T_Tessa_UI_Tiles_ITilePanel.htm), которые используют этот
источник данных.  
[ITileGenerator](T_Tessa_UI_Tiles_ITileGenerator.htm)|  Создаёт элементы UI
для отображения плиток.  
[ITileManager](T_Tessa_UI_Tiles_ITileManager.htm)|  Объект, управляющий
жизненным циклом локальной рабочей области с плитками.  
[ITilePanel](T_Tessa_UI_Tiles_ITilePanel.htm)|  Панель с плитками.  
[ITilePanelContentSource](T_Tessa_UI_Tiles_ITilePanelContentSource.htm)|
Источник контента и команд для боковой панели, реализованной посредством
элемента управления [TileSlider](T_Tessa_UI_Tiles_Controls_TileSlider.htm).  
[ITileQueueExecutor](T_Tessa_UI_Tiles_ITileQueueExecutor.htm)|  Объект,
используемый для отложенного выполнения команд после закрытия панели с
плитками.  
[ITileSource](T_Tessa_UI_Tiles_ITileSource.htm)|  Базовый интерфейс для
объектов, предоставляющих доступ к коллекции дочерних плиток и текущему
контексту.  
[ITileUIContext](T_Tessa_UI_Tiles_ITileUIContext.htm)|  Объект, управляющий
информацией по плиткам, которая может быть связана с контекстом
[IUIContext](T_Tessa_UI_IUIContext.htm).  
[ITileVisual](T_Tessa_UI_Tiles_ITileVisual.htm)|  Визуальный объект, который
был сгенерирован посредством
[ITileGenerator](T_Tessa_UI_Tiles_ITileGenerator.htm). При выходе из
визуального дерева следует вызывать метод
[Dispose()](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose) для исправления утечек памяти.  
[ITileWorkspace](T_Tessa_UI_Tiles_ITileWorkspace.htm)|  Рабочая область с
панелями плиток.  
[ITileWorkspaceModel](T_Tessa_UI_Tiles_ITileWorkspaceModel.htm)|  Модель
представления для рабочей области с боковыми панелями плиток.  
## __Перечисления
[TileCommandBehavior](T_Tessa_UI_Tiles_TileCommandBehavior.htm)|  Поведение
панели с плитками после выполнения команды.  
---|---  
[TileCommandEventType](T_Tessa_UI_Tiles_TileCommandEventType.htm)|  Тип
события, в результате которого выполняется команда плитки.  
[TileDirection](T_Tessa_UI_Tiles_TileDirection.htm)|  Направление отрисовки
плиток.  
[TileDividerAppearance](T_Tessa_UI_Tiles_TileDividerAppearance.htm)|
Отображение вертикального разделителя, который индицирует наличие команды для
выполнения при нажатии плитки.  
[TilePanelLocation](T_Tessa_UI_Tiles_TilePanelLocation.htm)|  Местоположение
панели с плитками на рабочей области.  
[TileVerticalAlignment](T_Tessa_UI_Tiles_TileVerticalAlignment.htm)|
Вертикальное выравнивание плитки, используемое при её размещении в панели.
