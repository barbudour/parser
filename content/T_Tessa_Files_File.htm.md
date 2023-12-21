# File - класс
Файл.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class File : FileObject, IFile, IFileObject, 
    	IFileEntity, IEquatable<IFileEntity>, INotifyPropertyChanged, IEquatable<IFileObject>, 
    	IEquatable<IFile>
VB __Копировать
     Public Class File
    	Inherits FileObject
    	Implements IFile, IFileObject, IFileEntity, IEquatable(Of IFileEntity), 
    	INotifyPropertyChanged, IEquatable(Of IFileObject), IEquatable(Of IFile)
C++ __Копировать
     public ref class File : public FileObject, 
    	IFile, IFileObject, IFileEntity, IEquatable<IFileEntity^>, 
    	INotifyPropertyChanged, IEquatable<IFileObject^>, IEquatable<IFile^>
F# __Копировать
     type File = 
        class
            inherit FileObject
            interface IFile
            interface IFileObject
            interface IFileEntity
            interface IEquatable<IFileEntity>
            interface INotifyPropertyChanged
            interface IEquatable<IFileObject>
            interface IEquatable<IFile>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[NotificationObject](T_Tessa_Platform_NotificationObject.htm) __[FileEntity](T_Tessa_Files_FileEntity.htm) __[FileObject](T_Tessa_Files_FileObject.htm) __ File
