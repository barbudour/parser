# IFileSignatureCreationToken - интерфейс
Токен, используемый для создания посредством источника файлов
[IFileSource](T_Tessa_Files_IFileSource.htm) объектов с информацией о подписи
для версий файлов.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IFileSignatureCreationToken
VB __Копировать
     Public Interface IFileSignatureCreationToken
C++ __Копировать
     public interface class IFileSignatureCreationToken
F# __Копировать
     type IFileSignatureCreationToken = interface end
##  __Свойства
[Comment](P_Tessa_Files_IFileSignatureCreationToken_Comment.htm)|
Произвольный комментарий к подписи, который может использоваться для указания
источника подписи и др.  
---|---  
[Company](P_Tessa_Files_IFileSignatureCreationToken_Company.htm)| Название
компании, указанное в файле подписи.  
[Data](P_Tessa_Files_IFileSignatureCreationToken_Data.htm)|  Бинарные данные
файла подписи или null, если бинарные данные не заданы.  
[EventType](P_Tessa_Files_IFileSignatureCreationToken_EventType.htm)|  Тип
действия, в результате которого подпись была создана. По умолчанию равен
[Tessa.Files.FileSignatureEventType.Other].  
[ID](P_Tessa_Files_IFileSignatureCreationToken_ID.htm)|  Идентификатор подписи
или null, если при для каждого объекта подписи создаётся случайный
идентификатор.  
[IssuerName](P_Tessa_Files_IFileSignatureCreationToken_IssuerName.htm)|
Издатель сертификата, указанный в файле с подписью.  
[SerialNumber](P_Tessa_Files_IFileSignatureCreationToken_SerialNumber.htm)|
Серийный номер сертификата, указанный в файле с подписью.  
[SignatureProfile](P_Tessa_Files_IFileSignatureCreationToken_SignatureProfile.htm)|
Профиль ЭЦП, обычно для типа подписи [Tessa.Platform.EDS.SignatureType.CAdES].  
[SignatureType](P_Tessa_Files_IFileSignatureCreationToken_SignatureType.htm)|
Тип подписи.  
[Signed](P_Tessa_Files_IFileSignatureCreationToken_Signed.htm)|  Дата и время
подписи, указанная в файле подписи, или null, если используется текущая дата.  
[State](P_Tessa_Files_IFileSignatureCreationToken_State.htm)|  Состояние
подписи. По умолчанию равно [Tessa.Files.FileSignatureState.NotChecked].  
[SubjectName](P_Tessa_Files_IFileSignatureCreationToken_SubjectName.htm)|
Получатель сертификата, указанный в файле подписи.  
[UserID](P_Tessa_Files_IFileSignatureCreationToken_UserID.htm)| Идентификатор
пользователя, который зарегистрировал подпись в системе.  
[UserName](P_Tessa_Files_IFileSignatureCreationToken_UserName.htm)| Имя
пользователя, который зарегистрировал подпись в системе.  
[ValidationResult](P_Tessa_Files_IFileSignatureCreationToken_ValidationResult.htm)|
Сообщения, возникшие при проверке подписи. Значение может быть равно null.  
## __См. также
#### Ссылки
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
