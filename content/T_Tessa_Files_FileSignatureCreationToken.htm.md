# FileSignatureCreationToken - класс
Токен, используемый для создания посредством источника файлов
[IFileSource](T_Tessa_Files_IFileSource.htm) объектов с информацией о подписи
для версий файлов.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class FileSignatureCreationToken : IFileSignatureCreationToken
VB __Копировать
     Public Class FileSignatureCreationToken
    	Implements IFileSignatureCreationToken
C++ __Копировать
     public ref class FileSignatureCreationToken : IFileSignatureCreationToken
F# __Копировать
     type FileSignatureCreationToken = 
        class
            interface IFileSignatureCreationToken
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ FileSignatureCreationToken
Implements
    [IFileSignatureCreationToken](T_Tessa_Files_IFileSignatureCreationToken.htm)
##  __Заметки
Наследник класса может иметь дополнительные свойства, специфичные для
источника [IFileSource](T_Tessa_Files_IFileSource.htm).
## __Конструкторы
[FileSignatureCreationToken](M_Tessa_Files_FileSignatureCreationToken__ctor.htm)|
Создаёт экземпляр класса с параметрами по умолчанию.  
---|---  
##  __Свойства
[Comment](P_Tessa_Files_FileSignatureCreationToken_Comment.htm)|  Произвольный
комментарий к подписи, который может использоваться для указания источника
подписи и др.  
---|---  
[Company](P_Tessa_Files_FileSignatureCreationToken_Company.htm)| Название
компании, указанное в файле подписи.  
[Data](P_Tessa_Files_FileSignatureCreationToken_Data.htm)|  Бинарные данные
файла подписи или null, если бинарные данные не заданы.  
[EventType](P_Tessa_Files_FileSignatureCreationToken_EventType.htm)|  Тип
действия, в результате которого подпись была создана. По умолчанию равен
[Tessa.Files.FileSignatureEventType.Other].  
[ID](P_Tessa_Files_FileSignatureCreationToken_ID.htm)|  Идентификатор подписи
или null, если при для каждого объекта подписи создаётся случайный
идентификатор.  
[IssuerName](P_Tessa_Files_FileSignatureCreationToken_IssuerName.htm)|
Издатель сертификата, указанный в файле с подписью.  
[SerialNumber](P_Tessa_Files_FileSignatureCreationToken_SerialNumber.htm)|
Серийный номер сертификата, указанный в файле с подписью.  
[SignatureProfile](P_Tessa_Files_FileSignatureCreationToken_SignatureProfile.htm)|
Профиль ЭЦП, обычно для типа подписи [Tessa.Platform.EDS.SignatureType.CAdES].  
[SignatureType](P_Tessa_Files_FileSignatureCreationToken_SignatureType.htm)|
Тип подписи.  
[Signed](P_Tessa_Files_FileSignatureCreationToken_Signed.htm)|  Дата и время
подписи, указанная в файле подписи, или null, если используется текущая дата.  
[State](P_Tessa_Files_FileSignatureCreationToken_State.htm)|  Состояние
подписи. По умолчанию равно [Tessa.Files.FileSignatureState.NotChecked].  
[SubjectName](P_Tessa_Files_FileSignatureCreationToken_SubjectName.htm)|
Получатель сертификата, указанный в файле подписи.  
[UserID](P_Tessa_Files_FileSignatureCreationToken_UserID.htm)| Идентификатор
пользователя, который зарегистрировал подпись в системе.  
[UserName](P_Tessa_Files_FileSignatureCreationToken_UserName.htm)| Имя
пользователя, который зарегистрировал подпись в системе.  
[ValidationResult](P_Tessa_Files_FileSignatureCreationToken_ValidationResult.htm)|
Сообщения, возникшие при проверке подписи. Значение может быть равно null.  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
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
