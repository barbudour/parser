# LocalFileContent - класс
Контент файла, доступный локально во временной папке пользователя.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class LocalFileContent : FileContent
VB __Копировать
     Public Class LocalFileContent
    	Inherits FileContent
C++ __Копировать
     public ref class LocalFileContent : public FileContent
F# __Копировать
     type LocalFileContent = 
        class
            inherit FileContent
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[NotificationObject](T_Tessa_Platform_NotificationObject.htm) __[FileContent](T_Tessa_Files_FileContent.htm) __ LocalFileContent
##  __Заметки
В классах-наследниках могут быть переопределены или дополнены методы.
## __Конструкторы
[LocalFileContent(String, Func<IFileContent, ValueTask>,
IFileCancellationSource, RegisterFileDelayedDisposalAction,
IFileContentNameReplacer)](M_Tessa_Files_LocalFileContent__ctor.htm)|  Создаёт
контент файла, доступный локально во временной папке пользователя. После
вызова конструктора объекта требуется инициализировать методом
[InitializeAsync(CancellationToken)](M_Tessa_Platform_IAsyncInitializable_InitializeAsync.htm).  
---|---  
[LocalFileContent(String, String, Func<IFileContent, ValueTask>,
IFileCancellationSource, RegisterFileDelayedDisposalAction,
IFileContentNameReplacer)](M_Tessa_Files_LocalFileContent__ctor_1.htm)|
Создаёт контент файла, доступный локально в заданной папке. После вызова
конструктора объекта требуется инициализировать методом
[InitializeAsync(CancellationToken)](M_Tessa_Platform_IAsyncInitializable_InitializeAsync.htm).  
## __Свойства
[Cancellation](P_Tessa_Files_FileContent_Cancellation.htm)|  Объект, который
может использоваться для отмены асинхронных операций с содержимым файла, если
оно поддерживает отмену. На текущий момент это доступно для загрузки
содержимого версии файла.  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
---|---  
[HasCurrentContentData](P_Tessa_Files_FileContent_HasCurrentContentData.htm)|
Признак, который определяет доступность текущего контента для получения,
например, по наличию файла в локальной папке. Свойство
[HasData](P_Tessa_Files_FileContent_HasData.htm) определяет доступность как
текущего контента, так и родительского. Связь родительский-дочерний актуально
для последней версии файла.  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
[HasData](P_Tessa_Files_FileContent_HasData.htm)|  Возвращает признак того,
что контент файла был установлен методом [IFileContent.Set].  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
[IsBoundToFileSource](P_Tessa_Files_LocalFileContent_IsBoundToFileSource.htm)|
Признак того, что контент был создан источником файлов, а не передан снаружи,
поэтому для оптимизации обращения к содержимому можно использовать источник
файлов. Обычно актуально для Remote-контента.  
(Переопределяет
[FileContent.IsBoundToFileSource](P_Tessa_Files_FileContent_IsBoundToFileSource.htm))  
[IsDirty](P_Tessa_Files_FileContent_IsDirty.htm)|  Признак того, что контент
мог быть изменён. Следует установить значение равным true перед открытием
контента на редактирование во внешней программе. Определить точно, был ли
изменён контент, можно, вызвав метод [IFileContent.IsModified].  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
[IsDisposed](P_Tessa_Files_FileContent_IsDisposed.htm)| Признак того, что
контент был освобождён и объект нельзя использовать.  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
[IsLocal](P_Tessa_Files_LocalFileContent_IsLocal.htm)|  Признак того, что
контент является локальным, т.е. к нему можно получить локальный путь
посредством метода [IFileContent.GetLocalFilePath].  
(Переопределяет [FileContent.IsLocal](P_Tessa_Files_FileContent_IsLocal.htm))  
[IsSealed](P_Tessa_Files_FileContent_IsSealed.htm)| Признак того, что объект
был защищён от изменений.  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
[Parent](P_Tessa_Files_FileContent_Parent.htm)|  Родительский контент или
null, если родительский контент отсутствует. Если производится запрос текущего
контента, и он не был установлен, то он сначала локально копируется из
родительского, если тот существует, а затем считывается локально.  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
[RequestInfo](P_Tessa_Files_FileContent_RequestInfo.htm)|  Дополнительная
пользовательская информация, передаваемая в запросы к серверу, которые
относятся к загрузке содержимого файла или версии, которые сохраняются в
текущем объекте. Рекомендуется, чтобы все данные были сериализуемых типов (в
соответствии с типовой BSON-сериализацией в системе). Такие данные могут
перезаписать данные из [IFileObject.RequestInfo].  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
[Size](P_Tessa_Files_FileContent_Size.htm)|  Размер контента файла в байтах
или 0, если контент ещё не был загружен. Проверить, был ли загружен контент,
можно, обратившись к свойству [IFileContent.HasData].  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
[Uri](P_Tessa_Files_LocalFileContent_Uri.htm)|  Ссылка к контенту файла,
который может быть доступен как локально (на диске), так и удалённо (сетевой
ресурс). Значение может быть равно null, если контент недоступен по ссылке.  
(Переопределяет [FileContent.Uri](P_Tessa_Files_FileContent_Uri.htm))  
##  __Методы
[CheckDisposed](M_Tessa_Files_FileContent_CheckDisposed.htm)|  Выбрасывает
исключение [ObjectDisposedException], если ресурсы текущего объекта были
освобождены.  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
---|---  
[CheckSealed](M_Tessa_Files_FileContent_CheckSealed.htm)|  Выбрасывает
исключение [Tessa.Platform.ObjectSealedException], если объект был защищён от
изменений.  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
[DisposeAsync()](M_Tessa_Files_FileContent_DisposeAsync.htm)| Освобождает
ресурсы, занимаемые объектом.  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
[DisposeAsync(Boolean)](M_Tessa_Files_FileContent_DisposeAsync_1.htm)|
Освобождает ресурсы, занимаемые объектом.  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
[EnsureLocalUpdatedAsync](M_Tessa_Files_FileContent_EnsureLocalUpdatedAsync.htm)|
Удостоверяет, что файл будет загружен локально и доступен по пути
[IFileContent.GetLocalFilePath], если файл является локальным
[IFileContent.IsLocal]. Если файл не локальный, то метод не выполняет
действий.  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
[EnterLockAsync](M_Tessa_Files_FileContent_EnterLockAsync.htm)|  Выполняет
вход в блок, в пределах которого нет других обращений к контенту файла.
Вызовите метод в блоке using(await
content.EnterLockAsync().ConfigureAwait(false)).  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetAsync](M_Tessa_Files_FileContent_GetAsync.htm)|  Открывает и возвращает
поток с контентом файла. Если контент файла отсутствует, то вызывает
исключение [System.InvalidOperationException]. Поэтому перед получением
контента можно обратиться к свойству [IFileContent.HasData].  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
[GetCoreAsync](M_Tessa_Files_LocalFileContent_GetCoreAsync.htm)|  Возвращает
поток с содержимым файла. Если файл не был загружен, то может быть выброшено
исключение.  
(Переопределяет
[FileContent.GetCoreAsync(CancellationToken)](M_Tessa_Files_FileContent_GetCoreAsync.htm))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetLocalFilePath](M_Tessa_Files_FileContent_GetLocalFilePath.htm)|
Возвращает локальный путь к контенту файла, если контент доступен локально.
Если контент не доступен локально, то вызывает исключение
[System.InvalidOperationException]. Поэтому перед вызовом метода можно
обратиться к свойству [IFileContent.IsLocal].  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
[GetLocalFilePathCore](M_Tessa_Files_LocalFileContent_GetLocalFilePathCore.htm)|
Возвращает путь к файлу с локальным контентом, даже если он ещё не был
загружен, или null, если контент не представлен локальным файлом.  
(Переопределяет
[FileContent.GetLocalFilePathCore()](M_Tessa_Files_FileContent_GetLocalFilePathCore.htm))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[InitializeAsync](M_Tessa_Files_FileContent_InitializeAsync.htm)| Выполняет
асинхронную инициализацию объекта.  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
[InvalidateAsync](M_Tessa_Files_FileContent_InvalidateAsync.htm)|  Удаляет
локально загруженный контент, переводя его в начальное состояние. Следующий
раз при получении контента он будет заново загружен.  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
[InvalidateCoreAsync](M_Tessa_Files_LocalFileContent_InvalidateCoreAsync.htm)|
Сбрасывает информацию о контенте файла. Например, очищает дату изменения
файла. Если контент не является локальным, то может не выполнять действий.  
(Переопределяет
[FileContent.InvalidateCoreAsync(CancellationToken)](M_Tessa_Files_FileContent_InvalidateCoreAsync.htm))  
[IsModifiedAsync](M_Tessa_Files_FileContent_IsModifiedAsync.htm)|  Возвращает
признак того, что контент файла на диске был изменён с момента его установки
методом [IFileContent.Set]. Для защищённых от изменений объектов метод всегда
возвращает false.  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
[IsModifiedCoreAsync](M_Tessa_Files_LocalFileContent_IsModifiedCoreAsync.htm)|
Возвращает признак того, что локальный контент был изменён. Например, был
изменён файл на диске по дате изменения. При изменении контента может быть
обновлён его размер, а также он может быть, например, помечен как изменённый в
структуре карточки.  
(Переопределяет
[FileContent.IsModifiedCoreAsync(CancellationToken)](M_Tessa_Files_FileContent_IsModifiedCoreAsync.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
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
[PrepareContentLocationCoreAsync](M_Tessa_Files_LocalFileContent_PrepareContentLocationCoreAsync.htm)|
Подготавливает местоположение контента перед его записью или перемещением в
это местоположение. Например, создаёт папку на диске, если контент представлен
файлом на диске.  
(Переопределяет
[FileContent.PrepareContentLocationCoreAsync(CancellationToken)](M_Tessa_Files_FileContent_PrepareContentLocationCoreAsync.htm))  
[RemoveContentSafeCoreAsync](M_Tessa_Files_LocalFileContent_RemoveContentSafeCoreAsync.htm)|
Метод удаляет локальный контент, если он был создан. Если контент не является
локальным, то метод не должен выполнять действий. Метод не должен выбрасывать
исключений, даже критичных.  
(Переопределяет
[FileContent.RemoveContentSafeCoreAsync(CancellationToken)](M_Tessa_Files_FileContent_RemoveContentSafeCoreAsync.htm))  
[RenameAsync](M_Tessa_Files_FileContent_RenameAsync.htm)|  Переименовывает
файл, в который записывается контент. Если файл ещё не существует, то он будет
назван по-другому в момент создания. Метод гарантированно сработает только в
том случае, если контент является локальным, т.е. свойство
[IFileContent.IsLocal] возвращает true.  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
[RenameCoreAsync](M_Tessa_Files_LocalFileContent_RenameCoreAsync.htm)|
Переименовывает имя контента в соответствии с новым именем файла. Если контент
представлен локальным файлом на диске, то метод должен переименовать этот
файл. Если контент не является локальным, то метод может не выполнять
действий.  
(Переопределяет [FileContent.RenameCoreAsync(String,
CancellationToken)](M_Tessa_Files_FileContent_RenameCoreAsync.htm))  
[Seal](M_Tessa_Files_FileContent_Seal.htm)| Защищает объект от изменений.  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
[SetAsync](M_Tessa_Files_FileContent_SetAsync.htm)| Открывает и возвращает
поток, выполняющий перезапись контента файла.  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
[SetCoreAsync](M_Tessa_Files_LocalFileContent_SetCoreAsync.htm)|
Устанавливает содержимое файла. Если контент запрещено изменять, то может быть
выброшено исключение.  
(Переопределяет [FileContent.SetCoreAsync(Stream,
CancellationToken)](M_Tessa_Files_FileContent_SetCoreAsync.htm))  
[SetLocalAsync](M_Tessa_Files_FileContent_SetLocalAsync.htm)| Устанавливает
контент локального файла по заданному пути.  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
[SetLocalCoreAsync](M_Tessa_Files_LocalFileContent_SetLocalCoreAsync.htm)|
Устанавливает локальное содержимое файла, представленное в виде файла на
диске, по заданному методу, который получает в параметре путь к файлу на диске
и может его создать или изменить некоторым способом. Если содержимое файла не
является локальным, то может быть выброшено исключение.  
(Переопределяет [FileContent.SetLocalCoreAsync(Func<String, CancellationToken,
ValueTask>,
CancellationToken)](M_Tessa_Files_FileContent_SetLocalCoreAsync.htm))  
[SetRemoteAsync](M_Tessa_Files_FileContent_SetRemoteAsync.htm)|  Устанавливает
содержимое файла, представленное заданными методами. Если контент запрещено
изменять, то может быть выброшено исключение. Метод доступен как для локальных
файлов, так и для нелокальных (remote), в т.ч. для файлов большого размера.  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
[SetRemoteCoreAsync](M_Tessa_Files_LocalFileContent_SetRemoteCoreAsync.htm)|
Устанавливает содержимое файла, представленное заданными методами. Если
контент запрещено изменять, то может быть выброшено исключение. Метод доступен
как для локальных файлов, так и для нелокальных (remote), в т.ч. для файлов
большого размера.  
(Переопределяет [FileContent.SetRemoteCoreAsync(Func<CancellationToken,
ValueTask<Stream>>, Func<CancellationToken, ValueTask<Int64>>,
CancellationToken)](M_Tessa_Files_FileContent_SetRemoteCoreAsync.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[UpdateLocalContentFromParentCoreAsync](M_Tessa_Files_LocalFileContent_UpdateLocalContentFromParentCoreAsync.htm)|
Обновляет локальный контент на основании контента родительского объекта. При
вызове этого метода гарантируется, что у текущего контента есть родительский
контент, в котором присутствуют загруженные данные. Если контент не локальный,
то метод может не выполнять действий, но не должен выбрасывать исключений.  
(Переопределяет
[FileContent.UpdateLocalContentFromParentCoreAsync(CancellationToken)](M_Tessa_Files_FileContent_UpdateLocalContentFromParentCoreAsync.htm))  
[UpdateModifiedCoreAsync](M_Tessa_Files_LocalFileContent_UpdateModifiedCoreAsync.htm)|
Обновляет информацию, на основании которой можно определить, изменялся ли
контент. Например, сохраняет время изменения файла, чтобы его можно было
сравнить со временем изменения в любой другой момент.  
(Переопределяет
[FileContent.UpdateModifiedCoreAsync(CancellationToken)](M_Tessa_Files_FileContent_UpdateModifiedCoreAsync.htm))  
[UpdateSizeAsync](M_Tessa_Files_FileContent_UpdateSizeAsync.htm)|  Обновляет
свойство с размером контента [IFileContent.Size] для загруженных файлов.  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
[UpdateSizeCoreAsync](M_Tessa_Files_LocalFileContent_UpdateSizeCoreAsync.htm)|
Обновляет размер локального контента. Возвращает true, если размер был
обновлён.  
(Переопределяет
[FileContent.UpdateSizeCoreAsync(CancellationToken)](M_Tessa_Files_FileContent_UpdateSizeCoreAsync.htm))  
##  __События
[PropertyChanged](E_Tessa_Platform_NotificationObject_PropertyChanged.htm)|
Событие, уведомляющее об изменении свойства с определённым именем у модели
представления.  
(Унаследован от [NotificationObject](T_Tessa_Platform_NotificationObject.htm))  
---|---  
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
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
