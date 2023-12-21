# FileSignature - конструктор
Создаёт экземпляр класса с указанием значений его свойств.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public FileSignature(
    	Guid id,
    	Guid userID,
    	string userName,
    	FileSignatureEventType eventType,
    	string comment,
    	string subjectName,
    	string company,
    	DateTime signed,
    	string serialNumber,
    	string issuerName,
    	FileSignatureState state,
    	ValidationResult validationResult,
    	IFileSignatureData data,
    	IFileVersion version,
    	SignatureType signatureType = SignatureType.None,
    	SignatureProfile signatureProfile = SignatureProfile.None
    )
VB __Копировать
     Public Sub New ( 
    	id As Guid,
    	userID As Guid,
    	userName As String,
    	eventType As FileSignatureEventType,
    	comment As String,
    	subjectName As String,
    	company As String,
    	signed As DateTime,
    	serialNumber As String,
    	issuerName As String,
    	state As FileSignatureState,
    	validationResult As ValidationResult,
    	data As IFileSignatureData,
    	version As IFileVersion,
    	Optional signatureType As SignatureType = SignatureType.None,
    	Optional signatureProfile As SignatureProfile = SignatureProfile.None
    )
C++ __Копировать
     public:
    FileSignature(
    	Guid id, 
    	Guid userID, 
    	String^ userName, 
    	FileSignatureEventType eventType, 
    	String^ comment, 
    	String^ subjectName, 
    	String^ company, 
    	DateTime signed, 
    	String^ serialNumber, 
    	String^ issuerName, 
    	FileSignatureState state, 
    	ValidationResult^ validationResult, 
    	IFileSignatureData^ data, 
    	IFileVersion^ version, 
    	SignatureType signatureType = SignatureType::None, 
    	SignatureProfile signatureProfile = SignatureProfile::None
    )
F# __Копировать
     new : 
            id : Guid * 
            userID : Guid * 
            userName : string * 
            eventType : FileSignatureEventType * 
            comment : string * 
            subjectName : string * 
            company : string * 
            signed : DateTime * 
            serialNumber : string * 
            issuerName : string * 
            state : FileSignatureState * 
            validationResult : ValidationResult * 
            data : IFileSignatureData * 
            version : IFileVersion * 
            ?signatureType : SignatureType * 
            ?signatureProfile : SignatureProfile 
    (* Defaults:
            let _signatureType = defaultArg signatureType SignatureType.None
            let _signatureProfile = defaultArg signatureProfile SignatureProfile.None
    *)
    -> FileSignature
#### Параметры
id [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор подписи.
userID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
     Идентификатор пользователя, который зарегистрировал подпись в системе. 
userName [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя пользователя, который зарегистрировал подпись в системе. Не может быть равно null. 
eventType [FileSignatureEventType](T_Tessa_Files_FileSignatureEventType.htm)
    Тип действия, в результате которого подпись была создана.
comment [String](https://learn.microsoft.com/dotnet/api/system.string)
     Произвольный комментарий к подписи, который может использоваться для указания источника подписи и др. 
subjectName [String](https://learn.microsoft.com/dotnet/api/system.string)
    ФИО сотрудника, указанное в файле подписи.
company [String](https://learn.microsoft.com/dotnet/api/system.string)
    Название компании, указанное в файле подписи.
signed [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)
    Дата и время подписи, указанная в файле подписи.
serialNumber [String](https://learn.microsoft.com/dotnet/api/system.string)
    Серийный номер сертификата, указанный в файле с подписью.
issuerName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Издатель сертификата, указанный в файле с подписью.
state [FileSignatureState](T_Tessa_Files_FileSignatureState.htm)
    Состояние подписи.
validationResult
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)
     Устанавливаемые сообщения, возникшие при проверке подписи, или null, если ошибок не возникло. 
data [IFileSignatureData](T_Tessa_Files_IFileSignatureData.htm)
    Бинарные данные подписи. Не может быть равны null.
version [IFileVersion](T_Tessa_Files_IFileVersion.htm)
     Версия файла, к которой относится подпись. Не может быть равна null. 
signatureType [SignatureType](T_Tessa_Platform_EDS_SignatureType.htm)
(Optional)
     Тип подписи 
signatureProfile [SignatureProfile](T_Tessa_Platform_EDS_SignatureProfile.htm)
(Optional)
     Профиль подписи 
## __См. также
#### Ссылки
[FileSignature - ](T_Tessa_Files_FileSignature.htm)
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