Derived
[Tessa.Extensions.Default.Client.ExternalFiles.ExternalFile](T_Tessa_Extensions_Default_Client_ExternalFiles_ExternalFile.htm)
Implements
    [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<[IFileEntity](T_Tessa_Files_IFileEntity.htm)>, [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<[IFileObject](T_Tessa_Files_IFileObject.htm)>, [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<[IFile](T_Tessa_Files_IFile.htm)>, [IFile](T_Tessa_Files_IFile.htm), [IFileEntity](T_Tessa_Files_IFileEntity.htm), [IFileObject](T_Tessa_Files_IFileObject.htm)
##  __Заметки
Наследники класса могут содержать дополнительные свойства, связанные с внешней
подсистемой, в которой располагается файл.
## __Конструкторы
[File](M_Tessa_Files_File__ctor.htm)|  Создаёт экземпляр класса с указанием
значений его свойств.  
---|---  
## __Свойства
[Cancellation](P_Tessa_Files_FileObject_Cancellation.htm)|  Объект, который
может использоваться для отмены асинхронных операций с файлом или версией
файла, которые поддерживают отмену. На текущий момент это доступно для
загрузки содержимого версии файла.  
(Унаследован от [FileObject](T_Tessa_Files_FileObject.htm))  
---|---  
[Category](P_Tessa_Files_File_Category.htm)|  Категория файла или null, если
файл не имеет категории.  
[Content](P_Tessa_Files_FileObject_Content.htm)|  Контент файла или версии
файла. Контент файла обычно равен контенту его последней версии, но имя файла
на файловой системе может отличаться.  
(Унаследован от [FileObject](T_Tessa_Files_FileObject.htm))  
[ContentState](P_Tessa_Files_FileObject_ContentState.htm)|  Состояние загрузки
контента файла или версии файла в кэш для последующего отображения
пользователю.  
(Унаследован от [FileObject](T_Tessa_Files_FileObject.htm))  
[Hash](P_Tessa_Files_FileObject_Hash.htm)|  Хеш контента файла или версии
файла, или null, если хеш не вычислен. Хеш является необязательным свойством,
которое по умолчанию не заполняется системой.  
(Унаследован от [FileObject](T_Tessa_Files_FileObject.htm))  
[ID](P_Tessa_Files_FileEntity_ID.htm)| Идентификатор объекта.  
(Унаследован от [FileEntity](T_Tessa_Files_FileEntity.htm))  
[Info](P_Tessa_Files_FileObject_Info.htm)| Дополнительная информация,
используемая в расширениях.  
(Унаследован от [FileObject](T_Tessa_Files_FileObject.htm))  
[InitialState](P_Tessa_Files_File_InitialState.htm)| Изначальное состояние
файла.  
[IsLocal](P_Tessa_Files_File_IsLocal.htm)|  Признак того, что файл был
загружен локально и отсутствует во внешней подсистеме. Значение используется
при просмотре превью или при открытии файла, только что добавленного в элемент
управления и не существующего на сервере.  
[Modified](P_Tessa_Files_File_Modified.htm)|  Дата и время последнего
изменения файла.  
[ModifiedByID](P_Tessa_Files_File_ModifiedByID.htm)|  Идентификатор
пользователя изменившего файл.  
[ModifiedByName](P_Tessa_Files_File_ModifiedByName.htm)|  Имя пользователя
изменившего файл.  
[Name](P_Tessa_Files_FileObject_Name.htm)|  Имя файла или версии файла,
которое является допустимым именем файла на файловой системе, но может
отличаться от отображаемого имени файла.  
(Унаследован от [FileObject](T_Tessa_Files_FileObject.htm))  
[NewVersionTags](P_Tessa_Files_File_NewVersionTags.htm)|  Список тегов,
связанных с добавляемой версией файла, т.е. при изменении содержимого файла в
случае замены, редактирования и др. Сериализуются в карточке в форме строки.  
[Options](P_Tessa_Files_FileObject_Options.htm)| Настройки файла или версии
файла. Сериализуются в карточке в форме JSON.  
(Унаследован от [FileObject](T_Tessa_Files_FileObject.htm))  
[Origin](P_Tessa_Files_File_Origin.htm)|  Исходный файл, из которого был
скопирован текущий файл, или null, если текущий файл не был скопирован.  
[Permissions](P_Tessa_Files_File_Permissions.htm)| Разрешения на действия с
файлом.  
[PreviewContent](P_Tessa_Files_File_PreviewContent.htm)|  Содержимое файла,
отображаемое для предпросмотра. По умолчанию значение равно
[IFileObject.Content], но оно может быть переопределено. Рекомендуется
создавать такой контент из кэша, например:
file.AllocateAdditionalLocalContent("filename.txt"). Возвращаемое значение не
равно null.  
[RequestInfo](P_Tessa_Files_FileObject_RequestInfo.htm)|  Дополнительная
пользовательская информация, передаваемая в запросы к серверу, которые
относятся к загрузке содержимого файла/версии, к загрузке списка версий файла
или к загрузке списка подписей.  
(Унаследован от [FileObject](T_Tessa_Files_FileObject.htm))  
[Size](P_Tessa_Files_FileObject_Size.htm)|  Размер файла или версии файла в
байтах. Устанавливается при создании объекта и затем обновляется в зависимости
от действительного размера контента [IFileContent.Size]. Значение
[FileContent.UnknownSize] определяет, что размер неизвестен.  
(Унаследован от [FileObject](T_Tessa_Files_FileObject.htm))  
[Source](P_Tessa_Files_FileEntity_Source.htm)|  Объект, обеспечивающий
взаимодействие текущего объекта с подсистемой, в которой он был создан,
например, с карточкой.  
(Унаследован от [FileEntity](T_Tessa_Files_FileEntity.htm))  
[Type](P_Tessa_Files_File_Type.htm)| Тип файла.  
[Versions](P_Tessa_Files_File_Versions.htm)|  Список версий файла. Коллекция
может быть пустой, если информация по версиям ещё не была запрошена.  
## __Методы
[Equals(IFile)](M_Tessa_Files_File_Equals.htm)| Сравнивает текущий объект с
заданным.  
---|---  
[Equals(IFileEntity)](M_Tessa_Files_FileEntity_Equals_1.htm)| Сравнивает
текущий объект с заданным.  
(Унаследован от [FileEntity](T_Tessa_Files_FileEntity.htm))  
[Equals(IFileObject)](M_Tessa_Files_FileObject_Equals.htm)| Сравнивает текущий
объект с заданным.  
(Унаследован от [FileObject](T_Tessa_Files_FileObject.htm))  
[Equals(Object)](M_Tessa_Files_FileEntity_Equals.htm)| Сравнивает текущий
объект с заданным.  
(Унаследован от [FileEntity](T_Tessa_Files_FileEntity.htm))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](M_Tessa_Files_FileEntity_GetHashCode.htm)| Возвращает хеш-код
объекта.  
(Унаследован от [FileEntity](T_Tessa_Files_FileEntity.htm))  
[GetState](M_Tessa_Files_File_GetState.htm)| Возвращает текущее состояние
файла.  
[GetStateCore](M_Tessa_Files_File_GetStateCore.htm)| Возвращает текущее
состояние файла.  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[HasChanges](M_Tessa_Files_File_HasChanges.htm)| Возвращает признак того, что
заданное состояние файла отличается от его текущего состояния.  
[HasChangesCore](M_Tessa_Files_File_HasChangesCore.htm)| Возвращает признак
того, что заданное состояние файла отличается от его текущего состояния.  
[InvalidateContentAsync](M_Tessa_Files_FileObject_InvalidateContentAsync.htm)|
Удаляет локально загруженный контент, переводя его в начальное состояние.
Следующий раз при получении контента он будет заново загружен.  
(Унаследован от [FileObject](T_Tessa_Files_FileObject.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[OnContentPropertyChanged](M_Tessa_Files_FileObject_OnContentPropertyChanged.htm)|
Обработчик события на изменение свойства для контента текущего объекта
[IFileObject.Content].  
(Унаследован от [FileObject](T_Tessa_Files_FileObject.htm))  
[OnPropertyChanged(PropertyChangedEventArgs)](M_Tessa_Platform_NotificationObject_OnPropertyChanged.htm)|
Уведомляет об изменении свойства с именем, заданным в аргументах события.  
(Унаследован от [NotificationObject](T_Tessa_Platform_NotificationObject.htm))  
[OnPropertyChanged(String)](M_Tessa_Platform_NotificationObject_OnPropertyChanged_1.htm)|
Уведомляет об изменении свойства с заданным именем у объекта.  
(Унаследован от [NotificationObject](T_Tessa_Platform_NotificationObject.htm))  
[OnPropertyChangedAsync(PropertyChangedEventArgs,
Boolean)](M_Tessa_Platform_NotificationObject_OnPropertyChangedAsync.htm)|
Уведомляет об изменении свойства с именем, заданным в аргументах события,
асинхронно, в соответствии с принятым для текущего объекта поведением. Если
есть возможность вызвать событие синхронно, то оно вызывается синхронно. Если
объект является моделью представления WPF и текущий поток отличен от потока
диспетчера WPF для приложения (основной поток UI), то выполнение асинхронно
переключается в этот поток. Если это не так, то событие выполняется синхронно.  
(Унаследован от [NotificationObject](T_Tessa_Platform_NotificationObject.htm))  
[OnPropertyChangedAsync(String,
Boolean)](M_Tessa_Platform_NotificationObject_OnPropertyChangedAsync_1.htm)|
Уведомляет об изменении свойства с заданным именем у объекта асинхронно, в
соответствии с принятым для текущего объекта поведением. Если есть возможность
вызвать событие синхронно, то оно вызывается синхронно. Если объект является
моделью представления WPF и текущий поток отличен от потока диспетчера WPF для
приложения (основной поток UI), то выполнение асинхронно переключается в этот
поток. Если это не так, то событие выполняется синхронно.  
(Унаследован от [NotificationObject](T_Tessa_Platform_NotificationObject.htm))  
[SetCategoryAsync](M_Tessa_Files_File_SetCategoryAsync.htm)| Устанавливает
категорию файла или null, если файл не имеет категории.  
[SetContentStateAsync](M_Tessa_Files_FileObject_SetContentStateAsync.htm)|
Устанавливает состояние загрузки контента файла или версии файла в кэш для
последующего отображения пользователю.  
(Унаследован от [FileObject](T_Tessa_Files_FileObject.htm))  
[SetHashAsync](M_Tessa_Files_FileObject_SetHashAsync.htm)|  Устанавливает хеш
контента файла или версии файла, или null, если хеш не вычислен. Хеш является
необязательным свойством, которое по умолчанию не заполняется системой.  
(Унаследован от [FileObject](T_Tessa_Files_FileObject.htm))  
[SetInitialStateAsync](M_Tessa_Files_File_SetInitialStateAsync.htm)|
Устанавливает тип файла.  
[SetModifiedAsync](M_Tessa_Files_File_SetModifiedAsync.htm)|  
[SetModifiedByIDAsync](M_Tessa_Files_File_SetModifiedByIDAsync.htm)|  
[SetModifiedByNameAsync](M_Tessa_Files_File_SetModifiedByNameAsync.htm)|  
[SetNameAsync](M_Tessa_Files_FileObject_SetNameAsync.htm)|  Устанавливает имя
файла или версии файла, которое является допустимым именем файла на файловой
системе, но может отличаться от отображаемого имени файла.  
(Унаследован от [FileObject](T_Tessa_Files_FileObject.htm))  
[SetOriginAsync](M_Tessa_Files_File_SetOriginAsync.htm)|  Устанавливает
исходный файл, из которого был скопирован текущий файл, или null, если текущий
файл не был скопирован.  
[SetPreviewContentAsync](M_Tessa_Files_File_SetPreviewContentAsync.htm)|
Устанавливает содержимое файла, отображаемое для предпросмотра. По умолчанию
значение равно [IFileObject.Content], но оно может быть переопределено.
Рекомендуется создавать такой контент из кэша, например:
file.AllocateAdditionalLocalContent("filename.txt").  
[SetSizeAsync](M_Tessa_Files_FileObject_SetSizeAsync.htm)|  Устанавливает
размер файла или версии файла в байтах.  
(Унаследован от [FileObject](T_Tessa_Files_FileObject.htm))  
[SetStateAsync](M_Tessa_Files_File_SetStateAsync.htm)| Устанавливает текущее
состояние файла, равное заданному состоянию.  
[SetStateCoreAsync](M_Tessa_Files_File_SetStateCoreAsync.htm)| Устанавливает
текущее состояние файла, равное заданному состоянию.  
[SetTypeAsync](M_Tessa_Files_File_SetTypeAsync.htm)| Устанавливает тип файла.  
[ToString](M_Tessa_Files_FileObject_ToString.htm)| Возвращает строковое
представление объекта.  
(Унаследован от [FileObject](T_Tessa_Files_FileObject.htm))  
[UpdateInitialStateAsync](M_Tessa_Files_File_UpdateInitialStateAsync.htm)|
Обновляет начальное состояние файла и устанавливаем его как равное заданному
состоянию. Не рекомендуется вызывать этот метод для существующих файлов,
которые уже мог отредактировать пользователь.  
[UpdateInitialStateCoreAsync](M_Tessa_Files_File_UpdateInitialStateCoreAsync.htm)|
Обновляет начальное состояние файла и устанавливаем его как равное заданному
состоянию. Не рекомендуется вызывать этот метод для существующих файлов,
которые уже мог отредактировать пользователь.  
## __События
[PropertyChanged](E_Tessa_Platform_NotificationObject_PropertyChanged.htm)|
Событие, уведомляющее об изменении свойства с определённым именем у модели
представления.  
(Унаследован от [NotificationObject](T_Tessa_Platform_NotificationObject.htm))  
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
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
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
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
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
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
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
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
