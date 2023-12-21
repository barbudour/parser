# IFileVersion - интерфейс
Версия файла.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IFileVersion : IFileObject, 
    	IFileEntity, IEquatable<IFileEntity>, INotifyPropertyChanged, IEquatable<IFileObject>, 
    	IEquatable<IFileVersion>
VB __Копировать
     Public Interface IFileVersion
    	Inherits IFileObject, IFileEntity, IEquatable(Of IFileEntity), 
    	INotifyPropertyChanged, IEquatable(Of IFileObject), IEquatable(Of IFileVersion)
C++ __Копировать
     public interface class IFileVersion : IFileObject, 
    	IFileEntity, IEquatable<IFileEntity^>, INotifyPropertyChanged, IEquatable<IFileObject^>, 
    	IEquatable<IFileVersion^>
F# __Копировать
     type IFileVersion = 
        interface
            interface IFileObject
            interface IFileEntity
            interface IEquatable<IFileEntity>
            interface INotifyPropertyChanged
            interface IEquatable<IFileObject>
            interface IEquatable<IFileVersion>
        end
Implements
    [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<[IFileEntity](T_Tessa_Files_IFileEntity.htm)>, [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<[IFileObject](T_Tessa_Files_IFileObject.htm)>, [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<IFileVersion>, [IFileEntity](T_Tessa_Files_IFileEntity.htm), [IFileObject](T_Tessa_Files_IFileObject.htm)
##  __Свойства
[Cancellation](P_Tessa_Files_IFileObject_Cancellation.htm)|  Объект, который
может использоваться для отмены асинхронных операций с файлом или версией
файла, которые поддерживают отмену. На текущий момент это доступно для
загрузки содержимого версии файла.  
(Унаследован от [IFileObject](T_Tessa_Files_IFileObject.htm))  
---|---  
[Content](P_Tessa_Files_IFileObject_Content.htm)|  Контент файла или версии
файла. Контент файла обычно равен контенту его последней версии, но имя файла
на файловой системе может отличаться.  
(Унаследован от [IFileObject](T_Tessa_Files_IFileObject.htm))  
[ContentSource](P_Tessa_Files_IFileVersion_ContentSource.htm)| Местоположение
контента версии файла.  
[ContentState](P_Tessa_Files_IFileObject_ContentState.htm)|  Состояние
загрузки контента файла или версии файла в кэш для последующего отображения
пользователю.  
(Унаследован от [IFileObject](T_Tessa_Files_IFileObject.htm))  
[Created](P_Tessa_Files_IFileVersion_Created.htm)| Дата создания версии.  
[CreatedByID](P_Tessa_Files_IFileVersion_CreatedByID.htm)| Идентификатор
пользователя, который создал версию.  
[CreatedByName](P_Tessa_Files_IFileVersion_CreatedByName.htm)| Имя
пользователя, который создал версию.  
[ErrorInfo](P_Tessa_Files_IFileVersion_ErrorInfo.htm)|  Информация по ошибке,
возникшей при сохранении версии файла, или null, если ошибок не было.  
[File](P_Tessa_Files_IFileVersion_File.htm)|  Файл, к которому относится
версия. Свойства файла имеют текущее состояние, а не таковое на момент
создания версии.  
[Hash](P_Tessa_Files_IFileObject_Hash.htm)|  Хеш контента файла или версии
файла, или null, если хеш не вычислен. Хеш является необязательным свойством,
которое по умолчанию не заполняется системой.  
(Унаследован от [IFileObject](T_Tessa_Files_IFileObject.htm))  
[ID](P_Tessa_Files_IFileEntity_ID.htm)| Идентификатор объекта.  
(Унаследован от [IFileEntity](T_Tessa_Files_IFileEntity.htm))  
[Info](P_Tessa_Files_IFileObject_Info.htm)| Дополнительная информация,
используемая в расширениях.  
(Унаследован от [IFileObject](T_Tessa_Files_IFileObject.htm))  
[LinkID](P_Tessa_Files_IFileVersion_LinkID.htm)|  Внешний идентификатор версии
файла или null, если такой идентификатор не задан. Может использоваться в
расширениях для связи с содержимым во внешнем местоположении.  
[Name](P_Tessa_Files_IFileObject_Name.htm)|  Имя файла или версии файла,
которое является допустимым именем файла на файловой системе, но может
отличаться от отображаемого имени файла.  
(Унаследован от [IFileObject](T_Tessa_Files_IFileObject.htm))  
[Number](P_Tessa_Files_IFileVersion_Number.htm)|  Порядковый номер версии
файла, отсчитываемый от 1.  
[Options](P_Tessa_Files_IFileObject_Options.htm)| Настройки файла или версии
файла. Сериализуются в карточке в форме JSON.  
(Унаследован от [IFileObject](T_Tessa_Files_IFileObject.htm))  
[RequestInfo](P_Tessa_Files_IFileObject_RequestInfo.htm)|  Дополнительная
пользовательская информация, передаваемая в запросы к серверу, которые
относятся к загрузке содержимого файла/версии, к загрузке списка версий файла
или к загрузке списка подписей.  
(Унаследован от [IFileObject](T_Tessa_Files_IFileObject.htm))  
[Signatures](P_Tessa_Files_IFileVersion_Signatures.htm)| Подписи для версии
файла.  
[Size](P_Tessa_Files_IFileObject_Size.htm)|  Размер файла или версии файла в
байтах. Устанавливается при создании объекта и затем обновляется в зависимости
от действительного размера контента [IFileContent.Size]. Значение
[FileContent.UnknownSize] определяет, что размер неизвестен.  
(Унаследован от [IFileObject](T_Tessa_Files_IFileObject.htm))  
[Source](P_Tessa_Files_IFileEntity_Source.htm)|  Объект, обеспечивающий
взаимодействие текущего объекта с подсистемой, в которой он был создан,
например, с карточкой.  
(Унаследован от [IFileEntity](T_Tessa_Files_IFileEntity.htm))  
[State](P_Tessa_Files_IFileVersion_State.htm)| Состояние версии файла.  
[Tags](P_Tessa_Files_IFileVersion_Tags.htm)|  Теги, связанные с версией файла.
Например, признак того, что размер содержимого файла трактуется как большой
файл, поэтому файл не копируется во временную папку.  
## __Методы
[Equals(T)](https://learn.microsoft.com/dotnet/api/system.iequatable-1.equals#system-
iequatable-1-equals\(-0\))| Indicates whether the current object is equal to
another object of the same type.  
(Унаследован от
[IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<[IFileEntity](T_Tessa_Files_IFileEntity.htm)>)  
---|---  
[Equals(T)](https://learn.microsoft.com/dotnet/api/system.iequatable-1.equals#system-
iequatable-1-equals\(-0\))|  
(Унаследован от
[IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<[IFileObject](T_Tessa_Files_IFileObject.htm)>)  
[Equals(T)](https://learn.microsoft.com/dotnet/api/system.iequatable-1.equals#system-
iequatable-1-equals\(-0\))|  
(Унаследован от
[IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<IFileVersion>)  
[InvalidateContentAsync](M_Tessa_Files_IFileObject_InvalidateContentAsync.htm)|
Удаляет локально загруженный контент, переводя его в начальное состояние.
Следующий раз при получении контента он будет заново загружен.  
(Унаследован от [IFileObject](T_Tessa_Files_IFileObject.htm))  
[SetContentStateAsync](M_Tessa_Files_IFileObject_SetContentStateAsync.htm)|
Устанавливает состояние загрузки контента файла или версии файла в кэш для
последующего отображения пользователю.  
(Унаследован от [IFileObject](T_Tessa_Files_IFileObject.htm))  
[SetHashAsync](M_Tessa_Files_IFileObject_SetHashAsync.htm)|  Устанавливает хеш
контента файла или версии файла, или null, если хеш не вычислен. Хеш является
необязательным свойством, которое по умолчанию не заполняется системой.  
(Унаследован от [IFileObject](T_Tessa_Files_IFileObject.htm))  
[SetNameAsync](M_Tessa_Files_IFileObject_SetNameAsync.htm)|  Устанавливает имя
файла или версии файла, которое является допустимым именем файла на файловой
системе, но может отличаться от отображаемого имени файла.  
(Унаследован от [IFileObject](T_Tessa_Files_IFileObject.htm))  
##  __События
[PropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged.propertychanged)|
Occurs when a property value changes.  
(Унаследован от
[INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged))  
---|---  
##  __Методы расширения
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
[EnsureSignaturesLoadedAsync](M_Tessa_Files_FileExtensions_EnsureSignaturesLoadedAsync.htm)|
Загружает подписи для версии файла, если они ещё не были загружены.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[GetActionName](M_Tessa_Files_FileExtensions_GetActionName.htm)|  Возвращает
имя действия, в рамках которого был создан файл или версия файла, или null,
если файл не был создан специальным способом.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[GetLinkAsync](M_Tessa_Files_FileExtensions_GetLinkAsync_1.htm)| Возвращает
ссылку на версию файла.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[IsLarge](M_Tessa_Files_FileExtensions_IsLarge_1.htm)|  Возвращает признак
того, что содержимое версии файла считается большим файлом, поэтому будет
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
[RestoreDownloadingContentAfterCancel](M_Tessa_Files_FileExtensions_RestoreDownloadingContentAfterCancel.htm)|
Восстанавливает возможность асинхронной загрузки содержимого файла или версии
после отмены. При восстановлении загрузки файла также восстанавливается
загрузка всех его версий.  
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
версией IFileVersion.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[TryGetActualVersion](M_Tessa_Files_FileExtensions_TryGetActualVersion.htm)|
Возвращает объект IFileVersion, соответствующей переданной версии или
последней версии переданного файла. Возвращает null, если переданный объект не
является файлом [IFile](T_Tessa_Files_IFile.htm) или версией IFileVersion.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
