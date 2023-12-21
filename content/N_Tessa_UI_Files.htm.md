# Tessa.UI.Files - пространство имён
API для управления файлами в UI.
##  __Классы
[AggregateFilePreviewInfoCache](T_Tessa_UI_Files_AggregateFilePreviewInfoCache.htm)|
Кэш, предоставляющий информацию по предпросмотру файлов на основании агрегации
других объектов
[IFilePreviewInfoCache](T_Tessa_UI_Files_IFilePreviewInfoCache.htm).  
---|---  
[ConfigurationFilePreviewInfoCache](T_Tessa_UI_Files_ConfigurationFilePreviewInfoCache.htm)|
Кэш, предоставляющий информацию по предпросмотру файлов из конфигурационного
файла. Доступен только для чтения.  
[EmptyFileControlManager](T_Tessa_UI_Files_EmptyFileControlManager.htm)|
Объект, не выполняющий действий при управлении контролами
[IFileControl](T_Tessa_UI_Files_IFileControl.htm).  
[FileCaptionSorting](T_Tessa_UI_Files_FileCaptionSorting.htm)|  Сортировка
файлов по отображаемому имени
[Caption](P_Tessa_UI_Files_IFileViewModel_Caption.htm), которая может быть
выбрана в элементе управления
[IFileControl](T_Tessa_UI_Files_IFileControl.htm).  
[FileCategoryGrouping](T_Tessa_UI_Files_FileCategoryGrouping.htm)|
Группировка по категории файла [Category](P_Tessa_Files_IFile_Category.htm).  
[FileControl](T_Tessa_UI_Files_FileControl.htm)|  Элемент управления,
отображающий файлы.  
[FileControl.State](T_Tessa_UI_Files_FileControl_State.htm)|  Состояние
элемента управления.  
[FileControlCancelEventArgs](T_Tessa_UI_Files_FileControlCancelEventArgs.htm)|
Аргументы событий, отслеживающих изменения с файлами
[IFile](T_Tessa_Files_IFile.htm) внутри контейнера
[IFileContainer](T_Tessa_Files_IFileContainer.htm) для произведения действий с
элементом управления [IFileControl](T_Tessa_UI_Files_IFileControl.htm). Если
обработчик таких событий устанавливает значение
[Cancel](https://learn.microsoft.com/dotnet/api/system.componentmodel.canceleventargs.cancel#system-
componentmodel-canceleventargs-cancel) равным true, то изменений в элементе
управления не производится.  
[FileControlEventArgs](T_Tessa_UI_Files_FileControlEventArgs.htm)|  Аргументы
событий, отслеживающих изменения с файлами [IFile](T_Tessa_Files_IFile.htm)
внутри контейнера [IFileContainer](T_Tessa_Files_IFileContainer.htm) для
произведения действий с элементом управления
[IFileControl](T_Tessa_UI_Files_IFileControl.htm).  
[FileControlExtension](T_Tessa_UI_Files_FileControlExtension.htm)|  Базовый
класс для расширения, связанного с элементом управления файлами. Все методы
расширения по умолчанию не выполняются действий.  
[FileControlExtensionContext](T_Tessa_UI_Files_FileControlExtensionContext.htm)|
Контекст расширений, выполняемых для элемента управления файлами
[IFileControl](T_Tessa_UI_Files_IFileControl.htm).  
[FileControlManager](T_Tessa_UI_Files_FileControlManager.htm)|  Объект,
управляющий контролами [IFileControl](T_Tessa_UI_Files_IFileControl.htm).  
[FileControlObject](T_Tessa_UI_Files_FileControlObject.htm)|  Базовый класс
для сортировки [IFileSorting](T_Tessa_UI_Files_IFileSorting.htm), группировки
[IFileGrouping](T_Tessa_UI_Files_IFileGrouping.htm) и фильтрации
[IFileFiltering](T_Tessa_UI_Files_IFileFiltering.htm).  
[FileCopyGrouping](T_Tessa_UI_Files_FileCopyGrouping.htm)|  Группировка по
копиям файла в зависимости от ссылки на файл в свойстве
[Origin](P_Tessa_Files_IFile_Origin.htm).  
[FileCopySorting](T_Tessa_UI_Files_FileCopySorting.htm)|  Сортировка по связи
копия - оригинал.  
[FileDelegate<TDelegate>](T_Tessa_UI_Files_FileDelegate_1.htm)|  Объект,
описывающий делегат, вызываемый при изменении свойств файла
[IFile](T_Tessa_Files_IFile.htm) и / или модели представления файла
[IFileViewModel](T_Tessa_UI_Files_IFileViewModel.htm).  
[FileDelegateFiltering](T_Tessa_UI_Files_FileDelegateFiltering.htm)|
Фильтрация файлов, поведение которой определяется посредством делегатов.
Фильтрация может быть выбрана в элементе управления
[IFileControl](T_Tessa_UI_Files_IFileControl.htm).  
[FileDelegateGrouping](T_Tessa_UI_Files_FileDelegateGrouping.htm)|
Группировка файлов, поведение которой определяется посредством делегатов.
Группировка может быть выбрана в элементе управления
[IFileControl](T_Tessa_UI_Files_IFileControl.htm).  
[FileDelegateManager<TDelegate>](T_Tessa_UI_Files_FileDelegateManager_1.htm)|
Объект, управляющий стеком делегатов
[FileDelegate<TDelegate>](T_Tessa_UI_Files_FileDelegate_1.htm), в котором
можно запоминать и восстанавливать делегаты.  
[FileDelegateSorting](T_Tessa_UI_Files_FileDelegateSorting.htm)|  Сортировка
файлов, поведение которой определяется посредством делегатов. Сортировка может
быть выбрана в элементе управления
[IFileControl](T_Tessa_UI_Files_IFileControl.htm).  
[FileExtension](T_Tessa_UI_Files_FileExtension.htm)|  Базовый класс для
расширения, связанного с файлом, который расположен в элементе управления
файлами. Все методы расширения по умолчанию не выполняются действий.  
[FileExtensionCachedAccessor](T_Tessa_UI_Files_FileExtensionCachedAccessor.htm)|
Объект, предоставляющий доступ к списку расширений файлов, который содержится
в указанной карточке настроек в заданном поле как список расширений,
разделённых пробелами.  
[FileExtensionContext](T_Tessa_UI_Files_FileExtensionContext.htm)|  Контекст
расширений, выполняемых для файла [IFile](T_Tessa_Files_IFile.htm) в элементе
управления файлами [IFileControl](T_Tessa_UI_Files_IFileControl.htm).  
[FileExtensionContextBase](T_Tessa_UI_Files_FileExtensionContextBase.htm)|
Базовый объект для контекста расширений, выполняемых для объекта файлового
API, такого как файл, версия файла или элемент управления файлами.  
[FileFiltering](T_Tessa_UI_Files_FileFiltering.htm)|  Базовый класс для
фильтрации файлов.  
[FileGrouping](T_Tessa_UI_Files_FileGrouping.htm)|  Базовый класс для
группировки файлов, которая может быть выбрана в элементе управления
[IFileControl](T_Tessa_UI_Files_IFileControl.htm).  
[FileGroupingCollection](T_Tessa_UI_Files_FileGroupingCollection.htm)|
Коллекция группировок файлов
[IFileGrouping](T_Tessa_UI_Files_IFileGrouping.htm).  
[FileGroupingFiltering](T_Tessa_UI_Files_FileGroupingFiltering.htm)|
Фильтрация файлов, привязанная к группе.  
[FileGroupingNames](T_Tessa_UI_Files_FileGroupingNames.htm)|  Имена
стандартных группировок, добавляемых в платформенных расширениях.  
[FileMenuActionNames](T_Tessa_UI_Files_FileMenuActionNames.htm)|  Имена
стандартных действий, которые создаются платформенными расширениями.  
[FileModelPropertyListener](T_Tessa_UI_Files_FileModelPropertyListener.htm)|
Объект файлового API, поддерживающий уведомление об изменении свойств с
заданными именами у модели [IFile](T_Tessa_Files_IFile.htm).  
[FileModifiedSorting](T_Tessa_UI_Files_FileModifiedSorting.htm)|  Сортировка
файлов по дате последнего изменения, т.е. дате создания
[Created](P_Tessa_Files_IFileVersion_Created.htm) для последней версии
[Last](P_Tessa_Files_IFileVersionCollection_Last.htm), которая может быть
выбрана в элементе управления
[IFileControl](T_Tessa_UI_Files_IFileControl.htm).  
[FilePreviewContext](T_Tessa_UI_Files_FilePreviewContext.htm)|  Контекст
операции по отображению файла в области предпросмотра.  
[FilePreviewInfoCache](T_Tessa_UI_Files_FilePreviewInfoCache.htm)|  Кэш,
предоставляющий информацию по предпросмотру файлов. Значения кэша можно
изменять.  
[FilePreviewManager](T_Tessa_UI_Files_FilePreviewManager.htm)|  Объект,
управляющий доступностью предпросмотра.  
[FilePreviewModel](T_Tessa_UI_Files_FilePreviewModel.htm)|  Модель
представления для предварительного просмотра содержимого файла.  
[FileSignatureExportContext](T_Tessa_UI_Files_FileSignatureExportContext.htm)|
Контекст операции по экспорту электронных подписей.  
[FileSignatureExporter](T_Tessa_UI_Files_FileSignatureExporter.htm)|  Объект,
используемый для расширения экспорта электронных подписей.  
[FileSizeSorting](T_Tessa_UI_Files_FileSizeSorting.htm)|  Сортировка файлов по
размеру контента [Size](P_Tessa_Files_IFileContent_Size.htm), которая может
быть выбрана в элементе управления
[IFileControl](T_Tessa_UI_Files_IFileControl.htm).  
[FileSorting](T_Tessa_UI_Files_FileSorting.htm)|  Базовый класс для сортировки
файлов, которая может быть выбрана в элементе управления
[IFileControl](T_Tessa_UI_Files_IFileControl.htm).  
[FileSortingCollection](T_Tessa_UI_Files_FileSortingCollection.htm)|
Коллекция сортировок файлов [IFileSorting](T_Tessa_UI_Files_IFileSorting.htm).  
[FileSortingNames](T_Tessa_UI_Files_FileSortingNames.htm)|  Имена стандартных
сортировок, добавляемых в платформенных расширениях.  
[FileTagViewModel](T_Tessa_UI_Files_FileTagViewModel.htm)|  Тег, который может
быть визуально прикреплён к файлу правее иконки с подписью.  
[FileToolTip](T_Tessa_UI_Files_FileToolTip.htm)|  Всплывающая подсказка для
файла.  
[FileUIContainer](T_Tessa_UI_Files_FileUIContainer.htm)|  Контейнер,
содержащий все доступные файлы и учитывающий взаимодействие с UI.  
[FileUIExtensions](T_Tessa_UI_Files_FileUIExtensions.htm)|  Методы-расширения
для пространства имён Tessa.UI.Files.  
[FileUIManager](T_Tessa_UI_Files_FileUIManager.htm)|  Объект, управляющий
взаимодействием с файлами с учётом использования файлов в UI.  
[FileVersionExtension](T_Tessa_UI_Files_FileVersionExtension.htm)|  Базовый
класс для расширения, связанного с версией файла, которая расположена в
элементе управления файлами. Все методы расширения по умолчанию не выполняются
действий.  
[FileVersionExtensionContext](T_Tessa_UI_Files_FileVersionExtensionContext.htm)|
Контекст расширений, выполняемых для версии файла
[IFileVersion](T_Tessa_Files_IFileVersion.htm) в элементе управления файлами
[IFileControl](T_Tessa_UI_Files_IFileControl.htm).  
[FileViewModel](T_Tessa_UI_Files_FileViewModel.htm)|  Модель представления для
отображения файла с поддержкой сортировки и группировки.  
[FileViewModelAggregateListener](T_Tessa_UI_Files_FileViewModelAggregateListener.htm)|
Объект, агрегирующий взаимодействие с несколькими объектами
[IFileViewModelListener](T_Tessa_UI_Files_IFileViewModelListener.htm).  
[FileViewModelCollection](T_Tessa_UI_Files_FileViewModelCollection.htm)|
Коллекция моделей представления для отображения файлов с поддержкой сортировки
и группировки.  
[FileViewModelEmptyListener](T_Tessa_UI_Files_FileViewModelEmptyListener.htm)|
Объект файлового API, не выполняющий уведомлений об изменении свойств моделей
или моделей представления файлов. Используйте такой объект вместе null.  
[FileViewModelListener](T_Tessa_UI_Files_FileViewModelListener.htm)|  Объект
файлового API, поддерживающий уведомление об изменении свойств моделей или
моделей представления файлов.  
[FileViewModelPropertyListener](T_Tessa_UI_Files_FileViewModelPropertyListener.htm)|
Объект файлового API, поддерживающий уведомление об изменении свойств с
заданными именами у модели представления
[IFileViewModel](T_Tessa_UI_Files_IFileViewModel.htm).  
[NewFileContext](T_Tessa_UI_Files_NewFileContext.htm)|  Контекст определения
информации по добавляемому файлу. Используется в таких событиях, как
добавление файла с результатами сканирования.  
[NewPhysicalFileContext](T_Tessa_UI_Files_NewPhysicalFileContext.htm)|
Контекст определения информации по файлу, добавляемому из папки на диске.  
[PreviewPageCommand](T_Tessa_UI_Files_PreviewPageCommand.htm)|  Команда,
выполняемая в области предпросмотра страниц документа.  
[PreviewPageContext](T_Tessa_UI_Files_PreviewPageContext.htm)|  Контекст
операции, связанной с областью предпросмотра.  
[PreviewPageExtractorContext](T_Tessa_UI_Files_PreviewPageExtractorContext.htm)|
Контекст по извлечению страницы для предпросмотра из многостраничного
документа, такого как PDF/TIFF.  
[PreviewPageOptions](T_Tessa_UI_Files_PreviewPageOptions.htm)|  Настройки
отображения области предпросмотра документа, разделённого на страницы.  
[RegistryFilePreviewInfoCache](T_Tessa_UI_Files_RegistryFilePreviewInfoCache.htm)|
Кэш, предоставляющий информацию по предпросмотру файлов из реестра Windows.
Доступен только для чтения.  
[ViewFileControl](T_Tessa_UI_Files_ViewFileControl.htm)|  Элемент управления,
отображающий файлы для контрола "Представление".  
## __Структуры
[FileGroupInfo](T_Tessa_UI_Files_FileGroupInfo.htm)|  Структура, описывающая
информацию по группе, в которою входит файл с текущим набором свойств.  
---|---  
## __Интерфейсы
[IFileControl](T_Tessa_UI_Files_IFileControl.htm)|  Элемент управления,
отображающий файлы.  
---|---  
[IFileControlExtension](T_Tessa_UI_Files_IFileControlExtension.htm)|
Расширение, связанное с элементом управления файлами.  
[IFileControlExtensionContext](T_Tessa_UI_Files_IFileControlExtensionContext.htm)|
Контекст расширений, выполняемых для элемента управления файлами
[IFileControl](T_Tessa_UI_Files_IFileControl.htm).  
[IFileControlManageable](T_Tessa_UI_Files_IFileControlManageable.htm)|
Объект, жизненным циклом которого управляет элемент управления
[IFileControl](T_Tessa_UI_Files_IFileControl.htm).  
[IFileControlManager](T_Tessa_UI_Files_IFileControlManager.htm)|  Объект,
управляющий контролами [IFileControl](T_Tessa_UI_Files_IFileControl.htm).  
[IFileControlNotificationObserver](T_Tessa_UI_Files_IFileControlNotificationObserver.htm)|
Объект, посредством которого можно отправить уведомления для элементов
управления файлами [IFileControl](T_Tessa_UI_Files_IFileControl.htm) о
событиях, происходящих при изменении файлов в контейнере
[IFileContainer](T_Tessa_Files_IFileContainer.htm).  
[IFileControlNotificationSource](T_Tessa_UI_Files_IFileControlNotificationSource.htm)|
Объект, посредством которого можно подписываться на события, происходящие при
изменении файлов в контейнере
[IFileContainer](T_Tessa_Files_IFileContainer.htm).  
[IFileControlObject](T_Tessa_UI_Files_IFileControlObject.htm)|  Базовый
интерфейс для сортировки
[IFileFiltering](T_Tessa_UI_Files_IFileFiltering.htm), группировки
[IFileGrouping](T_Tessa_UI_Files_IFileGrouping.htm) и фильтрации
[IFileFiltering](T_Tessa_UI_Files_IFileFiltering.htm).  
[IFileControlState](T_Tessa_UI_Files_IFileControlState.htm)|  Состояние
элемента управления [IFileControl](T_Tessa_UI_Files_IFileControl.htm), которое
можно восстановить, в т.ч. на другом таком же элементе управления.  
[IFileExtension](T_Tessa_UI_Files_IFileExtension.htm)|  Расширение, связанное
с файлом, который расположен в элементе управления файлами.  
[IFileExtensionContext](T_Tessa_UI_Files_IFileExtensionContext.htm)|  Контекст
расширений, выполняемых для файла [IFile](T_Tessa_Files_IFile.htm) в элементе
управления файлами [IFileControl](T_Tessa_UI_Files_IFileControl.htm).  
[IFileExtensionContextBase](T_Tessa_UI_Files_IFileExtensionContextBase.htm)|
Базовый интерфейс для контекста расширений, выполняемых для объекта файлового
API, такого как файл, версия файла или элемент управления файлами.  
[IFileFiltering](T_Tessa_UI_Files_IFileFiltering.htm)|  Фильтрация файлов,
используемая в элементе управления
[IFileControl](T_Tessa_UI_Files_IFileControl.htm).  
[IFileGrouping](T_Tessa_UI_Files_IFileGrouping.htm)|  Группировка файлов,
которая может быть выбрана в элементе управления
[IFileControl](T_Tessa_UI_Files_IFileControl.htm).  
[IFileGroupingCollection](T_Tessa_UI_Files_IFileGroupingCollection.htm)|
Коллекция группировок файлов
[IFileGrouping](T_Tessa_UI_Files_IFileGrouping.htm).  
[IFilePagingControlModel](T_Tessa_UI_Files_IFilePagingControlModel.htm)|
Модель представления для постраничного предпросмотра файлов PDF/TIFF.  
[IFilePreviewContext](T_Tessa_UI_Files_IFilePreviewContext.htm)|  Контекст
операции по отображению файла в области предпросмотра.  
[IFilePreviewControl](T_Tessa_UI_Files_IFilePreviewControl.htm)|  Элемент
управления для области предпросмотра.  
[IFilePreviewInfoCache](T_Tessa_UI_Files_IFilePreviewInfoCache.htm)|  Кэш,
предоставляющий информацию по предпросмотру файлов.  
[IFilePreviewInfoCacheProvider](T_Tessa_UI_Files_IFilePreviewInfoCacheProvider.htm)|
Поставщик кэша, предоставляющего информацию по предпросмотру файлов.  
[IFilePreviewManager](T_Tessa_UI_Files_IFilePreviewManager.htm)|  Объект,
управляющий доступностью предпросмотра.  
[IFilePreviewModel](T_Tessa_UI_Files_IFilePreviewModel.htm)|  Модель
представления для предварительного просмотра содержимого файла.  
[IFileSignatureExportContext](T_Tessa_UI_Files_IFileSignatureExportContext.htm)|
Контекст операции по экспорту электронных подписей.  
[IFileSignatureExporter](T_Tessa_UI_Files_IFileSignatureExporter.htm)|
Объект, используемый для расширения экспорта электронных подписей.  
[IFileSorting](T_Tessa_UI_Files_IFileSorting.htm)|  Сортировка файлов, которая
может быть выбрана в элементе управления
[IFileControl](T_Tessa_UI_Files_IFileControl.htm).  
[IFileSortingCollection](T_Tessa_UI_Files_IFileSortingCollection.htm)|
Коллекция сортировок файлов [IFileSorting](T_Tessa_UI_Files_IFileSorting.htm).  
[IFileTagViewModel](T_Tessa_UI_Files_IFileTagViewModel.htm)|  Тег, который
может быть визуально прикреплён к файлу правее иконки с подписью.  
[IFileToolTip](T_Tessa_UI_Files_IFileToolTip.htm)|  Всплывающая подсказка для
файла.  
[IFileUIContainer](T_Tessa_UI_Files_IFileUIContainer.htm)|  Контейнер,
содержащий все доступные файлы и учитывающий взаимодействие с UI.  
[IFileVersionExtension](T_Tessa_UI_Files_IFileVersionExtension.htm)|
Расширение, связанное с версией файла, которая расположена в элементе
управления файлами.  
[IFileVersionExtensionContext](T_Tessa_UI_Files_IFileVersionExtensionContext.htm)|
Контекст расширений, выполняемых для версии файла
[IFileVersion](T_Tessa_Files_IFileVersion.htm) в элементе управления файлами
[IFileControl](T_Tessa_UI_Files_IFileControl.htm).  
[IFileViewModel](T_Tessa_UI_Files_IFileViewModel.htm)|  Модель представления
для отображения файла с поддержкой сортировки и группировки.  
[IFileViewModelCollection](T_Tessa_UI_Files_IFileViewModelCollection.htm)|
Коллекция моделей представления для отображения файлов с поддержкой сортировки
и группировки.  
[IFileViewModelListener](T_Tessa_UI_Files_IFileViewModelListener.htm)|  Объект
файлового API, поддерживающий уведомление об изменении свойств моделей или
моделей представления файлов.  
[IHtmlSanitizerProvider](T_Tessa_UI_Files_IHtmlSanitizerProvider.htm)|
Предоставляет доступ к объекту, выполняющему санитайзинг HTML-документов.  
[INewFileContext](T_Tessa_UI_Files_INewFileContext.htm)|  Контекст определения
информации по добавляемому файлу. Используется в таких событиях, как
добавление файла с результатами сканирования.  
[INewPhysicalFileContext](T_Tessa_UI_Files_INewPhysicalFileContext.htm)|
Контекст определения информации по файлу, добавляемому из папки на диске.  
[IPreviewPageCommand](T_Tessa_UI_Files_IPreviewPageCommand.htm)|  Команда,
выполняемая в области предпросмотра страниц документа.  
[IPreviewPageContext](T_Tessa_UI_Files_IPreviewPageContext.htm)|  Контекст
операции, связанной с областью предпросмотра.  
[IPreviewPageExtractor](T_Tessa_UI_Files_IPreviewPageExtractor.htm)|  Объект,
выполняющий извлечение страницы для предпросмотра из многостраничного
документа, такого как PDF/TIFF.  
[IPreviewPageExtractorContext](T_Tessa_UI_Files_IPreviewPageExtractorContext.htm)|
Контекст по извлечению страницы для предпросмотра из многостраничного
документа, такого как PDF/TIFF.  
[IPreviewPageExtractorProvider](T_Tessa_UI_Files_IPreviewPageExtractorProvider.htm)|
Предоставляет доступ к объекту, выполняющему извлечение страницы для
предпросмотра из многостраничного документа, такого как PDF/TIFF.  
[IPreviewPageOptions](T_Tessa_UI_Files_IPreviewPageOptions.htm)|  Настройки
отображения области предпросмотра документа, разделённого на страницы.  
## __Делегаты
[CreateFileUIContainerFuncAsync](T_Tessa_UI_Files_CreateFileUIContainerFuncAsync.htm)|
Создаёт контейнер файлов для заданного источника файлов, обеспечивающего
взаимодействие созданных с его помощью файлов с внешней подсистемой и
учитывающий взаимодействие с UI.  
---|---  
[FileCaptionFunc](T_Tessa_UI_Files_FileCaptionFunc.htm)|  Функция,
возвращающая значение свойства
[Caption](P_Tessa_UI_Files_IFileViewModel_Caption.htm) для заданной модели
представления файла.  
[FileGetGroupInfoFunc](T_Tessa_UI_Files_FileGetGroupInfoFunc.htm)|  Возвращает
структуру, которая описывает информацию по группе для заданной модели
представления файла, по которой выполняется группировка grouping. Структура
определяется идентификатор группы, отображаемое название и строку для
сортировки.  
[FileIsVisibleFunc](T_Tessa_UI_Files_FileIsVisibleFunc.htm)|  Функция,
определяющая видимость заданной модели представления в рамках фильтрации.
Функция должна вернуть true, если модель представления должна быть видимой, и
false в противном случае.  
[FilePropertyAction](T_Tessa_UI_Files_FilePropertyAction.htm)|  Метод,
устанавливающий произвольные свойства модели представления файла в зависимости
от свойств модели файла. Не используйте для свойств
[Caption](P_Tessa_UI_Files_IFileViewModel_Caption.htm) и
[ToolTip](P_Tessa_UI_Files_IFileViewModel_ToolTip.htm).  
[FileToolTipAction](T_Tessa_UI_Files_FileToolTipAction.htm)|  Метод,
устанавливающий свойства всплывающей подсказки
[ToolTip](P_Tessa_UI_Files_IFileViewModel_ToolTip.htm) для заданной модели
представления файла.  
## __Перечисления
[FilePagingControlFlags](T_Tessa_UI_Files_FilePagingControlFlags.htm)|  Флаги,
определяющие функции, поддерживаемые объектом
[IFilePagingControlModel](T_Tessa_UI_Files_IFilePagingControlModel.htm).  
---|---  
[PreviewPageQuality](T_Tessa_UI_Files_PreviewPageQuality.htm)|  Качество
страницы для рендеринга в предпросмотре. Используется в PDF, но не в TIFF.
