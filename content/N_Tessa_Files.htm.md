# Tessa.Files - пространство имён
API файлов, используемых совместно или раздельно с карточками.
##  __Классы
[EmptyFileSource](T_Tessa_Files_EmptyFileSource.htm)|  Источник файлов, не
обеспечивающий взаимодействие файла с внешней подсистемой. Позволяет
использовать виртуальные файлы, управляемые только из расширений.  
---|---  
[File](T_Tessa_Files_File.htm)|  Файл.  
[FileBuilder](T_Tessa_Files_FileBuilder.htm)|  Выполняет поэтапное создание
файла с возможностью последующего добавления в коллекцию файлов.  
[FileCache](T_Tessa_Files_FileCache.htm)|  Кэш для контента файлов.  
[FileCancellationSource](T_Tessa_Files_FileCancellationSource.htm)|  Объект,
управляющий отменой асинхронных операций с файлами.  
[FileCategory](T_Tessa_Files_FileCategory.htm)|  Категория файла.  
[FileCollection](T_Tessa_Files_FileCollection.htm)|  Коллекция файлов.
Обеспечивает доступ по идентификаторам [ID](P_Tessa_Files_IFileEntity_ID.htm).  
[FileContainer](T_Tessa_Files_FileContainer.htm)|  Контейнер, содержащий все
доступные файлы.  
[FileContainerPermissions](T_Tessa_Files_FileContainerPermissions.htm)|
Разрешения, определяющие возможности, доступные пользователю при работе с
контейнером файлов.  
[FileContent](T_Tessa_Files_FileContent.htm)|  Базовый класс для контента
файла.  
[FileContentNameReplacer](T_Tessa_Files_FileContentNameReplacer.htm)|  Объект,
выполняющий исправление имени файла, создаваемого в кэше.  
[FileContentOptions](T_Tessa_Files_FileContentOptions.htm)|  Настройки,
связанные с хранением контента файлов.  
[FileContentRequest](T_Tessa_Files_FileContentRequest.htm)|  Запрос на
загрузку содержимого файла.  
[FileContentResponse](T_Tessa_Files_FileContentResponse.htm)|  Ответ на запрос
на получение контента файла.  
[FileContentSources](T_Tessa_Files_FileContentSources.htm)|  Источники
контента файла, доступные в системе.  
[FileCreationToken](T_Tessa_Files_FileCreationToken.htm)|  Токен, используемый
для создания файлов посредством источника файлов
[IFileSource](T_Tessa_Files_IFileSource.htm).  
[FileEntity](T_Tessa_Files_FileEntity.htm)|  Базовый класс для всех объектов в
API файлов, которые идентифицируются по идентификатору
[Guid](https://learn.microsoft.com/dotnet/api/system.guid) и связаны с
источником [IFileSource](T_Tessa_Files_IFileSource.htm).  
[FileEntityCollection<TItem,
TCollection>](T_Tessa_Files_FileEntityCollection_2.htm)|  Коллекция объектов,
реализующих интерфейс [IFileEntity](T_Tessa_Files_IFileEntity.htm), для
которой доступны уведомление об изменениях и клонирование, а также
идентификация по неуникальному ключу [ID](P_Tessa_Files_IFileEntity_ID.htm).  
[FileErrorInfo](T_Tessa_Files_FileErrorInfo.htm)|  Информация по ошибке,
которая возникла при сохранении файла.  
[FileExtensions](T_Tessa_Files_FileExtensions.htm)|  Методы-расширения для
пространства имён Tessa.Files.  
[FileLink](T_Tessa_Files_FileLink.htm)|  Ссылка на файл.  
[FileLocalCache](T_Tessa_Files_FileLocalCache.htm)|  Кэш для контента файлов,
расположенного локально для текущего пользователя.  
[FileManager](T_Tessa_Files_FileManager.htm)|  Объект, управляющий
взаимодействием с файлами.  
[FileObject](T_Tessa_Files_FileObject.htm)|  Базовый объект для файлов и
версий файлов.  
[FilePermissions](T_Tessa_Files_FilePermissions.htm)|  Разрешения,
определяющие возможности, доступные пользователю при работе с файлом.  
[FileRequest](T_Tessa_Files_FileRequest.htm)|  Запрос на получение коллекции
доступных файлов.  
[FileResolverContext](T_Tessa_Files_FileResolverContext.htm)|  Контекст по
определению объектов, которые могут быть заменены в пределах некоторой
области.  
[FileResponse](T_Tessa_Files_FileResponse.htm)|  Ответ на запрос на получение
коллекции доступных файлов.  
[FileSignature](T_Tessa_Files_FileSignature.htm)|  Информация о подписи для
версии файла.  
[FileSignatureAddedCollection](T_Tessa_Files_FileSignatureAddedCollection.htm)|
Коллекция подписей для версии файла, которые были добавлены и ещё не были
сохранены.  
[FileSignatureCollection](T_Tessa_Files_FileSignatureCollection.htm)|
Коллекция подписей для версии файла.  
[FileSignatureCollectionBase<TCollection>](T_Tessa_Files_FileSignatureCollectionBase_1.htm)|
Базовый класс для коллекции подписей для версии файла.  
[FileSignatureCreationToken](T_Tessa_Files_FileSignatureCreationToken.htm)|
Токен, используемый для создания посредством источника файлов
[IFileSource](T_Tessa_Files_IFileSource.htm) объектов с информацией о подписи
для версий файлов.  
[FileSignatureData](T_Tessa_Files_FileSignatureData.htm)|  Объект, содержащий
информацию по бинарным данным файла подписи.  
[FileSignatureResponse](T_Tessa_Files_FileSignatureResponse.htm)|  Ответ на
запрос на получение коллекции доступных версий файла.  
[FileSource](T_Tessa_Files_FileSource.htm)|  Базовый класс для источника
файлов, обеспечивающего взаимодействие файлов с внешней подсистемой.  
[FileState](T_Tessa_Files_FileState.htm)|  Состояние файла на определённый
момент времени.  
[FileTag](T_Tessa_Files_FileTag.htm)|  Тег, связанный с версией файла.
Например, признак того, что размер содержимого файла трактуется как большой
файл, поэтому файл не копируется во временную папку.  
[FileTagCollection](T_Tessa_Files_FileTagCollection.htm)|  Коллекция тегов
[IFileTag](T_Tessa_Files_IFileTag.htm).  
[FileType](T_Tessa_Files_FileType.htm)|  Тип файла.  
[FileVersion](T_Tessa_Files_FileVersion.htm)|  Версия файла.  
[FileVersionCollection](T_Tessa_Files_FileVersionCollection.htm)|  Коллекция
версий файла.  
[FileVersionCreationToken](T_Tessa_Files_FileVersionCreationToken.htm)|
Токен, используемый для создания версий файлов посредством источника файлов
[IFileSource](T_Tessa_Files_IFileSource.htm).  
[FileVersionLink](T_Tessa_Files_FileVersionLink.htm)|  Ссылка на версию файла.  
[FileVersionResponse](T_Tessa_Files_FileVersionResponse.htm)|  Ответ на запрос
на получение коллекции доступных версий файла.  
[LocalFileContent](T_Tessa_Files_LocalFileContent.htm)|  Контент файла,
доступный локально во временной папке пользователя.  
[RemoteFileContent](T_Tessa_Files_RemoteFileContent.htm)|  Контент файла,
доступный удалённо с использованием заданных функций.  
[VirtualFile](T_Tessa_Files_VirtualFile.htm)|  Виртуальный файл, указываемый
при добавлении.  
[VirtualFileVersion](T_Tessa_Files_VirtualFileVersion.htm)|  Версия
виртуального файла, указываемая при добавлении.  
## __Структуры
[FileContentSource](T_Tessa_Files_FileContentSource.htm)|  Местоположение
контента файла.  
---|---  
## __Интерфейсы
[IFile](T_Tessa_Files_IFile.htm)|  Файл.  
---|---  
[IFileBuilder](T_Tessa_Files_IFileBuilder.htm)|  Выполняет поэтапное создание
файла с возможностью последующего добавления в коллекцию файлов.  
[IFileCache](T_Tessa_Files_IFileCache.htm)|  Кэш для контента файлов.  
[IFileCancellationSource](T_Tessa_Files_IFileCancellationSource.htm)|  Объект,
управляющий отменой асинхронных операций с файлами.  
[IFileCategory](T_Tessa_Files_IFileCategory.htm)|  Категория файла.  
[IFileCollection](T_Tessa_Files_IFileCollection.htm)|  Коллекция файлов.
Обеспечивает доступ по идентификаторам [ID](P_Tessa_Files_IFileEntity_ID.htm).  
[IFileContainer](T_Tessa_Files_IFileContainer.htm)|  Контейнер, содержащий все
доступные файлы.  
[IFileContainerPermissions](T_Tessa_Files_IFileContainerPermissions.htm)|
Разрешения, определяющие возможности, доступные пользователю при работе с
контейнером файлов.  
[IFileContent](T_Tessa_Files_IFileContent.htm)|  Контент файла.  
[IFileContentNameReplacer](T_Tessa_Files_IFileContentNameReplacer.htm)|
Объект, выполняющий исправление имени файла, создаваемого в кэше. Например,
имя файла может сокращаться, из него могут исключаться некорректные символы.  
[IFileContentOptions](T_Tessa_Files_IFileContentOptions.htm)|  Настройки,
связанные с хранением контента файлов.  
[IFileContentRequest](T_Tessa_Files_IFileContentRequest.htm)|  Запрос на
загрузку содержимого файла.  
[IFileContentResponse](T_Tessa_Files_IFileContentResponse.htm)|  Ответ на
запрос на получение контента файла.  
[IFileCreationToken](T_Tessa_Files_IFileCreationToken.htm)|  Токен,
используемый для создания файлов посредством источника файлов
[IFileSource](T_Tessa_Files_IFileSource.htm).  
[IFileEntity](T_Tessa_Files_IFileEntity.htm)|  Базовый интерфейс для всех
объектов в API файлов, которые идентифицируются по идентификатору
[Guid](https://learn.microsoft.com/dotnet/api/system.guid) и связаны с
источником [IFileSource](T_Tessa_Files_IFileSource.htm).  
[IFileEntityCollection<TItem,
TCollection>](T_Tessa_Files_IFileEntityCollection_2.htm)|  Коллекция объектов,
реализующих интерфейс [IFileEntity](T_Tessa_Files_IFileEntity.htm), для
которой доступны уведомление об изменениях и клонирование, а также
идентификация по неуникальному ключу [ID](P_Tessa_Files_IFileEntity_ID.htm).  
[IFileErrorInfo](T_Tessa_Files_IFileErrorInfo.htm)|  Информация по ошибке,
которая возникла при сохранении файла.  
[IFileLink](T_Tessa_Files_IFileLink.htm)|  Ссылка на файл.  
[IFileManager](T_Tessa_Files_IFileManager.htm)|  Объект, управляющий
взаимодействием с файлами.  
[IFileObject](T_Tessa_Files_IFileObject.htm)|  Базовый интерфейс для файлов и
версий файлов.  
[IFilePermissions](T_Tessa_Files_IFilePermissions.htm)|  Разрешения,
определяющие возможности, доступные пользователю при работе с файлом.  
[IFileRequest](T_Tessa_Files_IFileRequest.htm)|  Запрос на получение коллекции
доступных файлов.  
[IFileResolverContext](T_Tessa_Files_IFileResolverContext.htm)|  Контекст по
определению объектов, которые могут быть заменены в пределах некоторой
области.  
[IFileResponse](T_Tessa_Files_IFileResponse.htm)|  Ответ на запрос на
получение коллекции доступных файлов.  
[IFileSignature](T_Tessa_Files_IFileSignature.htm)|  Информация о подписи для
версии файла.  
[IFileSignatureAddedCollection](T_Tessa_Files_IFileSignatureAddedCollection.htm)|
Коллекция подписей для версии файла, которые были добавлены и ещё не были
сохранены.  
[IFileSignatureCollection](T_Tessa_Files_IFileSignatureCollection.htm)|
Коллекция подписей для версии файла.  
[IFileSignatureCollectionBase<TCollection>](T_Tessa_Files_IFileSignatureCollectionBase_1.htm)|
Базовый интерфейс для коллекции подписей для версии файла.  
[IFileSignatureCreationToken](T_Tessa_Files_IFileSignatureCreationToken.htm)|
Токен, используемый для создания посредством источника файлов
[IFileSource](T_Tessa_Files_IFileSource.htm) объектов с информацией о подписи
для версий файлов.  
[IFileSignatureData](T_Tessa_Files_IFileSignatureData.htm)|  Объект,
содержащий информацию по бинарным данным файла подписи.  
[IFileSignatureResponse](T_Tessa_Files_IFileSignatureResponse.htm)|  Ответ на
запрос на получение коллекции доступных подписей для версии файла.  
[IFileSource](T_Tessa_Files_IFileSource.htm)|  Источник файлов, обеспечивающий
взаимодействие файлов с внешней подсистемой.  
[IFileState](T_Tessa_Files_IFileState.htm)|  Состояние файла на определённый
момент времени.  
[IFileTag](T_Tessa_Files_IFileTag.htm)|  Тег, связанный с версией файла.
Например, признак того, что размер содержимого файла трактуется как большой
файл, поэтому файл не копируется во временную папку.  
[IFileTagCollection](T_Tessa_Files_IFileTagCollection.htm)|  Коллекция тегов
[IFileTag](T_Tessa_Files_IFileTag.htm).  
[IFileType](T_Tessa_Files_IFileType.htm)|  Тип файла.  
[IFileVersion](T_Tessa_Files_IFileVersion.htm)|  Версия файла.  
[IFileVersionCollection](T_Tessa_Files_IFileVersionCollection.htm)|  Коллекция
версий файла.  
[IFileVersionCreationToken](T_Tessa_Files_IFileVersionCreationToken.htm)|
Токен, используемый для создания версий файлов посредством источника файлов
[IFileSource](T_Tessa_Files_IFileSource.htm).  
[IFileVersionLink](T_Tessa_Files_IFileVersionLink.htm)|  Ссылка на версию
файла.  
[IFileVersionResponse](T_Tessa_Files_IFileVersionResponse.htm)|  Ответ на
запрос на получение коллекции доступных версий файла.  
## __Делегаты
[CreateFileContainerFuncAsync](T_Tessa_Files_CreateFileContainerFuncAsync.htm)|
Создаёт контейнер файлов для заданного источника файлов, обеспечивающего
взаимодействие созданных с его помощью файлов с внешней подсистемой.  
---|---  
[FileModifyTokenActionAsync](T_Tessa_Files_FileModifyTokenActionAsync.htm)|
Метод, выполняющий изменение файла и его версии перед созданием.  
[RegisterFileDelayedDisposalAction](T_Tessa_Files_RegisterFileDelayedDisposalAction.htm)|
Функция регистрации отложенного удаления содержимого (удаления временного
файла), которое невозможно выполнить сразу же.  
## __Перечисления
[FileBuilder.ContentCreationType](T_Tessa_Files_FileBuilder_ContentCreationType.htm)|
Способ создания контента.  
---|---  
[FileCacheOptions](T_Tessa_Files_FileCacheOptions.htm)|  Опции, которые
дополнительно поддерживает кэш файлов.  
[FileContentDownloadState](T_Tessa_Files_FileContentDownloadState.htm)|
Состояние загрузки в кэш для контента версии файла для последующего
отображения пользователю.  
[FileNotificationType](T_Tessa_Files_FileNotificationType.htm)|  Тип
уведомления, которое отправляется для файла [IFile](T_Tessa_Files_IFile.htm)
посредством [IFileSource](T_Tessa_Files_IFileSource.htm) во внешнюю
подсистему.  
[FileOpeningMode](T_Tessa_Files_FileOpeningMode.htm)|  Способ открытия
контента файла или версии файла.  
[FileSignatureDataState](T_Tessa_Files_FileSignatureDataState.htm)|  Состояние
бинарных данных файла подписи.  
[FileSignatureEventType](T_Tessa_Files_FileSignatureEventType.htm)|  Тип
действия, в результате которого подпись была создана.  
[FileSignatureLoadingMode](T_Tessa_Files_FileSignatureLoadingMode.htm)|
Способ загрузки подписей.  
[FileSignatureNotificationType](T_Tessa_Files_FileSignatureNotificationType.htm)|
Тип уведомления, которое отправляется для подписи файла
[IFileSignature](T_Tessa_Files_IFileSignature.htm) посредством
[IFileSource](T_Tessa_Files_IFileSource.htm) во внешнюю подсистему.  
[FileSignatureState](T_Tessa_Files_FileSignatureState.htm)|  Состояние подписи
для версии файла.  
[FileVersionState](T_Tessa_Files_FileVersionState.htm)|  Состояние версии
файла.
