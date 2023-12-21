# IFileSignature - интерфейс
Информация о подписи для версии файла.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IFileSignature : IFileEntity, 
    	IEquatable<IFileEntity>, INotifyPropertyChanged, IEquatable<IFileSignature>
VB __Копировать
     Public Interface IFileSignature
    	Inherits IFileEntity, IEquatable(Of IFileEntity), INotifyPropertyChanged, 
    	IEquatable(Of IFileSignature)
C++ __Копировать
     public interface class IFileSignature : IFileEntity, 
    	IEquatable<IFileEntity^>, INotifyPropertyChanged, IEquatable<IFileSignature^>
F# __Копировать
     type IFileSignature = 
        interface
            interface IFileEntity
            interface IEquatable<IFileEntity>
            interface INotifyPropertyChanged
            interface IEquatable<IFileSignature>
        end
Implements
    [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<[IFileEntity](T_Tessa_Files_IFileEntity.htm)>, [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<IFileSignature>, [IFileEntity](T_Tessa_Files_IFileEntity.htm)
##  __Свойства
[Comment](P_Tessa_Files_IFileSignature_Comment.htm)|  Произвольный комментарий
к подписи, который может использоваться для указания источника подписи и др.  
---|---  
[Company](P_Tessa_Files_IFileSignature_Company.htm)| Название компании,
указанное в файле подписи.  
[Data](P_Tessa_Files_IFileSignature_Data.htm)| Объект, содержащий информацию
по бинарным данным файла подписи.  
[EventType](P_Tessa_Files_IFileSignature_EventType.htm)| Тип действия, в
результате которого подпись была создана.  
[ExtendedValidationInfos](P_Tessa_Files_IFileSignature_ExtendedValidationInfos.htm)|
Дополнительная информация по проверкам подписей.  
[ID](P_Tessa_Files_IFileEntity_ID.htm)| Идентификатор объекта.  
(Унаследован от [IFileEntity](T_Tessa_Files_IFileEntity.htm))  
[IssuerName](P_Tessa_Files_IFileSignature_IssuerName.htm)| Издатель
сертификата, указанный в файле с подписью.  
[SerialNumber](P_Tessa_Files_IFileSignature_SerialNumber.htm)| Серийный номер
сертификата, указанный в файле с подписью.  
[SignatureProfile](P_Tessa_Files_IFileSignature_SignatureProfile.htm)| Профиль
ЭЦП, обычно для типа подписи [Tessa.Platform.EDS.SignatureType.CAdES].  
[SignatureType](P_Tessa_Files_IFileSignature_SignatureType.htm)| Тип подписи.  
[Signed](P_Tessa_Files_IFileSignature_Signed.htm)| Дата и время подписи,
указанная в файле подписи.  
[Source](P_Tessa_Files_IFileEntity_Source.htm)|  Объект, обеспечивающий
взаимодействие текущего объекта с подсистемой, в которой он был создан,
например, с карточкой.  
(Унаследован от [IFileEntity](T_Tessa_Files_IFileEntity.htm))  
[State](P_Tessa_Files_IFileSignature_State.htm)| Состояние подписи.  
[SubjectName](P_Tessa_Files_IFileSignature_SubjectName.htm)| Получатель
сертификата, указанный в файле подписи.  
[UserID](P_Tessa_Files_IFileSignature_UserID.htm)| Идентификатор пользователя,
который зарегистрировал подпись в системе.  
[UserName](P_Tessa_Files_IFileSignature_UserName.htm)| Имя пользователя,
который зарегистрировал подпись в системе.  
[ValidationResult](P_Tessa_Files_IFileSignature_ValidationResult.htm)|
Сообщения, возникшие при проверке подписи. Значение не равно null.  
[Version](P_Tessa_Files_IFileSignature_Version.htm)| Версия файла, к которой
относится подпись.  
##  __Методы
[Equals(T)](https://learn.microsoft.com/dotnet/api/system.iequatable-1.equals#system-
iequatable-1-equals\(-0\))| Indicates whether the current object is equal to
another object of the same type.  
(Унаследован от
[IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<[IFileEntity](T_Tessa_Files_IFileEntity.htm)>)  
---|---  
[Equals(T)](https://learn.microsoft.com/dotnet/api/system.iequatable-1.equals#system-
iequatable-1-equals\(-0\))|  
(Унаследован от
[IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<IFileSignature>)  
[SetDataAsync](M_Tessa_Files_IFileSignature_SetDataAsync.htm)| Устанавливает
объект, содержащий информацию по бинарным данным файла подписи.  
[SetStateAsync](M_Tessa_Files_IFileSignature_SetStateAsync.htm)| Устанавливает
состояние подписи.  
[SetValidationResultAsync](M_Tessa_Files_IFileSignature_SetValidationResultAsync.htm)|
Устанавливает сообщения ошибок и предупреждения, возникшие при проверке
подписи, или null, если сообщений не возникло.  
## __События
[PropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged.propertychanged)|
Occurs when a property value changes.  
(Унаследован от
[INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged))  
---|---  
##  __Методы расширения
[NotifyAsync](M_Tessa_Files_FileExtensions_NotifyAsync_1.htm)|  Уведомляет
источник заданной подписи [IFileSource](T_Tessa_Files_IFileSource.htm) о
возникшем событии
[FileSignatureNotificationType](T_Tessa_Files_FileSignatureNotificationType.htm).
Используйте при изменении свойств подписи вручную, чтобы эти свойства были
сохранены в пакете карточки (если подпись связана с карточкой).  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
