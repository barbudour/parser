# ExternalFile - класс
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Client.ExternalFiles](N_Tessa_Extensions_Default_Client_ExternalFiles.htm)  
 **Сборка:** Tessa.Extensions.Default.Client (в
Tessa.Extensions.Default.Client.dll) Версия: 3.6.0.17
C# __Копировать
     public class ExternalFile : File
VB __Копировать
     Public Class ExternalFile
    	Inherits File
C++ __Копировать
     public ref class ExternalFile : public File
F# __Копировать
     type ExternalFile = 
        class
            inherit File
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[NotificationObject](T_Tessa_Platform_NotificationObject.htm) __[FileEntity](T_Tessa_Files_FileEntity.htm) __[FileObject](T_Tessa_Files_FileObject.htm) __[File](T_Tessa_Files_File.htm) __ ExternalFile
##  __Конструкторы
[ExternalFile](M_Tessa_Extensions_Default_Client_ExternalFiles_ExternalFile__ctor.htm)|
Инициализирует новый экземпляр класса ExternalFile  
---|---  
##  __Свойства
[Cancellation](P_Tessa_Files_FileObject_Cancellation.htm)|  Объект, который
может использоваться для отмены асинхронных операций с файлом или версией
файла, которые поддерживают отмену. На текущий момент это доступно для
загрузки содержимого версии файла.  
(Унаследован от [FileObject](T_Tessa_Files_FileObject.htm))  
---|---  
[Category](P_Tessa_Files_File_Category.htm)|  Категория файла или null, если
файл не имеет категории.  
(Унаследован от [File](T_Tessa_Files_File.htm))  
[Content](P_Tessa_Files_FileObject_Content.htm)|  Контент файла или версии
файла. Контент файла обычно равен контенту его последней версии, но имя файла
на файловой системе может отличаться.  
(Унаследован от [FileObject](T_Tessa_Files_FileObject.htm))  
[ContentState](P_Tessa_Files_FileObject_ContentState.htm)|  Состояние загрузки
контента файла или версии файла в кэш для последующего отображения
пользователю.  
(Унаследован от [FileObject](T_Tessa_Files_FileObject.htm))  
[Description](P_Tessa_Extensions_Default_Client_ExternalFiles_ExternalFile_Description.htm)|  
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
(Унаследован от [File](T_Tessa_Files_File.htm))  
[IsLocal](P_Tessa_Files_File_IsLocal.htm)|  Признак того, что файл был
загружен локально и отсутствует во внешней подсистеме. Значение используется
при просмотре превью или при открытии файла, только что добавленного в элемент
управления и не существующего на сервере.  
(Унаследован от [File](T_Tessa_Files_File.htm))  
[Modified](P_Tessa_Files_File_Modified.htm)|  Дата и время последнего
изменения файла.  
(Унаследован от [File](T_Tessa_Files_File.htm))  
[ModifiedByID](P_Tessa_Files_File_ModifiedByID.htm)|  Идентификатор
пользователя изменившего файл.  
(Унаследован от [File](T_Tessa_Files_File.htm))  
[ModifiedByName](P_Tessa_Files_File_ModifiedByName.htm)|  Имя пользователя
изменившего файл.  
(Унаследован от [File](T_Tessa_Files_File.htm))  
[Name](P_Tessa_Files_FileObject_Name.htm)|  Имя файла или версии файла,
которое является допустимым именем файла на файловой системе, но может
отличаться от отображаемого имени файла.  
(Унаследован от [FileObject](T_Tessa_Files_FileObject.htm))  
[NewVersionTags](P_Tessa_Files_File_NewVersionTags.htm)|  Список тегов,
связанных с добавляемой версией файла, т.е. при изменении содержимого файла в
случае замены, редактирования и др. Сериализуются в карточке в форме строки.  
(Унаследован от [File](T_Tessa_Files_File.htm))  
[Options](P_Tessa_Files_FileObject_Options.htm)| Настройки файла или версии
файла. Сериализуются в карточке в форме JSON.  
(Унаследован от [FileObject](T_Tessa_Files_FileObject.htm))  
[Origin](P_Tessa_Files_File_Origin.htm)|  Исходный файл, из которого был
скопирован текущий файл, или null, если текущий файл не был скопирован.  
(Унаследован от [File](T_Tessa_Files_File.htm))  
[Permissions](P_Tessa_Files_File_Permissions.htm)| Разрешения на действия с
файлом.  
(Унаследован от [File](T_Tessa_Files_File.htm))  
[PreviewContent](P_Tessa_Files_File_PreviewContent.htm)|  Содержимое файла,
отображаемое для предпросмотра. По умолчанию значение равно
[IFileObject.Content], но оно может быть переопределено. Рекомендуется
создавать такой контент из кэша, например:
file.AllocateAdditionalLocalContent("filename.txt"). Возвращаемое значение не
равно null.  
(Унаследован от [File](T_Tessa_Files_File.htm))  
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
(Унаследован от [File](T_Tessa_Files_File.htm))  
[Versions](P_Tessa_Files_File_Versions.htm)|  Список версий файла. Коллекция
может быть пустой, если информация по версиям ещё не была запрошена.  
(Унаследован от [File](T_Tessa_Files_File.htm))  
##  __Методы
[Equals(IFile)](M_Tessa_Files_File_Equals.htm)| Сравнивает текущий объект с
заданным.  
(Унаследован от [File](T_Tessa_Files_File.htm))  
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
(Унаследован от [File](T_Tessa_Files_File.htm))  
[GetStateCore](M_Tessa_Files_File_GetStateCore.htm)| Возвращает текущее
состояние файла.  
(Унаследован от [File](T_Tessa_Files_File.htm))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[HasChanges](M_Tessa_Files_File_HasChanges.htm)| Возвращает признак того, что
заданное состояние файла отличается от его текущего состояния.  
(Унаследован от [File](T_Tessa_Files_File.htm))  
[HasChangesCore](M_Tessa_Files_File_HasChangesCore.htm)| Возвращает признак
того, что заданное состояние файла отличается от его текущего состояния.  
(Унаследован от [File](T_Tessa_Files_File.htm))  
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
(Унаследован от [File](T_Tessa_Files_File.htm))  
[SetContentStateAsync](M_Tessa_Files_FileObject_SetContentStateAsync.htm)|
Устанавливает состояние загрузки контента файла или версии файла в кэш для
последующего отображения пользователю.  
(Унаследован от [FileObject](T_Tessa_Files_FileObject.htm))  
[SetDescriptionAsync](M_Tessa_Extensions_Default_Client_ExternalFiles_ExternalFile_SetDescriptionAsync.htm)|  
[SetHashAsync](M_Tessa_Files_FileObject_SetHashAsync.htm)|  Устанавливает хеш
контента файла или версии файла, или null, если хеш не вычислен. Хеш является
необязательным свойством, которое по умолчанию не заполняется системой.  
(Унаследован от [FileObject](T_Tessa_Files_FileObject.htm))  
[SetInitialStateAsync](M_Tessa_Files_File_SetInitialStateAsync.htm)|
Устанавливает тип файла.  
(Унаследован от [File](T_Tessa_Files_File.htm))  
[SetModifiedAsync](M_Tessa_Files_File_SetModifiedAsync.htm)|  
(Унаследован от [File](T_Tessa_Files_File.htm))  
[SetModifiedByIDAsync](M_Tessa_Files_File_SetModifiedByIDAsync.htm)|  
(Унаследован от [File](T_Tessa_Files_File.htm))  
[SetModifiedByNameAsync](M_Tessa_Files_File_SetModifiedByNameAsync.htm)|  
(Унаследован от [File](T_Tessa_Files_File.htm))  
[SetNameAsync](M_Tessa_Files_FileObject_SetNameAsync.htm)|  Устанавливает имя
файла или версии файла, которое является допустимым именем файла на файловой
системе, но может отличаться от отображаемого имени файла.  
(Унаследован от [FileObject](T_Tessa_Files_FileObject.htm))  
[SetOriginAsync](M_Tessa_Files_File_SetOriginAsync.htm)|  Устанавливает
исходный файл, из которого был скопирован текущий файл, или null, если текущий
файл не был скопирован.  
(Унаследован от [File](T_Tessa_Files_File.htm))  
[SetPreviewContentAsync](M_Tessa_Files_File_SetPreviewContentAsync.htm)|
Устанавливает содержимое файла, отображаемое для предпросмотра. По умолчанию
значение равно [IFileObject.Content], но оно может быть переопределено.
Рекомендуется создавать такой контент из кэша, например:
file.AllocateAdditionalLocalContent("filename.txt").  
(Унаследован от [File](T_Tessa_Files_File.htm))  
[SetSizeAsync](M_Tessa_Files_FileObject_SetSizeAsync.htm)|  Устанавливает
размер файла или версии файла в байтах.  
(Унаследован от [FileObject](T_Tessa_Files_FileObject.htm))  
[SetStateAsync](M_Tessa_Files_File_SetStateAsync.htm)| Устанавливает текущее
состояние файла, равное заданному состоянию.  
(Унаследован от [File](T_Tessa_Files_File.htm))  
[SetStateCoreAsync](M_Tessa_Files_File_SetStateCoreAsync.htm)| Устанавливает
текущее состояние файла, равное заданному состоянию.  
(Унаследован от [File](T_Tessa_Files_File.htm))  
[SetTypeAsync](M_Tessa_Files_File_SetTypeAsync.htm)| Устанавливает тип файла.  
(Унаследован от [File](T_Tessa_Files_File.htm))  
[ToString](M_Tessa_Files_FileObject_ToString.htm)| Возвращает строковое
представление объекта.  
(Унаследован от [FileObject](T_Tessa_Files_FileObject.htm))  
[UpdateInitialStateAsync](M_Tessa_Files_File_UpdateInitialStateAsync.htm)|
Обновляет начальное состояние файла и устанавливаем его как равное заданному
состоянию. Не рекомендуется вызывать этот метод для существующих файлов,
которые уже мог отредактировать пользователь.  
(Унаследован от [File](T_Tessa_Files_File.htm))  
[UpdateInitialStateCoreAsync](M_Tessa_Files_File_UpdateInitialStateCoreAsync.htm)|
Обновляет начальное состояние файла и устанавливаем его как равное заданному
состоянию. Не рекомендуется вызывать этот метод для существующих файлов,
которые уже мог отредактировать пользователь.  
(Унаследован от [File](T_Tessa_Files_File.htm))  
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
[Tessa.Extensions.Default.Client.ExternalFiles - пространство
имён](N_Tessa_Extensions_Default_Client_ExternalFiles.htm)
