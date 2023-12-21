# FileSignature - класс
Информация о подписи для версии файла.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class FileSignature : FileEntity, 
    	IFileSignature, IFileEntity, IEquatable<IFileEntity>, INotifyPropertyChanged, 
    	IEquatable<IFileSignature>
VB __Копировать
     Public Class FileSignature
    	Inherits FileEntity
    	Implements IFileSignature, IFileEntity, IEquatable(Of IFileEntity), 
    	INotifyPropertyChanged, IEquatable(Of IFileSignature)
C++ __Копировать
     public ref class FileSignature : public FileEntity, 
    	IFileSignature, IFileEntity, IEquatable<IFileEntity^>, INotifyPropertyChanged, 
    	IEquatable<IFileSignature^>
F# __Копировать
     type FileSignature = 
        class
            inherit FileEntity
            interface IFileSignature
            interface IFileEntity
            interface IEquatable<IFileEntity>
            interface INotifyPropertyChanged
            interface IEquatable<IFileSignature>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[NotificationObject](T_Tessa_Platform_NotificationObject.htm) __[FileEntity](T_Tessa_Files_FileEntity.htm) __ FileSignature
Implements
    [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<[IFileEntity](T_Tessa_Files_IFileEntity.htm)>, [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<[IFileSignature](T_Tessa_Files_IFileSignature.htm)>, [IFileEntity](T_Tessa_Files_IFileEntity.htm), [IFileSignature](T_Tessa_Files_IFileSignature.htm)
##  __Заметки
Наследники класса могут содержать дополнительные свойства, связанные с внешней
подсистемой, в которой располагается подписанная версия.
## __Конструкторы
[FileSignature](M_Tessa_Files_FileSignature__ctor.htm)|  Создаёт экземпляр
класса с указанием значений его свойств.  
---|---  
## __Свойства
[Comment](P_Tessa_Files_FileSignature_Comment.htm)|  Произвольный комментарий
к подписи, который может использоваться для указания источника подписи и др.  
---|---  
[Company](P_Tessa_Files_FileSignature_Company.htm)| Название компании,
указанное в файле подписи.  
[Data](P_Tessa_Files_FileSignature_Data.htm)| Объект, содержащий информацию по
бинарным данным файла подписи.  
[EventType](P_Tessa_Files_FileSignature_EventType.htm)| Тип действия, в
результате которого подпись была создана.  
[ExtendedValidationInfos](P_Tessa_Files_FileSignature_ExtendedValidationInfos.htm)|
Дополнительная информация по проверкам подписей.  
[ID](P_Tessa_Files_FileEntity_ID.htm)| Идентификатор объекта.  
(Унаследован от [FileEntity](T_Tessa_Files_FileEntity.htm))  
[IssuerName](P_Tessa_Files_FileSignature_IssuerName.htm)| Издатель
сертификата, указанный в файле с подписью.  
[SerialNumber](P_Tessa_Files_FileSignature_SerialNumber.htm)| Серийный номер
сертификата, указанный в файле с подписью.  
[SignatureProfile](P_Tessa_Files_FileSignature_SignatureProfile.htm)| Профиль
ЭЦП, обычно для типа подписи [Tessa.Platform.EDS.SignatureType.CAdES].  
[SignatureType](P_Tessa_Files_FileSignature_SignatureType.htm)| Тип подписи.  
[Signed](P_Tessa_Files_FileSignature_Signed.htm)| Дата и время подписи,
указанная в файле подписи.  
[Source](P_Tessa_Files_FileEntity_Source.htm)|  Объект, обеспечивающий
взаимодействие текущего объекта с подсистемой, в которой он был создан,
например, с карточкой.  
(Унаследован от [FileEntity](T_Tessa_Files_FileEntity.htm))  
[State](P_Tessa_Files_FileSignature_State.htm)| Состояние подписи.  
[SubjectName](P_Tessa_Files_FileSignature_SubjectName.htm)| Получатель
сертификата, указанный в файле подписи.  
[UserID](P_Tessa_Files_FileSignature_UserID.htm)| Идентификатор пользователя,
который зарегистрировал подпись в системе.  
[UserName](P_Tessa_Files_FileSignature_UserName.htm)| Имя пользователя,
который зарегистрировал подпись в системе.  
[ValidationResult](P_Tessa_Files_FileSignature_ValidationResult.htm)|
Сообщения, возникшие при проверке подписи. Значение не равно null.  
[Version](P_Tessa_Files_FileSignature_Version.htm)| Версия файла, к которой
относится подпись.  
##  __Методы
[Equals(IFileEntity)](M_Tessa_Files_FileEntity_Equals_1.htm)| Сравнивает
текущий объект с заданным.  
(Унаследован от [FileEntity](T_Tessa_Files_FileEntity.htm))  
---|---  
[Equals(IFileSignature)](M_Tessa_Files_FileSignature_Equals.htm)| Сравнивает
текущий объект с заданным.  
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
[SetDataAsync](M_Tessa_Files_FileSignature_SetDataAsync.htm)| Устанавливает
объект, содержащий информацию по бинарным данным файла подписи.  
[SetStateAsync](M_Tessa_Files_FileSignature_SetStateAsync.htm)| Устанавливает
состояние подписи.  
[SetValidationResultAsync](M_Tessa_Files_FileSignature_SetValidationResultAsync.htm)|
Устанавливает сообщения ошибок и предупреждения, возникшие при проверке
подписи, или null, если сообщений не возникло.  
[ToString](M_Tessa_Files_FileSignature_ToString.htm)| Возвращает строковое
представление объекта.  
(Переопределяет
[FileEntity.ToString()](M_Tessa_Files_FileEntity_ToString.htm))  
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
[NotifyAsync](M_Tessa_Files_FileExtensions_NotifyAsync_1.htm)|  Уведомляет
источник заданной подписи [IFileSource](T_Tessa_Files_IFileSource.htm) о
возникшем событии
[FileSignatureNotificationType](T_Tessa_Files_FileSignatureNotificationType.htm).
Используйте при изменении свойств подписи вручную, чтобы эти свойства были
сохранены в пакете карточки (если подпись связана с карточкой).  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
