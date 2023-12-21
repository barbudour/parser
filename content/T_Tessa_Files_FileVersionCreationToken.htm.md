# FileVersionCreationToken - класс
Токен, используемый для создания версий файлов посредством источника файлов
[IFileSource](T_Tessa_Files_IFileSource.htm).
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class FileVersionCreationToken : IFileVersionCreationToken, 
    	ICloneable
VB __Копировать
     Public Class FileVersionCreationToken
    	Implements IFileVersionCreationToken, ICloneable
C++ __Копировать
     public ref class FileVersionCreationToken : IFileVersionCreationToken, 
    	ICloneable
F# __Копировать
     type FileVersionCreationToken = 
        class
            interface IFileVersionCreationToken
            interface ICloneable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ FileVersionCreationToken
Implements
    [ICloneable](https://learn.microsoft.com/dotnet/api/system.icloneable), [IFileVersionCreationToken](T_Tessa_Files_IFileVersionCreationToken.htm)
##  __Заметки
Наследник класса может иметь дополнительные свойства, специфичные для
источника [IFileSource](T_Tessa_Files_IFileSource.htm).
## __Конструкторы
[FileVersionCreationToken](M_Tessa_Files_FileVersionCreationToken__ctor.htm)|
Создаёт экземпляр класса с параметрами по умолчанию.  
---|---  
##  __Свойства
[ContentSource](P_Tessa_Files_FileVersionCreationToken_ContentSource.htm)|
Местоположение контента файла.  
---|---  
[Created](P_Tessa_Files_FileVersionCreationToken_Created.htm)| Дата создания
версии.  
[CreatedByID](P_Tessa_Files_FileVersionCreationToken_CreatedByID.htm)|
Идентификатор пользователя, который создал версию.  
[CreatedByName](P_Tessa_Files_FileVersionCreationToken_CreatedByName.htm)| Имя
пользователя, который создал версию.  
[ErrorInfo](P_Tessa_Files_FileVersionCreationToken_ErrorInfo.htm)|  Информация
по ошибке, возникшей при сохранении версии файла, или null, если ошибок не
было.  
[Hash](P_Tessa_Files_FileVersionCreationToken_Hash.htm)|  Хеш контента версии
файла или null, если хеш не вычислен. Хеш является необязательным свойством,
которое по умолчанию не заполняется системой.  
[ID](P_Tessa_Files_FileVersionCreationToken_ID.htm)|  Идентификатор версии
файла или null, если при создании версии ей присваивается новый идентификатор.  
[LinkID](P_Tessa_Files_FileVersionCreationToken_LinkID.htm)|  Внешний
идентификатор версии файла или null, если такой идентификатор не задан. Может
использоваться в расширениях для связи с содержимым во внешнем местоположении.  
[Name](P_Tessa_Files_FileVersionCreationToken_Name.htm)|  Имя файла
[IFileObject.Name] на момент создания версии. Если указано null или пустая
строка, то в момент создания версии будет использовано имя файла.  
[Number](P_Tessa_Files_FileVersionCreationToken_Number.htm)|  Порядковый номер
версии файла, отсчитываемый от 1. По умолчанию устанавливается номер, равный
1.  
[Options](P_Tessa_Files_FileVersionCreationToken_Options.htm)| Настройки
версии файла. Сериализуются в карточке в форме JSON.  
[RequestInfo](P_Tessa_Files_FileVersionCreationToken_RequestInfo.htm)|
Дополнительная пользовательская информация, передаваемая в запросы к серверу,
которые относятся к загрузке содержимого версии или к загрузке списка её
подписей.  
[Size](P_Tessa_Files_FileVersionCreationToken_Size.htm)|  Начальный размер
создаваемой версии файла в байтах. Задавать значение свойства имеет смысл для
версий, контент которых может быть установлен позднее, чем запрошен размер.
Значение по умолчанию [FileContent.UnknownSize] определяет, что размер
неизвестен.  
[State](P_Tessa_Files_FileVersionCreationToken_State.htm)|  Состояние версии
файла. По умолчанию устанавливается состояние
[Tessa.Files.FileVersionState.Created].  
[Tags](P_Tessa_Files_FileVersionCreationToken_Tags.htm)| Список тегов,
связанных с версией файла. Сериализуются в карточке в форме строки.  
##  __Методы
[Clone](M_Tessa_Files_FileVersionCreationToken_Clone.htm)| Создаёт полную
копию объекта с информацией по токену. Дочерние объекты также копируются.  
---|---  
[CloneCore](M_Tessa_Files_FileVersionCreationToken_CloneCore.htm)| Создаёт
полную копию объекта с информацией по токену. Дочерние объекты также
копируются.  
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
[Set(IFileVersion)](M_Tessa_Files_FileVersionCreationToken_Set.htm)|
Устанавливает свойства текущего объекта по свойствам заданной версии файла.  
[Set(IFileVersionCreationToken)](M_Tessa_Files_FileVersionCreationToken_Set_1.htm)|
Устанавливает свойства текущего объекта по свойствам заданного токена.  
[SetCore(IFileVersion)](M_Tessa_Files_FileVersionCreationToken_SetCore.htm)|
Устанавливает свойства текущего объекта по свойствам заданной версии файла.  
[SetCore(IFileVersionCreationToken)](M_Tessa_Files_FileVersionCreationToken_SetCore_1.htm)|
Устанавливает свойства текущего объекта по свойствам заданного токена.  
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
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
