# IFile - методы
##  __Методы
[Equals(T)](https://learn.microsoft.com/dotnet/api/system.iequatable-1.equals#system-
iequatable-1-equals\(-0\))| Indicates whether the current object is equal to
another object of the same type.  
(Унаследован от
[IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<[IFile](T_Tessa_Files_IFile.htm)>)  
---|---  
[Equals(T)](https://learn.microsoft.com/dotnet/api/system.iequatable-1.equals#system-
iequatable-1-equals\(-0\))|  
(Унаследован от
[IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<[IFileEntity](T_Tessa_Files_IFileEntity.htm)>)  
[Equals(T)](https://learn.microsoft.com/dotnet/api/system.iequatable-1.equals#system-
iequatable-1-equals\(-0\))|  
(Унаследован от
[IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<[IFileObject](T_Tessa_Files_IFileObject.htm)>)  
[GetState](M_Tessa_Files_IFile_GetState.htm)| Возвращает текущее состояние
файла.  
[HasChanges](M_Tessa_Files_IFile_HasChanges.htm)| Возвращает признак того, что
заданное состояние файла отличается от его текущего состояния.  
[InvalidateContentAsync](M_Tessa_Files_IFileObject_InvalidateContentAsync.htm)|
Удаляет локально загруженный контент, переводя его в начальное состояние.
Следующий раз при получении контента он будет заново загружен.  
(Унаследован от [IFileObject](T_Tessa_Files_IFileObject.htm))  
[SetCategoryAsync](M_Tessa_Files_IFile_SetCategoryAsync.htm)| Устанавливает
категорию файла или null, если файл не имеет категории.  
[SetContentStateAsync](M_Tessa_Files_IFileObject_SetContentStateAsync.htm)|
Устанавливает состояние загрузки контента файла или версии файла в кэш для
последующего отображения пользователю.  
(Унаследован от [IFileObject](T_Tessa_Files_IFileObject.htm))  
[SetHashAsync](M_Tessa_Files_IFileObject_SetHashAsync.htm)|  Устанавливает хеш
контента файла или версии файла, или null, если хеш не вычислен. Хеш является
необязательным свойством, которое по умолчанию не заполняется системой.  
(Унаследован от [IFileObject](T_Tessa_Files_IFileObject.htm))  
[SetModifiedAsync](M_Tessa_Files_IFile_SetModifiedAsync.htm)|  Устанавливает
дату и время последнего изменения файла.  
[SetModifiedByIDAsync](M_Tessa_Files_IFile_SetModifiedByIDAsync.htm)|
Устанавливает идентификатор пользователя, изменившего файл.  
[SetModifiedByNameAsync](M_Tessa_Files_IFile_SetModifiedByNameAsync.htm)|
Устанавливает имя пользователя, изменившего файл.  
[SetNameAsync](M_Tessa_Files_IFileObject_SetNameAsync.htm)|  Устанавливает имя
файла или версии файла, которое является допустимым именем файла на файловой
системе, но может отличаться от отображаемого имени файла.  
(Унаследован от [IFileObject](T_Tessa_Files_IFileObject.htm))  
[SetOriginAsync](M_Tessa_Files_IFile_SetOriginAsync.htm)|  Устанавливает
исходный файл, из которого был скопирован текущий файл, или null, если текущий
файл не был скопирован.  
[SetPreviewContentAsync](M_Tessa_Files_IFile_SetPreviewContentAsync.htm)|
Устанавливает содержимое файла, отображаемое для предпросмотра. По умолчанию
значение равно [IFileObject.Content], но оно может быть переопределено.
Рекомендуется создавать такой контент из кэша, например:
file.AllocateAdditionalLocalContent("filename.txt").  
[SetStateAsync](M_Tessa_Files_IFile_SetStateAsync.htm)| Устанавливает текущее
состояние файла, равное заданному состоянию.  
[SetTypeAsync](M_Tessa_Files_IFile_SetTypeAsync.htm)| Устанавливает тип файла.  
[UpdateInitialStateAsync](M_Tessa_Files_IFile_UpdateInitialStateAsync.htm)|
Обновляет начальное состояние файла и устанавливаем его как равное заданному
состоянию. Не рекомендуется вызывать этот метод для существующих файлов,
которые уже мог отредактировать пользователь.  
## __Методы расширения
[AllocateAdditionalLocalContentAsync](M_Tessa_Files_FileExtensions_AllocateAdditionalLocalContentAsync.htm)|
Создаёт дополнительный объект локального содержимого (на диске) для файла или
версии файла. Загрузка такого содержимого отменяется вместе с основным
содержимым.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
---|---  
[CancelDownloadingContent](M_Tessa_Files_FileExtensions_CancelDownloadingContent.htm)|
Отменяет асинхронную загрузку содержимого файла или версии. При отмене
загрузки файла также отменяется загрузка всех его версий.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[ChangeCategoryAsync](M_Tessa_Files_FileExtensions_ChangeCategoryAsync_2.htm)|
Изменяет категорию файла и уведомляет об этом его источник, если категория в
действительности изменилась.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[ChangeCategoryAsync](M_Tessa_Files_FileExtensions_ChangeCategoryAsync_1.htm)|
Изменяет категорию файла без указания идентификатора категории.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[ChangeCategoryAsync](M_Tessa_Files_FileExtensions_ChangeCategoryAsync.htm)|
Изменяет категорию файла с указанием идентификатора категории.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[CopyAsync](M_Tessa_Files_FileExtensions_CopyAsync.htm)|  Создаёт копию
заданного файла. Если контент копируемого файла не загружен, то он загружается
перед созданием копии. Первым значением возвращается копия заданного файла или
null, если копию создать не удалось. В этом случае возвращённый результат
валидации не будет успешным.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[EnsureContentDownloadedAsync](M_Tessa_Files_FileExtensions_EnsureContentDownloadedAsync.htm)|
Загружает контент файла или версии файла, если он ещё не был загружен. На
загруженном контенте вызывается метод [IFileContent.EnsureLocalUpdatedAsync].  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[EnsureContentDownloadedInUIAsync](M_Tessa_Files_FileExtensions_EnsureContentDownloadedInUIAsync.htm)|
Загружает контент файла или версии файла, если он ещё не был загружен. На
загруженном контенте вызывается метод [IFileContent.EnsureLocalUpdatedAsync].
Изменение состояния контента выполняется в основном потоке UI, если выполнение
производится на клиенте, и в текущем потоке, если выполнение производится
посредством серверного API.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[EnsureContentModifiedAsync](M_Tessa_Files_FileExtensions_EnsureContentModifiedAsync.htm)|
Проверяет, что источник файла был уведомлён об изменениях, сделанных для
контента файла [IFileObject.Content].  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[EnsureVersionsLoadedAsync](M_Tessa_Files_FileExtensions_EnsureVersionsLoadedAsync.htm)|
Загружает версии файла, если они ещё не были загружены.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[GetActionName](M_Tessa_Files_FileExtensions_GetActionName.htm)|  Возвращает
имя действия, в рамках которого был создан файл или версия файла, или null,
если файл не был создан специальным способом.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[GetLinkAsync](M_Tessa_Files_FileExtensions_GetLinkAsync.htm)| Возвращает
ссылку на файл.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[GetRootedOrigin](M_Tessa_Files_FileExtensions_GetRootedOrigin.htm)|
Возвращает корневой элемент в дереве файлов, связанных посредством свойства
[Origin](P_Tessa_Files_IFile_Origin.htm), или null, если значение свойства
[Origin](P_Tessa_Files_IFile_Origin.htm) для файла file равно null.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[IsLarge](M_Tessa_Files_FileExtensions_IsLarge.htm)|  Возвращает признак того,
что содержимое версии файла считается большим файлом, поэтому будет
обрабатываться особым образом. Проверка выполняется по наличию тега
[Large](F_Tessa_Files_FileTag_Large.htm).  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
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
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[NotifyAsync](M_Tessa_Files_FileExtensions_NotifyAsync.htm)|  Уведомляет
источник заданного файла [IFileSource](T_Tessa_Files_IFileSource.htm) о
возникшем событии
[FileNotificationType](T_Tessa_Files_FileNotificationType.htm). Используйте
при изменении свойств файла вручную, чтобы эти свойства были сохранены в
пакете карточки (если файл связан с карточкой).  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[OpenAsync](M_Tessa_Files_FileExtensions_OpenAsync.htm)| Открывает контент
заданного файла или версии файла для чтения или для редактирования.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[OpenInFolderAsync](M_Tessa_Files_FileExtensions_OpenInFolderAsync.htm)|
Открывает контент заданного файла или версии файла для чтения или для
редактирования в окне проводника.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
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
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
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
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[RenameAsync](M_Tessa_Files_FileExtensions_RenameAsync.htm)| Переименовывает
файл с уведомлением его источника, если имя изменилось.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[ReplaceAsync](M_Tessa_Files_FileExtensions_ReplaceAsync.htm)|  Заменяет
содержимое файла на заданный массив байт.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[ReplaceAsync](M_Tessa_Files_FileExtensions_ReplaceAsync_2.htm)| Заменяет
контент заданного файла на контент из заданного потока.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[ReplaceAsync](M_Tessa_Files_FileExtensions_ReplaceAsync_1.htm)| Заменяет
контент заданного файла на контент, определяемый заданными функциями.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[ReplaceAsync](M_Tessa_Files_FileExtensions_ReplaceAsync_3.htm)|  Заменяет
контент заданного файла на контент файла с указанным именем. Если отличается
не только путь к указанному файлу, но и имя, а также параметр changeName равен
true, то имя файла также будет изменено.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[ReplaceTextAsync](M_Tessa_Files_FileExtensions_ReplaceTextAsync.htm)|
Заменяет содержимое файла на заданный текст с указанием кодировки. Содержимое
файла будет сохранено во временной папке и доступно для пользователя в UI.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[RestoreDownloadingContentAfterCancel](M_Tessa_Files_FileExtensions_RestoreDownloadingContentAfterCancel.htm)|
Восстанавливает возможность асинхронной загрузки содержимого файла или версии
после отмены. При восстановлении загрузки файла также восстанавливается
загрузка всех его версий.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[RevertAsync](M_Tessa_Files_FileExtensions_RevertAsync.htm)| Восстанавливает
контент и имя файла к виду до его изменения.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[SaveAsync](M_Tessa_Files_FileExtensions_SaveAsync.htm)| Сохраняет контент
заданного файла или версии файла в файле с указанным именем.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[SaveAsync](M_Tessa_Files_FileExtensions_SaveAsync_1.htm)| Сохраняет контент
заданного файла или версии файла в файле с указанным именем.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[SetActionName](M_Tessa_Files_FileExtensions_SetActionName.htm)|
Устанавливает имя действия, в рамках которого был создан файл или версия
файла. Например: FileMenuActionNames.Scan или
FileMenuActionNames.AddFromTemplate.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[TryGetActualFile](M_Tessa_Files_FileExtensions_TryGetActualFile.htm)|
Возвращает объект [IFile](T_Tessa_Files_IFile.htm), соответствующей
переданному файлу или файлу переданной версии. Возвращает null, если
переданный объект не является файлом [IFile](T_Tessa_Files_IFile.htm) или
версией [IFileVersion](T_Tessa_Files_IFileVersion.htm).  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[TryGetActualVersion](M_Tessa_Files_FileExtensions_TryGetActualVersion.htm)|
Возвращает объект [IFileVersion](T_Tessa_Files_IFileVersion.htm),
соответствующей переданной версии или последней версии переданного файла.
Возвращает null, если переданный объект не является файлом
[IFile](T_Tessa_Files_IFile.htm) или версией
[IFileVersion](T_Tessa_Files_IFileVersion.htm).  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
##  __См. также
#### Ссылки
[IFile - ](T_Tessa_Files_IFile.htm)
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
