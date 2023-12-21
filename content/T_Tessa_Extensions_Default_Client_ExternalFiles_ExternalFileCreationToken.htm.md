# ExternalFileCreationToken - класс
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Client.ExternalFiles](N_Tessa_Extensions_Default_Client_ExternalFiles.htm)  
 **Сборка:** Tessa.Extensions.Default.Client (в
Tessa.Extensions.Default.Client.dll) Версия: 3.6.0.17
C# __Копировать
     public class ExternalFileCreationToken : FileCreationToken
VB __Копировать
     Public Class ExternalFileCreationToken
    	Inherits FileCreationToken
C++ __Копировать
     public ref class ExternalFileCreationToken : public FileCreationToken
F# __Копировать
     type ExternalFileCreationToken = 
        class
            inherit FileCreationToken
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[FileCreationToken](T_Tessa_Files_FileCreationToken.htm) __ ExternalFileCreationToken
##  __Конструкторы
[ExternalFileCreationToken](M_Tessa_Extensions_Default_Client_ExternalFiles_ExternalFileCreationToken__ctor.htm)|
Инициализирует новый экземпляр класса ExternalFileCreationToken  
---|---  
##  __Свойства
[Category](P_Tessa_Files_FileCreationToken_Category.htm)|  Категория файла или
null, если файл не имеет категории.  
(Унаследован от [FileCreationToken](T_Tessa_Files_FileCreationToken.htm))  
---|---  
[Description](P_Tessa_Extensions_Default_Client_ExternalFiles_ExternalFileCreationToken_Description.htm)|  
[Hash](P_Tessa_Files_FileCreationToken_Hash.htm)|  Хеш контента файла или
null, если хеш не вычислен. Хеш является необязательным свойством, которое по
умолчанию не заполняется системой.  
(Унаследован от [FileCreationToken](T_Tessa_Files_FileCreationToken.htm))  
[ID](P_Tessa_Files_FileCreationToken_ID.htm)|  Идентификатор файла или null,
если создаётся случайный идентификатор.  
(Унаследован от [FileCreationToken](T_Tessa_Files_FileCreationToken.htm))  
[IsLocal](P_Tessa_Files_FileCreationToken_IsLocal.htm)|  Признак того, что
файл был загружен локально и отсутствует во внешней подсистеме. Значение
используется при просмотре превью или при открытии файла, только что
добавленного в элемент управления и не существующего на сервере. По умолчанию
значение равно true.  
(Унаследован от [FileCreationToken](T_Tessa_Files_FileCreationToken.htm))  
[LastVersionTags](P_Tessa_Files_FileCreationToken_LastVersionTags.htm)|
Список тегов, связанных с последней существующей версией файла. Актуально для
загружаемых или копируемых файлов. В объект [Tessa.Files.IFile] такой список
не копируется.  
(Унаследован от [FileCreationToken](T_Tessa_Files_FileCreationToken.htm))  
[Modified](P_Tessa_Files_FileCreationToken_Modified.htm)|  Дата и время
последнего изменения файла.  
(Унаследован от [FileCreationToken](T_Tessa_Files_FileCreationToken.htm))  
[ModifiedByID](P_Tessa_Files_FileCreationToken_ModifiedByID.htm)|
Идентификатор пользователя изменившего файл.  
(Унаследован от [FileCreationToken](T_Tessa_Files_FileCreationToken.htm))  
[ModifiedByName](P_Tessa_Files_FileCreationToken_ModifiedByName.htm)|  Имя
пользователя изменившего файл.  
(Унаследован от [FileCreationToken](T_Tessa_Files_FileCreationToken.htm))  
[Name](P_Tessa_Files_FileCreationToken_Name.htm)| Имя файла, которое является
допустимым именем файла на файловой системе.  
(Унаследован от [FileCreationToken](T_Tessa_Files_FileCreationToken.htm))  
[NewVersionTags](P_Tessa_Files_FileCreationToken_NewVersionTags.htm)|  Список
тегов, связанных с добавляемой версией файла, т.е. при изменении содержимого
файла в случае замены, редактирования и др. Сериализуются в карточке в форме
строки.  
(Унаследован от [FileCreationToken](T_Tessa_Files_FileCreationToken.htm))  
[Options](P_Tessa_Files_FileCreationToken_Options.htm)| Настройки файла.
Сериализуются в карточке в форме JSON.  
(Унаследован от [FileCreationToken](T_Tessa_Files_FileCreationToken.htm))  
[Permissions](P_Tessa_Files_FileCreationToken_Permissions.htm)| Разрешения на
действия с файлом.  
(Унаследован от [FileCreationToken](T_Tessa_Files_FileCreationToken.htm))  
[RequestInfo](P_Tessa_Files_FileCreationToken_RequestInfo.htm)|
Дополнительная пользовательская информация, передаваемая в запросы к серверу,
которые относятся к загрузке содержимого файла и его версий, к загрузке списка
версий этого файла или к загрузке списка подписей.  
(Унаследован от [FileCreationToken](T_Tessa_Files_FileCreationToken.htm))  
[Size](P_Tessa_Files_FileCreationToken_Size.htm)|  Начальный размер
создаваемого файла в байтах. Задавать значение свойства имеет смысл для
файлов, контент которых может быть установлен позднее, чем запрошен размер.
Значение по умолчанию [FileContent.UnknownSize] определяет, что размер
неизвестен.  
(Унаследован от [FileCreationToken](T_Tessa_Files_FileCreationToken.htm))  
[Type](P_Tessa_Files_FileCreationToken_Type.htm)| Тип файла.  
(Унаследован от [FileCreationToken](T_Tessa_Files_FileCreationToken.htm))  
##  __Методы
[Clone](M_Tessa_Files_FileCreationToken_Clone.htm)| Создаёт полную копию
объекта с информацией по токену. Дочерние объекты также копируются.  
(Унаследован от [FileCreationToken](T_Tessa_Files_FileCreationToken.htm))  
---|---  
[CloneCore](M_Tessa_Files_FileCreationToken_CloneCore.htm)| Создаёт полную
копию объекта с информацией по токену. Дочерние объекты также копируются.  
(Унаследован от [FileCreationToken](T_Tessa_Files_FileCreationToken.htm))  
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
[Set(IFile)](M_Tessa_Files_FileCreationToken_Set.htm)| Устанавливает свойства
текущего объекта по свойствам заданного файла.  
(Унаследован от [FileCreationToken](T_Tessa_Files_FileCreationToken.htm))  
[Set(IFileCreationToken)](M_Tessa_Files_FileCreationToken_Set_1.htm)|
Устанавливает свойства текущего объекта по свойствам заданного токена.  
(Унаследован от [FileCreationToken](T_Tessa_Files_FileCreationToken.htm))  
[SetCore(IFile)](M_Tessa_Extensions_Default_Client_ExternalFiles_ExternalFileCreationToken_SetCore.htm)|  
(Переопределяет
[FileCreationToken.SetCore(IFile)](M_Tessa_Files_FileCreationToken_SetCore.htm))  
[SetCore(IFileCreationToken)](M_Tessa_Extensions_Default_Client_ExternalFiles_ExternalFileCreationToken_SetCore_1.htm)|  
(Переопределяет
[FileCreationToken.SetCore(IFileCreationToken)](M_Tessa_Files_FileCreationToken_SetCore_1.htm))  
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
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Extensions.Default.Client.ExternalFiles - пространство
имён](N_Tessa_Extensions_Default_Client_ExternalFiles.htm)
