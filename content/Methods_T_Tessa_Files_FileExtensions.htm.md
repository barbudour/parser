# FileExtensions - методы
##  __Методы
[AddRangeIfNotExists](M_Tessa_Files_FileExtensions_AddRangeIfNotExists.htm)|
Добавляет указанные теги в коллекцию, если они не были добавлены ранее.  
---|---  
[AddVirtualAsync(IFileContainer, VirtualFile, CancellationToken,
VirtualFileVersion[])](M_Tessa_Files_FileExtensions_AddVirtualAsync_1.htm)|
Создаёт и добавляет виртуальный файл, возвращает созданный файл. Этот метод
добавляет файл в источник по умолчанию
[Source](P_Tessa_Files_IFileContainer_Source.htm) для контейнера container.  
[AddVirtualAsync(IFileContainer, IFileSource, VirtualFile, CancellationToken,
VirtualFileVersion[])](M_Tessa_Files_FileExtensions_AddVirtualAsync.htm)|
Создаёт и добавляет виртуальный файл, возвращает созданный файл. Этот метод
добавляет файл в указанный источник fileSource, что позволяет, например,
добавить файл в структуру карточки [CardFile](T_Tessa_Cards_CardFile.htm), с
которой не связан контейнер файлов container.  
[AddWithNotificationAsync(ICollection<IFileSignature>,
IEnumerable<IFileSignature>,
CancellationToken)](M_Tessa_Files_FileExtensions_AddWithNotificationAsync_2.htm)|
Добавляет несколько подписей файла с уведомлением их источников Source. При
этом автоматически устанавливается свойство
[Added](P_Tessa_Files_IFileSignatureCollection_Added.htm), если тип коллекции
signatures задан соответствующий. Этот метод следует использовать для
стандартного добавления новых подписей.  
[AddWithNotificationAsync(ICollection<IFileSignature>, IFileSignature,
CancellationToken)](M_Tessa_Files_FileExtensions_AddWithNotificationAsync_3.htm)|
Добавляет подпись файла с уведомлением её источника Source. При этом
автоматически устанавливается свойство
[Added](P_Tessa_Files_IFileSignatureCollection_Added.htm), если тип коллекции
signatures задан соответствующий. Этот метод следует использовать для
стандартного добавления новой подписи.  
[AddWithNotificationAsync(ICollection<IFile>, IEnumerable<IFile>, Boolean,
CancellationToken)](M_Tessa_Files_FileExtensions_AddWithNotificationAsync.htm)|
Добавляет несколько файлов с уведомлением их источников Source. Этот метод
следует использовать для стандартного добавления новых файлов.  
[AddWithNotificationAsync(ICollection<IFile>, IFile, Boolean,
CancellationToken)](M_Tessa_Files_FileExtensions_AddWithNotificationAsync_1.htm)|
Добавляет файл с уведомлением его источника Source. Этот метод следует
использовать для стандартного добавления нового файла.  
[AllocateAdditionalLocalContentAsync](M_Tessa_Files_FileExtensions_AllocateAdditionalLocalContentAsync.htm)|
Создаёт дополнительный объект локального содержимого (на диске) для файла или
версии файла. Загрузка такого содержимого отменяется вместе с основным
содержимым.  
[BuildFile](M_Tessa_Files_FileExtensions_BuildFile.htm)|  Возвращает объект,
выполняющий поэтапное создание файла с возможностью последующего добавления в
коллекцию файлов заданного контейнера. По умолчанию файл создаётся с
использованием источника [Source](P_Tessa_Files_IFileContainer_Source.htm),
заданного в контейнере. На возвращаемом объекте
[IFileBuilder](T_Tessa_Files_IFileBuilder.htm) необходимо вызвать один из
методов установки контента SetContent.  
[CancelDownloadingContent](M_Tessa_Files_FileExtensions_CancelDownloadingContent.htm)|
Отменяет асинхронную загрузку содержимого файла или версии. При отмене
загрузки файла также отменяется загрузка всех его версий.  
[ChangeCategoryAsync(IFile, String,
CancellationToken)](M_Tessa_Files_FileExtensions_ChangeCategoryAsync_1.htm)|
Изменяет категорию файла без указания идентификатора категории.  
[ChangeCategoryAsync(IFile, IFileCategory,
CancellationToken)](M_Tessa_Files_FileExtensions_ChangeCategoryAsync_2.htm)|
Изменяет категорию файла и уведомляет об этом его источник, если категория в
действительности изменилась.  
[ChangeCategoryAsync(IFile, String, Guid,
CancellationToken)](M_Tessa_Files_FileExtensions_ChangeCategoryAsync.htm)|
Изменяет категорию файла с указанием идентификатора категории.  
[CopyAsync](M_Tessa_Files_FileExtensions_CopyAsync.htm)|  Создаёт копию
заданного файла. Если контент копируемого файла не загружен, то он загружается
перед созданием копии. Первым значением возвращается копия заданного файла или
null, если копию создать не удалось. В этом случае возвращённый результат
валидации не будет успешным.  
[CreateFileAsync(IFileSource, Stream, String, IFileType, IFileCategory, IUser,
Func<IFileCreationToken, CancellationToken, ValueTask>,
Func<IFileVersionCreationToken, CancellationToken, ValueTask>,
CancellationToken)](M_Tessa_Files_FileExtensions_CreateFileAsync.htm)|
Создаёт файл с указанными параметрами и единственной версией. Возвращает
созданный файл или null, если создать файл не удалось.  
[CreateFileAsync(IFileSource, String, IFileType, IFileCategory,
Func<CancellationToken, ValueTask<IFileContent>>, IUser,
Func<IFileCreationToken, CancellationToken, ValueTask>,
Func<IFileVersionCreationToken, CancellationToken, ValueTask>,
CancellationToken)](M_Tessa_Files_FileExtensions_CreateFileAsync_1.htm)|
Создаёт файл с указанными параметрами и единственной версией. Это
вспомогательный метод, который нельзя переопределить. Возвращает созданный
файл или null, если создать файл не удалось.  
[CreateFileAsync(IFileSource, String, IFileType, IFileCategory,
Func<IFileContent, CancellationToken, ValueTask>, IUser,
Func<IFileCreationToken, CancellationToken, ValueTask>,
Func<IFileVersionCreationToken, CancellationToken, ValueTask>,
CancellationToken)](M_Tessa_Files_FileExtensions_CreateFileAsync_2.htm)|
Создаёт файл с указанными параметрами и единственной версией. Это
вспомогательный метод, который нельзя переопределить. Возвращает созданный
файл или null, если создать файл не удалось.  
[CreateFileAsync(IFileSource, String, IFileType, IFileCategory, String, IUser,
Func<IFileCreationToken, CancellationToken, ValueTask>,
Func<IFileVersionCreationToken, CancellationToken, ValueTask>,
CancellationToken)](M_Tessa_Files_FileExtensions_CreateFileAsync_3.htm)|
Создаёт файл с указанными параметрами и единственной версией. Возвращает
созданный файл или null, если создать файл не удалось.  
[EnsureAllContentModifiedAsync](M_Tessa_Files_FileExtensions_EnsureAllContentModifiedAsync.htm)|
Проверяет, что источник файла был уведомлён об изменениях, сделанных для
контента файла [Content](P_Tessa_Files_IFileObject_Content.htm) для каждого из
файлов в текущей коллекции.  
[EnsureContentDownloadedAsync](M_Tessa_Files_FileExtensions_EnsureContentDownloadedAsync.htm)|
Загружает контент файла или версии файла, если он ещё не был загружен. На
загруженном контенте вызывается метод [IFileContent.EnsureLocalUpdatedAsync].  
[EnsureContentDownloadedInUIAsync](M_Tessa_Files_FileExtensions_EnsureContentDownloadedInUIAsync.htm)|
Загружает контент файла или версии файла, если он ещё не был загружен. На
загруженном контенте вызывается метод [IFileContent.EnsureLocalUpdatedAsync].
Изменение состояния контента выполняется в основном потоке UI, если выполнение
производится на клиенте, и в текущем потоке, если выполнение производится
посредством серверного API.  
[EnsureContentModifiedAsync](M_Tessa_Files_FileExtensions_EnsureContentModifiedAsync.htm)|
Проверяет, что источник файла был уведомлён об изменениях, сделанных для
контента файла [IFileObject.Content].  
[EnsureSignaturesLoadedAsync](M_Tessa_Files_FileExtensions_EnsureSignaturesLoadedAsync.htm)|
Загружает подписи для версии файла, если они ещё не были загружены.  
[EnsureVersionsLoadedAsync](M_Tessa_Files_FileExtensions_EnsureVersionsLoadedAsync.htm)|
Загружает версии файла, если они ещё не были загружены.  
[GetActionName](M_Tessa_Files_FileExtensions_GetActionName.htm)|  Возвращает
имя действия, в рамках которого был создан файл или версия файла, или null,
если файл не был создан специальным способом.  
[GetLinkAsync(IFile,
CancellationToken)](M_Tessa_Files_FileExtensions_GetLinkAsync.htm)| Возвращает
ссылку на файл.  
[GetLinkAsync(IFileVersion,
CancellationToken)](M_Tessa_Files_FileExtensions_GetLinkAsync_1.htm)|
Возвращает ссылку на версию файла.  
[GetNullableBytesAsync](M_Tessa_Files_FileExtensions_GetNullableBytesAsync.htm)|
Возвращает бинарные данные подписи файла в виде массива байт или null, если
бинарные данные отсутствуют или ещё не загружены.  
[GetRootedOrigin](M_Tessa_Files_FileExtensions_GetRootedOrigin.htm)|
Возвращает корневой элемент в дереве файлов, связанных посредством свойства
[Origin](P_Tessa_Files_IFile_Origin.htm), или null, если значение свойства
[Origin](P_Tessa_Files_IFile_Origin.htm) для файла file равно null.  
[Has](M_Tessa_Files_FileExtensions_Has.htm)| Возвращает признак того, что
заданный флаг установлен.  
[HasAny](M_Tessa_Files_FileExtensions_HasAny.htm)| Возвращает признак того,
что один из заданных флагов установлен.  
[HasNot](M_Tessa_Files_FileExtensions_HasNot.htm)| Возвращает признак того,
что заданный флаг не установлен.  
[IsLarge(IFile)](M_Tessa_Files_FileExtensions_IsLarge.htm)|  Возвращает
признак того, что содержимое версии файла считается большим файлом, поэтому
будет обрабатываться особым образом. Проверка выполняется по наличию тега
[Large](F_Tessa_Files_FileTag_Large.htm).  
[IsLarge(IFileVersion)](M_Tessa_Files_FileExtensions_IsLarge_1.htm)|
Возвращает признак того, что содержимое версии файла считается большим файлом,
поэтому будет обрабатываться особым образом. Проверка выполняется по наличию
тега [Large](F_Tessa_Files_FileTag_Large.htm).  
[IsValidForContentOperations](M_Tessa_Files_FileExtensions_IsValidForContentOperations.htm)|
Возвращает признак того, что заданный объект (файл или версия файла) может
участвовать в операциях, связанных с контентом. Обычно это означает, что при
загрузке контента не возникло ошибок и контент полностью загружен на сервер
(не находится в процессе загрузки). При этом на клиент контент мог ещё не быть
загружен, т.е. потребуется вызвать [EnsureContentDownloadedAsync(IFileObject,
Func<IFileObject, FileContentDownloadState>, Func<FileContentDownloadState,
CancellationToken, ValueTask>, Func<IFileObject, CancellationToken,
ValueTask<IFileContent>>,
CancellationToken)](M_Tessa_Files_FileExtensions_EnsureContentDownloadedAsync.htm).  
[NotifyAsync(IFile, FileNotificationType,
CancellationToken)](M_Tessa_Files_FileExtensions_NotifyAsync.htm)|  Уведомляет
источник заданного файла [IFileSource](T_Tessa_Files_IFileSource.htm) о
возникшем событии
[FileNotificationType](T_Tessa_Files_FileNotificationType.htm). Используйте
при изменении свойств файла вручную, чтобы эти свойства были сохранены в
пакете карточки (если файл связан с карточкой).  
[NotifyAsync(IFileSignature, FileSignatureNotificationType,
CancellationToken)](M_Tessa_Files_FileExtensions_NotifyAsync_1.htm)|
Уведомляет источник заданной подписи
[IFileSource](T_Tessa_Files_IFileSource.htm) о возникшем событии
[FileSignatureNotificationType](T_Tessa_Files_FileSignatureNotificationType.htm).
Используйте при изменении свойств подписи вручную, чтобы эти свойства были
сохранены в пакете карточки (если подпись связана с карточкой).  
[OpenAsync](M_Tessa_Files_FileExtensions_OpenAsync.htm)| Открывает контент
заданного файла или версии файла для чтения или для редактирования.  
[OpenInFolderAsync](M_Tessa_Files_FileExtensions_OpenInFolderAsync.htm)|
Открывает контент заданного файла или версии файла для чтения или для
редактирования в окне проводника.  
[ReadAllBytesAsync](M_Tessa_Files_FileExtensions_ReadAllBytesAsync.htm)|
Возвращает контент файла или версии файла в виде массива байт. Контент должен
быть уже загружен методом [EnsureContentDownloadedAsync(IFileObject,
Func<IFileObject, FileContentDownloadState>, Func<FileContentDownloadState,
CancellationToken, ValueTask>, Func<IFileObject, CancellationToken,
ValueTask<IFileContent>>,
CancellationToken)](M_Tessa_Files_FileExtensions_EnsureContentDownloadedAsync.htm)
или [EnsureContentDownloadedInUIAsync(IFileObject, Func<IFileObject,
CancellationToken, ValueTask<IFileContent>>,
CancellationToken)](M_Tessa_Files_FileExtensions_EnsureContentDownloadedInUIAsync.htm).
Этот метод оптимизирован по потреблению памяти, поэтому для получения данных
рекомендуется использовать именно его.  
[ReadAllTextAsync](M_Tessa_Files_FileExtensions_ReadAllTextAsync.htm)|
Возвращает контент текстового файла или версии файла в виде строки. Контент
должен быть уже загружен методом [EnsureContentDownloadedAsync(IFileObject,
Func<IFileObject, FileContentDownloadState>, Func<FileContentDownloadState,
CancellationToken, ValueTask>, Func<IFileObject, CancellationToken,
ValueTask<IFileContent>>,
CancellationToken)](M_Tessa_Files_FileExtensions_EnsureContentDownloadedAsync.htm)
или [EnsureContentDownloadedInUIAsync(IFileObject, Func<IFileObject,
CancellationToken, ValueTask<IFileContent>>,
CancellationToken)](M_Tessa_Files_FileExtensions_EnsureContentDownloadedInUIAsync.htm).
Этот метод оптимизирован по потреблению памяти, поэтому для получения данных
рекомендуется использовать именно его.  
[RegisterFilesOnServer](M_Tessa_Files_FileExtensions_RegisterFilesOnServer.htm)|
Регистрирует API файлов в контейнере Unity со стороны сервера.  
[RemoveWithNotificationAsync(ICollection<IFile>, IEnumerable<IFile>,
CancellationToken)](M_Tessa_Files_FileExtensions_RemoveWithNotificationAsync.htm)|
Удаляет файлы с уведомлением их источников Source. Этот метод следует
использовать для стандартного удаления файлов.  
[RemoveWithNotificationAsync(ICollection<IFile>, IFile,
CancellationToken)](M_Tessa_Files_FileExtensions_RemoveWithNotificationAsync_1.htm)|
Удаляет файл с уведомлением его источника Source. Этот метод следует
использовать для стандартного удаления файла.  
[RemoveWithNotificationAsync(ICollection<IFileSignature>,
IEnumerable<IFileSignature>,
CancellationToken)](M_Tessa_Files_FileExtensions_RemoveWithNotificationAsync_2.htm)|
Удаляет подписи файла с уведомлением их источников Source. Этот метод следует
использовать для стандартного удаления подписей файла.  
[RemoveWithNotificationAsync(ICollection<IFileSignature>, IFileSignature,
CancellationToken)](M_Tessa_Files_FileExtensions_RemoveWithNotificationAsync_3.htm)|
Удаляет подпись файла с уведомлением её источника Source. Этот метод следует
использовать для стандартного удаления подписи файла.  
[RenameAsync](M_Tessa_Files_FileExtensions_RenameAsync.htm)| Переименовывает
файл с уведомлением его источника, если имя изменилось.  
[ReplaceAsync(IFile, Byte[],
CancellationToken)](M_Tessa_Files_FileExtensions_ReplaceAsync.htm)|  Заменяет
содержимое файла на заданный массив байт.  
[ReplaceAsync(IFile, Stream,
CancellationToken)](M_Tessa_Files_FileExtensions_ReplaceAsync_2.htm)| Заменяет
контент заданного файла на контент из заданного потока.  
[ReplaceAsync(IFile, Func<CancellationToken, ValueTask<Stream>>,
Func<CancellationToken, ValueTask<Int64>>,
CancellationToken)](M_Tessa_Files_FileExtensions_ReplaceAsync_1.htm)| Заменяет
контент заданного файла на контент, определяемый заданными функциями.  
[ReplaceAsync(IFile, String, Boolean,
CancellationToken)](M_Tessa_Files_FileExtensions_ReplaceAsync_3.htm)|
Заменяет контент заданного файла на контент файла с указанным именем. Если
отличается не только путь к указанному файлу, но и имя, а также параметр
changeName равен true, то имя файла также будет изменено.  
[ReplaceAsync(IFileManager, IFile, Byte[],
CancellationToken)](M_Tessa_Files_FileExtensions_ReplaceAsync_4.htm)|
Заменяет содержимое файла на заданный массив байт.  
[ReplaceTextAsync(IFile, String, Encoding,
CancellationToken)](M_Tessa_Files_FileExtensions_ReplaceTextAsync.htm)|
Заменяет содержимое файла на заданный текст с указанием кодировки. Содержимое
файла будет сохранено во временной папке и доступно для пользователя в UI.  
[ReplaceTextAsync(IFileManager, IFile, String, Encoding,
CancellationToken)](M_Tessa_Files_FileExtensions_ReplaceTextAsync_1.htm)|
Заменяет содержимое файла на заданный текст с указанием кодировки. Содержимое
файла будет сохранено во временной папке и доступно для пользователя в UI.  
[ResolveRoot](M_Tessa_Files_FileExtensions_ResolveRoot.htm)|  Возвращает
корневой объект содержимого по свойствам
[Parent](P_Tessa_Files_IFileContent_Parent.htm). Возвращает текущий объект
content, если у него отсутствует родитель
[Parent](P_Tessa_Files_IFileContent_Parent.htm).  
[RestoreDownloadingContentAfterCancel](M_Tessa_Files_FileExtensions_RestoreDownloadingContentAfterCancel.htm)|
Восстанавливает возможность асинхронной загрузки содержимого файла или версии
после отмены. При восстановлении загрузки файла также восстанавливается
загрузка всех его версий.  
[RevertAsync](M_Tessa_Files_FileExtensions_RevertAsync.htm)| Восстанавливает
контент и имя файла к виду до его изменения.  
[SaveAsync(IFileObject, Stream, Func<IFileObject, FileContentDownloadState>,
Func<FileContentDownloadState, CancellationToken, ValueTask>,
Func<IFileObject, CancellationToken, ValueTask<IFileContent>>,
CancellationToken)](M_Tessa_Files_FileExtensions_SaveAsync.htm)| Сохраняет
контент заданного файла или версии файла в файле с указанным именем.  
[SaveAsync(IFileObject, String, Func<IFileObject, FileContentDownloadState>,
Func<FileContentDownloadState, CancellationToken, ValueTask>,
Func<IFileObject, CancellationToken, ValueTask<IFileContent>>,
CancellationToken)](M_Tessa_Files_FileExtensions_SaveAsync_1.htm)| Сохраняет
контент заданного файла или версии файла в файле с указанным именем.  
[SetActionName](M_Tessa_Files_FileExtensions_SetActionName.htm)|
Устанавливает имя действия, в рамках которого был создан файл или версия
файла. Например: FileMenuActionNames.Scan или
FileMenuActionNames.AddFromTemplate.  
[SetCategory(IFileBuilder,
String)](M_Tessa_Files_FileExtensions_SetCategory.htm)|  Устанавливает
категорию файла в виде строки без указания идентификатора категории.  
[SetCategory(IFileBuilder, String,
Guid)](M_Tessa_Files_FileExtensions_SetCategory_1.htm)|  Устанавливает
категорию файла в виде строки без указания идентификатора категории.  
[SetContent(IFileBuilder,
IFileContent)](M_Tessa_Files_FileExtensions_SetContent_3.htm)|  Устанавливает
содержимое создаваемого файла по заданному объекту контента
[IFileContent](T_Tessa_Files_IFileContent.htm). Содержимое и размер
создаваемого файла будут вычисляться на основании заданного объекта.
Содержимое является нелокальным, т.е. не сохраняется во временную папку.
Поэтому не используйте его на клиенте, если файл будет доступен пользователю в
UI.  
[SetContent(IFileBuilder, Byte[],
Boolean)](M_Tessa_Files_FileExtensions_SetContent.htm)|  Устанавливает
содержимое создаваемого файла по заданному массиву байт.  
[SetContent(IFileBuilder, Func<CancellationToken, ValueTask<Stream>>,
Func<CancellationToken,
ValueTask<Int64>>)](M_Tessa_Files_FileExtensions_SetContent_1.htm)|
Устанавливает содержимое создаваемого файла по функции, возвращающей контент,
и по функции, возвращающей его размер. Содержимое является нелокальным, т.е.
не сохраняется во временную папку. Поэтому не используйте его на клиенте, если
файл будет доступен пользователю в UI.  
[SetContent(IFileBuilder, Func<CancellationToken, ValueTask<Stream>>,
Int64)](M_Tessa_Files_FileExtensions_SetContent_2.htm)|  Устанавливает
содержимое создаваемого файла по функции, возвращающей контент, и по
фиксированному (заранее вычисленному) размеру. Содержимое является
нелокальным, т.е. не сохраняется во временную папку. Поэтому не используйте
его на клиенте, если файл будет доступен пользователю в UI.  
[SetContentReadOnly](M_Tessa_Files_FileExtensions_SetContentReadOnly.htm)|
Устанавливает содержимое создаваемого файла на основании локального файла,
который не копируется в папку с кэшем. Рекомендуется использовать этот способ,
если файл создаётся только для чтения, например, для того, чтобы сохраниться
на сервер. Содержимое является нелокальным, т.е. не сохраняется во временную
папку. Поэтому не используйте его на клиенте, если файл будет доступен
пользователю в UI.  
[SetContentText](M_Tessa_Files_FileExtensions_SetContentText.htm)|
Устанавливает содержимое создаваемого файла по заданному тексту с указанием
кодировки.  
[SetRemoteFromPathAsync](M_Tessa_Files_FileExtensions_SetRemoteFromPathAsync.htm)|
Устанавливает содержимое [IFileContent](T_Tessa_Files_IFileContent.htm) по
физическому файлу, расположенному по заданному пути. Метод доступен и для
локального, и для нелокального (remote) содержимого.  
[TryGetActualFile](M_Tessa_Files_FileExtensions_TryGetActualFile.htm)|
Возвращает объект [IFile](T_Tessa_Files_IFile.htm), соответствующей
переданному файлу или файлу переданной версии. Возвращает null, если
переданный объект не является файлом [IFile](T_Tessa_Files_IFile.htm) или
версией [IFileVersion](T_Tessa_Files_IFileVersion.htm).  
[TryGetActualVersion](M_Tessa_Files_FileExtensions_TryGetActualVersion.htm)|
Возвращает объект [IFileVersion](T_Tessa_Files_IFileVersion.htm),
соответствующей переданной версии или последней версии переданного файла.
Возвращает null, если переданный объект не является файлом
[IFile](T_Tessa_Files_IFile.htm) или версией
[IFileVersion](T_Tessa_Files_IFileVersion.htm).  
[TryGetFile(IFileContainer,
Guid)](M_Tessa_Files_FileExtensions_TryGetFile.htm)|  Возвращает файл,
полученный по заданному идентификатору [ID](P_Tessa_Files_IFileEntity_ID.htm),
или null, если подходящий файл не был найден.  
[TryGetFile(IFileContainer,
String)](M_Tessa_Files_FileExtensions_TryGetFile_1.htm)|  Возвращает файл,
полученный по заданному имени [Name](P_Tessa_Files_IFileObject_Name.htm), или
null, если подходящий файл не был найден.  
## __См. также
#### Ссылки
[FileExtensions - ](T_Tessa_Files_FileExtensions.htm)
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
