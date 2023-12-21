# FileManager - класс
Объект, управляющий взаимодействием с файлами.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class FileManager : IFileManager
VB __Копировать
     Public Class FileManager
    	Implements IFileManager
C++ __Копировать
     public ref class FileManager : IFileManager
F# __Копировать
     type FileManager = 
        class
            interface IFileManager
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ FileManager
Derived
[Tessa.UI.Files.FileUIManager](T_Tessa_UI_Files_FileUIManager.htm)
Implements
    [IFileManager](T_Tessa_Files_IFileManager.htm)
##  __Заметки
Дочерние классы могут переопределить часть функционала в виртуальных методах.
## __Конструкторы
[FileManager](M_Tessa_Files_FileManager__ctor.htm)|  Создаёт экземпляр класса
с указанием его зависимостей.  
---|---  
## __Методы
[ChangeCategoryAsync](M_Tessa_Files_FileManager_ChangeCategoryAsync.htm)|
Изменяет категорию файла и уведомляет об этом его источник, если категория в
действительности изменилась.  
---|---  
[ChangeCategoryCoreAsync](M_Tessa_Files_FileManager_ChangeCategoryCoreAsync.htm)|
Изменяет категорию файла и уведомляет об этом его источник, если категория в
действительности изменилась.  
[CopyAsync](M_Tessa_Files_FileManager_CopyAsync.htm)|  Создаёт копию заданного
файла. Если контент копируемого файла не загружен, то он загружается перед
созданием копии. Первым значением возвращается копия заданного файла или null,
если копию создать не удалось. В этом случае возвращённый результат валидации
не будет успешным.  
[CopyCoreAsync](M_Tessa_Files_FileManager_CopyCoreAsync.htm)|  Создаёт копию
заданного файла. Если контент копируемого файла не загружен, то он загружается
перед созданием копии. Первым значением возвращается копия заданного файла или
null, если копию создать не удалось. В этом случае возвращённый результат
валидации не будет успешным.  
[CreateFileAsync(IFileSource, Stream, String, IFileType, IFileCategory, IUser,
Func<IFileCreationToken, CancellationToken, ValueTask>,
Func<IFileVersionCreationToken, CancellationToken, ValueTask>,
CancellationToken)](M_Tessa_Files_FileManager_CreateFileAsync.htm)|  Создаёт
файл с указанными параметрами и единственной версией. Возвращает созданный
файл или null, если создать файл не удалось.  
[CreateFileAsync(IFileSource, String, IFileType, IFileCategory,
Func<CancellationToken, ValueTask<IFileContent>>, IUser,
Func<IFileCreationToken, CancellationToken, ValueTask>,
Func<IFileVersionCreationToken, CancellationToken, ValueTask>,
CancellationToken)](M_Tessa_Files_FileManager_CreateFileAsync_1.htm)|  Создаёт
файл с указанными параметрами и единственной версией. Это вспомогательный
метод, который нельзя переопределить. Возвращает созданный файл или null, если
создать файл не удалось.  
[CreateFileAsync(IFileSource, String, IFileType, IFileCategory,
Func<IFileContent, CancellationToken, ValueTask>, IUser,
Func<IFileCreationToken, CancellationToken, ValueTask>,
Func<IFileVersionCreationToken, CancellationToken, ValueTask>,
CancellationToken)](M_Tessa_Files_FileManager_CreateFileAsync_2.htm)|  Создаёт
файл с указанными параметрами и единственной версией. Это вспомогательный
метод, который нельзя переопределить. Возвращает созданный файл или null, если
создать файл не удалось.  
[CreateFileAsync(IFileSource, String, IFileType, IFileCategory, String, IUser,
Func<IFileCreationToken, CancellationToken, ValueTask>,
Func<IFileVersionCreationToken, CancellationToken, ValueTask>,
CancellationToken)](M_Tessa_Files_FileManager_CreateFileAsync_3.htm)|  Создаёт
файл с указанными параметрами и единственной версией. Возвращает созданный
файл или null, если создать файл не удалось.  
[CreateFileCoreAsync(IFileSource, Stream, String, IFileType, IFileCategory,
IUser, Func<IFileCreationToken, CancellationToken, ValueTask>,
Func<IFileVersionCreationToken, CancellationToken, ValueTask>,
CancellationToken)](M_Tessa_Files_FileManager_CreateFileCoreAsync.htm)|
Создаёт файл с указанными параметрами и единственной версией. Возвращает
созданный файл или null, если создать файл не удалось.  
[CreateFileCoreAsync(IFileSource, String, IFileType, IFileCategory,
Func<CancellationToken, ValueTask<IFileContent>>, IUser,
Func<IFileCreationToken, CancellationToken, ValueTask>,
Func<IFileVersionCreationToken, CancellationToken, ValueTask>,
CancellationToken)](M_Tessa_Files_FileManager_CreateFileCoreAsync_1.htm)|
Создаёт файл с указанными параметрами и единственной версией. Это
вспомогательный метод, который нельзя переопределить. Возвращает созданный
файл или null, если создать файл не удалось.  
[CreateFileCoreAsync(IFileSource, String, IFileType, IFileCategory,
Func<IFileContent, CancellationToken, ValueTask>, IUser,
Func<IFileCreationToken, CancellationToken, ValueTask>,
Func<IFileVersionCreationToken, CancellationToken, ValueTask>,
CancellationToken)](M_Tessa_Files_FileManager_CreateFileCoreAsync_2.htm)|
Создаёт файл с указанными параметрами и единственной версией. Это
вспомогательный метод, который нельзя переопределить. Возвращает созданный
файл или null, если создать файл не удалось.  
[CreateFileCoreAsync(IFileSource, String, IFileType, IFileCategory, String,
IUser, Func<IFileCreationToken, CancellationToken, ValueTask>,
Func<IFileVersionCreationToken, CancellationToken, ValueTask>,
CancellationToken)](M_Tessa_Files_FileManager_CreateFileCoreAsync_3.htm)|
Создаёт файл с указанными параметрами и единственной версией. Возвращает
созданный файл или null, если создать файл не удалось.  
[EnsureContentDownloadedAsync](M_Tessa_Files_FileManager_EnsureContentDownloadedAsync.htm)|
Загружает контент файла или версии файла, если он ещё не был загружен. На
загруженном контенте вызывается метод [IFileContent.EnsureLocalUpdatedAsync].  
[EnsureContentDownloadedCoreAsync](M_Tessa_Files_FileManager_EnsureContentDownloadedCoreAsync.htm)|
Загружает контент файла или версии файла, если он ещё не был загружен. На
загруженном контенте вызывается метод [IFileContent.EnsureLocalUpdatedAsync].  
[EnsureContentDownloadedInUIAsync](M_Tessa_Files_FileManager_EnsureContentDownloadedInUIAsync.htm)|
Загружает контент файла или версии файла, если он ещё не был загружен. На
загруженном контенте вызывается метод [IFileContent.EnsureLocalUpdatedAsync].
Изменение состояния контента выполняется в основном потоке UI, если выполнение
производится на клиенте, и в текущем потоке, если выполнение производится
посредством серверного API.  
[EnsureContentDownloadedInUICoreAsync](M_Tessa_Files_FileManager_EnsureContentDownloadedInUICoreAsync.htm)|
Загружает контент файла или версии файла, если он ещё не был загружен. На
загруженном контенте вызывается метод [IFileContent.EnsureLocalUpdatedAsync].
Изменение состояния контента выполняется в основном потоке UI, если выполнение
производится на клиенте, и в текущем потоке, если выполнение производится
посредством серверного API.  
[EnsureContentModifiedAsync](M_Tessa_Files_FileManager_EnsureContentModifiedAsync.htm)|
Проверяет, что источник файла был уведомлён об изменениях, сделанных для
контента файла [IFileObject.Content].  
[EnsureContentModifiedCoreAsync](M_Tessa_Files_FileManager_EnsureContentModifiedCoreAsync.htm)|
Проверяет, что источник файла был уведомлён об изменениях, сделанных для
контента файла [IFileObject.Content].  
[EnsureSignaturesLoadedAsync](M_Tessa_Files_FileManager_EnsureSignaturesLoadedAsync.htm)|
Загружает подписи для версии файла, если они ещё не были загружены.  
[EnsureSignaturesLoadedCoreAsync](M_Tessa_Files_FileManager_EnsureSignaturesLoadedCoreAsync.htm)|
Загружает подписи для версии файла, если они ещё не были загружены.  
[EnsureVersionsLoadedAsync](M_Tessa_Files_FileManager_EnsureVersionsLoadedAsync.htm)|
Загружает версии файла, если они ещё не были загружены.  
[EnsureVersionsLoadedCoreAsync](M_Tessa_Files_FileManager_EnsureVersionsLoadedCoreAsync.htm)|
Загружает версии файла, если они ещё не были загружены.  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ExecutePropertyChangedAsync](M_Tessa_Files_FileManager_ExecutePropertyChangedAsync.htm)|
Асинхронно выполняет действие, соответствующее вызову события PropertyChanged.  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[OpenAsync](M_Tessa_Files_FileManager_OpenAsync.htm)| Открывает контент
заданного файла или версии файла для чтения или для редактирования.  
[OpenCoreAsync](M_Tessa_Files_FileManager_OpenCoreAsync.htm)| Открывает
контент заданного файла или версии файла для чтения или для редактирования.  
[OpenInFolderAsync](M_Tessa_Files_FileManager_OpenInFolderAsync.htm)|
Открывает контент заданного файла или версии файла для чтения или для
редактирования в окне проводника.  
[OpenInFolderCoreAsync](M_Tessa_Files_FileManager_OpenInFolderCoreAsync.htm)|
Открывает контент заданного файла или версии файла для чтения или для
редактирования в окне проводника.  
[PerformActionWithFilePathAsync](M_Tessa_Files_FileManager_PerformActionWithFilePathAsync.htm)|
Выполняет заданное действие с контентом файла на диске, загружая его при
необходимости.  
[RenameAsync](M_Tessa_Files_FileManager_RenameAsync.htm)| Переименовывает файл
с уведомлением его источника, если имя изменилось.  
[RenameCoreAsync](M_Tessa_Files_FileManager_RenameCoreAsync.htm)|
Переименовывает файл с уведомлением его источника, если имя изменилось.  
[ReplaceAsync(IFile, Stream,
CancellationToken)](M_Tessa_Files_FileManager_ReplaceAsync_1.htm)| Заменяет
контент заданного файла на контент из заданного потока.  
[ReplaceAsync(IFile, Func<CancellationToken, ValueTask<Stream>>,
Func<CancellationToken, ValueTask<Int64>>,
CancellationToken)](M_Tessa_Files_FileManager_ReplaceAsync.htm)| Заменяет
контент заданного файла на контент, определяемый заданными функциями.  
[ReplaceAsync(IFile, String, Boolean,
CancellationToken)](M_Tessa_Files_FileManager_ReplaceAsync_2.htm)|  Заменяет
контент заданного файла на контент файла с указанным именем. Если отличается
не только путь к указанному файлу, но и имя, а также параметр changeName равен
true, то имя файла также будет изменено.  
[ReplaceCoreAsync(IFile, Stream,
CancellationToken)](M_Tessa_Files_FileManager_ReplaceCoreAsync_1.htm)|
Заменяет контент заданного файла на контент из заданного потока.  
[ReplaceCoreAsync(IFile, Func<CancellationToken, ValueTask<Stream>>,
Func<CancellationToken, ValueTask<Int64>>,
CancellationToken)](M_Tessa_Files_FileManager_ReplaceCoreAsync.htm)| Заменяет
контент заданного файла на контент, определяемый заданными функциями.  
[ReplaceCoreAsync(IFile, String, Boolean,
CancellationToken)](M_Tessa_Files_FileManager_ReplaceCoreAsync_2.htm)|
Заменяет контент заданного файла на контент файла с указанным именем. Если
отличается не только путь к указанному файлу, но и имя, а также параметр
changeName равен true, то имя файла также будет изменено.  
[ReplaceOrAddVersionAsync](M_Tessa_Files_FileManager_ReplaceOrAddVersionAsync.htm)|
Добавляет или изменяет последнюю добавленную версию файла, чтобы отразить
замену контента. Контент file.[Content](P_Tessa_Files_IFileObject_Content.htm)
уже должен быть заменён. Это вспомогательный метод, который нельзя
переопределить.  
[RevertAsync](M_Tessa_Files_FileManager_RevertAsync.htm)| Восстанавливает
контент и имя файла к виду до его изменения.  
[RevertCoreAsync](M_Tessa_Files_FileManager_RevertCoreAsync.htm)|
Восстанавливает контент и имя файла к виду до его изменения.  
[SaveAsync(IFileObject, Stream, Func<IFileObject, FileContentDownloadState>,
Func<FileContentDownloadState, CancellationToken, ValueTask>,
Func<IFileObject, CancellationToken, ValueTask<IFileContent>>,
CancellationToken)](M_Tessa_Files_FileManager_SaveAsync.htm)| Сохраняет
контент заданного файла или версии файла в файле с указанным именем.  
[SaveAsync(IFileObject, String, Func<IFileObject, FileContentDownloadState>,
Func<FileContentDownloadState, CancellationToken, ValueTask>,
Func<IFileObject, CancellationToken, ValueTask<IFileContent>>,
CancellationToken)](M_Tessa_Files_FileManager_SaveAsync_1.htm)| Сохраняет
контент заданного файла или версии файла в файле с указанным именем.  
[SaveCoreAsync(IFileObject, Stream, Func<IFileObject,
FileContentDownloadState>, Func<FileContentDownloadState, CancellationToken,
ValueTask>, Func<IFileObject, CancellationToken, ValueTask<IFileContent>>,
CancellationToken)](M_Tessa_Files_FileManager_SaveCoreAsync.htm)| Сохраняет
контент заданного файла или версии файла в файле с указанным именем.  
[SaveCoreAsync(IFileObject, String, Func<IFileObject,
FileContentDownloadState>, Func<FileContentDownloadState, CancellationToken,
ValueTask>, Func<IFileObject, CancellationToken, ValueTask<IFileContent>>,
CancellationToken)](M_Tessa_Files_FileManager_SaveCoreAsync_1.htm)| Сохраняет
контент заданного файла или версии файла в файле с указанным именем.  
[SetDownloadStateInUIAsync](M_Tessa_Files_FileManager_SetDownloadStateInUIAsync.htm)|
Устанавливает состояние содержимого в потоке UI.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[ReplaceAsync](M_Tessa_Files_FileExtensions_ReplaceAsync_4.htm)|  Заменяет
содержимое файла на заданный массив байт.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[ReplaceTextAsync](M_Tessa_Files_FileExtensions_ReplaceTextAsync_1.htm)|
Заменяет содержимое файла на заданный текст с указанием кодировки. Содержимое
файла будет сохранено во временной папке и доступно для пользователя в UI.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
