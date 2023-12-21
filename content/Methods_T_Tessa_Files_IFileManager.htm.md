# IFileManager - методы
##  __Методы
[ChangeCategoryAsync](M_Tessa_Files_IFileManager_ChangeCategoryAsync.htm)|
Изменяет категорию файла и уведомляет об этом его источник, если категория в
действительности изменилась.  
---|---  
[CopyAsync](M_Tessa_Files_IFileManager_CopyAsync.htm)|  Создаёт копию
заданного файла. Если контент копируемого файла не загружен, то он загружается
перед созданием копии. Первым значением возвращается копия заданного файла или
null, если копию создать не удалось. В этом случае возвращённый результат
валидации не будет успешным.  
[CreateFileAsync(IFileSource, Stream, String, IFileType, IFileCategory, IUser,
Func<IFileCreationToken, CancellationToken, ValueTask>,
Func<IFileVersionCreationToken, CancellationToken, ValueTask>,
CancellationToken)](M_Tessa_Files_IFileManager_CreateFileAsync.htm)|  Создаёт
файл с указанными параметрами и единственной версией. Возвращает созданный
файл или null, если создать файл не удалось.  
[CreateFileAsync(IFileSource, String, IFileType, IFileCategory,
Func<CancellationToken, ValueTask<IFileContent>>, IUser,
Func<IFileCreationToken, CancellationToken, ValueTask>,
Func<IFileVersionCreationToken, CancellationToken, ValueTask>,
CancellationToken)](M_Tessa_Files_IFileManager_CreateFileAsync_1.htm)|
Создаёт файл с указанными параметрами и единственной версией. Это
вспомогательный метод, который нельзя переопределить. Возвращает созданный
файл или null, если создать файл не удалось.  
[CreateFileAsync(IFileSource, String, IFileType, IFileCategory,
Func<IFileContent, CancellationToken, ValueTask>, IUser,
Func<IFileCreationToken, CancellationToken, ValueTask>,
Func<IFileVersionCreationToken, CancellationToken, ValueTask>,
CancellationToken)](M_Tessa_Files_IFileManager_CreateFileAsync_2.htm)|
Создаёт файл с указанными параметрами и единственной версией. Это
вспомогательный метод, который нельзя переопределить. Возвращает созданный
файл или null, если создать файл не удалось.  
[CreateFileAsync(IFileSource, String, IFileType, IFileCategory, String, IUser,
Func<IFileCreationToken, CancellationToken, ValueTask>,
Func<IFileVersionCreationToken, CancellationToken, ValueTask>,
CancellationToken)](M_Tessa_Files_IFileManager_CreateFileAsync_3.htm)|
Создаёт файл с указанными параметрами и единственной версией. Возвращает
созданный файл или null, если создать файл не удалось.  
[EnsureContentDownloadedAsync](M_Tessa_Files_IFileManager_EnsureContentDownloadedAsync.htm)|
Загружает контент файла или версии файла, если он ещё не был загружен. На
загруженном контенте вызывается метод [IFileContent.EnsureLocalUpdatedAsync].  
[EnsureContentDownloadedInUIAsync](M_Tessa_Files_IFileManager_EnsureContentDownloadedInUIAsync.htm)|
Загружает контент файла или версии файла, если он ещё не был загружен. На
загруженном контенте вызывается метод [IFileContent.EnsureLocalUpdatedAsync].
Изменение состояния контента выполняется в основном потоке UI, если выполнение
производится на клиенте, и в текущем потоке, если выполнение производится
посредством серверного API.  
[EnsureContentModifiedAsync](M_Tessa_Files_IFileManager_EnsureContentModifiedAsync.htm)|
Проверяет, что источник файла был уведомлён об изменениях, сделанных для
контента файла [IFileObject.Content].  
[EnsureSignaturesLoadedAsync](M_Tessa_Files_IFileManager_EnsureSignaturesLoadedAsync.htm)|
Загружает подписи для версии файла, если они ещё не были загружены.  
[EnsureVersionsLoadedAsync](M_Tessa_Files_IFileManager_EnsureVersionsLoadedAsync.htm)|
Загружает версии файла, если они ещё не были загружены.  
[OpenAsync](M_Tessa_Files_IFileManager_OpenAsync.htm)| Открывает контент
заданного файла или версии файла для чтения или для редактирования.  
[OpenInFolderAsync](M_Tessa_Files_IFileManager_OpenInFolderAsync.htm)|
Открывает контент заданного файла или версии файла для чтения или для
редактирования в окне проводника.  
[RenameAsync](M_Tessa_Files_IFileManager_RenameAsync.htm)| Переименовывает
файл с уведомлением его источника, если имя изменилось.  
[ReplaceAsync(IFile, Stream,
CancellationToken)](M_Tessa_Files_IFileManager_ReplaceAsync_1.htm)| Заменяет
контент заданного файла на контент из заданного потока.  
[ReplaceAsync(IFile, Func<CancellationToken, ValueTask<Stream>>,
Func<CancellationToken, ValueTask<Int64>>,
CancellationToken)](M_Tessa_Files_IFileManager_ReplaceAsync.htm)| Заменяет
контент заданного файла на контент, определяемый заданными функциями.  
[ReplaceAsync(IFile, String, Boolean,
CancellationToken)](M_Tessa_Files_IFileManager_ReplaceAsync_2.htm)|  Заменяет
контент заданного файла на контент файла с указанным именем. Если отличается
не только путь к указанному файлу, но и имя, а также параметр changeName равен
true, то имя файла также будет изменено.  
[RevertAsync](M_Tessa_Files_IFileManager_RevertAsync.htm)| Восстанавливает
контент и имя файла к виду до его изменения.  
[SaveAsync(IFileObject, Stream, Func<IFileObject, FileContentDownloadState>,
Func<FileContentDownloadState, CancellationToken, ValueTask>,
Func<IFileObject, CancellationToken, ValueTask<IFileContent>>,
CancellationToken)](M_Tessa_Files_IFileManager_SaveAsync.htm)| Сохраняет
контент заданного файла или версии файла в файле с указанным именем.  
[SaveAsync(IFileObject, String, Func<IFileObject, FileContentDownloadState>,
Func<FileContentDownloadState, CancellationToken, ValueTask>,
Func<IFileObject, CancellationToken, ValueTask<IFileContent>>,
CancellationToken)](M_Tessa_Files_IFileManager_SaveAsync_1.htm)| Сохраняет
контент заданного файла или версии файла в файле с указанным именем.  
##  __Методы расширения
[ReplaceAsync](M_Tessa_Files_FileExtensions_ReplaceAsync_4.htm)|  Заменяет
содержимое файла на заданный массив байт.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
---|---  
[ReplaceTextAsync](M_Tessa_Files_FileExtensions_ReplaceTextAsync_1.htm)|
Заменяет содержимое файла на заданный текст с указанием кодировки. Содержимое
файла будет сохранено во временной папке и доступно для пользователя в UI.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
##  __См. также
#### Ссылки
[IFileManager - ](T_Tessa_Files_IFileManager.htm)
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
